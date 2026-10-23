# Class Lab: topo_order and the Morning

`04 - Class Lab - topo_order and the Morning.mp4` — 1920x1080, 30 fps, 8:24, voice Ava, subtitles burned in (the spoken word is highlighted) and in the `.srt`.

**Covers:** Class 21 mini lab Bonus; your 10/19 drawings; JEA 6.1, 6.3

Your A-B-C-D graph as a morning routine, a 7-task dinner DAG with 12 rules (plus a second start task, 'set the table', to show both start orders), why the reversed finish order works and the start order does not, then your topo_order line by line, the one-line fix (shown only, your file is unchanged), and your two tests.

Every trace, count, and table shown on screen comes from running real code in this folder (see the `*log.py` / `trace_check.py` file), not from hand-typed numbers.

## Chapters
| Time | Beat |
|---|---|
| 0:00 | From your notes |
| 0:16 | Two layouts |
| 0:40 | Why no cycles? |
| 0:54 | A bigger example: dinner |
| 1:15 | The trick |
| 1:33 | Going down |
| 1:50 | Backing up |
| 2:04 | The rest |
| 2:25 | Reverse the finish order |
| 2:44 | Why it works |
| 3:05 | What about the start order? |
| 3:24 | A second start task |
| 3:45 | Case one: the loop starts at Shop |
| 4:03 | Case two: the loop starts at Table |
| 4:26 | Both ways |
| 4:53 | Your code |
| 5:11 | A function inside a function |
| 5:26 | What one call does |
| 5:43 | Where is the base case? |
| 6:03 | The outer loop |
| 6:20 | The bug |
| 6:43 | Your test |
| 6:59 | Reading the real test |
| 7:26 | Running it |
| 7:46 | How fast? |
| 8:02 | Recap |

## Files
`04 - Class Lab - topo_order and the Morning.mp4`, `*.srt`, `transcript.md` · `storyboard.py` (narration + cues) · `scenes*.py` (animation) · `build.py` · `cache/` (synthesized voice; rebuild needs no network) · shared engine in `../common/`.

Rebuild: `python build.py all` (about 2 to 8 minutes). Preview one frame: `python build.py snap <beat> <seconds>`. Check how letters are pronounced: `python ../common/verify_letters.py`.
