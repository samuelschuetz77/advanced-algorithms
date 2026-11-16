# Chapter 6: Two Lessons in Ten Minutes

Combines the October 26 and 28 class notes into a reading primer: Figure 6.4, DFS intervals and edge types, strongly connected components, paths to/from/through a vertex, and cut vertices.

The narration follows Samuel's edit: describe what paths do before deriving conditions about all paths. It uses neutral descriptions of reaching vertices, recording groups, and finding another connection.

## Deliverables

- `Chapter 6 - Two Lessons in Ten Minutes.mp4`: 10:00, 1920?1080, 30 fps, Ava narration, burned word-synchronized captions, embedded chapters.
- Matching `.srt`: external subtitles.
- `script-combined.md`: narration and production notes.
- `transcript.md`: final narration grouped by chapter.
- `Draft - visual check.mp4`: short 480p visual-check reel, not the finished lesson.

## Chapters

| Time | Topic |
|---|---|
| 0:00 | Three path questions |
| 0:19 | Figure 6.4 |
| 0:39 | Arrival and return |
| 0:56 | Nested calls |
| 1:44 | The discovery forest |
| 2:01 | Three vertex states |
| 2:21 | Four edge types |
| 2:43 | Finish order |
| 3:03 | Return-trip groups |
| 3:24 | A DAG of components |
| 3:40 | Search from d |
| 4:06 | Collect one group |
| 4:25 | Two reversals |
| 5:05 | The ordering proof |
| 5:32 | State for each pass |
| 5:50 | Reading the notes |
| 6:11 | To, from, through |
| 6:47 | Two counting passes |
| 7:05 | Compare the paths |
| 7:34 | Remove a vertex |
| 7:54 | The DFS root |
| 8:36 | Another connection |
| 8:54 | Chapter reading route |
| 9:33 | Try it on paper |

## Sources and interpretation

The live published notes were saved separately for October 26 and October 28 under `sources/`. Figure 6.4 and Exercise 4 were inspected in the local Erickson textbook PDF. Book references are visible in the video.

?To / from / through? is the interpretation accepted by Samuel: fixed endpoints in a DAG, with through(v) = to(v) ? from(v). The 40-word rationale remains in the narration. The three-component graph is counted as a DAG in its own right; its counts are not counts of paths inside the original cyclic graph.

The final cut-vertex section explicitly switches to an undirected version. Exercise 4(b)(ii) in this PDF appears to omit a negation; the video uses the correct subtree-connection criterion.

## Verification

`trace_check.py` verifies the SCC trace against independent mutual reachability. `combined_trace_check.py` reproduces Figure 6.4's printed preorder and postorder, checks narrated intervals, DAG counts, DFS-root children, and connectivity after removal. Caption bounds and audio joins were checked. Selected pronunciation checks used Whisper; an initially missed E was changed to ?vertex E? and rechecked. Snapshot contact sheets are in `snaps/`. The teaching edge between a and c is curved separately from the original arrow. The final paper-task view explicitly uses the undirected version.

The 600-second timeline contains five prediction pauses and brief reflection holds after the component proof, path comparison, and final paper task. Those holds account for the remaining time without cutting narration.

## Rebuild

Use the system Python, which has edge-tts, Pillow, and numpy; ffmpeg and ffprobe must be on PATH. The shared engine remains in `../advanced-algorithms-2026-10-22/common/`.

Run `python build.py prepare`, then `python render.py qa`, then `python render.py`. To remux existing checked frames, run `python render.py assemble`. `prepared.json`, `timeline.json`, and `render-results.json` preserve the production state. No coursework or learning-log files are modified.
