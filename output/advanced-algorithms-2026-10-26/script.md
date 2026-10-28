# When DFS Finds Too Much: Strongly Connected Components

Status: complete narration draft for Samuel's review; not approved or rendered.
Voice: Ava, -4%. Target: 8–10 minutes including five 5-second prediction pauses.
Each numbered beat is one visual change; narration is the quoted text.
Letters are spoken as “vertex A”, “vertex B”, etc., preserving lowercase labels in the drawing.

## Visual contract

Keep the October 26 drawing visible throughout. Use its original positions and eleven solid arrows. One dashed purple arrow, a→c, is an explicitly labeled teaching addition to meet the standing twelve-edge minimum; it changes neither the components nor the component graph. Introduce it in beat 02. Never present it as part of the original notes.

Use a courier on one-way streets: intersections are vertices, streets are directed edges. The courier only points to the current vertex; avoid extra story exposition. Right panel: graph being searched, current recursive path, finish stack, assigned vertices, current component. Show only the relevant rows until introduced. Keep the original/ reversed badge visible during every pass. Stack top is at the right.

Use word-boundary cues on the named vertex, edge, or state change. Subtitles occupy their own bottom band. Each prediction holds the complete question and graph, then gives five silent seconds. Reveal answers in the next beat. Values come from trace.json, never separately typed into animation logic.

## 01 — The question in your drawing

Visual: original graph, d highlighted; reveal d→e→f→g as spoken.

“Here’s your drawing from today. A courier starts at intersection D and follows the one-way streets. D can reach E, then F, then G. But can the courier get back? That question changes what we should group together.”

## 02 — Fix the example

Visual: pair ‘intersection / vertex’ and ‘one-way street / directed edge’; reveal dashed a→c.

“Intersections are vertices. One-way streets are directed edges. This dashed edge, from vertex A to vertex C, is my teaching addition. Solid arrows reproduce your drawing. The groups stay unchanged.”

## 03 — Return trips

Visual: trace d→e and e→d, then e→f; leave return route from f absent.

“Vertex D reaches vertex E, and vertex E reaches vertex D. They belong together. Vertex E also reaches vertex F. But vertex F cannot get back to vertex E. Being reachable in one direction isn’t enough.”

## 04 — Predict the groups

Visual: PAUSE AND PREDICT; question ‘Which vertices can reach each other in BOTH directions?’

“Look for the largest groups where every vertex can reach every other vertex. Routes can use several edges. How many groups do you see? Pause and trace the return journeys.”

Pause: 5 seconds.

## 05 — Give the groups a name

Visual: enclose abc, de, fg in distinct outlines; show no new arrows.

“There are three: A, B, C together; D and E together; F and G together. These are strongly connected components. ‘Strongly connected’ means reachability both ways. ‘Component’ means the entire group, not a smaller selection we could still enlarge.”

## 06 — Why this is more than spotting circles

Visual: emphasize paths a→b→c→a; then put all three inside one boundary.

“Group by return journeys, not circles drawn on paper. Cycles sharing vertices belong to one larger group. A vertex without return-trip partners forms a component by itself.”

## 07 — Collapse the picture

Visual: ease groups into three boxes, retain original drawing as persistent inset. Deduplicate the two abc→de arrows.

“Shrink each group into one box. Keep arrows between different boxes, and merge duplicates. We get A-B-C to D-E, D-E to F-G, and a shortcut from A-B-C to F-G. This smaller picture is the component graph.”

## 08 — Why the smaller graph cannot cycle

Visual: hypothetical dashed arrow fg→abc, with round-trip route highlighted; then remove it.

“Suppose these boxes formed a directed loop. We could travel from any box around the loop and return. Then all those boxes should have been one component. So the component graph has no directed cycles: it’s a directed acyclic graph, or DAG.”

## 09 — Bridge from the earlier videos

Visual: expand boxes back into original graph; show outgoing arrows from d.

“A topological order puts each vertex before everything it points to. Cycles make that impossible here. But the component graph has a topological order. How do we discover its boxes?”

## 10 — What DFS actually promises

Visual: cursor d; current recursive path panel starts [d].

“Depth-first search, or DFS, explores a neighbor, then comes back. Returning connects DFS to backtracking. It discovers reachable vertices, without checking whether they can return to the start.”

## 11 — Predict the mistake

