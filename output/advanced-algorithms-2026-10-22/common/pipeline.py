"""Narration -> voice (Ava) with word timings -> subtitles -> frames -> mp4."""
from __future__ import annotations

import asyncio
import hashlib
import json
import os
import re
import subprocess
import sys
import wave
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path.cwd()
CACHE = HERE / "cache"
FRAMES = HERE / "frames"


def configure(here):
    """Point the pipeline at one video folder (cache/ and frames/ live there)."""
    global HERE, CACHE, FRAMES
    HERE = Path(here)
    CACHE = HERE / "cache"
    FRAMES = HERE / "frames"
VOICE = "en-US-AvaMultilingualNeural"
RATE = "-4%"
FPS = 30
PAD_IN = 0.30
PAD_OUT = 0.55
SR = 24000

# Vertex letters are spoken as plain capital letters. Phonetic spellings failed an
# audition (checked with Whisper small.en): "ay" is read as "I", "ess" as "as", and "ee" as the
# nonsense word "Ee". A bare capital E gets a trailing period (see parse_narration).
PHON = {k: k for k in "SABCDEFXYV"}


# ---------------------------------------------------------------- parsing
def parse_narration(text):
    words, pending = [], []
    text = re.sub(r"(?<=\S)(\[\[\w+\]\])", r" ", text)  # a cue glued after a word attaches to the next word
    for tok in text.split():
        while tok.startswith("[["):
            end = tok.index("]]")
            pending.append(tok[2:end])
            tok = tok[end + 2:]
        if not tok:
            continue

        def disp_sub(m):
            return m.group(1).split("|")[0]

        def spoken_sub(m):
            inner = m.group(1)
            return (inner.split("|")[1] if "|" in inner else PHON.get(inner, inner)).replace("~", " ")

        spoken = re.sub(r"\{([^}]*)\}", spoken_sub, tok)
        # Ava swallows a bare capital E ("E has" -> "He has"); a trailing period makes it a clear letter
        spoken = re.sub(r"E(?![.,:;?!])", "E.", spoken)
        words.append({
            "disp": re.sub(r"\{([^}]*)\}", disp_sub, tok),
            "spoken": spoken,
            "letter": bool(re.search(r"\{[SABCDEFXYV]\}", tok)),
            "cues": pending,
        })
        pending = []
    return words


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


# ---------------------------------------------------------------- tts
async def _tts(text, mp3):
    import edge_tts
    comm = edge_tts.Communicate(text, VOICE, rate=RATE, boundary="WordBoundary")
    events = []
    with open(mp3, "wb") as f:
        async for ch in comm.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                events.append({"text": ch["text"], "t0": ch["offset"] / 1e7, "d": ch["duration"] / 1e7})
    return events


def audio_duration(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(path)], text=True)
    return float(out.strip())


def synth(spoken_text):
    CACHE.mkdir(exist_ok=True)
    key = hashlib.sha1((VOICE + RATE + spoken_text).encode()).hexdigest()[:16]
    mp3, js = CACHE / f"{key}.mp3", CACHE / f"{key}.json"
    if not (mp3.exists() and js.exists()):
        for attempt in range(4):
            try:
                events = asyncio.run(_tts(spoken_text, mp3))
                break
            except Exception as e:  # network hiccup
                print("tts retry", attempt, e)
        else:
            raise RuntimeError("TTS failed")
        js.write_text(json.dumps({"events": events, "dur": audio_duration(mp3)}))
    data = json.loads(js.read_text())
    return mp3, data["events"], data["dur"]


