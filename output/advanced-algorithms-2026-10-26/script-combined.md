# Reading DFS: From the Call Stack to Components and Cut Vertices

Combined script for the October 26 and 28 lessons. Supersedes the SCC-only narration in script.md. Samuel approved the interpretation and authorized rendering after applying his neutral, descriptive phrasing throughout. Final video target: ten minutes.

Teaching voice: describe what the picture shows, ask a concrete question, then derive the condition. Prefer “goes through,” “stays within,” “already recorded,” and “another route” to metaphors about force, mistakes, refusal, escape, or vulnerability. Introduce formal necessity through the precise statement “every path passes through this vertex.”

Goal: make Chapter 6 fast to read with understanding, rather than replace its proofs. Ava, -4%; target 8–10 minutes, subject to measured speech duration. Render 1080p/30 fps with word-synced cues, captions, persistent state, and five five-second prediction holds. Break each numbered passage into 15–35-word animation beats. No full implementation walkthrough: use the saved time to teach how to read the figures and proof claims.

## Visual and source contract

Keep the graph currently being discussed visible. Explicitly switch among three views: the actual Figure 6.4; Monday's class drawing and its component graph; an undirected version of Monday's drawing. These changes serve the user's combined-lesson request. Never silently treat a directed picture as undirected or a cyclic graph as a DAG. Preserve original layouts. The existing dashed a→c teaching addition may appear only when labeled; it changes none of the conclusions. Do not pretend the component graph preserves original path counts.

Figure 6.4: local JEA PDF page 247, printed page 229. Paths/cut vertices: Exercises 3–4, PDF pages 263–264, printed pages 245–246. SCCs: §§6.5–6.6, PDF pages 255–259. Today's raw notes and rendered textbook pages are in sources/2026-10-28/.

The 40-word rationale below is an inference from notes and textbook context, not a recovered quotation from the instructor. The paths formula applies to a DAG with fixed endpoints. Runtime statements count arithmetic operations; exact path counts can require large integers.

## 01 — One search, several questions

Visual: Monday's graph; highlight d→e→f→g.

“Start at vertex D in Monday's drawing. Following arrows reaches E, F, and G. But reaching somewhere, returning from somewhere, and going through somewhere are different questions. Both class periods used depth-first search to make those differences visible.”

## 02 — Open the chapter's picture

Visual: Figure 6.4, graph above and interval bars below. Reveal title and PDF-page chip.

“Open Figure six point four. Above is a directed graph: vertices joined by one-way arrows. Below are bars recording the search. Depth-first search follows an unexplored neighbor, finishes that exploration, then returns. Let's connect the arrows to the bars.”

## 03 — Arrival and return

Visual: grow the bar for a, then b, then f. Show active call stack alongside.

“A bar opens when the recursive call begins and closes when it returns. The left endpoint is the starting time, called pre. The right endpoint is the finishing time, called post. A call stays active while it waits for calls below it.”

## 04 — Read nesting

Visual: highlight h=[6,17], d=[7,8], l=[9,16]. Prediction chip, five-second hold.

“Vertex H starts at six and finishes at seventeen. Vertex D's whole interval fits inside it. So does vertex L's. Which one finishes first? And can D still be active when L starts? Read the endpoints before answering.”

“D finishes at eight, before L starts at nine. Both are descendants of H in the search tree. Recursive calls nest or finish before another begins. Their active intervals cannot partly overlap like two sliding windows.”

## 05 — What the discovery tree records

Visual: distinguish solid discovery edges from dashed non-tree edges in the actual figure.

“The solid arrows record which call first discovered each vertex. They form a forest: one or more search trees. The other arrows still exist in the graph. A visited mark prevents another recursive call, not another incoming edge.”

## 06 — Three states explain the arrows

Visual: new/active/finished legend, then d→c as a back edge. Keep call path visible.

“A vertex is new, active, or finished. An arrow back to an active ancestor closes a directed cycle: the search already followed a path down to us. An arrow to a finished vertex need not close a cycle. ‘Visited’ alone hides that distinction.”

## 07 — Read Figure 6.5 next

Visual: identify a tree, forward, back, and cross edge on Figure 6.4; use names from Fig.6.5 as legend.

“The book names four edge types. Tree edges discover children. Forward edges lead to other descendants. Back edges lead to ancestors. Cross edges connect different branches or trees. The timestamps let you recognize these relationships without trusting how the graph is drawn.”

