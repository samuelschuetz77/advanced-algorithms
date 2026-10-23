# Reading Primer: Topological Sort and Dynamic Programming

`06 - Reading Primer - Topological Sort and Dynamic Programming.mp4` — 1920x1080, 30 fps, 12:17, voice Ava, subtitles burned in (the spoken word is highlighted) and in the `.srt`.

**Covers:** JEA 6.3-6.4, PDF pp.250-254

The hiking map again, with scenery scores: the book's array filled from the back (Figure 6.9), plain Python, processing at the finish, the reversed graph and footnote 3, dependency graphs, memoization = DFS (Fig 6.10), DP = postorder (Fig 6.11), edit-distance grid (Fig 6.12), and longest path in a DAG (memoized and DP versions, value 19).

Every trace, count, and table shown on screen comes from running real code in this folder (see the `*log.py` / `trace_check.py` file), not from hand-typed numbers.

## Chapters
| Time | Beat |
|---|---|
| 0:00 | Topological ordering |
| 0:40 | Why a cycle breaks it |
| 1:19 | One map, two goals |
| 1:42 | The book's version: an array filled from the back |
| 2:23 | Check the array |
| 2:40 | The same thing in Python |
| 3:06 | What if there might be a cycle? |
| 3:27 | Often, you do not need the list |
| 3:57 | Forward order: reverse the graph |
| 4:22 | Two orders, both correct |
| 4:48 | Section 6.4: the dependency graph |
| 5:20 | Memoization is depth-first search |
| 5:54 | Dynamic programming is a postorder |
| 6:21 | Why DP uses nested loops |
| 6:47 | Two small differences |
| 7:18 | An irregular graph: longest path |
| 7:42 | The recurrence |
| 8:21 | Run it on the hiking map |
| 9:20 | The Python: the setup |
| 9:37 | The Python: base case and cache check |
| 9:53 | The Python: the maximum |
| 10:19 | The Python: the answer |
| 10:35 | The route, and an extra |
| 10:56 | The same answer by dynamic programming |
| 11:38 | Recap |

## Files
`06 - Reading Primer - Topological Sort and Dynamic Programming.mp4`, `*.srt`, `transcript.md` · `storyboard.py` (narration + cues) · `scenes*.py` (animation) · `build.py` · `cache/` (synthesized voice; rebuild needs no network) · shared engine in `../common/`.

Rebuild: `python build.py all` (about 2 to 8 minutes). Preview one frame: `python build.py snap <beat> <seconds>`. Check how letters are pronounced: `python ../common/verify_letters.py`.
