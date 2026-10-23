# Video 01: Whatever-First Search, Part 1 — The Mole-Rat Colony

`01 - Whatever-First Search, Part 1 - The Mole-Rat Colony.mp4`
1920x1080, 30 fps, 10:57, voice Ava (en-US-AvaMultilingualNeural), loudness -16.3 LUFS.
Subtitles are burned in (karaoke style: the spoken word is highlighted) and also in the `.srt`.

Covers JEA 5.5 (PDF pp.217-219): reachability, marks, the bag, the pair `(came_from, current)`,
the four rules of WhateverFirstSearch, Lemma 5.1 (the three promises and the domino proof), and the
Python version read line by line. Parts 2 of the book section (analysis, variants, directed graphs)
are video 02. The trace shown is produced by running the real code (`trace_check.py`).

## Chapters
| Time | Beat | Content |
|---|---|---|
| 0:00 | meet | Wrinkles, the colony, vertex and edge |
| 0:17 | question | reachability (pause and predict) |
| 0:44 | circles / marks | walking in circles; the scent mark |
| 1:16 | three ... translate | the token pile, the pair, the four rules, the book's letters |
| 3:19 | map ... answer | the 25-step run on the colony; stale tokens; the 25 = 1 + 2 x 12 count |
| 7:00 | parents, tree | why keep the pair; the parent tree |
| 7:40 | stops ... dominoes2 | the three promises and the induction proof |
| 8:53 | code_all ... recursion | the Python, symbol by symbol; link to `build_topo_from` |
| 10:34 | recap | retell it; try it on your page-one graph |

## Files
- `*.mp4`, `*.srt`, `transcript.md` (narration per beat, with times)
- `script.md` design notes and the approved Part 1 text (the final narration is in `storyboard.py`)
- `storyboard.py` beats and narration, `scenes.py` and `scenes2.py` animation, `widgets.py`, `engine.py` drawing
- `pipeline.py` voice, word timing, subtitles, frames, mux; `build.py` entry point; `qa.py` checks
- `trace_check.py` the real code behind the on-screen trace; `cache/` synthesized voice (so a rebuild needs no network)

Rebuild: `python build.py all` (about 8 minutes). Preview a frame: `python build.py snap <beat> <seconds>`.

## Choices and cuts
- The optional "different neighbor order, different tree" beat was cut to keep the length near 11 minutes.
- Mole-rat story words are paired with graph words the first time (chamber = vertex); after that the narration uses graph words.
- The graph has 7 reachable vertices and 12 edges plus a cut-off X-Y burrow (Samuel's size rule).
- Page-one graph from the 10/19 notes is used in video 02 (edge directions still to be confirmed).
