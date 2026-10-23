# Transcript: Reading Primer: Topological Sort and Dynamic Programming

Voice: Ava. Cue markers and phonetic markup removed.

## 01 · 0:00 · Topological ordering

Section six point three starts with a simple idea. Here is the hiking map from the count paths video. In a drawing, the trails can point in any direction. A topological ordering rearranges the junctions onto a line, so that every trail points forward, from left to right. Watch the junctions slide into place. Every arrow now points right. Here is a line-up that fails: some arrows point backward. In symbols: for every edge from vertex u to vertex v, u comes before v. The book calls this a total order: any two vertices have a definite before and after.

## 02 · 0:40 · Why a cycle breaks it

Why can a graph with a cycle never have one? Take three tasks: x before y, y before z, and z before x, closing the circle. Who goes first? Not task x, because task z must come before it. Not task y, because task x must come before it. And not task z, because task y must come before it. Nobody can go first: every vertex on a cycle has an arrow pointing into it. The book says it from the other end: the rightmost vertex has an arrow that can only point left. So a cycle rules out any topological ordering.

## 03 · 1:19 · One map, two goals

To make this concrete, we will keep using the hiking map: seven junctions, twelve one-way trails. This time, every trail has a number: the scenery points you collect walking it. We have two goals. First: an order of the junctions that respects every trail. Second: the most scenic route from Start to Summit.

## 04 · 1:42 · The book's version: an array filled from the back

First goal. The book's algorithm uses an array S, with one slot per vertex. A clock starts at V, which is seven. Run depth-first search, and whenever a vertex finishes, put it in the slot the clock points to, then move the clock down. Summit finishes first: it goes in the last slot, S seven. Meadow finishes next, into S six. Falls, into S five. Creek, into S four. Ridge, into S three. Pine, into S two. And Start finishes last, into S one. Read the array from left to right, and every trail points to the right.

## 05 · 2:23 · Check the array

Lay the vertices out in the order of S. Start, Pine, Ridge, Creek, Falls, Meadow, Summit. All twelve trails point to the right: zero point left. One depth-first search did all of it, so the time is V plus E.

## 06 · 2:40 · The same thing in Python

In Python, the simplest version needs no clock. Visit a vertex by visiting every neighbor not yet visited. Then append the vertex to a list, after all its neighbors. That puts the vertices in finish order. The last line reverses the list in place, which is the same as filling the array from the back. And an outer loop starts a search from every vertex not yet visited.

## 07 · 3:06 · What if there might be a cycle?

This version assumes the graph has no cycle. If we already know it is acyclic, plain marking is enough. If it might have a cycle, use the three-state version from the last video, and fail gracefully the moment an edge leads to an active vertex. The book writes that failure as: fail gracefully.

## 08 · 3:27 · Often, you do not need the list

Often, the sorted list is not the real goal. We want to do something at each vertex, in order. Then we can do that something at the end of each vertex's search, which handles the vertices in reverse topological order. No array is needed: the book just renames the post-visit step to process. Summit is processed first, then Meadow, Falls, Creek, Ridge, Pine, and Start last. Every vertex is processed after everything it points to.

## 09 · 3:57 · Forward order: reverse the graph

What if we want the vertices in forward order instead? One way: search the reversal of the graph, written rev of G, where every edge is flipped. Every source of G becomes a sink of rev of G, and the other way round. A reversed cycle is still a cycle, so reversing a DAG gives another DAG. And building the reversal takes V plus E time.

## 10 · 4:22 · Two orders, both correct

There is a subtle point, in the book's footnote. Here is the reverse of G's postorder. And here is a postorder of the reversed graph. Both are topological orderings of G, with zero backward edges. But they are different: Ridge and Creek swap places. So a postordering of rev of G is not necessarily the reversal of a postordering of G.

## 11 · 4:48 · Section 6.4: the dependency graph

Section six point four. Remember the frog. The ways from stone i is the ways from stone i plus one, plus the ways from stone i plus two. The book draws a dependency graph for any recurrence: a vertex for every subproblem, and an edge from one subproblem to another, if evaluating the first needs the second. For the frog, that graph is the stepping-stone graph itself. And it has to be acyclic. Otherwise, the plain recursion would never halt.

## 12 · 5:20 · Memoization is depth-first search

Here is the big claim. Evaluating a recurrence with memoization is exactly the same as a depth-first search of the dependency graph. Is the value still undefined? That is the same as: is the vertex unmarked. Starting to evaluate is the pre-visit. Evaluating every subproblem it needs is the recursive calls along the edges. And finishing the value is the post-visit. A vertex is marked when its value has been computed. The pre-visit and post-visit steps stand in for the actual arithmetic.

## 13 · 5:54 · Dynamic programming is a postorder

