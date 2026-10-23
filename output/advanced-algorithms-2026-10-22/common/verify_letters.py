"""python ../common/verify_letters.py  -> transcribe each beat with Whisper; compare vertex letters with the script.
Note: Whisper often writes 'two' for 'to' between letters, so compare as a sorted multiset ratio, not exactly."""
import re
import sys
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
here = Path.cwd()
sys.path.insert(0, str(here))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline
pipeline.configure(here)
import storyboard
import whisper

LETTERS = set("SABCDEFXYV")
tl = pipeline.prepare(storyboard.BEATS)
m = whisper.load_model("small.en")
bad = total = 0
for i, b in enumerate(tl, 1):
    exp = [w["disp"].strip(".,:;?!'s") if w["disp"].endswith("'s") else w["disp"].strip(".,:;?!") for w in b["words"] if w.get("letter")]
    exp = [e.upper() for e in exp if e.upper() in LETTERS]
    if not exp:
        continue
    heard = m.transcribe(b["audio"], language="en", fp16=False)["text"]
    toks = [t.strip(".,:;?!-'") for t in re.split(r"\s+", heard)]
    got = [t for t in toks if t in LETTERS]
    # Whisper writes lone 'A' as the article too; count only uppercase single letters it produced
    ce, cg = Counter(exp), Counter(got)
    miss = {k: ce[k] - cg.get(k, 0) for k in ce if ce[k] - cg.get(k, 0) > 0}
    total += 1
    if miss:
        bad += 1
        print(f"{i:02d} {b['id']:<14} letters missing from transcript: {miss}")
print(f"{bad} of {total} letter-bearing beats had at least one letter not heard as that letter")