## 08 — Finish order becomes a schedule

Visual: return to Monday's picture; show its three component outlines only after explaining return paths.

“In a graph without directed cycles, reading finish order backward puts every vertex before its outgoing neighbors. That's a topological order. For a recurrence whose arrows point to needed subproblems, evaluate in the opposite order: finish the needed values before using them.”

## 09 — Group the return journeys

Visual: trace a→b→c→a, d↔e, f↔g; collapse to ABC→DE→FG plus ABC→FG.

“Monday's graph has cycles. A, B, C can all reach one another; D and E can return to each other; so can F and G. These maximal return-trip groups are strongly connected components. Collapse them into boxes. The box graph has no directed cycles.”

## 10 — Why the boxes cannot cycle

Visual: hypothetical return arrow between boxes, then merge outline and undo.

“If several boxes formed a cycle, we could travel around it and return. Those boxes would belong to one larger component. This is why we can order the components even though we cannot topologically order the original vertices.”

## 11 — What does this search collect?

Visual: original d highlighted; show question before five-second hold.

“Does one DFS from D collect exactly its strongly connected component? Trace every reachable arrow. It reaches D, E, F, and G. That's two components. A DFS tree records discovery; a strongly connected component requires return journeys.”

Production: pause after the question, before revealing the final three sentences.

## 12 — A search that stays within one group

Visual: fg as sink; then de as sink after fg is assigned.

“Starting in F-G visits both vertices and stays within their group. No edge points to another component, so this is a sink component. Record F and G as assigned. A search from D then collects D and E, skipping the vertices already recorded.”

## 13 — The two reversals

Visual: reversed-graph badge; checked finish stack b,c,a,e,d,g,f; then original-graph badge and stack pop animation.

“Reverse the arrows and run DFS over every vertex, recording vertices when they finish. Our stack is B, C, A, vertex E, D, G, F. Return to the original graph and pop. F comes first, then the next unassigned start is D, then A.”

“Reversing arrows swaps source and sink components. Decreasing finishing time selects source components of the reversed graph, which are sinks of the original. Popping already reverses finishing order. That explains Monday's ‘no need to reverse’ note.”

## 14 — What to watch for in the proof

Visual: component arrow X→Y with maximum finishing times; use existing component boxes.

“Across an arrow between distinct components, the upstream component has the greater maximum finishing time. If explored first, it finishes after exploring downstream. If downstream is explored first, it cannot reach upstream and finishes earlier. That's the ordering fact to watch for in the proof.”

## 15 — Keep the passes separate

Visual: first-pass visited cleared; global assigned retained across new component lists.

“Start fresh discovery state for pass two. Keep one assigned set across all components, but a new list for each component. Each pass checks vertices and edges once. That's linear time: big O of V plus E.”

## 16 — What today's shorthand probably meant

Visual: quote the notes' fragments, then show fixed endpoints s and t on component graph.

“Your notes mention counting paths to and from vertices, multiplying those counts, and removing vertices. The chapter’s nearby exercise asks which vertices every source-to-target path crosses. Together, these suggest counting paths through each vertex, then comparing with all complete paths.”

Production: this paragraph is the accepted 40-word rationale. Label it “Interpretation of the notes.” It explains the inference, not a proof of the formula.

## 17 — Define to, from, and through

Visual: treat the component graph as its own DAG: s=ABC, middle=DE, t=FG. Persistent badge “Counting paths in THIS DAG.”

“Use our three-box DAG as a graph in its own right. Call the first box the start and the last the destination. ‘To’ counts paths from the start to a chosen box. ‘From’ counts paths from that box to the destination.”

“Every complete path through the box splits uniquely into one prefix and one suffix. In a DAG, joining them cannot repeat another vertex: that would create a cycle. So paths through equals paths to multiplied by paths from.”

## 18 — Compute both directions

Visual: to counts [1,1,2], from counts [2,1,1]; animate arrows for each addition.

“Give the start one empty prefix. Add incoming counts in topological order. Give the destination one empty suffix, then add outgoing counts in reverse order. The middle box has one path to it and one from it. Their product is one.”

## 19 — How many routes use the middle?

Visual: show both complete routes, total=2, through-middle=1; five-second prediction hold.

