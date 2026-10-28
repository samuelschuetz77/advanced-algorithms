# Class 22 - Connections to Memoization

- Canvas page: https://snow.instructure.com/courses/1254074/pages/class-22-connections-to-memoization (Module 06)
- Class activity, not graded. Reading for prep: JEA 6.4 (memoization and dynamic programming).
- Synced 2026-10-23.

## Mini Lab

### Part 1
`longest_from(graph, s)` returns the number of edges on the longest path starting at `s` in a DAG (graph maps each vertex to the list of vertices its edges point to). Must pass the test below in O(V + E).

```python
g = {"s": ["a", "b"], "a": ["c", "t"], "b": ["c", "d"], "c": ["t"], "d": ["t"], "t": []}

def test_longest_from():
    assert longest_from(g, "s") == 3
    assert longest_from(g, "c") == 1
    assert longest_from(g, "t") == 0
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    assert longest_from(ladder, 0) == 60
```

### Bonus
`lis_length(a)`: length of the longest strictly increasing subsequence. Hint: it is a longest path in a DAG you never have to build. O(n^2).

```python
def test_lis_length():
    assert lis_length([3, 1, 4, 1, 5, 9, 2, 6]) == 4
    assert lis_length([5, 4, 3]) == 1
    assert lis_length([]) == 0
```

## Main Points
- Every recurrence has a dependency graph: one vertex per subproblem, an edge from each subproblem to the ones it calls. A terminating recurrence gives a DAG; a cycle would mean a subproblem waits on itself forever.
- Memoized recursion is DFS of that DAG: the memo is the "visited" mark, and a value is filled in when the DFS finishes the subproblem. Memo entries fill in postorder. A bottom-up table needs an order where every subproblem comes after the ones it depends on (reverse topological order of the dependency edges).
- DP on a DAG: longest path out of v is 0 if v has no out-edges, otherwise the max over edges v->w of 1 + longest(w). Each vertex and edge handled once: O(V + E).
- Meta-idea: DP and graph search are the same idea from two sides. Choosing subproblems is choosing a DAG; running time is the size of that DAG (number of subproblems x work per subproblem).

## Practice Quiz
"Class 22 Practice Quiz" (external link from the page; not read/saved).
