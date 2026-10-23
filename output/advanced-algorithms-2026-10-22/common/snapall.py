"""python ../common/snapall.py [fraction] [first] [last]  -> snaps/sheet_NN.png (4 beats per sheet, each at fraction of its length)"""
import sys
from pathlib import Path
from PIL import Image

here = Path.cwd()
sys.path.insert(0, str(here))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline
pipeline.configure(here)
import storyboard

frac = float(sys.argv[1]) if len(sys.argv) > 1 else 0.7
first = int(sys.argv[2]) if len(sys.argv) > 2 else 1
last = int(sys.argv[3]) if len(sys.argv) > 3 else len(storyboard.BEATS)
tl = pipeline.prepare(storyboard.BEATS)
files = []
for i in range(first, last + 1):
    t = max(0.1, tl[i - 1]["dur"] * frac)
    files += pipeline.snap(tl, i, [t], here / "snaps")
for k in range(0, len(files), 4):
    tiles = [Image.open(f).convert("RGB").resize((960, 540), Image.LANCZOS) for f in files[k:k + 4]]
    sheet = Image.new("RGB", (1920, 1080))
    for j, t in enumerate(tiles):
        sheet.paste(t, ((j % 2) * 960, (j // 2) * 540))
    sheet.save(here / "snaps" / f"sheet_{first + k:02d}.png")
print("sheets:", sorted(p.name for p in (here / "snaps").glob("sheet_*.png")))
