from collections import deque



class Graph:
    def __init__(self):
        self.node_data = {}
        self.neighbors = {}
        self.parents = {}
        self.edges = []

    def add_node(self, node, data=None):
        if node not in self.node_data:
            self.node_data[node] = data
            self.neighbors[node] = {}
            self.parents[node] = []

    def add_edge(self, parent, child, data=None):
        self.neighbors[parent][child] = data
        if parent not in self.parents[child]:
            self.parents[child].append(parent)
        self.edges.append((parent,child))

    def add_undirected_edge(self, node1, node2, data=None):
        self.add_edge( node1, node2, data)
        self.add_edge( node2, node1, data)

    def get_node_data(self, node):
        return self.node_data[node]

    def get_edge_data(self, parent, child):
        return self.neighbors[parent][child]

    def get_children(self, parent):
        return list(self.neighbors[parent].keys())

    def get_parents(self, node):
        return self.parents[node]

    def contains_node(self, node):
        return node in self.node_data

    def contains_edge(self, parent, child):
        return child in self.neighbors[parent]

    def get_nodes(self):
        return self.node_data.keys()

    def all_nodes(self):
        return self.get_nodes()

    def get_edges(self):
        return self.edges


def reverse(graph):
    reversed_graph = Graph()
    for node in graph.get_nodes():
        reversed_graph.add_node(node, graph.get_node_data(node))
    for u, v in graph.get_edges():
        reversed_graph.add_edge(v, u, graph.get_edge_data(u, v))
    return reversed_graph

def dfs_trees(graph, start_order):
    # visited remembers which nodes we have already reached, across all trees.
    visited = set()
    for node_1 in start_order:
        if node_1 not in visited:
            traveled = []
            stack = deque()
            stack.append(("visit", node_1))
            while stack:
                action, vertex = stack.pop()
                if action == "finish":
                    traveled.append(vertex)
                elif vertex not in visited:
                    visited.add(vertex)
                    stack.append("finish", vertex)
                    children = graph.get_neighbors(vertex)
                    for child in children[::-1]: 
                        dfs_finish_order()




                    # beleow the stack append loop over outgoing neighbors
                    # loop of verte children into reverse order
                    # inside each child work 





















            # Remaining adsfjhs: work in the locations described, not necessarily here.
            # visited tracks discoveries; traveled records nodes when they finish.
            # Each stack task holds an action followed by the node it concerns.

            # adsfjh 12: Can you fix visited.append(n) inside the elif?
            # visited is a set: its insertion method is add, not append.
            # The current node is vertex; n is not defined in this function.



            # adsfjh 13: Right after marking vertex visited, can you push a "finish"
            # task for vertex? Use one tuple, like your initial "visit" task.
            # Stay inside the elif. Schedule completion; do not add to traveled here.
            # Push this BEFORE child tasks so the stack processes it AFTER them.

            # adsfjh 14: Below that finish task, still inside the elif, can you loop
            # over vertex's outgoing neighbors? Your Graph method is get_children.
            # Give it vertex, not node_1: each popped node has its own children.
            # To explore children in the order returned, push them in reverse order.
            # Hint: the built-in reversed works on the list get_children returns.
            # The last child pushed is the first child popped.

            #  Inside the child loop, can you push a "visit" task for each               push visit task from each child 
            # child that is not already in visited? Each task is one action-node tuple.
            # Hint: check membership, then use stack's append method.
            # Do not mark children visited here; your elif does that when popped.
            # Duplicate pending visits are okay: the visited check on pop skips repeats.

            # adsfjh 16: After while finishes, can you give the caller this tree's
            # traveled list and still allow the outer for loop to try later starts?
            # Hint: yield produces one result and lets the function resume afterward.
            # Place it OUTSIDE while but INSIDE if node_1 not in visited.
            # Align it with while. A return here would stop before later trees.

            # adsfjh 17: Can you run the five existing tests below with pytest?
            # Select this file explicitly; its name does not start with test_.
            # Check finish order, SCC membership, component order, and the deep chain.
            # Inspect any failure before changing unrelated working code.

            # adsfjh 18: Can you add tests for the missing edge cases below?
            # Put new test functions beside the existing tests, outside dfs_trees.
            # Empty graph: no trees. One isolated node: one tree containing that node.
            # Self-loop: the node finishes once, without endless exploration.
            # Branching: a points to b and c; b points to d. Add a-to-b before a-to-c.
            # Following that child order should finish d, b, c, a in one tree.
            # Shared child: a points to b and c; b also points to c.
            # Each node finishes once even when several visit tasks name it.

            # adsfjh 19: Can you explain why dfs_trees takes O(V + E) time when
            # start_order lists each vertex once? Count expansions and edge scans.
            # A vertex expands only on its first visit; later visits are skipped.
            # Include building and reversing each get_children list in your count.
            # This checks DFS only: Graph.add_edge scans a parent list, so the
            # surrounding graph-building code needs a separate runtime review.
                




    
                    



    