Visual: PAUSE AND PREDICT; d highlighted, all graph arrows available.

“Suppose we start at vertex D and call everything this search discovers one component. Will that produce the correct group? Trace every outgoing edge before answering.”

Pause: 5 seconds.

## 12 — Watch it fail

Visual: progressive d,e,f,g discovery, four vertices in current search, de and fg boundaries preserved.

“The search reaches D, E, F, and G. It has crossed from one component into another. The DFS worked; our interpretation failed. To collect exactly one component, we need a starting group the search cannot escape.”

## 13 — Start at a sink

Visual: fg boundary highlighted; component graph fg has no outgoing arrows.

“The F-G group has no edge leaving for another component. That makes it a sink component. Starting anywhere inside it reaches all of that group and nothing outside. Internal arrows are allowed. ‘Sink’ describes the box, not each individual vertex.”

## 14 — Remove without deleting

Visual: fg fades and receives assigned marks; de becomes remaining sink.

“Mark F and G assigned. Future searches skip them. Now D-E is a sink among the remaining groups. We can peel off components without deleting vertices.”

## 15 — The missing ingredient

Visual: full graph restored; question ‘How do we find a sink without knowing the groups?’

“We used the answer to choose our start. How can the computer find a sink before knowing the components? Two different reversals supply the missing ingredient.”

## 16 — Reverse edges

Visual: all edge arrowheads animate to opposite ends; badge ‘PASS 1: REVERSED GRAPH’.

“First reverse every edge. Keep every vertex. Return journeys remain return journeys, so the strongly connected groups stay the same. But arrows between groups flip. A sink in the original graph becomes a source in the reversed graph.”

## 17 — Define source and finishing

Visual: fg outlined as source of reversed component graph; introduce empty finish stack.

“A source component has no incoming edge from another component. Now run DFS over the whole reversed graph. Whenever a call has checked every neighbor, it finishes. We record its vertex then, not when we first arrive.”

## 18 — First tree, slowly

Visual: reversed edges a→c→b, active path [a,c,b].

“Use alphabetical starting vertices and the neighbor order shown here. Start at vertex A. The reversed arrows take us to vertex C, then vertex B. Vertex B points back to an already visited vertex, so that call doesn’t start again.”

## 19 — Finish, then backtrack

Visual: append b,c,a individually to finish stack as calls return.

“Vertex B finishes first. Put it on the stack. Return to vertex C; its remaining neighbor is already visited, so C finishes. Then A finishes. The stack now reads B, C, A. Recording on return gives postorder.”

## 20 — Finish the whole graph

Visual: event-driven trace d→e and f→g, stack becomes b,c,a,e,d,g,f.

“The outer loop continues. Vertex D starts the next search: E finishes, then D. Vertex F starts the last: G finishes, then F. The finish stack is B, C, A, E, D, G, F. One starting vertex wasn’t enough.”

## 21 — Predict the next start

Visual: PAUSE AND PREDICT; stack right end marked TOP; original graph shown beside reversed inset.

“The last vertex pushed is F. When we return to the original graph, which component will a search from F collect? And why does that starting point protect us from the earlier mistake?”

Pause: 5 seconds.

## 22 — Pop reverses the order

Visual: pop f; original badge restored; fg highlighted.

“It collects F and G, our sink component. Here’s the second reversal: popping a stack reads finishing order backward. We already reversed the edges. Now the stack reverses the order. Those are different operations.”

## 23 — Resolve the note

Visual: equivalence ‘append on finish + pop’ = ‘reverse finish list + iterate’; cross out ‘reverse list + pop’.

“Your note says, ‘No need to reverse.’ That works if we pop the finish stack. If we walk a list from left to right instead, we must reverse it first. Don’t reverse the list and then pop: that reverses the order twice.”

## 24 — Why last finish works, first case

Visual: reversed component arrow X→Y illustrated using de→abc; annotate greatest finish per group.

“Consider groups X and Y in the reversed graph, with an arrow from X to Y. If DFS reaches X first, it explores Y before X's starting call finishes.”

## 25 — Why last finish works, other case

Visual: same two groups, Y completed before X starts; keep original graph inset.

“If DFS reaches Y first, Y cannot reach X. Otherwise they would be one group. Y therefore finishes before X is explored. In either case, X has the later maximum finishing time. The greatest remaining finish belongs to a source group.”

