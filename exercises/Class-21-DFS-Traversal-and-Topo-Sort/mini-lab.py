#Part 1

from functools import cache

# count_paths(graph, s, t) returns how many different paths go from s to t in
# a DAG, where graph maps each vertex to the list of vertices its edges point
# to. (In the graph g below, a reaches e by a-b-d-e and by a-c-d-e.)

# Write it so that this pytest test passes in O(V + E) time:
# g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}

def count_paths(graph, s, t):
    # base case
    @cache
    def nested(s):
        if (s == t):
            return 1
        return sum(nested(child) for child in graph[s])
    return nested(s)


def topo_order(children):
    pre_order = []
    post_order = []
    visited = set()
    def build_topo_from(node):
        pre_order.append(node)
        visited.add(node)
        for child in children[node]:
            if child not in visited:
                build_topo_from(child)
        post_order.append(node)
        
    for node in children:
        if node not in visited:
            build_topo_from(node)
    return pre_order


#at this point he wanted to 



#recursive step

g = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}


def test_count_paths():
    assert count_paths(g, "a", "e") == 2
    assert count_paths(g, "b", "e") == 1
    assert count_paths(g, "e", "a") == 0
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    assert count_paths(ladder, 0, 60) == 2504730781961

def test_topo_order():
    assert topo_order(g, "a", "e") == 2
    assert topo_order(g, "b", "e") == 1
    assert topo_order(g, "e", "a") == 0
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    assert topo_order(ladder, 0, 60) == 2504730781961