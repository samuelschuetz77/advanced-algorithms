# Samuel Schuetz 11/14/2026-11/15/2026


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


textbook_square = [
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,0,0,0],
    [1,0,1,0,1,0,0,0,0],
    [1,1,1,0,1,0,1,1,0],
    [0,0,1,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,1,0]
    ]


def eleven_point_nine(input_square):
    graph = Graph()
    graph.add_node('source')
    graph.add_node('sink')
    rows = len(input_square)
    column = len(input_square[0])

    for i in range(0, rows, 1):
        graph.add_node(f"row {i}")
        graph.add_node(f"col {i}")
        graph.add_edge('source',f"row {i}", 1)
        graph.add_edge(f"col {i}", 'sink', 1) 
  
    for i in range(0, rows, 1):
        for t in range(0, column,1):
            if input_square[i][t] == 1:
                graph.add_edge(f"row {i}", f"col {t}", 1) 

    return graph



# UNFINISHED Not Part of assignment
def max_flow_9(capacity_graph):
    flow_graph = Graph()
    node_copy = list(capacity_graph.get_nodes())
    edge_copy = list(capacity_graph.get_edges())
    for n in node_copy:
        flow_graph.add_node(n)
    for p,c in edge_copy:
        flow_graph.add_edge(p,c,0)
    return flow_graph



#edge leaving source 
def solution(graph, n): #returns whether all n tokens can be placed
    source_children = graph.get_children("source")
    source_from_count = sum(graph.get_edge_data('source', child) for child in source_children)
    return source_from_count == n


test_square = [[1]]
diagonal = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
           ]

def test_1by1():
    graph = eleven_point_nine(test_square)
    nodes = list(graph.get_nodes())
    edges = set(graph.get_edges())
    assert len(nodes) == 4
    assert nodes[0:2] == ['source', 'sink']
    assert edges == {("source", "row 0"), ("row 0", "col 0"), ("col 0", "sink")}
    for parent, child in edges:
        assert graph.get_edge_data(parent, child) == 1

    

def test_1by1_black():
    graph = eleven_point_nine([[0]])
    nodes = list(graph.all_nodes())
    edges = set(graph.get_edges())
    assert nodes == ['source', 'sink', 'row 0', 'col 0']
    assert edges == {('source', 'row 0'), ('col 0', 'sink')}
    for parent, child in edges:
        assert graph.get_edge_data(parent, child) == 1

def test_sln_1by1():
    graph = eleven_point_nine(test_square)
    graph_b = eleven_point_nine([[0]])
    # Hand-computed flows: the white route carries 1; the black board carries 0.
    graph_b.neighbors['source']['row 0'] = 0
    graph_b.neighbors['col 0']['sink'] = 0
    sln = solution(graph, 1)
    sln2 = solution(graph_b, 1)
    assert sln == True
    assert sln2 == False

def test_3by3():
    graph = eleven_point_nine(diagonal)
    assert set(graph.get_edges()) == {
        ('source', 'row 0'), ('source', 'row 1'), ('source', 'row 2'),
        ('row 0', 'col 0'), ('row 1', 'col 1'), ('row 2', 'col 2'),
        ('col 0', 'sink'), ('col 1', 'sink'), ('col 2', 'sink'),
    }
    for parent, child in graph.get_edges():
        assert graph.get_edge_data(parent, child) == 1



    
   


