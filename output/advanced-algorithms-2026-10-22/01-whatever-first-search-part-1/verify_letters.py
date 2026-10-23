"""Transcribe every beat's audio with Whisper and compare the standalone vertex letters with the script."""
import re, sys, warnings
warnings.filterwarnings("ignore")
import whisper
import pipeline, storyboard
tl = pipeline.prepare(storyboard.BEATS)
m = whisper.load_model("base.en")
LETTERS = set("SABCDEFXY")
bad = 0
for i, b in enumerate(tl, 1):
    expected = [w["disp"].strip(".,:;?!") for w in b["words"] if w.get("letter")]
    if not expected:
        continue
    heard = m.transcribe(b["audio"], language="en", fp16=False)["text"]
    toks = [t.strip(".,:;?!-") for t in re.split(r"[\s]+", heard)]
    got = [t for t in toks if t in LETTERS]  # uppercase only: lowercase "a" is the article
    flag = "" if got == expected else "   <-- differs"
    if flag:
        bad += 1
    print(f"{i:02d} {b['id']:<10} expect {''.join(expected):<24} heard {''.join(got):<24}{flag}")
    if flag:
        print("     whisper:", heard.strip())
print("beats that differ:", bad)
