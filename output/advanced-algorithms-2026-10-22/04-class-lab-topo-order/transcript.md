# Transcript: Class Lab: topo_order and the Morning

Voice: Ava. Cue markers and phonetic markup removed.

## 01 · 0:00 · From your notes

In your notes, you drew this graph, and two ways to lay it out. Let us give it a story: a morning routine. A is shower. B is get dressed. C is coffee. D is leave. An arrow means: this task must come before that one.

## 02 · 0:16 · Two layouts

Now lay the four tasks on a line. In this order, C, B, A, D, three arrows point backward. You would drink coffee before showering. In this order, A, B, C, D, every arrow points the same way. That is called a topological order. Your note says: a DAG always has one.

## 03 · 0:40 · Why no cycles?

Why a DAG? Suppose get dressed had to come before shower, and shower before get dressed. No order could satisfy both. With no cycles, an order always exists.

## 04 · 0:54 · A bigger example: dinner

A bigger one. Priya is cooking dinner: seven tasks, and twelve rules. An arrow from one task to another means the first must be finished before the second starts. In what order can Priya do everything?

## 05 · 1:15 · The trick

Here is a trick, using depth-first search. When you reach a task, start it. Then visit everything it unlocks, before anything else. Only then, call this task finished. So a task always finishes after everything that depends on it. Watch.

## 06 · 1:33 · Going down

Start at Shop. Shop unlocks Chop, so go there. Chop unlocks Boil. Boil unlocks Sauce. Sauce unlocks Plate. Plate unlocks Eat. Eat unlocks nothing, so Eat is the first task to finish.

## 07 · 1:50 · Backing up

Now back up. Plate has nothing left, so Plate is finished. Sauce is finished. Back at Boil, its other task, Plate, is already finished, so skip it. Boil is finished.

## 08 · 2:04 · The rest

Back at Chop. Its next task, Fry, is new, so go there. Fry's tasks, Sauce and Plate, are both finished: skip them. Fry is finished. Chop's last task, Sauce, is done too. Chop is finished. Back at Shop, Boil and Fry are done. Shop finishes last of all.

## 09 · 2:25 · Reverse the finish order

The finish order is Eat, Plate, Sauce, Boil, Fry, Chop, Shop. That is called the postorder. Reverse it: Shop, Chop, Fry, Boil, Sauce, Plate, Eat. Lay the tasks out in that order, and all twelve arrows point forward.

## 10 · 2:44 · Why it works

Why does it work? Look at the arrow from Fry to Sauce. Sauce finished before Fry did. And at the arrow from Chop to Boil: Boil finished before Chop. For every arrow, the task it points to finishes first. So when the finish order is reversed, every task comes before the tasks it points to.

## 11 · 3:05 · What about the start order?

What about the order the tasks start? That is called the preorder: Shop, Chop, Boil, Sauce, Plate, Eat, Fry. Look: Fry comes last, but Fry must come before Sauce and Plate. Two arrows point backward. The preorder is not a topological order.

## 12 · 3:24 · A second start task

Back to the dinner, with one more detail. Priya also wants to set the table. Setting the table has nothing before it, and its only arrow leads to Eat. Now there are two tasks with nothing before them: Shop, and Table. So a loop over all the tasks could start at either one. Let us run both.

## 13 · 3:45 · Case one: the loop starts at Shop

Case one: the dictionary lists Shop first. The search runs exactly as before, and Shop finishes. Then the loop reaches Table, a new task. Its only arrow leads to Eat, which is already finished. So Table finishes last of all.

## 14 · 4:03 · Case two: the loop starts at Table

Case two: the dictionary lists Table first. Table starts. Its arrow leads to Eat, a new task, so Eat starts, and finishes at once, since it unlocks nothing. Then Table finishes. Now the loop reaches Shop, and the whole dinner search runs. But Eat is already finished, so every arrow into Eat is skipped.

## 15 · 4:26 · Both ways

Here are both cases side by side. Case two, below. In both, the start order fails: three arrows point backward each time. But the reversed finish order is a valid topological order in both. They are not the same order. In case one, Table comes first. In case two, Table comes late, right before Eat. Both are correct, because Table only has to come before Eat.

## 16 · 4:53 · Your code

Now your code. It keeps three things: the start order, the finish order, and a set of visited tasks. A function inside a function, build topo from, handles one task. And an outer loop tries every task, so every one is covered.

## 17 · 5:11 · A function inside a function

build_topo_from is defined inside topo order, like nested was in count paths. So it can read and change pre order, and visited, and post order, from outside. Every call shares the same three.

## 18 · 5:26 · What one call does

One call, step by step. Write the task into the start order. Mark it visited. For each task it unlocks, if that task is not visited yet, go and handle it first. Only after all of them are done, write this task into the finish order.

## 19 · 5:43 · Where is the base case?

Where is the base case? There is no if for it. When a task has no children, or all of them have been started, the for loop does nothing. The function falls through to post order, and returns. That is what your note says: none of the recursive calls happen when all the children have already been started.

## 20 · 6:03 · The outer loop

The outer loop. For each node in the dictionary, in the order the dictionary lists them, if it was not already covered, start a fresh depth-first search from it. That is the loop from the earlier videos, and it is why the dictionary order mattered in the two cases.

## 21 · 6:20 · The bug

Now the bug. The last line returns pre order. We just saw that the start order is not a topological order. The fix: return the reverse of post order, with list of reversed post order. Reversed hands the items back to front, and list turns that into a list. This is shown here only. Your file stays as you wrote it.

## 22 · 6:43 · Your test

Now your test. Your test_topo_order is a copy of the first test. It calls topo order with three arguments, but topo order takes only one: the graph. The spec's test is different. It checks the order itself.

## 23 · 6:59 · Reading the real test

The real test, line by line. Sorted order equals sorted graph: the same vertices, none lost. Order dot index of u is less than order dot index of w. Index gives a position in the list. For every vertex u, and every child w of u, all means every one of those checks must be true. In other words: every arrow points forward.

## 24 · 7:26 · Running it

Run your function as written. On the first graph it returns A, B, D, E, C. C points to D, but C comes after D. The test fails. With the fix, both graphs pass: A, C, B, D, E, and then Z, Y, X.

## 25 · 7:46 · How fast?

How fast is it? Each task is visited once. Each arrow is looked at once. So the function runs in V plus E time. The test uses index, which scans the list, so the test is slower. The function is not.

## 26 · 8:02 · Recap

To recap. A topological order puts every arrow pointing the same way. Depth-first search gives one: reverse the finish order. The start order is not enough. Your code needs one change: return the reversed post order. Next: the book's chapter six, preorder, postorder, and cycles, in detail.
