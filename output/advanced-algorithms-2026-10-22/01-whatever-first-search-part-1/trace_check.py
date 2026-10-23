# Generates the exact trace shown in video 01 (the mole-rat colony, newest token first).
# The video's step table must match this output line for line.
#
# 7 reachable chambers (S, A, B, C, D, E, F) joined by 12 tunnels,
# plus a separate burrow X-Y cut off by a cave-in.

tunnels = [
    ("S", "A"), ("S", "B"), ("S", "C"),
    ("A", "B"), ("A", "C"), ("A", "D"),
    ("B", "C"), ("B", "E"),
    ("C", "F"),
    ("D", "E"), ("D", "F"),
    ("E", "F"),
    ("X", "Y"),
]

graph = {}
for first, second in tunnels:
    graph.setdefault(first, []).append(second)
    graph.setdefault(second, []).append(first)
for chamber in graph:
    graph[chamber].sort()


def whatever_first_search(graph, start, show=True, log=None):
    to_visit = [(None, start)]
    visited = []
    parent_of = {}
    step = 0
    while len(to_visit) > 0:
        pile_before = list(to_visit)
        came_from, current = to_visit.pop()
        step += 1
        new = current not in visited
        if not new:
            if show:
                print(f"{step:2}. take ({came_from},{current})  already checked -> discard   pile size {len(to_visit)}")
        else:
            visited.append(current)
            parent_of[current] = came_from
            for neighbor in graph[current]:
                to_visit.append((current, neighbor))
            if show:
                print(f"{step:2}. take ({came_from},{current})  CHECK {current}, parent={came_from}   pile size {len(to_visit)}")
                print(f"      pile (newest last): {to_visit}")
        if log is not None:
            log.append({
                "step": step, "came_from": came_from, "current": current, "new": new,
                "pile_before": pile_before, "pile_after": list(to_visit),
                "added": [(current, n) for n in graph[current]] if new else [],
                "marked_after": list(visited), "parent_after": dict(parent_of),
            })
    return visited, parent_of, step


if __name__ == "__main__":
    for chamber in sorted(graph):
        print(chamber, graph[chamber])
    print()
    visited, parent_of, steps = whatever_first_search(graph, "S")
    print()
    print("checked order:", visited)
    print("parent_of:", parent_of)
    print("never checked:", [c for c in graph if c not in visited])
    reachable_tunnels = sum(len(graph[c]) for c in visited) // 2
    print("tunnels in the checked component:", reachable_tunnels)
    print("tokens ever written and taken:", steps, "= 2 x", reachable_tunnels, "+ 1")
    print("tokens that checked a new chamber:", len(visited), "| discarded:", steps - len(visited))
    print("parent tunnels:", len(visited) - 1)