def align(words, events, total):
    """Give each word a t0/t1 (seconds into its audio)."""
    out = []
    i = 0
    ok = True
    prev_end = 0.0
    for w in words:
        n = norm(w["spoken"])
        if n == "":
            out.append((prev_end, prev_end))
            continue
        acc, start, end = "", None, None
        while i < len(events) and acc != n:
            en = norm(events[i]["text"])
            if en == "":
                i += 1
                continue
            if start is None:
                start = events[i]["t0"]
            acc += en
            end = events[i]["t0"] + events[i]["d"]
            i += 1
            if not n.startswith(acc):
                break
        if acc != n:
            ok = False
            break
        out.append((start, end))
        prev_end = end
    if not ok:
        print("  align fallback (proportional)")
        lens = [max(1, len(norm(w["spoken"]))) for w in words]
        tot = sum(lens)
        acc = 0
        out = []
        for L in lens:
            out.append((total * acc / tot, total * (acc + L) / tot))
            acc += L
    return out


# ---------------------------------------------------------------- subtitles
def layout_lines(idxs, words, text_w, line_px):
    space = text_w(" ")
    lines, line, wpx = [], [], 0.0
    for k in idxs:
        wd = text_w(words[k]["disp"])
        if line and wpx + space + wd > line_px:
            lines.append(line)
            line, wpx = [], 0.0
        wpx += (space if line else 0.0) + wd
        line.append(k)
    if line:
        lines.append(line)
    return lines


def make_chunks(words, text_w, max_chars=84, line_px=1640):
    """Split narration into caption chunks of at most two lines. text_w(str)->px."""
    raw, cur, length = [], [], 0
    for k, w in enumerate(words):
        cur.append(k)
        length += len(w["disp"]) + 1
        last = w["disp"][-1]
        if last in ".?!" or (last in ",:;" and length > 48) or length > max_chars:
            raw.append(cur)
            cur, length = [], 0
    if cur:
        raw.append(cur)
    out = []
    for idxs in raw:
        rest = idxs
        while rest:
            lines = layout_lines(rest, words, text_w, line_px)
            keep = lines[:2]
            if len(lines) <= 2 and len(keep) == 2:
                # balance the two lines: pick the split that minimizes the wider line
                ks = rest
                best, best_w = None, 1e9
                for cut in range(1, len(ks)):
                    wa = sum(text_w(words[k]["disp"]) for k in ks[:cut]) + text_w(" ") * (cut - 1)
                    wb = sum(text_w(words[k]["disp"]) for k in ks[cut:]) + text_w(" ") * (len(ks) - cut - 1)
                    if max(wa, wb) < best_w:
                        best, best_w = cut, max(wa, wb)
                keep = [ks[:best], ks[best:]]
            used = sum(len(l) for l in keep)
            out.append({"idx": rest[:used], "lines": keep})
            rest = rest[used:]
    return out


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"


# ---------------------------------------------------------------- timeline
def prepare(beats):
    """Synthesize every beat and compute the global timeline. Returns list of dicts."""
    from engine import font
    text_w = lambda s: font(46, True).getlength(s) / 2
    tl, t_global = [], 0.0
    for b in beats:
        words = parse_narration(b["narration"])
        spoken = " ".join(w["spoken"] for w in words)
        mp3, events, dur = synth(spoken)
        times = align(words, events, dur)
        cues = {}
        for w, (t0, t1) in zip(words, times):
            w["t0"], w["t1"] = PAD_IN + t0, PAD_IN + t1
            for c in w["cues"]:
                cues[c] = w["t0"]
        pause = b.get("pause", 0.0)
        pause_start = PAD_IN + dur
        length = max(PAD_IN + dur + pause + PAD_OUT, b.get("min_len", 0.0))
        for name, anchor, off in b.get("extra_cues", []):
            cues[name] = cues[anchor] + off
        chunks = make_chunks(words, text_w)
        for i, ch in enumerate(chunks):
            ch["t0"] = words[ch["idx"][0]]["t0"]
        beat = dict(b)
        beat.update(words=words, cues=cues, chunks=chunks, dur=length, audio=str(mp3), audio_dur=dur,
                    pause_start=pause_start, pause_len=pause, start=t_global)
        beat.pop("scene", None)
        tl.append(beat)
        t_global += length
    return tl


