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
            post_order = []
            stack = deque()
            stack.append(("visit", node_1))
            while stack:
                action, vertex = stack.pop() # pop off first item 
                if action == "finish":
                    post_order.append(vertex) #if item is finished we mark    post_order
                elif vertex not in visited:
                    visited.add(vertex)
                    stack.append(("finish", vertex))
                    children = graph.get_children(vertex)
                    for child in children[::-1]: 
                        if child not in visited:
                            stack.append(("visit", child))
            yield   post_order 


                        


def dfs_finish_order(graph):
    post_order = []

    for tree in dfs_trees(graph, graph.get.nodes()):
        for node in tree: 
            post_order.append(node)
    return finish_order


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
