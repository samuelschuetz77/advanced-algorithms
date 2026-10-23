"""python ../common/transcribe_beats.py beatid [beatid...]  -> expected narration vs Whisper transcript"""
import re, sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
here = Path.cwd()
sys.path.insert(0, str(here)); sys.path.insert(0, str(Path(__file__).resolve().parent))
import pipeline
pipeline.configure(here)
import storyboard, whisper
tl = pipeline.prepare(storyboard.BEATS)
m = whisper.load_model("small.en")
for b in tl:
    if b["id"] in sys.argv[1:]:
        exp = " ".join(w["disp"] for w in b["words"])
        got = m.transcribe(b["audio"], language="en", fp16=False)["text"].strip()
        print(f"--- {b['id']}\nEXPECT: {exp}\nHEARD : {got}\n")
