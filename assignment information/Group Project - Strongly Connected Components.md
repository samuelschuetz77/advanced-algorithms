# Group Project - Strongly Connected Components

- Canvas assignment id: 19302737 (course 1254074)
- Due: Canvas API says 2026-10-31T04:59Z, which is Fri 10/30/2026, 10:59pm Mountain (MDT). Lock 2026-11-01T04:59Z (Sat 10/31, 10:59pm). This is an hour earlier than the usual 11:59pm; check the assignment page for the displayed time.
- Points: 21
- Submission: Canvas text entry (paste Python code including tests)
- Partner project
- Pulled: 2026-10-21

## Overview

As usual, do not use AI code generation or completion for this assignment. Use your non-AI-enabled Classwork Profile.

With a partner, implement and test (with pytest) Kosaraju's algorithm in Python using the graph class that you created in an earlier project (at most half credit if you do not use the graph interface that we specified on the earlier project).

This project builds up to Kosaraju's algorithm in three stages: a warm-up, a checkpoint, and the main problem, mirroring its three logical steps — (1) DFS on G to record finishing order, (2) reverse the graph, and (3) DFS on the reversed graph in decreasing finish-time order, where each resulting DFS tree is a strongly connected component.

## Part 1 — Reverse the Graph (warm-up / easy)

Write a function that accepts an instance G of your graph class and, in O(V + E) time, returns an instance G' of your graph class where:

- the nodes are the same as in G
- the edges are reversed from those in G (there is an edge s->t in G' if and only if there is an edge t->s in G)

## Part 2 — DFS Finish Order (checkpoint / medium)

Write a function that accepts an instance G of your graph class and, in O(V + E) time, returns a list of all nodes in order of DFS finishing time (the order in which a recursive DFS would finish/pop each node off the call stack). This is the first of Kosaraju's two DFS passes, done standalone before it gets combined with the reversed graph.

## Part 3 — Strongly Connected Components via Kosaraju's Algorithm (main)

Write a function that accepts an instance G of your graph class and, in O(V + E) time, returns an instance G' of your graph class where:

- G' is the meta graph of G (the DAG of the strongly connected components of G). Each node in G' represents a strongly connected component of G and its id should be a `frozenset` of the node ids in G for that component.
- the order of the nodes returned by `all_nodes()` should be a topological sort of the nodes in G'.
- this function should combine Part 1's reversed graph with Part 2's finish order: process the nodes of the reversed graph in decreasing finish-time order from Part 2, and each resulting DFS tree is one strongly connected component.

## What to submit

Copy/paste your Python code (including tests) into the text area.
