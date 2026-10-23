"""QA for the finished mp4: probe, loudness, and frames at spoken-cue times.

    python qa.py            -> prints stats and writes qa/ frames + contact sheets
"""
import json
import random
import subprocess
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
MP4 = next(HERE.glob("01 - *.mp4"))
OUT = HERE / "qa"
OUT.mkdir(exist_ok=True)
tl = json.loads((HERE / "timeline.json").read_text())


def run(*a):
    return subprocess.run(a, capture_output=True, text=True)


probe = run("ffprobe", "-v", "error", "-show_entries", "stream=codec_name,width,height,r_frame_rate,duration",
            "-show_entries", "format=duration,size", "-of", "compact", str(MP4))
print(probe.stdout.strip())
loud = run("ffmpeg", "-hide_banner", "-i", str(MP4), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=summary",
           "-vn", "-f", "null", "-")
for line in loud.stderr.splitlines():
    if any(k in line for k in ("Input Integrated", "Input True Peak", "Input LRA")):
        print(line.strip())

# frames at cue times (sync test): pick one cue per ~3rd beat, plus first and last
random.seed(3)
picks = []
for b in tl:
    cues = b["cues"]
    if not cues:
        continue
    name = random.choice(sorted(cues))
    picks.append((b["id"], name, b["start"] + cues[name] + 0.25))
print(len(picks), "cue frames")
files = []
for bid, name, t in picks:
    f = OUT / f"{bid}__{name}.png"
    run("ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(MP4), "-frames:v", "1", str(f))
    files.append((bid, name, t, f))
for i in range(0, len(files), 4):
    tiles = [Image.open(f[3]).convert("RGB").resize((960, 540), Image.LANCZOS) for f in files[i:i + 4]]
    sheet = Image.new("RGB", (1920, 1080), (0, 0, 0))
    for j, t in enumerate(tiles):
        sheet.paste(t, ((j % 2) * 960, (j // 2) * 540))
    sheet.save(OUT / f"sheet_{i // 4:02d}.png")
print("sheets in", OUT)
for bid, name, t, f in files:
    print(f"  {bid:<12} cue {name:<10} at {t:7.2f}s")