## 26 — Translate back

Visual: reverse component arrows back; fg is sink again.

“A source of the reversed component graph is a sink of the original. That’s why we pop F first. After removing its group, the same ordering argument picks a sink among what remains. We need component finishing maxima, not a topological order of individual cyclic vertices.”

## 27 — Keep the two passes separate

Visual: clear first-pass visited marks; retain finish stack; introduce assigned={} and component=[].

“Keep the stack, but start fresh discovery state. Reusing the first pass's visited set would skip everyone. Visited for ordering and assigned to a component answer different questions.”

## 28 — Collect F-G

Visual: pop f, collect f,g, components=[[f,g]]; then pop g and skip it.

“Pop vertex F. Start an empty component, add F, follow its edge to G, and add G. G points to F, which is already assigned. Save this two-vertex component. Next pop G. It’s already assigned, so no new component starts.”

## 29 — Collect D-E

Visual: pop d, collect d,e; e→f grays on encounter; save second component.

“Next pop D. Collect D and E. E has an edge to F, but F is already assigned. That edge no longer lets this search escape into another uncollected group. Save D-E. Then pop E and skip it.”

## 30 — Finish the peel

Visual: pop a, collect a,b,c; outgoing cross-component edges skipped; pop c,b and skip.

“Pop A. Collect A, B, C. Their outgoing edges meet assigned vertices. Save this group; skip the remaining stack entries. Keep one global assigned set and a fresh list per component.”

## 31 — Predict the output order

Visual: PAUSE AND PREDICT; component list fg,de,abc beside original component arrows.

“We discovered F-G, then D-E, then A-B-C. Does that list put every component before the components its arrows point to? Or do we need to read these three groups in the other direction?”

Pause: 5 seconds.

## 32 — Two valid orientations

Visual: reverse component list to abc,de,fg; side-by-side two-pass orientation diagram.

“Our version produces sinks first, so reverse the component list for topological order. Another valid version searches the original graph first, then the reversed graph in decreasing finish order. That version produces original source components first. Keep each version’s two passes paired.”

## 33 — The Python finish hook

Visual: show only finish_order's inner visit helper from trace_check.py, eight lines; highlight visited.add, recursive call, then finished.append in successive cues.

“In the teaching Python, visited dot add marks arrival. The recursive call explores an unvisited neighbor. Finished dot append comes after the loop, when every neighbor has been checked. Moving that append before the loop would record arrival order, which isn’t the ordering this proof uses.”

## 34 — The Python collection hook

Visual: show collect_components' inner collect helper, up to twelve lines; values now: vertex=e, component=[d,e], assigned=[d,e,f,g].

“The collector records a vertex in assigned and in the current component. Assigned answers whether any component has already claimed it. Component records only this search’s new vertices. At vertex E, F is assigned, so we skip that edge. We do not clear assigned between components.”

## 35 — Why the time stays linear

Visual: counters for reversal, pass one, pass two; V=7, E=12 for teaching variant.

“Reversal scans vertices and edges once. Each DFS pass discovers each vertex once and checks each edge once. Total time: big O of V plus E, for V vertices and E edges.”

## 36 — Connection to memoization, with a boundary

Visual: component graph with internal fg cycle still visible; label ‘Order between groups ≠ solve inside group’.

“Earlier, memoization filled a value after its dependencies were ready. Cyclic dependencies can make that evaluation wait on itself. DFS avoids repeated visits by marking arrival. Collapsing components exposes an order between cyclic groups, but does not solve the equations or dependencies inside each group.”

## 37 — Clarify the recursion claim

Visual: labels ‘full subproblem state’ and ‘decreasing progress measure’; no new example graph.

“Ordinary terminating recurrences need acyclic dependencies between full subproblem states. Recursive DFS can still search a cyclic input graph: marking arrival prevents it from recursing into an already visited vertex.”

## 38 — Retell and try

Visual: original drawing, three component outlines, both-pass badges, paper exercise.

“DFS from D crossed component boundaries. Reversing edges and popping finish order selected sinks safely. Peeling those sinks recovered all three groups. Try removing the edge from E to F: which groups and ordering constraints change?”

Exercise answer for README, not spoken immediately: remove e→f. Components stay abc, de, fg. The meta-graph has abc→de and abc→fg; de and fg may appear in either topological order.
