# Kruskal's algorithm — October 12, 2026 class graph

The MP4 is a narrated, animated walkthrough of the graph embedded in the
[Advanced Algorithms Class Notes](https://docs.google.com/document/d/1myCP67cjrqx2AyWydVwta9xzXENrrA1kTPUHECX5j5I/edit).
Its node positions and edge set follow the class drawing. The weight badges,
especially **11** on E–G, have been moved away from the lines for legibility.

The C–E line has no visible weight in the source image. At the user's request,
this version assigns it **17** without changing the graph's topology or shape.
The original MST costs **38** and the D–E cost-6 hypothetical MST costs **35**.
Both totals now account for every edge in the drawn graph.

At each considered edge, the video shows `find` results before the decision,
the `union` or cycle skip, and the disjoint-set forest after it. Colored graph
edges and node outlines distinguish the current trees. In the hypothetical,
the D–E tree is purple until E–F bridges it to the teal tree.

The Python section treats each edge as `(cost, start, end)`. A named
`edge_cost` function makes the sort rule explicit, and an ordinary loop
initializes the first solution's group labels. The comparison then explains
`DisjointSet`: `find` returns a tree's representative, while `union` merges
different trees and reports whether the edge was accepted.

The alternate run changes only D–E from 9 to 6. D–E and H–F are then tied at
6, so either may be processed first. Both are accepted in this example.

Chapters: 0:00 MST problem; 0:32 Kruskal's forest and union-find rule; 1:09
first selections and cycle rejection; 1:39 class tree completion; 2:10
cost-6 hypothetical; 2:44 greedy hallmarks; 3:21 naive Python; 4:04
side-by-side union-find comparison.

Files:

- `Kruskal - October 12 Class Graph - Revised Code.mp4` — final video with
  the clearer Python explanation.
- `kruskal_solutions.py` — complete runnable naive and union-find solutions.
- `narration.json` — exact spoken transcript by scene.
- `render_video.py` — reproducible animation and video assembly.
- `source-class-graph.png` — the graph as embedded in the class notes.
- `poster.png` — opening-frame preview.

The MP4 uses generated voice tracks from the AI Voice Generator plugin and
Pillow/FFmpeg for animation. To rebuild, put the eight scene MP3s in `voice/`
and run `python render_video.py`.
