# Transcript: Class Lab: count_paths and the Frog

Voice: Ava (en-US-AvaMultilingualNeural). Cue markers and phonetic markup removed.

## 01 · 0:00 · Meet Hopper

Meet Hopper, a frog. Hopper wants to cross a river on eight stepping stones, numbered zero to seven. Each hop goes forward one stone, or two. Drawn as a graph, each stone is a vertex, and each hop is an arrow, a directed edge. How many different ways can Hopper get from stone zero to stone seven?

## 02 · 0:28 · Count backward from the far bank

Let us count backward, from the far bank. From stone seven, Hopper is done. That is one way: do nothing. From stone six, one way: hop one. From stone five, two ways: hop one, then one more, or hop two, straight to the bank.

## 03 · 0:47 · The pattern

See the pattern? The ways from a stone are the ways from the stone one ahead, plus the ways from the stone two ahead, because those are the only first hops. Stone four: two plus one is three. Stone three: three plus two is five.

## 04 · 1:03 · Twenty-one ways

Keep going. Eight. Thirteen. And from stone zero, twenty-one ways. Every count used only the counts of the stones it can hop to.

## 05 · 1:13 · Counting paths in general

In any graph, this is called counting paths. The graph must be a DAG: a directed acyclic graph, meaning arrows, and no cycles. To count the paths from s to t: if s is t, there is one path, the empty one. Otherwise, add up the counts of s's children. The children are the vertices that s points to.

## 06 · 1:37 · The graph from your lab

Here is the graph from your class lab. Vertex A points to B and C. B and C both point to D. D points to E. How many paths from A to E? From B to E: one. From C to E: one. So from A: two. One path goes A, B, D, E. The other goes A, C, D, E.

## 07 · 2:03 · How the code asks

The code asks these questions in a different order. To count from A, it asks B. B asks D. D asks E, and E answers one. D answers one. B answers one. Then A asks C, and C asks D all over again. D has to ask E all over again. The same question, twice. Seven calls, for five vertices.

## 08 · 2:28 · A bigger map

That repeat is harmless here. On a bigger map, it explodes. This is a hiking map: seven junctions, twelve one-way trails, all uphill. How many different routes lead from Start to Summit?

## 09 · 2:48 · Plain recursion

Plain recursion asks each child, and each child asks its own children, with no memory. Watch the calls pile up. Twenty-four calls, for a map with seven junctions.

## 10 · 3:02 · The repeats

Look at the repeats. Meadow is asked five times. Falls is asked four times. Every time, the answer is one, recomputed from scratch.

## 11 · 3:14 · The fix: a cache

The fix: write each answer down the first time, and look it up after. That is called memoization, and the table is a cache. Here is the same search with a cache. Whenever a junction was already answered, it is a cache hit: read the table, and stop there.

## 12 · 3:32 · The cache filling in

Here is the table filling in. Summit: one. Meadow: one. Falls: one. Creek: two. Ridge: two. Pine: five. Start: nine. Nine routes. Each junction was finished only after all of its children.

## 13 · 3:52 · How much work?

Count the work. Each junction is computed once: seven. Each trail is looked at once, when its starting junction is computed: twelve. So there are thirteen calls: one for the start, plus one per trail. That is V plus E: linear time.

## 14 · 4:11 · Your code: the import

Now your code. The first line: from functools import cache. Functools is a toolbox that comes with Python, and cache is one tool in it.

## 15 · 4:22 · Your code: the outline

Def count_paths takes the graph, a start s, and a target t. The last line, return nested of s, starts the whole search from the start.

## 16 · 4:32 · Your code: @cache

The line above the inner def is at cache. The at sign means: wrap the function underneath. The wrapped function keeps a table of answers. The first time it sees an input, it runs, and writes the answer down. The next time it sees the same input, it skips the function, and returns what is written.

## 17 · 4:53 · Your code: a function inside a function

Nested is a function inside a function, so it can read graph and t from outside. A new nested is built every time count_paths is called, so its table starts empty each time. That is why the table can be keyed by s alone, even though the answer depends on t: inside one call, t never changes. The s in the parentheses is a fresh variable: this call's vertex.

## 18 · 5:19 · Your code: the base case

If s equals t, return one. Arriving at the target is exactly one path, the empty path. The parentheses around the comparison are optional.

## 19 · 5:31 · Your code: the densest line

Now the densest line. Return sum of nested of child, for child in graph of s. Take it apart. Graph of s is the list of children of s. At vertex A in the diamond, that is B and C.

## 20 · 5:46 · Your code: the loop inside

For child in graph of s means: go through that list, one child at a time. Nested of child is the count for that child. Together they produce one number for each child. Wrapped in parentheses like this, it is called a generator expression.

## 21 · 6:03 · Your code: sum

Sum adds those numbers up. If s has no children, there is nothing to add, and the sum of nothing is zero. Here is the same thing written longhand: a total that starts at zero, a loop, and a return.

## 22 · 6:18 · Run it on the diamond

Run it on the diamond. A asks B, B asks D, D asks E, and E returns one. D is stored. B is stored. Then A asks C, and C asks D. A cache hit: one, instantly. C is stored. And A adds one plus one: two.

## 23 · 6:39 · Your third test

Your third test asks for E to A. Nested of E: E is not A, and E has no children, so the sum of nothing is zero. Zero paths.

## 24 · 6:49 · One rule: no cycles

One rule: no cycles. Suppose vertex A pointed to vertex B, B to C, and C back to A. Then nested of A would call B, which calls C, which calls A again, forever. Python gives up with a recursion error. That is why the graph must be acyclic. In the book's words, the dependency graph of a recurrence must have no cycles.

## 25 · 7:14 · Your last test: sixty stones

Now your last test: sixty stepping stones, hop one or two. The test builds the graph in one line. For i in range sixty, make a key i, with the list i plus one, i plus two. The vertical bar merges two dictionaries, here adding stones sixty and sixty-one, which have no hops.

## 26 · 7:36 · How many ways?

How many ways? Two trillion, five hundred four billion, seven hundred thirty million, seven hundred eighty-one thousand, nine hundred sixty-one. Those are Fibonacci numbers, like the ones from the dynamic programming reading: each count is the sum of the two ahead.

## 27 · 7:54 · Plain versus cached

Plain recursion would make over eight trillion calls. At ten million calls a second, that is more than nine days. With the cache: one hundred twenty-one calls. A fraction of a millisecond.

## 28 · 8:08 · Memoization is depth-first search

This is memoization, and it is depth-first search in disguise. Each junction is a vertex. Each call that needs another is an edge. Storing an answer is marking. Computing the value happens after the children, at the post-visit. The book puts it in one line: memoized recursion is depth-first search of the dependency graph.

## 29 · 8:31 · Recap

To recap. Paths from s to t: one if s is t, otherwise the sum over the children. Plain recursion repeats work. A cache answers each vertex once, so the time is V plus E. And the answers come out children first. Next video: the other half of your lab, topological order.
