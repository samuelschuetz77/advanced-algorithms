# Whatever-First Search, Part 2: The Metro Map

`02 - Whatever-First Search, Part 2 - The Metro Map.mp4` - 1920x1080, 30 fps, 8:59, voice Ava, subtitles burned in and in the `.srt`.

**Covers:** JEA 5.5 analysis, 5.6, 5.7 (PDF pp.219-224).

A city metro map (7 stations, 12 tracks) replaces the earlier school-rumor example, which Samuel found muddled. Station = vertex, track = edge, visited = marked, a track to try = token, the station you came from = parent. Shows the 2E + 1 token count and O(V + E T); stack vs queue on the same map (depth 6 vs depth 3, queue = fewest stops); best-first search (Prim, Dijkstra); a loop that counts separate networks; one-way tracks (directed graphs); flood fill as a reduction. Every run shown comes from real code in `metrolog.py`.

The earlier rumor version is kept in `superseded_rumor_version/` (not used).

## Chapters
| Time | Beat |
|---|---|
| 0:00 | Last time |
| 0:19 | A new example: a metro map |
| 0:41 | A guess |
| 0:58 | One track |
| 1:15 | All twelve tracks |
| 1:21 | Counting tokens |
| 1:35 | The cost of tokens |
| 1:48 | Marking costs too |
| 2:02 | With a stack |
| 2:15 | One warning |
| 2:33 | One pile, three rules |
| 2:54 | Three searches |
| 3:08 | The stack: depth-first |
| 3:27 | The stack's tree |
| 3:40 | Now the queue |
| 3:54 | The queue: one stop away |
| 4:09 | The queue: two stops away |
| 4:28 | The queue: three stops away |
| 4:42 | Two trees |
| 4:55 | Why the queue is special |
| 5:16 | Best-first search |
| 5:49 | Problem: a second network |
| 6:09 | The loop around the search |
| 6:22 | The loop in Python |
| 6:40 | Counting the networks |
| 7:00 | Directed graphs |
| 7:14 | Run it from Arch |
| 7:28 | The tree of what Arch reaches |
| 7:43 | Paint bucket as a graph |
| 8:03 | Recolor as we mark |
| 8:17 | A reduction |
| 8:38 | Recap |

Rebuild: `python build.py all`. Check names: `python ../common/transcribe_beats.py <beat id>`.