def dfs_finish_order(graph):
    return [node for tree in dfs_trees(graph, graph.get_nodes()) for node in tree]


def kosaraju(graph):
    scc_start = dfs_finish_order(graph)[::-1]
    reversed_graph = reverse(graph)

    g_prime = Graph()
    belongs_to = {}

    for tree in dfs_trees(reversed_graph, scc_start):
        scc_id = frozenset(tree)
        g_prime.add_node(scc_id)
        for node in scc_id:
            belongs_to[node] = scc_id

    for u, v in graph.get_edges():
        u, v = belongs_to[u], belongs_to[v]
        if u != v and not g_prime.contains_edge(u, v):
            g_prime.add_edge(u, v)

    return g_prime


def test_reverse():
    g = Graph()
    for n in "abcd":
        g.add_node(n)
    g.add_edge("a", "b", 7)
    g.add_edge("b", "c")

    r = reverse(g)
    assert set(r.get_nodes()) == set("abcd")
    assert set(r.get_edges()) == {("b", "a"), ("c", "b")}
    assert r.get_edge_data("b", "a") == 7


def test_finish_order():
    g = Graph()
    for n in "abcd":
        g.add_node(n)
    g.add_edge("a", "b")
    g.add_edge("b", "c")

    assert dfs_finish_order(g) == ["c", "b", "a", "d"]


def test_kosaraju():
    g = Graph()
    for n in "abcd":
        g.add_node(n)
    g.add_edge("a", "b")
    g.add_edge("b", "a")
    g.add_edge("b", "c")

    result = kosaraju(g)
    ab, c, d = frozenset({"a", "b"}), frozenset({"c"}), frozenset({"d"})
    assert set(result.get_nodes()) == {ab, c, d}
    assert set(result.get_edges()) == {(ab, c)}
    assert list(result.get_nodes()).index(ab) < list(result.get_nodes()).index(c)


def test_kosaraju_multiple_components():
    g = Graph()
    for node in "akvsgqerby":
        g.add_node(node)
    for u, v in [("a", "k"), ("k", "v"), ("v", "a"), ("k", "s"), ("k", "y"),
                 ("s", "g"), ("g", "s"), ("g", "q"), ("q", "e"), ("e", "q"),
                 ("r", "q"), ("r", "b"), ("b", "q")]:
        g.add_edge(u, v)

    result = kosaraju(g)
    order = list(result.all_nodes())
    assert set(order) == {
        frozenset({"a", "k", "v"}), frozenset({"s", "g"}),
        frozenset({"q", "e"}), frozenset({"r"}),
        frozenset({"b"}), frozenset({"y"}),
    }
    assert all(order.index(u) < order.index(v) for u, v in result.get_edges())


def test_deep_chain_no_recursion_limit():
    g = Graph()
    for i in range(5000):
        g.add_node(i)
    for i in range(4999):
        g.add_edge(i, i + 1)
    assert len(kosaraju(g).get_nodes()) == 5000
