# Project 2 - ADTs and Data Structures

- **Type:** Assignment (Canvas)
- **Due:** Fri 9/11/2026, 11:59pm (available until Sep 12, 2026 11:59pm — grace period)
- **Points:** 24
- **Canvas link:** https://snow.instructure.com/courses/1254074/assignments/19185501

## Motivation

Continue review/warmup:
- Review the ADTs used by graph search algorithms: priority queue and graph
- Implement reasonable data structures that implement those ADTs
- Note the difference between ADTs and data structures
- Review a classic graph algorithm (Prim's Minimum Spanning Tree) that uses these ADTs/data structures
- Use a popular graph library to generate random graphs

**Use your non-AI-enabled Classwork Profile for this assignment (no AI code generation or completion).**

Note: this project's priority queue is sometimes called a *locator heap*, since each entry's key acts as a stable locator/handle for O(log n) update and removal.

Builds up in three stages: warm-up ADT → checkpoint ADT → main task integrating both.

## Warm-up (easy): Graph ADT

Implement with a data structure achieving the given running-time bounds. Mostly dictionary/hash-map bookkeeping. (Nodes/keys assumed hashable; priorities assumed comparable via `<`, `<=`, `>`, `>=`.)

- constructor: create empty graph (optionally with initial nodes, edges, data)
- `add_node(node, data=None)` — O(1)
- `add_edge(parent, child, data=None)` — directed edge, O(1). Assumes parent/child already added via `add_node` — does not auto-create nodes.
- `add_undirected_edge(node1, node2, data=None)` — O(1), calls `add_edge` twice
- `get_node_data(node)` — O(1)
- `get_edge_data(parent, child)` — O(1)
- `get_children(parent)` — iterable, O(1) to construct + O(1)/child
- `get_parents(node)` — iterable, O(1) to construct + O(1)/parent
- `contains_node(node)` — O(1)
- `contains_edge(parent, child)` — O(1)
- `get_nodes()` — iterable in insertion order, O(1) to construct + O(1)/node
- `get_edges()` — iterable of `(parent, child)` tuples in insertion order, O(1) to construct + O(1)/edge

Copy the provided tests in as-is (below); add your own test(s) for `get_parents` (the one method they don't touch).

### Graph ADT tests (provided — copy as-is)
```python
def test_new_graph_has_no_nodes():
    graph = Graph()
    assert list(graph.get_nodes()) == []

def test_add_node_then_contains_node():
    graph = Graph()
    graph.add_node("a")
    assert graph.contains_node("a")
    assert not graph.contains_node("b")

def test_add_node_is_idempotent():
    graph = Graph()
    graph.add_node("a", data=1)
    graph.add_node("a", data=2)  # already present -- should not duplicate
    assert list(graph.get_nodes()) == ["a"]

def test_get_node_data():
    graph = Graph()
    graph.add_node("a", data="hello")
    assert graph.get_node_data("a") == "hello"

def test_add_edge_then_contains_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.contains_edge("a", "b")
    assert not graph.contains_edge("b", "a")  # directed, so the reverse shouldn't exist

def test_get_edge_data():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.get_edge_data("a", "b") == 5

def test_add_undirected_edge_creates_both_directions():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_undirected_edge("a", "b", data=7)
    assert graph.contains_edge("a", "b")
    assert graph.contains_edge("b", "a")
    assert graph.get_edge_data("a", "b") == 7
    assert graph.get_edge_data("b", "a") == 7

def test_get_children():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert set(graph.get_children("a")) == {"b", "c"}

def test_get_nodes_preserves_insertion_order():
    graph = Graph()
    graph.add_node("c")
    graph.add_node("a")
    graph.add_node("b")
    assert list(graph.get_nodes()) == ["c", "a", "b"]

def test_get_edges_preserves_insertion_order():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert list(graph.get_edges()) == [("a", "b"), ("a", "c")]

def test_contains_node_false_for_absent_node():
    graph = Graph()
    assert not graph.contains_node("nonexistent")

def test_contains_edge_false_for_absent_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    assert not graph.contains_edge("a", "b")
```

## Checkpoint (medium): Priority Queue / Locator Heap ADT

Harder than the Graph ADT: a binary heap that also supports O(log n) update-by-key and remove-by-key, not just push/pop.

- `update(key, priority, data=None, only_if_less=False)` — O(log n). Adds a new item, or updates priority (and optionally data) of an existing item. If `only_if_less` is True, only updates if the new priority is lower than current. A brand-new key is always added regardless of `only_if_less`.
- `peek_min()` — O(1), returns key with min priority without removing
- `remove(key)` — O(log n)
- `contains_key(key)` — O(1)
- `get_data(key)` — O(1)
- `get_priority(key)` — O(1)
- `count()` — O(1)

Copy the provided tests in as-is; add your own test(s) for `get_priority` (the one method they don't touch).

### Priority Queue ADT tests (provided — copy as-is)
```python
def test_new_priority_queue_has_count_zero():
    pq = PriorityQueue()
    assert pq.count() == 0

def test_update_adds_new_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_peek_min_returns_smallest_priority_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.update("c", 9)
    assert pq.peek_min() == "b"

def test_peek_min_does_not_remove():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.peek_min()
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_get_data_returns_associated_data():
    pq = PriorityQueue()
    pq.update("a", 5, data="hello")
    assert pq.get_data("a") == "hello"

def test_update_existing_key_changes_priority_without_duplicating():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 1)
    pq.update("a", 0)  # "a" should now be the minimum
    assert pq.peek_min() == "a"
    assert pq.count() == 2  # still just two keys, not duplicated

def test_update_only_if_less_ignores_higher_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("a", 10, only_if_less=True)  # 10 is not less than 5 -- should be ignored
    pq.update("b", 7)
    assert pq.peek_min() == "a"  # "a"'s priority should still be 5, which beats 7

def test_update_only_if_less_applies_lower_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 3)
    pq.update("a", 1, only_if_less=True)  # 1 is less than 5 -- should apply
    assert pq.peek_min() == "a"

def test_update_only_if_less_on_new_key_still_adds_it():
    pq = PriorityQueue()
    pq.update("a", 5, only_if_less=True)  # "a" wasn't present yet -- should still be added
    assert pq.contains_key("a")
    assert pq.count() == 1

def test_remove_deletes_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.remove("b")
    assert not pq.contains_key("b")
    assert pq.count() == 1
    assert pq.peek_min() == "a"

def test_remove_then_reinsert():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.remove("a")
    pq.update("a", 1)
    assert pq.contains_key("a")
    assert pq.peek_min() == "a"

def test_contains_key_false_for_absent_key():
    pq = PriorityQueue()
    assert not pq.contains_key("nonexistent")

def test_many_updates_and_removes_maintain_min_heap_order():
    pq = PriorityQueue()
    for key, priority in [("a", 5), ("b", 2), ("c", 8), ("d", 1), ("e", 9), ("f", 3)]:
        pq.update(key, priority)
    order = []
    while pq.count() > 0:
        m = pq.peek_min()
        order.append(m)
        pq.remove(m)
    assert order == ["d", "b", "f", "a", "c", "e"]
```

## Main: Prim's Minimum Spanning Tree

Integrates the Graph and Priority Queue/Locator Heap ADTs into a working algorithm. Include this provided implementation in `structures.py` and write sufficient pytest tests to verify it works correctly with your data structures:

```python
def prim_mst(graph, edge_weight=None, start_node=None):
    """
    Find minimum spanning tree using Prim's algorithm.

    Args:
        graph: an instance of your Graph data structure
        start_node: the node to start from; if None, uses first node from graph.get_nodes()
        edge_weight: function taking (parent, child) returning edge weight;
                     if None, uses edge data as weight

    Returns:
        Graph instance containing the minimum spanning tree
    """
    if edge_weight is None:
        edge_weight = lambda parent, child: graph.get_edge_data(parent, child)

    if start_node is None:
        start_node = next(iter(graph.get_nodes()))

    mst = Graph()  # assuming your Graph class is named Graph
    pq = PriorityQueue()  # assuming your PriorityQueue class is named PriorityQueue

    pq.update(start_node, 0, data=None)

    while pq.count() > 0:
        current_node = pq.peek_min()
        parent_node = pq.get_data(current_node)
        pq.remove(current_node)

        if not mst.contains_node(current_node):
            mst.add_node(current_node)
            if parent_node is not None:
                data = graph.get_edge_data(parent_node, current_node)
                mst.add_undirected_edge(parent_node, current_node, data=data)

            for child in graph.get_children(current_node):
                if not mst.contains_node(child):
                    weight = edge_weight(current_node, child)
                    pq.update(child, weight, data=current_node, only_if_less=True)

    return mst
```

Algorithm reference:
1. Initialize an empty graph to hold the MST.
2. Initialize an empty priority queue.
3. Push `start_node` with priority 0, `data=None`.
4. While the priority queue is not empty:
   - Let `current_node` = min-priority key, `parent_node` = its data.
   - Remove `current_node` from the priority queue.
   - If `current_node` not already in the spanning tree:
     - If `parent_node` is not None, add an undirected edge `parent_node`–`current_node` in the MST with the original edge's weight as data.
     - For each child of `current_node` not already in the MST: update its priority in the PQ (only if less) to the edge weight, with data = `current_node`.
5. Return the spanning tree graph.

## Bonus (optional): random graph via networkx

For fun: use [networkx](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.gnm_random_graph.html) to generate a random connected, undirected, weighted graph with 100 nodes and 300 edges, weights 1–10. Run the provided Prim's implementation on it (after converting the networkx graph to your `Graph`) and print the MST's total weight.

## Submission
- Upload `structures.py`: all code + tests in one file, run via `python -m pytest structures.py`. Include name/course/date at the top of the file.
- In the Canvas text box or a separate PDF, include a brief write-up: a sentence or two on how it went, plus a screenshot of the (hopefully passing) test results.

## Rubric
| Criteria | Points |
|---|---|
| Correct + efficient Graph ADT, passing provided tests + your own `get_parents` test | 8 pts |
| Correct + efficient Priority Queue ADT, passing provided tests + your own `get_priority` test | 8 pts |
| Effective tests showing the ADTs work with the provided Prim's MST algorithm, with a passing screenshot | 4 pts |
| Screenshots + reflection in the text box or PDF | 4 pts |
