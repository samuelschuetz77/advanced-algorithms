"""Video 06 data: the hiking map with scenery scores, explicit topological sort, reversal, longest path (all real runs)."""
import sys
sys.path.insert(0, "../common")
from dfslog import backward_edges, dfs, forward_ok

TRAIL = {
    "Start": ["Pine", "Creek", "Ridge"],
    "Pine": ["Creek", "Ridge", "Meadow"],
    "Creek": ["Meadow", "Falls"],
    "Ridge": ["Meadow", "Falls"],
    "Meadow": ["Summit"],
    "Falls": ["Summit"],
    "Summit": [],
}
SCORE = {("Start", "Pine"): 3, ("Start", "Creek"): 4, ("Start", "Ridge"): 2, ("Pine", "Creek"): 5, ("Pine", "Ridge"): 1,
         ("Pine", "Meadow"): 6, ("Creek", "Meadow"): 2, ("Creek", "Falls"): 7, ("Ridge", "Meadow"): 4,
         ("Ridge", "Falls"): 3, ("Meadow", "Summit"): 5, ("Falls", "Summit"): 4}
V = len(TRAIL)

RES = dfs(TRAIL, roots=["Start"])
POST = RES["post_order"]
TOPO = list(reversed(POST))

# explicit topological sort (book Figure 6.9): clock starts at V, finished vertex goes to S[clock], clock counts down
FILL = []  # (vertex, slot index 0-based, clock value 1-based)
_clock = V
for v in POST:
    FILL.append((v, _clock - 1, _clock))
    _clock -= 1


def reverse_graph(g):
    r = {v: [] for v in g}
    for u in g:
        for w in g[u]:
            r[w].append(u)
    for v in r:
        r[v].sort(key=lambda x: list(g).index(x))
    return r


REV = reverse_graph(TRAIL)
REV_RES = dfs(REV, roots=["Summit"])
REV_POST = REV_RES["post_order"]  # a postordering of rev(G): a topological order of G (book: not nec. the reversal of one of G)
REV_TOPO_OF_G = list(REV_POST)

# longest path with memoization (book's LongestPath), logging the order values are written
def longest_path_log(graph, length, s, t):
    best, log = {}, []

    def go(v):
        if v == t:
            return 0
        if v not in best:
            best[v] = float("-inf")
            cands = []
            for w in graph[v]:
                c = length[(v, w)] + go(w)
                cands.append((w, length[(v, w)], go(w), c))
                best[v] = max(best[v], c)
            log.append((v, cands, best[v]))
        return best[v]
    total = go(s)
    return total, best, log


LONGEST, BEST, LOG = longest_path_log(TRAIL, SCORE, "Start", "Summit")
BEST["Summit"] = 0

def best_route():
    route, v = ["Start"], "Start"
    while v != "Summit":
        v = max(TRAIL[v], key=lambda w: SCORE[(v, w)] + BEST[w])
        route.append(v)
    return route

ROUTE = best_route()

# dynamic programming: evaluate in reverse topological order = postorder
def dp_in_postorder():
    val = {}
    out = []
    for v in POST:
        if v == "Summit":
            val[v] = 0
        else:
            val[v] = max(SCORE[(v, w)] + val[w] for w in TRAIL[v])
        out.append((v, val[v]))
    return out

DP = dp_in_postorder()

# memoized recursion: order in which values get FINALIZED (compare with DP)
MEMO_ORDER = [("Summit", 0)] + [(v, best) for v, _c, best in LOG]

if __name__ == "__main__":
    print("post", POST, "topo", TOPO, "forward ok", forward_ok(TRAIL, TOPO))
    print("fill", FILL)
    print("rev graph", REV)
    print("rev post", REV_TOPO_OF_G, "forward ok in G?", forward_ok(TRAIL, REV_TOPO_OF_G), "== reversal of G's post?", REV_TOPO_OF_G == TOPO)
    print("longest", LONGEST, "route", ROUTE, "sum", sum(SCORE[(a, b)] for a, b in zip(ROUTE, ROUTE[1:])))
    print("DP", DP)
    print("memo order", MEMO_ORDER)
    print("edges", sum(len(v) for v in TRAIL.values()))
    print("DP == memo", dict(DP) == dict(MEMO_ORDER), [v for v, _ in DP] == [v for v, _ in MEMO_ORDER])
