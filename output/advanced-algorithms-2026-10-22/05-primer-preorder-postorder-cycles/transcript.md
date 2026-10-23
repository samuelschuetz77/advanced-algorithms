# Transcript: Reading Primer: Preorder, Postorder, and Cycles

Voice: Ava (en-US-AvaMultilingualNeural). Cue markers and phonetic markup removed.

## 01 · 0:00 · The thread

In an old story, Theseus walked into a labyrinth holding a ball of thread, so he could always find his way back. Depth-first search is that thread. This maze has seven rooms, joined by twelve one-way doors. Ada will explore it from room A, unrolling a thread behind her.

## 02 · 0:19 · Two stamps per room

Ada carries a clock. The first time she enters a room, she advances the clock, and writes the time on the room. That is the room's starting time, its preorder number. When she leaves a room for good, because every door out of it has been tried, she advances the clock again, and writes that: its finishing time, its postorder number.

## 03 · 0:42 · Three states

At any moment, every room is in one of three states. New: Ada has never entered it. Active: she has entered it, but not yet left it for good. Finished: she has left it for good. The active rooms always form one single path, from the start to Ada. That is the thread.

## 04 · 1:03 · The walk, part one

Ada enters A: clock one. The door to B leads to a new room, so she goes: clock two. B to D, clock three. D to E, clock four. E has a door back to B, but B is still on the thread. E has no more doors, so E is finished: clock five. Back in D: finished, clock six. Back in B: its other door, to E, leads to a finished room. B is finished: clock seven.

## 05 · 1:32 · The walk, part two

Back at A, the next door leads to C, a new room: clock eight. C to F, nine. F has a door back to C, which is on the thread. F to G, ten. G has a door to D, a finished room, in a branch Ada already completed. G is finished: eleven. F is finished: twelve. Back at C: its door to G leads to a finished room. C is finished: thirteen. Back at A: the last door, to E, also leads to a finished room. A is finished: fourteen. The walk is over.

## 06 · 2:11 · Two orderings

Read the rooms by starting time, A, B, D, E, C, F, G. That is a preorder. Read them by finishing time, E, D, B, G, F, C, A. That is a postorder. With a different order of doors, or a different starting room, you would get different ones.

## 07 · 2:34 · Active intervals

Draw each room as a bar, from its starting time to its finishing time. Any two bars are either nested, one inside the other, or completely apart. And one room's bar contains another's exactly when it is an ancestor in the thread tree. The bar for room B contains the bars for D and E.

## 08 · 2:54 · Four ways to say 'ancestor'

The book says this in four equivalent ways. One: u is an ancestor of v in the thread tree. Two: u's bar contains v's bar. Three: when v starts, u is active. Four: just before u starts, there is a path from u to v through rooms that are all new. All four mean the same thing.

## 09 · 3:17 · Four kinds of door

Now classify the doors. When Ada tries a door from u to v, there are four cases, depending on v's state at that moment. If v is new, it is a tree edge. If v is active, it is a back edge. If v is finished and below u, it is a forward edge. If v is finished, and somewhere else, it is a cross edge.

## 10 · 3:39 · Tree edges

A tree edge: v is new, so Ada walks through, and the door joins the thread tree. A to B is a tree edge. So are five more.

## 11 · 3:51 · Back edges

A back edge: v is active, already on the thread. E to B: B is on the thread, so this door loops back up it. F to C does the same. Two doors are back edges.

## 12 · 4:04 · Forward edges

A forward edge: v is finished, and it is below u. B to E: Ada already reached E through D. C to G and A to E are the same. Three doors are forward edges.

## 13 · 4:17 · Cross edges

A cross edge: v is finished, and not below u. G to D: D sits in a branch that Ada completed before she even entered G's branch. One door is a cross edge.

## 14 · 4:30 · What the bars look like

What do the bars look like? For a tree edge, u's bar contains v's. For a forward edge, the same. For a back edge, v's bar contains u's. For a cross edge, v's bar is entirely before u's. A fifth kind, with v starting after u has finished, is impossible, because Ada tries every door out of u before she leaves it.

## 15 · 4:55 · A back edge means a cycle

Here is the key fact. If any door leads to an active room, the maze has a cycle. The thread runs from B down to E, and the door from E back to B closes the loop. But doors to finished rooms never prove a cycle.

## 16 · 5:11 · The same test, with finishing times

There is a second way to see it, with finishing times. Here is every door, with the two finishing times. For a back edge, the room it points to is still active when u finishes, so it finishes later. If an edge u to v has u finishing before v, there is a cycle. In a DAG, every edge has u finishing after v.

## 17 · 5:34 · The algorithm in Python

Now the algorithm, in Python. It keeps a status for every room. First, an empty dictionary. A loop sets every room's status to new.

## 18 · 5:45 · Visiting a room

Visit is a function inside a function, one call per room. The moment Ada enters v, its status becomes active. Then, for each door out of v, to a room w, look at w's status.

## 19 · 5:59 · The three cases

If w is active, that is a back edge. Return False: there is a cycle. If w is new, that is a tree edge, so visit it. And if that visit comes back False, a cycle was found deeper down, so return False too. If w is finished, do nothing: it can never prove a cycle.

## 20 · 6:20 · Leaving the room

When every door out of v has been tried, v becomes finished. And visit returns True: no cycle was found at or below this room.

## 21 · 6:31 · The outer loop

The outer loop. Try every room as a starting point. Skip the ones an earlier walk already covered. If any walk finds a cycle, the answer is False. If every room is covered and no back edge was found, return True: the graph is a DAG.

## 22 · 6:49 · Run it on the maze

Run it on the maze. Visit A: active. Visit B. Visit D. Visit E. Now E's door leads to B, and B's status is active. Return False, right away: the maze has a cycle. It never even looks at the rest.

## 23 · 7:07 · Without the back edges

Remove the two back edges, E to B and F to C. Ten doors are left. Now no door ever leads to an active room, and the function returns True. This is a DAG. A room with no doors in is a source: here, room A. A room with no doors out is a sink: here, room E. Every DAG has at least one source and one sink.

## 24 · 7:33 · Starting everywhere

One more detail. If we start a walk from every room in turn, skipping the ones already entered, the number of separate trees depends on the order. Start at A: one tree. Start at G first, and the first walk is stuck after G, D, E, B. Then A starts a second tree. In a directed graph, even a connected one, the count can be anything from one to V.

## 25 · 7:58 · Recap

To recap. Every room gets two stamps from one clock. Every room is new, active, or finished, and the active rooms are the thread. Every door is a tree, forward, back, or cross edge. A back edge, an edge to an active room, means a cycle. Next: topological sort, and dynamic programming, sections six point three and six point four.
