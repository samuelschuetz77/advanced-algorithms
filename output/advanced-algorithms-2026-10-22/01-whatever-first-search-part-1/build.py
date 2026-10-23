"""Build video 01.  Usage:
    python build.py snap 2 0.5 4.0        # frames of beat 2 at those seconds
    python build.py render [beats...]     # render frames (all, or listed beats)
    python build.py all                   # full build -> mp4 + srt
"""
import json
import sys
import time
from pathlib import Path

import pipeline
import storyboard

OUT = pipeline.HERE
NAME = "01 - Whatever-First Search, Part 1 - The Mole-Rat Colony"


def timeline():
    return pipeline.prepare(storyboard.BEATS)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    tl = timeline()
    total = tl[-1]["start"] + tl[-1]["dur"]
    print(f"{len(tl)} beats, {total:.1f}s ({total / 60:.1f} min)")
    if cmd == "info":
        for i, b in enumerate(tl, 1):
            print(f"{i:02d} {b['id']:<14} start {b['start']:7.1f}  dur {b['dur']:5.1f}  audio {b['audio_dur']:5.1f}  words {len(b['words'])}")
            print("    cues:", {k: round(v, 2) for k, v in b["cues"].items()})
        return
    if cmd == "snap":
        beat = int(sys.argv[2])
        times = [float(x) for x in sys.argv[3:]]
        for p in pipeline.snap(tl, beat, times, OUT / "snaps"):
            print(p)
        return
    t0 = time.time()
    if cmd == "render":
        only = {int(x) for x in sys.argv[2:]} or None
        pipeline.render_all(tl, only)
        print(f"rendered in {time.time() - t0:.0f}s")
        return
    if cmd == "all":
        results = pipeline.render_all(tl)
        print(f"rendered in {time.time() - t0:.0f}s; assembling")
        out_mp4 = OUT / f"{NAME}.mp4"
        pipeline.assemble(tl, results, out_mp4, OUT / "work")
        pipeline.write_srt(tl, OUT / f"{NAME}.srt")
        (OUT / "timeline.json").write_text(json.dumps(
            [{k: v for k, v in b.items() if k in ('id', 'start', 'dur', 'narration', 'cues')} for b in tl], indent=1))
        print("wrote", out_mp4)


if __name__ == "__main__":
    main()
