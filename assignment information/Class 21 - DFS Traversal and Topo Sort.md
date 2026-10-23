# Class 21 - DFS Traversal and Topo Sort

Class activity page, not a separate graded submission.
Source: https://snow.instructure.com/courses/1254074/pages/class-21-dfs-traversal-and-topo-sort?module_item_id=35195826
Pulled: 2026-10-21

## Reading for Prep

JEA 6.1-6.3 — preorder and postorder, detecting cycles, topological sort.

## Mini Lab

### Part 1

`count_paths(graph, s, t)` returns how many different paths go from `s` to `t` in a DAG, where `graph` maps each vertex to the list of vertices its edges point to. (In `g` below, `a` reaches `e` by a-b-d-e and by a-c-d-e.)

Write it so this pytest test passes in O(V + E) time:

```python
g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}

def test_count_paths():
    assert count_paths(g, "a", "e") == 2
    assert count_paths(g, "b", "e") == 1
    assert count_paths(g, "e", "a") == 0
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    assert count_paths(ladder, 0, 60) == 2504730781961
```

### Bonus

If you get done early, write `topo_order(graph)`, which returns a list of all the vertices of a DAG in an order where every edge points forward. Make this pass, also in O(V + E) time:

```python
def test_topo_order():
    for graph in [g, {"x": [], "y": ["x"], "z": ["y", "x"]}]:
        order = topo_order(graph)
        assert sorted(order) == sorted(graph)
        assert all(order.index(u) < order.index(w) for u in graph for w in graph[u])
```

## Main Points

- DFS is whatever-first search with a stack (or recursion), and runs in O(V+E) on an adjacency list. Marking vertices keeps it from looping on cycles.
- Preorder and postorder: a vertex's preorder time is when DFS first reaches it; its postorder time is when DFS finishes it, after everything reachable from it is done. Each vertex is new, active (started, not finished), or finished.
- Detecting cycles: an edge u→v where v is still active points back up the current path, so the graph has a cycle. Edges to finished vertices never prove a cycle.
- Topological sort: in a DAG, every edge u→v has v finishing before u. So reverse postorder lists every vertex before everything it points to, and a cycle is exactly what makes a topological order impossible.
- Meta-idea: one traversal, different bookkeeping. DFS itself doesn't change; what you record (times, states, the finish order) answers different questions.

## Practice Quiz

Class 21 Practice Quiz (linked from the page; not opened in this pull).