Now dynamic programming. It evaluates every subproblem in reverse topological order: each one is considered after the subproblems it depends on. For the frog, that means stone seven, six, five, down to zero. That order is a postorder of the dependency graph. So every dynamic programming algorithm is equivalent to a postorder traversal of the dependency graph of its recurrence.

## 14 · 6:21 · Why DP uses nested loops

Most dynamic programming algorithms look different from a topological sort. Take edit distance. Each subproblem depends on its left, upper, and diagonal neighbors. The dependency graph is a regular grid. Because it is so regular, we hard-wire a good order into the algorithm, as nested loops, so no topological sort is needed at run time. The book calls that order the evaluation order.

## 15 · 6:47 · Two small differences

So there are two small differences between most dynamic programming and topological sort. First, the dependency graph is implicit. The recurrence encodes the edges, so there is no adjacency list in memory. That is minor, as long as we can list each subproblem's children in constant time. Second, the graph is usually regular, so nested loops replace the topological sort. When the graph is not regular, we can use depth-first search directly.

## 16 · 7:18 · An irregular graph: longest path

Here is an irregular graph: the hiking map. The longest path problem asks: given a weighted directed graph, a start s and a target t, find the path with the largest total weight. Here, the most scenic route. In general directed graphs, that problem is NP-hard. But if the graph is acyclic, it takes only linear time.

## 17 · 7:42 · The recurrence

For any vertex v, let LLP of v be the length of the longest path from v to t. If v is t, it is zero: you are already there. Otherwise, look at every edge from v to some w. Take the edge's length, plus LLP of w, and keep the maximum. If v has no edges out, and is not t, the maximum of nothing is minus infinity: there is no route. The dependency graph of this recurrence is the input graph itself. So a depth-first search, memoizing as we go, solves it in V plus E time.

## 18 · 8:21 · Run it on the hiking map

Run it. Summit is the target, so its score is zero. Meadow has one trail, to Summit, worth five. Five plus zero is five. Falls has one trail, worth four. Four. Creek has two trails. Via Meadow: two plus five is seven. Via Falls: seven plus four is eleven. The best is eleven. Ridge: via Meadow, four plus five is nine. Via Falls, three plus four is seven. The best is nine. Pine has three trails. Via Creek: five plus eleven is sixteen. Via Ridge: one plus nine is ten. Via Meadow: six plus five is eleven. The best is sixteen. Start: via Pine, three plus sixteen is nineteen. Via Creek, four plus eleven is fifteen. Via Ridge, two plus nine is eleven. The best is nineteen.

## 19 · 9:20 · The Python: the setup

Now the Python. The function takes the graph, a dictionary called length, whose keys are pairs: the pair v, w gives the points of the trail from v to w. And the start and the target. Best is an empty dictionary: the cache.

## 20 · 9:37 · The Python: base case and cache check

Inside, the helper function go. If v is t, return zero. If v is not in best yet, we have not computed it. Only then do the work. Otherwise, skip down to the last line, and return what is stored.

## 21 · 9:53 · The Python: the maximum

Now the heart. Start best of v at minus infinity: float of the text minus inf makes a special number, smaller than any other, which is the book's maximum of nothing. Then for each trail out of v, to a vertex w: look up the trail's points, using the pair v, w, add go of w, the best score from there, and keep the larger of that and the best so far.

## 22 · 10:19 · The Python: the answer

Return best of v. And the last line starts everything: return go of s. That is the book's LongestPath algorithm. Each vertex is computed once, and each trail is looked at once: V plus E.

## 23 · 10:35 · The route, and an extra

The answer is nineteen scenery points. Start to Pine, to Creek, to Falls, to Summit: three plus five plus seven plus four. One extra, which is not in the book. The algorithm computes the length. To recover the route itself, remember which trail gave the maximum at each junction.

## 24 · 10:56 · The same answer by dynamic programming

The book then says: we can turn this into dynamic programming, with a topological sort. Take the finish order from the depth-first search, and loop through it. Children always come before parents, so when we reach a vertex, every best of w it needs is already in the table, and no recursion is needed. Watch the table fill in: Summit, zero. Meadow, five. Falls, four. Creek, eleven. Ridge, nine. Pine, sixteen. Start, nineteen. The same table, in the same order, as the memoized version. Memoization and dynamic programming are two views of one postorder.

## 25 · 11:38 · Recap

To recap sections six point three and six point four. A topological order is the reverse of a depth-first search's finishing order. To process in reverse order, process each vertex as it finishes. For forward order, search the reversed graph. Memoization is a depth-first search of the dependency graph, which must be acyclic. And dynamic programming is a postorder of that same graph, so longest path in a DAG takes V plus E time. Pause, and say each of those four in your own words. That is a good start for your learning log.
