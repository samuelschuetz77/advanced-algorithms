"""Shared build CLI.  In a video folder's build.py:

    import sys; sys.path.insert(0, "../common")
    import buildlib; buildlib.main(NAME)
"""
import json
import sys
import time
from pathlib import Path

import pipeline


def main(name, here=None):
    here = Path(here or Path.cwd())
    sys.path.insert(0, str(here))
    pipeline.configure(here)
    import storyboard
    tl = pipeline.prepare(storyboard.BEATS)
    total = tl[-1]["start"] + tl[-1]["dur"]
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    print(f"{len(tl)} beats, {total:.1f}s ({total / 60:.1f} min)")
    if cmd == "info":
        for i, b in enumerate(tl, 1):
            print(f"{i:02d} {b['id']:<14} start {b['start']:7.1f}  dur {b['dur']:5.1f}  audio {b['audio_dur']:5.1f}")
            print("    cues:", {k: round(v, 2) for k, v in b["cues"].items()})
        return
    if cmd == "snap":
        beat = int(sys.argv[2])
        for p in pipeline.snap(tl, beat, [float(x) for x in sys.argv[3:]], here / "snaps"):
            print(p)
        return
    t0 = time.time()
    if cmd == "render":
        pipeline.render_all(tl, {int(x) for x in sys.argv[2:]} or None)
        return
    results = pipeline.render_all(tl)
    print(f"rendered in {time.time() - t0:.0f}s; assembling")
    out = here / f"{name}.mp4"
    pipeline.assemble(tl, results, out, here / "work")
    pipeline.write_srt(tl, here / f"{name}.srt")
    (here / "timeline.json").write_text(json.dumps(
        [{k: v for k, v in b.items() if k in ("id", "start", "dur", "narration", "cues")} for b in tl], indent=1))
    print("wrote", out)
