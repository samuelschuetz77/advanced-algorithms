# Class Lab: count_paths and the Frog

`03 - Class Lab - count_paths and the Frog.mp4` — 1920x1080, 30 fps, 8:54, voice Ava, subtitles burned in (the spoken word is highlighted) and in the `.srt`.

**Covers:** Class 21 mini lab Part 1; JEA 6.4, PDF pp.252-253

Hopper the frog on stepping stones, then your diamond, then a 7-junction, 12-trail hiking map: plain recursion makes 24 calls, a cache makes 13. Your count_paths line by line (import, @cache, nested function, generator expression, sum), the ladder test (Fibonacci, 8 trillion calls vs 121), and why it needs a DAG.

Every trace, count, and table shown on screen comes from running real code in this folder (see the `*log.py` / `trace_check.py` file), not from hand-typed numbers.

## Chapters
| Time | Beat |
|---|---|
| 0:00 | Meet Hopper |
| 0:28 | Count backward from the far bank |
| 0:47 | The pattern |
| 1:03 | Twenty-one ways |
| 1:13 | Counting paths in general |
| 1:37 | The graph from your lab |
| 2:03 | How the code asks |
| 2:28 | A bigger map |
| 2:48 | Plain recursion |
| 3:02 | The repeats |
| 3:14 | The fix: a cache |
| 3:32 | The cache filling in |
| 3:52 | How much work? |
| 4:11 | Your code: the import |
| 4:22 | Your code: the outline |
| 4:32 | Your code: @cache |
| 4:53 | Your code: a function inside a function |
| 5:19 | Your code: the base case |
| 5:31 | Your code: the densest line |
| 5:46 | Your code: the loop inside |
| 6:03 | Your code: sum |
| 6:18 | Run it on the diamond |
| 6:39 | Your third test |
| 6:49 | One rule: no cycles |
| 7:14 | Your last test: sixty stones |
| 7:36 | How many ways? |
| 7:54 | Plain versus cached |
| 8:08 | Memoization is depth-first search |
| 8:31 | Recap |

## Files
`03 - Class Lab - count_paths and the Frog.mp4`, `*.srt`, `transcript.md` · `storyboard.py` (narration + cues) · `scenes*.py` (animation) · `build.py` · `cache/` (synthesized voice; rebuild needs no network) · shared engine in `../common/`.

Rebuild: `python build.py all` (about 2 to 8 minutes). Preview one frame: `python build.py snap <beat> <seconds>`. Check how letters are pronounced: `python ../common/verify_letters.py`.