# ---------------------------------------------------------------- render
def _render_beat(args):
    index, beat, here = args
    configure(here)
    import storyboard
    from engine import Canvas, NullCanvas
    from widgets import Ctx
    scene = storyboard.BEATS[index]["scene"]
    out_dir = FRAMES / f"{index + 1:02d}"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = int(round(beat["dur"] * FPS))
    unique = []  # (path, nframes)
    prev_sig = None
    for k in range(n):
        t = k / FPS
        dry = Ctx(NullCanvas(), t, beat)
        scene(dry)
        sig = tuple(map(repr, dry.sig))
        if sig == prev_sig and unique:
            unique[-1][1] += 1
            continue
        cv = Canvas()
        ctx = Ctx(cv, t, beat)
        scene(ctx)
        path = out_dir / f"f{k:05d}.png"
        cv.finish().save(path, compress_level=1)
        unique.append([str(path), 1])
        prev_sig = sig
    return index, unique


def render_all(timeline, only=None, workers=14):
    jobs = [(i, b, str(HERE)) for i, b in enumerate(timeline) if only is None or (i + 1) in only]
    results = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for index, unique in ex.map(_render_beat, jobs):
            results[index] = unique
            print(f"  beat {index + 1:02d}: {len(unique)} unique frames", flush=True)
    return results


def snap(timeline, beat_no, times, out_dir):
    """Render single frames for visual QA."""
    import storyboard
    from engine import Canvas
    from widgets import Ctx
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    beat = timeline[beat_no - 1]
    scene = storyboard.BEATS[beat_no - 1]["scene"]
    paths = []
    for t in times:
        cv = Canvas()
        scene(Ctx(cv, t, beat))
        p = out_dir / f"b{beat_no:02d}_{t:05.2f}.png"
        cv.finish().save(p)
        paths.append(p)
    return paths


# ---------------------------------------------------------------- assemble
def build_audio(timeline, out_wav):
    import numpy as np
    total = timeline[-1]["start"] + timeline[-1]["dur"]
    buf = np.zeros(int((total + 1) * SR), dtype=np.float32)
    for b in timeline:
        wav = CACHE / (Path(b["audio"]).stem + ".wav")
        if not wav.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", b["audio"], "-ar", str(SR), "-ac", "1", str(wav)],
                           check=True)
        with wave.open(str(wav)) as w:
            raw = w.readframes(w.getnframes())
        data = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
        s = int((b["start"] + PAD_IN) * SR)
        buf[s:s + len(data)] += data
    pcm = (np.clip(buf, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(out_wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def write_srt(timeline, path):
    lines, n = [], 1
    for b in timeline:
        chunks = b["chunks"]
        for i, ch in enumerate(chunks):
            t0 = b["start"] + ch["t0"]
            if i + 1 < len(chunks):
                t1 = b["start"] + chunks[i + 1]["t0"]
            else:
                t1 = b["start"] + b["words"][ch["idx"][-1]]["t1"] + 0.4
            text = "\n".join(" ".join(b["words"][k]["disp"] for k in line) for line in ch["lines"])
            lines.append(f"{n}\n{srt_time(t0)} --> {srt_time(t1)}\n{text}\n")
            n += 1
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def assemble(timeline, results, out_mp4, work):
    work = Path(work)
    work.mkdir(exist_ok=True)
    wav = work / "narration.wav"
    build_audio(timeline, wav)
    listing = []
    last = None
    for i in range(len(timeline)):
        for path, nframes in results[i]:
            listing.append(f"file '{Path(path).as_posix()}'\nduration {nframes / FPS:.6f}")
            last = path
    listing.append(f"file '{Path(last).as_posix()}'")
    (work / "frames.txt").write_text("\n".join(listing), encoding="utf-8")
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "frames.txt"),
           "-i", str(wav),
           "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-shortest",
           "-movflags", "+faststart", str(out_mp4)]
    subprocess.run(cmd, check=True)
