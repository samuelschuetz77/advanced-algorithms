# Class 21 Review Quiz (DFS Traversal and Topo Sort)

Source: teichert.github.io/quizhub link shared by the student (questions decoded from the URL; answers are the ones marked in the link). Review material, not graded.
Saved: 2026-10-21

## 1. Reverse postorder
DFS starts at `a` and tries neighbors in alphabetical order. Edges: a→b, a→c, b→d, c→d, d→e. What is the **reverse postorder**?

- **a) a c b d e** ✔
- b) a b d e c
- c) e d b c a
- d) a b c d e

Why: postorder is e d b c a, so reversed it is a c b d e.

## 2. Detecting a cycle
During DFS you look at an edge u→v. Which state of v proves the graph has a cycle?

- **a) v is active: started but not yet finished** ✔
- b) v is finished
- c) v is new: not yet visited
- d) v has a smaller preorder number than u

## 3. Why reverse postorder gives a topological order of a DAG

- **a) For every edge u→v, v finishes before u, so u comes earlier once the finish order is reversed** ✔
- b) DFS visits vertices in order of their number of incoming edges
- c) Preorder and postorder are always the same in a DAG
- d) Every vertex in a DAG has an edge to the vertex that finishes right after it
