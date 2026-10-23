"""The metro-map graph and real runs of whatever-first search on it (stack and queue).

Everything the video shows about a run comes from `run()`, never from hand-typed values.
"""
PEOPLE = ["Arch", "Bay", "Cove", "Dock", "East", "Fort", "Gate"]
FRIENDS = [("Arch", "Bay"), ("Arch", "Cove"), ("Arch", "Dock"), ("Bay", "Cove"), ("Bay", "East"), ("Cove", "Dock"),
           ("Cove", "East"), ("Cove", "Fort"), ("Dock", "Fort"), ("East", "Fort"), ("East", "Gate"), ("Fort", "Gate")]
FERRY = [("Mill", "Nest"), ("Nest", "Oak"), ("Mill", "Oak")]
# one-way tracks: (a, b) means trains run only from a to b
ONE_WAY = [("Arch", "Bay"), ("Arch", "Cove"), ("Dock", "Arch"), ("Bay", "Cove"), ("Bay", "East"), ("Cove", "East"),
           ("Cove", "Fort"), ("Dock", "Fort"), ("Gate", "East"), ("Gate", "Fort"), ("East", "Fort"), ("Dock", "Cove")]

POS = {"Arch": (230, 520), "Bay": (500, 290), "Cove": (500, 520), "Dock": (500, 750),
       "East": (850, 330), "Fort": (850, 710), "Gate": (1100, 520)}


def undirected(edges):
    g = {}
    for u, v in edges:
        g.setdefault(u, []).append(v)
        g.setdefault(v, []).append(u)
    for k in g:
        g[k].sort()
    return g


def directed(edges):
    g = {}
    for u, v in edges:
        g.setdefault(u, [])
        g.setdefault(v, [])
        g[u].append(v)
    for k in g:
        g[k].sort()
    return g


G = undirected(FRIENDS)
G2 = undirected(FRIENDS + FERRY)
GD = directed(ONE_WAY)


def run(graph, start, mode):
    """Whatever-first search. mode 'stack' takes the newest token, 'queue' the oldest.
    Returns a list of step dicts. Piles are lists with the OLDEST token first."""
    bag = [(None, start)]
    visited, parent, depth, log = [], {}, {}, []
    step = 0
    while bag:
        before = list(bag)
        idx = len(bag) - 1 if mode == "stack" else 0
        came_from, current = bag.pop(idx)
        step += 1
        new = current not in visited
        added = []
        if new:
            visited.append(current)
            parent[current] = came_from
            depth[current] = 0 if came_from is None else depth[came_from] + 1
            for n in graph[current]:
                bag.append((current, n))
                added.append((current, n))
        log.append({"step": step, "came_from": came_from, "current": current, "new": new, "idx": idx,
                    "pile_before": before, "pile_after": list(bag), "added": added,
                    "marked_after": list(visited), "parent_after": dict(parent), "depth": dict(depth)})
    return log


STACK = run(G, "Arch", "stack")
QUEUE = run(G, "Arch", "queue")
STACK_PARENT = STACK[-1]["parent_after"]
QUEUE_PARENT = QUEUE[-1]["parent_after"]
QUEUE_DEPTH = QUEUE[-1]["depth"]
STACK_DEPTH = STACK[-1]["depth"]
DIRECTED = run(GD, "Arch", "stack")
REACHED_DIRECTED = DIRECTED[-1]["marked_after"]

if __name__ == "__main__":
    for name, log in (("stack", STACK), ("queue", QUEUE)):
        print(name, "steps", len(log), "order", log[-1]["marked_after"])
        print("  parents", log[-1]["parent_after"])
        print("  depths ", log[-1]["depth"])
        print("  max pile", max(len(s["pile_before"]) for s in log))
    print("directed reached:", REACHED_DIRECTED, "steps", len(DIRECTED))
    print("groups:", len(G2) and sorted(G2))
