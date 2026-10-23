"""python sheet.py out.png a.png b.png c.png d.png  -> 2x2 contact sheet at half size"""
import sys
from PIL import Image
out, files = sys.argv[1], sys.argv[2:]
tiles = [Image.open(f).convert("RGB").resize((960, 540), Image.LANCZOS) for f in files]
cols = 2
rows = (len(tiles) + 1) // 2
sheet = Image.new("RGB", (960 * cols, 540 * rows), (0, 0, 0))
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % cols) * 960, (i // cols) * 540))
sheet.save(out)
