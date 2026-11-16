# Graph class from the earlier data structures project.

class Graph:
    def __init__(self):
        self.node_data = {}   # node -> its data
        self.neighbors = {}   # node -> {child: edge data}  (dict of dicts, so edge lookup is O(1))
        self.parents = {}     # node -> list of nodes that point at it (reverse adjacency)
        self.edges = []       # flat list of (parent, child) so we can loop every edge in O(E)

    def add_node(self, node, data=None): # this one ony inserts new ones doesnt update
        if node not in self.node_data:
            self.node_data[node] = data
            self.neighbors[node] = {}
            self.parents[node] = []

    def add_edge(self, parent, child, data=None): # this one can update
        self.neighbors[parent][child] = data # neighnors is a dict of dict
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


# Part 1: build G' with the same nodes but every edge flipped. O(V + E).
def reverse(graph):
    reversed_graph = Graph()

    # copy every node (and its data) first, so add_edge below never hits a missing node
    for node in graph.get_nodes():
        reversed_graph.add_node(node, graph.get_node_data(node))
    # u->v in graph becomes v->u here; the edge data rides along unchanged
    for u, v in graph.get_edges():
        reversed_graph.add_edge(v, u, graph.get_edge_data(u, v))
    return reversed_graph


# Part 2: every node, in the order a recursive DFS finishes (pops) it. O(V + E).
def dfs_finish_order(graph):
    postorder = []
    visited = set()

    def build_topo_from(node):
        visited.add(node)
        for child in graph.get_children(node):
            if child not in visited:
                build_topo_from(child)
        # appended AFTER all descendants are done = finish time.
        # a node always finishes after everything reachable from it (that's new)
        postorder.append(node)

    # outer loop restarts DFS from unvisited nodes so disconnected
    # parts of the graph still get covered
    for node in graph.get_nodes():
        if node not in visited:
            build_topo_from(node)


    return postorder



# Part 3: Kosaraju. Returns the meta graph (one node per SCC, id = frozenset of members).
def kosaraju(graph):
    # 1. First pass: finish times on original graph
    # reversing puts the LAST finisher first. That node sits in a "source" SCC
    # (nothing outside its component can reach into it), so it is the safe place to start.
    scc_start = dfs_finish_order(graph)[::-1]

    reversed_graph = reverse(graph)


    visited = set()
    g_prime = Graph()
    belongs_to = {}   # original node -> the SCC (frozenset) it lives in


    # DFS on the REVERSED graph. Because the start is a source SCC of the original,
    # in the reversed graph it is a sink, so the DFS can't escape into another SCC:
    # everything it reaches is exactly one component.
    def collect_component(node, comp):
        visited.add(node)
        comp.add(node)
        for child in reversed_graph.get_children(node):
            if child not in visited:
                collect_component(child, comp)

    # 2. Second pass: take starts in decreasing finish time; each fresh start = one new SCC.
    for d in scc_start:
        if d not in visited:
            comp = set()
            collect_component(d, comp)
            scc_id = frozenset(comp)   # frozenset so it is hashable and can be a graph node id

            # components are discovered in topological order of the meta graph,
            # and nodes keep insertion order, so all_nodes() is already a topological sort
            g_prime.add_node(scc_id)
            for node in scc_id:
                belongs_to[node] = scc_id

    # 3. Build the meta graph's edges: map both ends of every original edge to their
    # components. Same component = internal edge, skip it. Also skip repeats. O(E).
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

    # c finishes first (deepest), then b, then a; d is a separate DFS start
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
    # topological order: the edge ab -> c means ab must come before c
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
    # every meta edge must point forward in all_nodes() order = valid topological sort
    assert all(order.index(u) < order.index(v) for u, v in result.get_edges())
