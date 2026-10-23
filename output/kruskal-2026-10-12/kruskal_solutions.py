"""Two readable Kruskal solutions for the October 12 class graph.

Each edge is a tuple: (cost, start, end). The class drawing leaves C-E
unlabeled; this video assigns it cost 17. A disconnected input produces a
minimum spanning forest rather than one spanning tree. Pass vertices as a
list or tuple so the algorithms can scan it more than once.
"""


def edge_cost(edge):
    """Tell sorted() which number to compare for each edge."""
    cost, start, end = edge
    return cost


def kruskal_naive(vertices, edges):
    """Keep a group label per vertex; scan every vertex after each merge."""
    group = {}
    for vertex in vertices:
        group[vertex] = vertex  # Every vertex starts in its own tree.

    tree = []
    for cost, start, end in sorted(edges, key=edge_cost):
        if group[start] == group[end]:
            continue  # The edge would make a cycle.

        old_group = group[end]
        new_group = group[start]
        for vertex in vertices:
            if group[vertex] == old_group:
                group[vertex] = new_group

        tree.append((cost, start, end))
        if len(tree) == len(vertices) - 1:
            break
    return tree


class DisjointSet:
    """Track which vertices belong to the same tree.

    find(vertex) returns that tree's representative. union(start, end)
    merges two different trees and returns True; if they are already one
    tree, it returns False. Parent links and tree sizes make this efficient.
    """

    def __init__(self, vertices):
        self.parent = {}
        self.size = {}
        for vertex in vertices:
            self.parent[vertex] = vertex
            self.size[vertex] = 1

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, start, end):
        first_root = self.find(start)
        second_root = self.find(end)
        if first_root == second_root:
            return False

        if self.size[first_root] < self.size[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        self.size[first_root] += self.size[second_root]
        return True


def kruskal_union_find(vertices, edges):
    """Use disjoint-set union to avoid repeated whole-group scans."""
    groups = DisjointSet(vertices)
    tree = []

    for cost, start, end in sorted(edges, key=edge_cost):
        if groups.union(start, end):
            tree.append((cost, start, end))
            if len(tree) == len(vertices) - 1:
                break
    return tree


VERTICES = tuple("ABCDEFGH")
CLASS_EDGES = [
    (1, "B", "C"), (3, "A", "C"), (4, "C", "H"), (5, "A", "B"),
    (9, "D", "E"), (6, "H", "F"), (7, "E", "F"), (8, "G", "F"),
    (10, "D", "G"), (11, "E", "G"), (17, "C", "E"),
]


if __name__ == "__main__":
    for solve in (kruskal_naive, kruskal_union_find):
        result = solve(VERTICES, CLASS_EDGES)
        assert [cost for cost, start, end in result] == [1, 3, 4, 6, 7, 8, 9]
        assert sum(cost for cost, start, end in result) == 38

        alternate = [
            (6 if (start, end) == ("D", "E") else cost, start, end)
            for cost, start, end in CLASS_EDGES
        ]
        assert sum(cost for cost, start, end in solve(VERTICES, alternate)) == 35
    print("Both solutions match the class graph and the cost-6 hypothetical.")
