"""Real data for video 03: graphs, call trees (naive and cached), cache order, and growth numbers."""
from functools import cache

# --- the lab's diamond (lowercase, as in mini-lab.py)
DIAMOND = {"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": ["e"], "e": []}

# --- the trail map: 7 junctions, 12 one-way trails (uphill only), so it has no cycles
TRAIL = {
    "Start": ["Pine", "Creek", "Ridge"],
    "Pine": ["Creek", "Ridge", "Meadow"],
    "Creek": ["Meadow", "Falls"],
    "Ridge": ["Meadow", "Falls"],
    "Meadow": ["Summit"],
    "Falls": ["Summit"],
    "Summit": [],
}

# --- stepping stones 0..7: hop one or two
STONES = {i: [j for j in (i + 1, i + 2) if j <= 7] for i in range(8)}


def naive_tree(graph, s, t):
    """Call tree of plain recursion: (vertex, [children subtrees])."""
    if s == t:
        return (s, [])
    return (s, [naive_tree(graph, c, t) for c in graph[s]])


def cached_tree(graph, s, t, seen=None):
    """Call tree of the cached version: (vertex, hit_flag, [children subtrees])."""
    seen = set() if seen is None else seen
    if s in seen:
        return (s, True, [])
    seen.add(s)
    if s == t:
        return (s, False, [])
    return (s, False, [cached_tree(graph, c, t, seen) for c in graph[s]])


def count(tree):
    return 1 + sum(count(c) for c in (tree[1] if len(tree) == 2 else tree[2]))


def paths(graph, s, t):
    @cache
    def nested(v):
        if v == t:
            return 1
        return sum(nested(c) for c in graph[v])
    return nested(s)


def finish_order(graph, s, t):
    """Order in which values are written into the cache (postorder), with each value."""
    out, done = [], set()

    def go(v):
        if v in done:
            return
        done.add(v)
        for c in graph[v]:
            go(c)
        val = 1 if v == t else sum(vals[c] for c in graph[v])
        vals[v] = val
        out.append((v, val))
    vals = {}
    go(s)
    return out


def calls_with_cache(graph, s, t):
    return count(cached_tree(graph, s, t))


def naive_calls_ladder(n):
    """Calls made by plain recursion on the lab's ladder (stones 0..n+1; n is the target)."""
    calls = {n + 1: 1, n: 1}
    for i in range(n - 1, -1, -1):
        calls[i] = 1 + calls[i + 1] + calls[i + 2]
    return calls[0]


def ladder_paths(n):
    p = {n: 1, n + 1: 0}
    for i in range(n - 1, -1, -1):
        p[i] = p[i + 1] + p[i + 2]
    return p[0]


def times_called(tree, name):
    here = 1 if tree[0] == name else 0
    kids = tree[1] if len(tree) == 2 else tree[2]
    return here + sum(times_called(k, name) for k in kids)


if __name__ == "__main__":
    print("diamond a->e", paths(DIAMOND, "a", "e"), "b->e", paths(DIAMOND, "b", "e"), "e->a", paths(DIAMOND, "e", "a"))
    nt = naive_tree(TRAIL, "Start", "Summit")
    ct = cached_tree(TRAIL, "Start", "Summit")
    print("trail paths", paths(TRAIL, "Start", "Summit"), "naive calls", count(nt), "cached calls", count(ct))
    print("meadow called", times_called(nt, "Meadow"), "times; falls", times_called(nt, "Falls"))
    print("finish order", finish_order(TRAIL, "Start", "Summit"))
    print("diamond naive calls", count(naive_tree(DIAMOND, "a", "e")), "cached", calls_with_cache(DIAMOND, "a", "e"))
    print("diamond order", finish_order(DIAMOND, "a", "e"))
    print("stones 0->7", paths(STONES, 0, 7), "naive", count(naive_tree(STONES, 0, 7)), "cached", calls_with_cache(STONES, 0, 7))
    print("stones order", finish_order(STONES, 0, 7))
    for n in (5, 10, 20, 40, 60):
        print(n, ladder_paths(n), naive_calls_ladder(n), n + 2)
    ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}
    print("lab ladder", paths(ladder, 0, 60), ladder_paths(60) == 2504730781961)
    print("edges trail", sum(len(v) for v in TRAIL.values()), "stones", sum(len(v) for v in STONES.values()))
