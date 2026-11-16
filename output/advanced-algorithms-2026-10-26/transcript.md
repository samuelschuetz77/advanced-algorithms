# Chapter 6: Two Lessons in Ten Minutes

## Three path questions

Start at vertex D in Monday's drawing. Following arrows reaches E, F, and G. But reaching somewhere, returning from somewhere, and going through somewhere are different questions.

Both class periods used depth-first search to make those differences visible.

## Figure 6.4

Open Figure six point four. Above is a directed graph: vertices joined by one-way arrows. Below are bars recording the search. Depth-first search follows an unexplored neighbor, finishes that exploration, then returns.

Let's connect the arrows to the bars.

## Arrival and return

A bar opens when the recursive call begins and closes when it returns. The left endpoint is the starting time, called pre. The right endpoint is the finishing time, called post.

A call stays active while it waits for calls below it.

## Nested calls

Vertex H starts at six and finishes at seventeen. Vertex D's whole interval fits inside it. So does vertex L's. Which one finishes first?

[Five-second prediction pause.]

And can D still be active when L starts?

[Five-second prediction pause.]

Read the endpoints before answering.

D finishes at eight, before L starts at nine. Both are descendants of H in the search tree. Recursive calls nest or finish before another begins.

Their active intervals cannot partly overlap like two sliding windows.

## The discovery forest

The solid arrows record which call first discovered each vertex. They form a forest: one or more search trees. The other arrows still exist in the graph.

A visited mark prevents another recursive call, not another incoming edge.

## Three vertex states

A vertex is new, active, or finished. An arrow back to an active ancestor closes a directed cycle: the search already followed a path down to us.

An arrow to a finished vertex need not close a cycle. ‘Visited’ alone hides that distinction.

## Four edge types

The book names four edge types. Tree edges discover children. Forward edges lead to other descendants. Back edges lead to ancestors. Cross edges connect different branches or trees.

The timestamps let you recognize these relationships without trusting how the graph is drawn.

## Finish order

In a graph without directed cycles, reading finish order backward puts every vertex before its outgoing neighbors. That's a topological order.

For a recurrence whose arrows point to needed subproblems, evaluate in the opposite order: finish the needed values before using them.

## Return-trip groups

Monday's graph has cycles. A, B, C can all reach one another; D and E can return to each other; so can F and G.

These maximal return-trip groups are strongly connected components. Collapse them into boxes. The box graph has no directed cycles.

## A DAG of components

If several boxes formed a cycle, we could travel around it and return. Those boxes would belong to one larger component.

This is why we can order the components even though we cannot topologically order the original vertices.

## Search from d

Does one DFS from D collect exactly its strongly connected component?

[Five-second prediction pause.]

Trace every reachable arrow. It reaches D, E, F, and G. That's two components. A DFS tree records discovery; a strongly connected component requires return journeys.

## Collect one group

Starting in F-G visits both vertices and stays within their group. No edge points to another component, so this is a sink component. Record F and G as assigned.

A search from D then collects D and E, skipping the vertices already recorded.

## Two reversals

Reverse the arrows and run DFS over every vertex, recording vertices when they finish. Our stack is B, C, A, vertex E, D, G, F. Return to the original graph and pop.

F comes first, then the next unassigned start is D, then A.

Reversing arrows swaps source and sink components. Decreasing finishing time selects source components of the reversed graph, which are sinks of the original. Popping already reverses finishing order.

That explains Monday's ‘no need to reverse’ note.

## The ordering proof

Across an arrow between distinct components, the upstream component has the greater maximum finishing time. If explored first, it finishes after exploring downstream.

If downstream is explored first, it cannot reach upstream and finishes earlier. That's the ordering fact to watch for in the proof.

## State for each pass

Start fresh discovery state for pass two. Keep one assigned set across all components, but a new list for each component. Each pass checks vertices and edges once.

That's linear time: big O of V plus E.

## Reading the notes

Your notes mention counting paths to and from vertices, multiplying those counts, and removing vertices. The chapter’s nearby exercise asks which vertices every source-to-target path crosses.

Together, these suggest counting paths through each vertex, then comparing with all complete paths.

## To, from, through

Use our three-box DAG as a graph in its own right. Call the first box the start and the last the destination. ‘To’ counts paths from the start to a chosen box.

‘From’ counts paths from that box to the destination.

Every complete path through the box splits uniquely into one prefix and one suffix. In a DAG, joining them cannot repeat another vertex: that would create a cycle.

So paths through equals paths to multiplied by paths from.

## Two counting passes

Give the start one empty prefix. Add incoming counts in topological order. Give the destination one empty suffix, then add outgoing counts in reverse order.

The middle box has one path to it and one from it. Their product is one.

## Compare the paths

There are two complete routes: directly across the shortcut, or through the middle. How many go through the middle?

[Five-second prediction pause.]

One of the two. Now remove the shortcut. One route remains, and it passes through the middle. Comparing these counts tells us whether every route uses that vertex.

## Remove a vertex

Now switch to an undirected graph: connections work both ways. Remove F from this picture. G becomes separated from the other vertices.

A vertex whose removal disconnects a connected graph is called a cut vertex. We can study that change using a DFS tree.

## The DFS root

Start DFS at F. One child branch explores the five vertices on the left. Another explores G. Could an edge join these branches without passing through F?

[Five-second prediction pause.]

If it did, DFS would have followed it and discovered them in the same branch.

That's why an undirected DFS root is a cut vertex exactly when it has at least two children in the DFS tree. Count tree children, not graph neighbors.

With only one child, the remaining tree stays connected after removing the root.

## Another connection

For a non-root vertex, look for a connection from a child subtree to an ancestor above it. That connection gives the subtree another route to the rest of the graph.

If one child subtree has no such connection, removing the vertex separates that subtree.

## Chapter reading route

Read section six point one asking what the bars reveal about ancestry. In six point two and six point three, connect back edges to cycles and finish order to schedules.

In six point four, connect those schedules to cached answers.

Then read six point five and the two-pass algorithm in six point six: why do return-trip groups form a DAG, and why does the next search stay inside one group?

Finish with Exercises three and four: count paths through vertices, then study what changes when a vertex is removed.

## Try it on paper

DFS records who discovered whom and when each call finished. Those records explain the chapter's bars, dependency orders, and component searches. Today's removal questions ask whether another route exists.

On paper, draw the root's two child branches and explain what remains when you remove the root.
