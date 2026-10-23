# Transcript: Whatever-First Search, Part 2: The Metro Map

Voice: Ava. Cue markers and phonetic markup removed.

## 01 · 0:00 · Last time

Last time, we ran one short algorithm on a graph. Take a token from the pile. If its vertex is new, mark it. Then add a token for every edge leaving that vertex. Today we ask two questions. How long does that take? And what happens if we change the pile?

## 02 · 0:19 · A new example: a metro map

Here is a city metro map. Each station is a vertex, and each track between two stations is an edge. You begin at Arch. A station counts as visited the first time you arrive there. Every track you could still try is a token: from which station, to which. And the station you arrived from is that station's parent.

## 03 · 0:41 · A guess

Before we count anything, guess. The map has twelve tracks. How many tokens get put in the pile in total, counting every track you could ever try?

## 04 · 0:58 · One track

Look at one track, between Arch and Bay. When you arrive at Arch, you add a token to try this track toward Bay. When you arrive at Bay, you add a token to try it back toward Arch. So every track makes two tokens, one from each end.

## 05 · 1:15 · All twelve tracks

Do that for all twelve tracks, one after another, and we get twenty-four tokens.

## 06 · 1:21 · Counting tokens

Add the one token we start with, at Arch. Twenty-five tokens in all. Two times E, plus one. Two times twelve, plus one, is twenty-five. That is exactly the count from last time.

## 07 · 1:35 · The cost of tokens

Every token is put in the pile once, and taken out once. Call the time for one put, or one take, T. Then all the tokens together cost about two E times T.

## 08 · 1:48 · Marking costs too

Each station is also marked only once, which adds about V more work. So the total time is V plus E times T. The V is the marking. The E times T is the tokens.

## 09 · 2:02 · With a stack

With a stack, a put or a take only touches the top of the pile, so T is a constant, however big the pile gets. The total is V plus E. We call that linear time.

## 10 · 2:15 · One warning

One warning. The book assumes the map is stored as a list of neighbors for each station. If it were stored as a table of yes or no answers, finding one station's neighbors would mean checking every cell in a row, V steps each time, and the total would grow like V times V.

## 11 · 2:33 · One pile, three rules

Now the pile. The proof only needed somewhere to put tokens in and take tokens out. It never said which one to take. Here is one pile with four numbered tokens. Take the newest, and that is a stack. Take the oldest, and that is a queue. Take the smallest number, and that is a priority queue.

## 12 · 2:54 · Three searches

Same algorithm, three behaviors. A stack gives depth-first search. A queue gives breadth-first search. A priority queue gives best-first search. Let us run the first two on the metro map.

## 13 · 3:08 · The stack: depth-first

First, the stack. The newest token always goes first. Watch how deep it goes. From Arch, ride to Dock, then Fort, then Gate, then East, then Cove, and last of all, Bay.

## 14 · 3:27 · The stack's tree

The came-from links form one long, skinny chain, six tracks deep. Bay is right next to Arch, yet in this tree, the route to Bay passes through five other stations.

## 15 · 3:40 · Now the queue

Now the queue. From Arch, three tokens are in the pile. This time we take the oldest token. Which one comes out first?

## 16 · 3:54 · The queue: one stop away

Arch to Bay, the oldest. Bay is new. Then Arch to Cove, Cove is new. Then Arch to Dock, Dock is new. Every station next to Arch is reached before we go any further. Those are one stop away.

## 17 · 4:09 · The queue: two stops away

Now the tokens from Bay, Cove, and Dock. Most lead to stations already visited, so they are thrown away. Bay to East: East is new. Most of Cove's tokens are thrown away. But Cove to Fort: Fort is new. East and Fort are two stops from Arch.

## 18 · 4:28 · The queue: three stops away

Next come Dock's tokens, and then East's. Most are thrown away. At last, East to Gate: Gate is new, the final station. Three stops. Everything left in the pile is thrown away.

## 19 · 4:42 · Two trees

The queue gives a short, bushy tree. Every station is at most three stops from Arch. Put it next to the stack's tree, and the difference is clear: depth six, against depth three.

## 20 · 4:55 · Why the queue is special

That is no accident. Each round reaches one stop further, so the number of stops at which a station is first reached is the fewest tracks between it and Arch. Bay: one stop. Gate: three stops, and no route is shorter. Breadth-first search finds the routes with the fewest stops. Depth-first search does not.

## 21 · 5:16 · Best-first search

The third rule puts a number on every track, say, the minutes of travel, and always takes the smallest. That is best-first search. With the track times as the numbers, it builds a minimum spanning tree: that is Jarník's algorithm, which most people call Prim's. With the time so far as the number, it finds the fastest routes on a weighted map: that is Dijkstra's algorithm. A priority queue costs a little more per token, so the time is V plus E log E. Later chapters return to both.

## 22 · 5:49 · Problem: a second network

A new problem. Across the water, a separate ferry network has three stations: Mill, Nest, and Oak. They connect only to each other. Your search from Arch visits the whole metro, and the pile empties. The search stops. Mill, Nest, and Oak are never visited.

## 23 · 6:09 · The loop around the search

To reach everywhere, add a loop. Go through every station. If a station has not been visited yet, it belongs to a new network. Count it, and start a fresh search from there.

## 24 · 6:22 · The loop in Python

In Python. A set called visited remembers which stations we have seen. Networks starts at zero. For each station in the graph, if the station is not in visited, we found a new network, so add one, and run the search from that station, which fills in visited.

## 25 · 6:40 · Counting the networks

Run it. Arch starts network one, and marks seven stations. Mill starts network two, and marks three. Two networks. Every vertex and every edge is still visited only once, so even with the loop, it is still V plus E. The same loop counts the networks for free.

## 26 · 7:00 · Directed graphs

Now make some tracks one-way. An arrow from Arch to Bay means trains only run from Arch to Bay. The search code does not change at all. A marked station just adds a token for each arrow leaving it.

## 27 · 7:14 · Run it from Arch

Run it from Arch. Bay, Cove, East, and Fort can all be reached. Dock and Gate cannot, even though they are on the map, because no arrow leads into them. Reachability is no longer symmetric.

## 28 · 7:28 · The tree of what Arch reaches

The came-from arrows still form a tree, pointing away from Arch. But it is a tree of only the stations Arch can reach, not a spanning tree of the whole map. Stacks, queues, and priority queues all still work.

## 29 · 7:43 · Paint bucket as a graph

One more use. The paint bucket in a drawing program. Each pixel is a vertex, and two neighboring pixels with the same color share an edge. Those edges form a graph on the pixels. Click a pixel, and the bucket must recolor everything reachable from it. That is reachability again.

## 30 · 8:03 · Recolor as we mark

So we run a search from the clicked pixel, and recolor each pixel the moment it is marked. The other blob of the same color is untouched, because no chain of same-colored neighbors leads to it.

## 31 · 8:17 · A reduction

This is called a reduction. We solve the paint bucket problem by calling reachability as a black box. A grid of n by n pixels has n squared vertices, and at most two n squared edges, so the search runs in n squared time. All that matters about the search is what it promises, not how it works.

## 32 · 8:38 · Recap

Let us retell it. About two E plus one tokens, so a stack or queue search is linear. Swap the pile, and you swap the search. Loop over every station, to cover every network. Arrows change who can be reached, not the code. Next time: counting paths, from class.
