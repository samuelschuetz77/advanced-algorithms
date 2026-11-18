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