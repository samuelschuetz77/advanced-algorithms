# Series plan: Graph search, DFS, and topological order (2026-10-22)

Spec for every video: `advanced algorithms/video-framework.md`.
Status: scripts first, nothing rendered until Samuel approves each script.

## The six videos

| # | Title (working) | Source | What the viewer can do afterward |
|---|---|---|---|
| 01 | Whatever-First Search, Part 1: The Naked Mole-Rat Colony | JEA 5.5 (PDF 217-219), Lemma 5.1 | Run the bag algorithm by hand on a 7-chamber, 12-tunnel colony; explain why it marks exactly the reachable vertices; read the Python. |
| 02 | Whatever-First Search, Part 2: One Algorithm, Four Searches | JEA 5.5 analysis, 5.6, 5.7 (PDF 219-223) | Say what changes for stack / queue / priority queue; count why it is O(V + E T); handle disconnected and directed graphs. Uses the page-1 drawing from the 10/19 notes. |
| 03 | Class 21 Lab: count_paths and the Diamond | Mini lab Part 1, class 21 page | Explain the naive explosion, the cache, and why O(V + E). Walk the diamond and the ladder. |
| 04 | Class 21 Lab: topo_order and the E Graph | Mini lab Bonus, Samuel's 10/19 drawings | Redo the professor's hand walk on the A-B-C-D graph and the E graph; see why preorder fails and reverse postorder works; fix the `topo_order` bug and the test. |
| 05 | Reading Primer: 6.1 and 6.2, Preorder, Postorder, Cycles | JEA 6.1-6.2 (PDF 245-250) | Stamp preorder and postorder times; classify the three vertex states; detect a cycle from an edge to an active vertex. |
| 06 | Reading Primer: 6.3 and 6.4, Topological Sort and DP in DAGs | JEA 6.3-6.4 (PDF 251-254) | State and justify "reverse postorder = topological order"; see memoization as DFS order over a DAG (links back to 03). |

Overlap is intentional. 03 and 04 replay what happened in class on Samuel's own
code. 05 and 06 are the book's definitions and proofs so the Friday reading
(Learning Log 11, due Fri 10/23 11:59pm Mountain) lands.

Suggested watch order: 01, 02, 05, 03, 04, 06. (Search first, then the
vocabulary of the reading, then the lab it makes sense of, then the proof.)
Samuel decides; the numbering stays as above either way.

## Shared anchors across the series
- **The Colony** (video 01): a naked mole-rat colony, 7 chambers (S, A to F) joined by 12 tunnels, plus a burrow X-Y cut off by a cave-in. Story words: chamber = vertex, tunnel = edge, scent mark = mark, token pile = bag.
- **Page-1 graph** from the 10/19 notes (video 02): B to D, D to A, D to E,
  A to B, A to C, C to B, C to E, with the stack drawing. Edge directions read
  from the drawing; to be confirmed.
- **A-B-C-D graph** and **E graph** from the 10/19 notes (videos 04 to 06).
- **Diamond** `g` and **ladder** from the lab (video 03).

## Open decisions for Samuel
1. Voice: **Ava** (chosen). Series-wide.
2. Length: scripts target 7 to 10 minutes each. OK, or shorter?
3. Watch order (above).
4. Is the page-1 edge reading correct?

---

## Status (2026-10-22): all six videos built

| # | Folder | Anchor story | Length |
|---|---|---|---|
| 01 | `01-whatever-first-search-part-1` | Wrinkles the naked mole-rat, colony of 7 chambers / 12 tunnels | 10:48 |
| 02 | `02-whatever-first-search-part-2` | City metro map, 7 stations / 12 tracks (redone from a school-rumor version); also a pixel grid | 8:59 |
| 03 | `03-class-lab-count-paths` | Hopper the frog on stepping stones; your diamond; a 7-junction / 12-trail hiking map | 8:54 |
| 04 | `04-class-lab-topo-order` | Morning routine (your A-B-C-D graph); Priya's dinner (7 tasks / 12 rules) plus a second start task, 'set the table', for the two start-order cases | 8:24 |
| 05 | `05-primer-preorder-postorder-cycles` | Ada and a ball of thread in a 7-room / 12-door maze | 8:24 |
| 06 | `06-primer-toposort-and-dp` | The hiking map from 03 again, with scenery scores, now drawn tangled (arrows in every direction) | 12:17 |

Samuel's notes (2026-10-22): video 01 "great", but pronounce A as "ay" and fix E; "don't reuse the mole rat" for the rest; "don't stop till all 6 are made". All applied. Video 06 deliberately reuses video 03's hiking map (a callback so longest path lands on a known graph); change it if that counts as reuse.

Video 02 was redone on 2026-10-22 as a metro map because Samuel found the rumor / telling / parent example muddled (old version in `02-.../superseded_rumor_version/`). The whole `output` folder now lives inside `advanced algorithms/`.

Video 04 was patched on 2026-10-22: the E-graph cases (E was the only start task) were replaced by dinner plus 'set the table', which has two start tasks, so the loop can start at either and the start order fails in both cases. Your E drawing is no longer shown.

Video 06's opening was rewritten on 2026-10-22: the old 'why a cycle breaks it' wording was unclear, so it now shows a tangled drawing of the hiking map sliding into a line, then a concrete three-task cycle where nobody can go first. The map is drawn with arrows in every direction (not all pointing right) in every beat of video 06. The video is now 12:17, further over the 10 minute cap.

Not done: the page-1 drawing (stack plus search tree) was never used on screen, because its edge directions were unconfirmed. Video 02 uses a metro graph instead.

## After-watching notes
(append: what clicked, what is still fuzzy)