“There are two complete routes: directly across the shortcut, or through the middle. How many go through the middle? One of the two. Now remove the shortcut. One route remains, and it passes through the middle. Comparing these counts tells us whether every route uses that vertex.”

Production: pause after the question before revealing the answer. Count only paths in this DAG, not routes inside the original SCCs. For an interior vertex, equality identifies a vertex that every complete path uses when at least one start-to-destination path exists.

## 20 — A different removal question

Visual: restore Monday's full drawing; explicitly remove arrowheads, merging reciprocal edges. Badge “UNDIRECTED VERSION.”

“Now switch to an undirected graph: connections work both ways. Remove F from this picture. G becomes separated from the other vertices. A vertex whose removal disconnects a connected graph is called a cut vertex. We can study that change using a DFS tree.”

## 21 — Why the DFS root is special

Visual: DFS rooted at f; children b and g. Show first branch containing a,b,c,d,e and second containing g. Five-second prediction hold.

“Start DFS at F. One child branch explores the five vertices on the left. Another explores G. Could an edge join these branches without passing through F? If it did, DFS would have followed it and discovered them in the same branch.”

“That's why an undirected DFS root is a cut vertex exactly when it has at least two children in the DFS tree. Count tree children, not graph neighbors. With only one child, the remaining tree stays connected after removing the root.”

## 22 — For other vertices, look for another connection

Visual: highlight child subtree and possible back edge strictly above parent; keep original edges distinct from hypothetical arrow.

“For a non-root vertex, look for a connection from a child subtree to an ancestor above it. That connection gives the subtree another route to the rest of the graph. If one child subtree has no such connection, removing the vertex separates that subtree.”

Production: define low[v] only in the reading guide: earliest discovery time reachable from v's subtree via tree edges down and at most one back edge; ignore the undirected parent edge. Non-root v is a cut vertex when some child c has low[c] >= pre[v]. Full low-value implementation is outside this primer. The local PDF's Exercise 4(b)(ii) appears to have a negation error: its printed connection condition characterizes NOT being a cut vertex. Display a short reading note, not the incorrect claim as fact.

## 23 — Read the chapter with questions in hand

Visual: reading route with sections and PDF pages; keep graph inset.

“Read section six point one asking what the bars reveal about ancestry. In six point two and six point three, connect back edges to cycles and finish order to schedules. In six point four, connect those schedules to cached answers.”

“Then read six point five and the two-pass algorithm in six point six: why do return-trip groups form a DAG, and why does the next search stay inside one group? Finish with Exercises three and four: count paths through vertices, then study what changes when a vertex is removed.”

## 24 — Retell the connection

Visual: three captions: discovery tree / evaluation order / safe component start.

“DFS records who discovered whom and when each call finished. Those records explain the chapter's bars, dependency orders, and component searches. Today's removal questions ask whether another route exists. On paper, draw the root's two child branches and explain what remains when you remove the root.”

## Reading route and honest limits

- §6.1: PDF 245–248, especially Fig.6.4 on 247. Covered: timestamps, nesting, forest, vertex states, edge types; Lemma 6.1 full equivalence proof left for reading.
- §§6.2–6.3: PDF 249–251. Covered: back-edge cycle connection, reverse finish order; full cycle reconstruction and array implementation left for reading.
- §6.4: PDF 252–254. Brief callback only; full longest-path worked example remains in prior video 06.
- §§6.5–6.6: PDF 255–259 for definitions and Kosaraju–Sharir. Covered: SCCs, condensation, sink peeling, pass orientation, finishing-max proof idea, state, runtime. Tarjan and its implementation left for later reading.
- Exercises 3–4: PDF 263–264. Covered: DAG path-through formula, unavoidable vertices, undirected root criterion, non-root connection intuition. Full cut-vertex implementation left as follow-on material.

Verification complete: combined_trace_check.py reproduces both traversal orders printed under Fig.6.4, checks the three narrated intervals, computes both DAG count tables, and verifies the undirected root's two children and connectivity after removal. Results are saved in combined-trace.json. Monday's SCC trace remains checked separately. The rationale is exactly 40 words; the final narration is in transcript.md. Rendering authorized by Samuel after the tone revision. The final timeline is 600 seconds; visual and selected pronunciation checks are recorded in README.md. These are educational extensions grounded in the book, not claims that the short October 28 notes contain a complete lecture transcript.
