"""Data for video 04: the dinner DAG (7 tasks, 12 arrows), the class graphs, and the lab code run for real."""
import sys
sys.path.insert(0, "../common")
from dfslog import backward_edges, dfs, forward_ok

DINNER = {
    "Shop": ["Chop", "Boil", "Fry"],
    "Chop": ["Boil", "Fry", "Sauce"],
    "Boil": ["Sauce", "Plate"],
    "Fry": ["Sauce", "Plate"],
    "Sauce": ["Plate"],
    "Plate": ["Eat"],
    "Eat": [],
}
# the class graphs, as in the 10/19 notes (letters) with a morning-routine story
G1 = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": []}
G2_E_FIRST = {"E": ["A"], "A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": []}
G2_A_FIRST = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": [], "E": ["A"]}
TASK = {"A": "Shower", "B": "Dress", "C": "Coffee", "D": "Leave", "E": "Wake up"}
# the lab's graphs
LAB_G = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}
LAB_G2 = {"x": [], "y": ["x"], "z": ["y", "x"]}


def topo_order_yours(children):
    """Your function as written in mini-lab.py (returns pre_order)."""
    pre_order, post_order, visited = [], [], set()

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


def topo_order_fixed(children):
    pre_order, post_order, visited = [], [], set()

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
    return list(reversed(post_order))


def spec_test(fn):
    results = []
    for graph in [LAB_G, LAB_G2]:
        order = fn(graph)
        ok_set = sorted(order) == sorted(graph)
        ok_edges = all(order.index(u) < order.index(w) for u in graph for w in graph[u])
        results.append((order, ok_set, ok_edges))
    return results


# dinner plus "set the table": a second task with nothing before it (two start tasks)
DINNER2_C1 = dict(DINNER)
DINNER2_C1["Table"] = ["Eat"]            # case 1: Shop is listed first, Table last
DINNER2_C2 = {"Table": ["Eat"]}
DINNER2_C2.update(DINNER)                # case 2: Table is listed first

DINNER_DFS = dfs(DINNER)
CASE1 = dfs(DINNER2_C1)
CASE2 = dfs(DINNER2_C2)
G1_DFS = dfs(G1)
E_FIRST = dfs(G2_E_FIRST)
A_FIRST = dfs(G2_A_FIRST)

if __name__ == "__main__":
    for nm, g, r in (("case1", DINNER2_C1, CASE1), ("case2", DINNER2_C2, CASE2)):
        print(nm, "pre", r["pre_order"], "backward", backward_edges(g, r["pre_order"]))
        print(nm, "rev", list(reversed(r["post_order"])), forward_ok(g, list(reversed(r["post_order"]))))
    d = DINNER_DFS
    print("dinner pre ", d["pre_order"])
    print("dinner post", d["post_order"], "-> reversed", list(reversed(d["post_order"])))
    print("preorder forward?", forward_ok(DINNER, d["pre_order"]), "backward:", backward_edges(DINNER, d["pre_order"]))
    print("rev post forward?", forward_ok(DINNER, list(reversed(d["post_order"]))))
    print("events", len(d["events"]), "edges", sum(len(v) for v in DINNER.values()))
    for name, g in (("G1", G1_DFS), ("E first", E_FIRST), ("A first", A_FIRST)):
        print(name, "pre", g["pre_order"], "post", g["post_order"], "rev", list(reversed(g["post_order"])))
    for name, fn in (("yours", topo_order_yours), ("fixed", topo_order_fixed)):
        print(name, spec_test(fn))
