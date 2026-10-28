# October 26: strongly connected components

Status: sources fetched, narration draft complete, algorithm trace checked. Awaiting script approval under video-framework.md §10 before any draft or final render.

## Learning objectives

After watching, reconstruct the three components in today's drawing; explain why DFS from d crosses component boundaries; distinguish edge reversal from reversing finish order; trace both passes; explain global assigned versus current component; justify O(V+E); distinguish sink-first and source-first variants; explain why a DAG of components does not automatically solve cyclic recurrences.

Prerequisites: following arrows and reading short Python loops. DFS, postorder, DAG, topological order, source, sink, and strong connectivity are defined within the narration. The prior video callback is useful but not required.

## Sources and fidelity

- Live class notes fetched October 26, 2026: https://docs.google.com/document/d/e/2PACX-1vSXfd6_O8lX7PtNtGEqH2fwBORadFJiDb2uKQzYpbp9AOahvHr_CvQJctE5ifhrJdDrcnrpkoIvPZ28/pub
- Snapshot: sources/class-notes.html and sources/class-notes.txt. Relevant heading Monday 10/26/2026; blank Friday heading precedes it.
- Embedded class drawing downloaded to sources/class-drawing.png. It contains seven vertices and eleven directed edges. Preserve vertex positions. Explicitly add only a→c as a dashed teaching edge for the standing twelve-edge video minimum. Independent checks confirm unchanged components and component graph.
- JEA local textbook §6.5–6.6, printed pp.237–241 / PDF pp.255–259. Focus is definitions and Kosaraju–Sharir, not Tarjan.
- Prior series: output/advanced-algorithms-2026-10-22, especially video 06. Reuse Ava and shared animation/subtitle engine after approval.
- Canvas class-23 page is linked in the notes but has not been fetched; do not claim its updated drawing was inspected. Use the actual embedded drawing, explicitly described in the notes as closest to the class version.
- Existing SCC assignment spec describes the opposite valid pass orientation. Beat 32 explains both; the learning video does not change coursework.

## Coverage checklist

| Topic | Treatment |
|---|---|
| Reachability versus mutual reachability | Covered 03–06, 10–12 |
| Maximal SCCs, singleton components | Covered 05–06 |
| Equivalence relation formal proof | Skipped: mutual-reachability definition and maximal grouping suffice for this lesson |
| Condensation graph and acyclicity, Fig.6.13 | Covered 07–09 using class drawing |
| Single-component two-way reachability method | Used as independent trace oracle; skipped in narration to keep one algorithm in focus |
| SCC connected subtree / Lemma 6.2 / Fig.6.14 | Skipped detailed proof; proof focuses on component finishing maxima |
| Sink peeling / Fig.6.15 | Covered 13–15, 28–30 |
| Source has last finish / Lemma 6.3 | Covered 24–26 with two-case component argument |
| Reversal preserves SCCs | Covered 16 |
| Kosaraju–Sharir two passes / Fig.6.16–6.17 | Covered 17–30, 33–35 with today's drawing |
| Reverse postorder of reversed graph is not original postorder | Covered through explicit graph and order pairing in 22–23,32 |
| Component labeling and deduplicated meta-edges | Covered 07,28–32; full implementation not read aloud |
| Runtime and traversal state | Covered 27–30,33–35 |
| Connection to memoization and limits | Covered 36–37 |
| Tarjan / lowlink, later §6.6 material | Skipped: separate algorithm, not required for today's two-pass explanation |

## Checked trace

DFS uses alphabetical outer-loop order and adjacency insertion order in trace_check.py.
Finish order on reversed teaching graph: b,c,a,e,d,g,f.
Pop order: f,g,d,e,a,c,b.
Original-graph components in discovery order: [f,g], [d,e], [a,b,c].
Topological component order: [a,b,c], [d,e], [f,g].
Original class graph and teaching variant independently checked against mutual reachability. Empty graph, isolated vertex, self-loop, and disconnected cycle cases pass.

## Render and QA remaining after approval

1. Turn script beats into the existing engine's word-cued storyboard, keeping narration as the source of truth.
2. Inspect actual voice duration; if above ten minutes, trim repetition or propose a split before rendering final.
3. Render draft; inspect graph arrows, both reversal operations, stack top, prediction state, captions, and three cue-time frames.
4. Validate spoken vertex names, caption bounds, code cards <=12 lines, and all values against trace.json.
5. Render 1920×1080, 30 fps MP4, Ava -4%, normalized audio, burned captions plus SRT and README chapters.

No video or audio has been rendered yet. After-watching reflections remain for Samuel to supply.
