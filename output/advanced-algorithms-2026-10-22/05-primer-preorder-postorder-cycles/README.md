# Reading Primer: Preorder, Postorder, and Cycles

`05 - Reading Primer - Preorder, Postorder, and Cycles.mp4` — 1920x1080, 30 fps, 8:24, voice Ava, subtitles burned in (the spoken word is highlighted) and in the `.srt`.

**Covers:** JEA 6.1-6.2, PDF pp.245-250

Ada and a ball of thread in a 7-room, 12-door maze: two stamps per room from one clock, new / active / finished, bars (Figure 6.4), Lemma 6.1, the four edge types, a back edge means a cycle, the book's IsAcyclic in Python, DFSAll.

Every trace, count, and table shown on screen comes from running real code in this folder (see the `*log.py` / `trace_check.py` file), not from hand-typed numbers.

## Chapters
| Time | Beat |
|---|---|
| 0:00 | The thread |
| 0:19 | Two stamps per room |
| 0:42 | Three states |
| 1:03 | The walk, part one |
| 1:32 | The walk, part two |
| 2:11 | Two orderings |
| 2:34 | Active intervals |
| 2:54 | Four ways to say 'ancestor' |
| 3:17 | Four kinds of door |
| 3:39 | Tree edges |
| 3:51 | Back edges |
| 4:04 | Forward edges |
| 4:17 | Cross edges |
| 4:30 | What the bars look like |
| 4:55 | A back edge means a cycle |
| 5:11 | The same test, with finishing times |
| 5:34 | The algorithm in Python |
| 5:45 | Visiting a room |
| 5:59 | The three cases |
| 6:20 | Leaving the room |
| 6:31 | The outer loop |
| 6:49 | Run it on the maze |
| 7:07 | Without the back edges |
| 7:33 | Starting everywhere |
| 7:58 | Recap |

## Files
`05 - Reading Primer - Preorder, Postorder, and Cycles.mp4`, `*.srt`, `transcript.md` · `storyboard.py` (narration + cues) · `scenes*.py` (animation) · `build.py` · `cache/` (synthesized voice; rebuild needs no network) · shared engine in `../common/`.

Rebuild: `python build.py all` (about 2 to 8 minutes). Preview one frame: `python build.py snap <beat> <seconds>`. Check how letters are pronounced: `python ../common/verify_letters.py`.
