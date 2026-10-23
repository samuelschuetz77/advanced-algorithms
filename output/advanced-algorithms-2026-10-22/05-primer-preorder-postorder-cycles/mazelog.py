"""Video 05 data: a one-way-door maze (7 rooms, 12 doors) and its real DFS, with edge types and cycle checks."""
import sys
sys.path.insert(0, "../common")
from dfslog import dfs

MAZE = {
    "A": ["B", "C", "E"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["E"],
    "E": ["B"],
    "F": ["C", "G"],
    "G": ["D"],
}
RES = dfs(MAZE, roots=["A"])
EVENTS = RES["events"]
PRE, POST = RES["pre"], RES["post"]
ETYPE = {(e["u"], e["v"]): e["etype"] for e in EVENTS if e["kind"] == "edge"}

# the maze with its two back edges removed: a DAG
DAG = {k: [w for w in v if ETYPE[(k, w)] != "back"] for k, v in MAZE.items()}


def is_acyclic(graph):
    """The book's IsAcyclic (Figure 6.7) in plain Python. Returns (answer, first offending edge)."""
    status = {v: "new" for v in graph}
    bad = []

    def visit(v):
        status[v] = "active"
        for w in graph[v]:
            if status[w] == "active":
                bad.append((v, w))
                return False
            if status[w] == "new":
                if visit(w) == False:
                    return False
        status[v] = "finished"
        return True

    for v in graph:
        if status[v] == "new":
            if visit(v) == False:
                return False, (bad[0] if bad else None)
    return True, None


def component_counts():
    """How many separate DFS trees DFSAll builds, for different start orders."""
    import itertools
    out = {}
    for order in (["A"], ["G", "A"], ["D", "A"], ["E", "A"]):
        res = dfs(MAZE, roots=order + [v for v in MAZE if v not in order])
        trees = sum(1 for v in MAZE if v not in res["parent"])
        out[tuple(order)] = trees
    return out


if __name__ == "__main__":
    for i, e in enumerate(EVENTS):
        if e["kind"] == "edge":
            print(i, "edge", e["u"], "->", e["v"], e["etype"])
        else:
            print(i, e["kind"], e["v"], e["clock"])
    print("pre ", RES["pre_order"], "post", RES["post_order"])
    print("types", sorted(set(ETYPE.values())), {t: sum(1 for x in ETYPE.values() if x == t) for t in set(ETYPE.values())})
    print("is_acyclic(MAZE)", is_acyclic(MAZE), "DAG", is_acyclic(DAG), "edges in DAG", sum(len(v) for v in DAG.values()))
    print("trees by start order", component_counts())
    print("edges", sum(len(v) for v in MAZE.values()))
