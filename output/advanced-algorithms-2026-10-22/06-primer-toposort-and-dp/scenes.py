"""Video 06 scenes: topological sort (JEA 6.3) and memoization / dynamic programming (JEA 6.4)."""
from __future__ import annotations

import math

import chars
import hikelog as H
from dfslog import backward_edges
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, RED, WHITE, YELLOW, clamp, ease, lerp, mix, point_along,
)
from graphview import GraphView
from widgets import (
    CodeCard, PANEL, chrome, draw_wrapped, notes_panel, panel_card, predict_chip, tag, token_pill, wrap,
)

PURPLE = (140, 80, 200)
ORANGE = (234, 140, 36)

T_POS = {"Start": (640, 470), "Pine": (340, 330), "Creek": (940, 330), "Ridge": (340, 640),
         "Meadow": (640, 230), "Falls": (940, 640), "Summit": (130, 470)}
T_EDGES = [(u, v) for u, vs in H.TRAIL.items() for v in vs]
T_BULGE = {("Ridge", "Meadow"): 90, ("Falls", "Summit"): -70, ("Meadow", "Summit"): 40}
GV = GraphView(T_POS, [(u, v, T_BULGE.get((u, v), 0)) for u, v in T_EDGES], directed=True, r=50, label_size=24, weights=H.SCORE)


def stage(ctx, kind="trail"):
    cv = ctx.cv
    bg = {"trail": (238, 246, 236), "plain": (244, 246, 250), "river": (238, 246, 252)}[kind]
    cv.rrect(30, 112, 1258, 916, 28, fill=bg, outline=(220, 226, 234), width=3)
    if kind == "trail":
        for (cx, cy, rx, ry) in [(640, 520, 560, 320), (640, 520, 420, 230), (640, 520, 270, 130)]:
            cv.ellipse(cx, cy, rx, ry, outline=(214, 230, 210), width=3)


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def badge(cv, x, y, val, a=1.0, color=ACCENT, r=26, size=28):
    cv.circle(x, y, r, fill=WHITE, outline=color, width=4, a=a)
    cv.text(x, y - 1, str(val), size, color, True, anchor="mm", a=a)


def chips(cv, x0, y0, labels, color=ACCENT, a=1.0, w=108, h=40, gap=8, size=20, per_row=5, on=True):
    for i, lab in enumerate(labels):
        col, row = i % per_row, i // per_row
        x, y = x0 + col * (w + gap), y0 + row * (h + 8)
        cv.rrect(x, y, x + w, y + h, h / 2, fill=ACCENT_SOFT if on else PAPER, outline=color, width=3, a=a)
        cv.text(x + w / 2, y + h / 2, lab, size, INK, True, anchor="mm", a=a)


# ---------------------------------------------------------------- line layout (same idea as video 4)
def line_view(order, graph, x0=100, x1=1180, y=520, r=36, size=22):
    n = len(order)
    pos = {v: (x0 + (x1 - x0) * i / max(1, n - 1), y) for i, v in enumerate(order)}
    idx = {v: i for i, v in enumerate(order)}
    edges = []
    for u in graph:
        for w in graph[u]:
            edges.append((u, w, -(60 + 40 * abs(idx[u] - idx[w]))))
    return GraphView(pos, edges, directed=True, r=r, label_size=size), idx


def draw_line(ctx, order, graph, y=520, a=1.0, r=36, size=22, x0=100, x1=1180, good=BLUE):
    gv, idx = line_view(order, graph, x0, x1, y, r, size)
    es = {gv.key(u, w): ((RED if idx[u] > idx[w] else good), 6, a) for u in graph for w in graph[u]}
    gv.draw(ctx, estyle=es, vfade={v: a for v in order})
    return gv, len(backward_edges(graph, order))


# ================================================================ part A: topological sort (6.3)
BAD_ORDER = ["Pine", "Start", "Ridge", "Falls", "Creek", "Meadow", "Summit"]


def line_pos(order, x0=120, x1=1160, y=330):
    n = len(order)
    return {v: (x0 + (x1 - x0) * i / (n - 1), y) for i, v in enumerate(order)}


def scene_def(ctx):
    """Start from the tangled drawing; slide the vertices into a line where every arrow points right."""
    stage(ctx, "plain")
    cv = ctx.cv
    t_ok = ctx.cue("ok")
    f = ease(ctx.ramp(t_ok, t_ok + 2.4)) if t_ok is not None else 0.0
    ok = ctx.p("ok", 0.5)
    bad = ctx.p("bad", 0.5)
    tgt = line_pos(H.TOPO)
    idx = {v: i for i, v in enumerate(H.TOPO)}
    pos = {v: (lerp(T_POS[v][0], tgt[v][0], f), lerp(T_POS[v][1], tgt[v][1], f)) for v in T_POS}
    edges = []
    for u, w in T_EDGES:
        line_bulge = -(60 + 40 * abs(idx[u] - idx[w]))
        edges.append((u, w, lerp(T_BULGE.get((u, w), 0), line_bulge, f)))
    gv = GraphView(pos, edges, directed=True, r=44, label_size=20)
    es = {gv.key(u, w): (mix(LINE, GREEN, f), 6, 1.0) for u, w in T_EDGES}
    gv.draw(ctx, estyle=es)
    if f >= 0.99:
        tag(cv, 640, 450, "line-up 1: every arrow points right", GREEN, a=ok, size=26)
    if bad > 0:
        _, nb = draw_line(ctx, BAD_ORDER, H.TRAIL, y=720, a=bad, r=44, size=20, x0=120, x1=1160)
        cv.text(80, 610, "line-up 2", 28, RED, True, a=bad)
        tag(cv, 640, 830, f"{len(backward_edges(H.TRAIL, BAD_ORDER))} arrows point backward", RED, a=bad, size=26)
    panel_card(ctx, "TOPOLOGICAL ORDERING  (PDF p.250)")
    fm, tt = ctx.p("formal", 0.5), ctx.p("tot", 0.5)
    cv.text(1330, 190, "line-up 1 is one.", 34, GREEN, True, a=ok)
    cv.text(1330, 240, "line-up 2 is not.", 34, RED, True, a=bad)
    cv.rrect(1316, 340, 1854, 560, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=fm)
    cv.text(1344, 362, "the rule", 26, MUTED, True, a=fm)
    draw_wrapped(cv, 1344, 404, "for every edge from u to v, u comes before v", 32, 480, ACCENT_DARK, True, a=fm)
    cv.rrect(1316, 600, 1854, 800, 20, fill=PAPER, outline=PANEL_LINE, width=3, a=tt)
    cv.text(1344, 622, "the book says: a total order", 26, MUTED, True, a=tt)
    draw_wrapped(cv, 1344, 664, "for any two vertices, one definitely comes before the other", 28, 480, INK, False, a=tt)
    finish(ctx)


CYC = GraphView({"x": (330, 560), "y": (640, 560), "z": (950, 560)}, [("x", "y", -120), ("y", "z", -120), ("z", "x", -260)],
                directed=True, r=48, label_size=40)


def scene_cycle(ctx):
    """Why a cycle breaks it: try each task as the first one; each is blocked by the arrow pointing into it."""
    stage(ctx, "plain")
    cv = ctx.cv
    cv.text(640, 150, "x before y,  y before z,  z before x", 34, INK, True, anchor="mm")
    tries = [("x", "x1", ("z", "x"), "task z must come before it"), ("y", "y1", ("x", "y"), "task x must come before it"),
             ("z", "z1", ("y", "z"), "task y must come before it")]
    es, rings = {}, {}
    cur = None
    for v, cue, edge, why in tries:
        a = ctx.p(cue, 0.4)
        if a > 0.02:
            cur = (v, edge, a)
    for v, cue, edge, why in tries:
        if ctx.reached(cue):
            es[edge] = (RED, 9, 0.45)
    if cur:
        v, edge, a = cur
        es[edge] = (RED, 14, 1.0)
        rings[v] = (ORANGE, a)
    al = ctx.p("all", 0.5)
    if al > 0:
        es = {e: (RED, 11, 1.0) for e in (("x", "y"), ("y", "z"), ("z", "x"))}
    CYC.draw(ctx, estyle=es or None, rings=rings)
    if cur and al < 0.2:
        v, edge, a = cur
        x, y = CYC.pos[v]
        tag(cv, x, y - 130, f"{v} first?", ORANGE, a=a, size=30)
    panel_card(ctx, "WHO CAN GO FIRST?")
    yy = 180
    for v, cue, edge, why in tries:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, yy, 1854, yy + 170, 20, fill=PAPER, outline=RED, width=4, a=a)
        cv.circle(1368, yy + 52, 26, fill=RED, a=a)
        cv.line((1357, yy + 41), (1379, yy + 63), WHITE, 5, a)
        cv.line((1379, yy + 41), (1357, yy + 63), WHITE, 5, a)
        cv.text(1416, yy + 24, f"not task {v}", 36, RED, True, a=a)
        draw_wrapped(cv, 1416, yy + 82, f"because {why}", 27, 420, INK, False, a=a)
        yy += 190
    c = ctx.p("all", 0.5)
    cv.rrect(40, 800, 1246, 906, 22, fill=(253, 232, 232), outline=RED, width=3, a=c)
    draw_wrapped(cv, 70, 818, "Every vertex on a cycle has an arrow pointing into it. Whichever one goes first has an arrow aiming back at it.", 28, 1150, RED, True, a=c)
    bk = ctx.p("book", 0.5)
    cv.text(1330, 770, "book, p.250: from the other end,", 24, MUTED, True, a=bk)
    cv.text(1330, 806, "the rightmost vertex has an arrow", 24, MUTED, False, a=bk)
    cv.text(1330, 838, "leaving it, and it can only point left.", 24, MUTED, False, a=bk)
    finish(ctx)


def scene_goals(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    GV.draw(ctx, show_weights=True, rings={"Start": (BLUE, ctx.pulse("s", 1.2)), "Summit": (ORANGE, ctx.pulse("s", 1.2))})
    panel_card(ctx, "THE HIKING MAP, AGAIN")
    cv.text(1330, 190, "7 junctions", 40, INK, True)
    cv.text(1330, 246, "12 one-way trails", 40, INK, True)
    cv.text(1330, 320, "the number on a trail:", 26, MUTED, True, a=ctx.p("score", 0.5))
    cv.text(1330, 360, "scenery points", 38, GREEN, True, a=ctx.p("score", 0.5))
    g1, g2 = ctx.p("g1", 0.5), ctx.p("g2", 0.5)
    cv.rrect(1316, 470, 1854, 610, 18, fill=PAPER, outline=BLUE, width=4, a=g1)
    cv.text(1344, 494, "goal 1", 26, MUTED, True, a=g1)
    cv.text(1344, 532, "an order that respects every trail", 30, BLUE, True, a=g1)
    cv.rrect(1316, 640, 1854, 780, 18, fill=PAPER, outline=GREEN, width=4, a=g2)
    cv.text(1344, 664, "goal 2", 26, MUTED, True, a=g2)
    cv.text(1344, 702, "the most scenic route to the Summit", 30, GREEN, True, a=g2)
    finish(ctx)


def scene_fill(ctx):
    """Explicit topological sort (Figure 6.9): finished vertices go into an array from the back."""
    stage(ctx, "trail")
    cv = ctx.cv
    fills = H.FILL
    placed = {}
    ringv = None
    for i, (v, slot, clock) in enumerate(fills):
        t = ctx.cue(f"f{i + 1}")
        took = t is not None and ctx.t >= t
        ctx.sig.append(1 if took else 0)
        if took:
            placed[v] = (slot, ctx.ramp(t, t + 0.8))
            ringv = v if ctx.t - t < 1.0 else ringv
    marked = {v: 1.0 for v in placed}
    GV.draw(ctx, marked=marked, rings={ringv: (BLUE, 1.0)} if ringv else None)
    # the array S
    x0, w, gap, y0 = 90, 146, 12, 790
    cv.text(70, 706, "the array S  (filled from the back)", 26, MUTED, True)
    nfilled = len(placed)
    clock = H.V - nfilled
    for i in range(H.V):
        x = x0 + i * (w + gap)
        cv.rrect(x, y0, x + w, y0 + 80, 16, fill=WHITE, outline=GRAY, width=3)
        cv.text(x + w / 2, y0 - 18, f"S[{i + 1}]", 20, MUTED, True, anchor="mm")
    for v, (slot, f) in placed.items():
        sx, sy = T_POS[v]
        tx, ty = x0 + slot * (w + gap) + w / 2, y0 + 40
        x, y = lerp(sx, tx, ease(f)), lerp(sy, ty, ease(f))
        cv.rrect(x - 62, y - 28, x + 62, y + 28, 14, fill=ACCENT_SOFT, outline=ACCENT, width=4)
        cv.text(x, y, v, 28, INK, True, anchor="mm")
    if clock >= 1:
        cx = x0 + (clock - 1) * (w + gap) + w / 2
        tag(cv, cx, y0 + 112, f"clock = {clock}", BLUE, size=24)
    panel_card(ctx, "BOOK: FIGURE 6.9, PDF p.251")
    draw_wrapped(cv, 1330, 190, "clock starts at V = 7. When a vertex finishes, it goes into S[clock], and the clock goes down by one.", 29, 510, INK, False)
    cv.text(1330, 420, "the first to finish:", 26, MUTED, True, a=ctx.p("f1", 0.4))
    cv.text(1330, 462, "Summit, into S[7]", 34, ACCENT_DARK, True, a=ctx.p("f1", 0.4))
    cv.text(1330, 540, "the last to finish:", 26, MUTED, True, a=ctx.p("f7", 0.4))
    cv.text(1330, 582, "Start, into S[1]", 34, ACCENT_DARK, True, a=ctx.p("f7", 0.4))
    d = ctx.p("done", 0.5)
    cv.rrect(1316, 650, 1854, 850, 20, fill=(228, 246, 236), outline=GREEN, width=4, a=d)
    draw_wrapped(cv, 1344, 674, "S is a topological order: every trail points to the right.", 31, 480, GREEN, True, a=d)
    finish(ctx)


def scene_order_check(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    a = ctx.p("line", 0.6)
    cv.text(640, 190, "S, read left to right", 30, GREEN, True, anchor="mm", a=a)
    if a > 0:
        gv, nb = draw_line(ctx, H.TOPO, H.TRAIL, y=560, a=a, r=44, size=22, x0=120, x1=1160, good=GREEN)
    panel_card(ctx, "CHECK IT")
    cv.text(1330, 190, "12 trails", 40, INK, True, a=a)
    cv.text(1330, 250, "0 point left", 48, GREEN, True, a=ctx.p("zero", 0.5))
    draw_wrapped(cv, 1330, 380, "Start, Pine, Ridge, Creek, Falls, Meadow, Summit", 30, 510, ACCENT_DARK, True, a=ctx.p("zero", 0.5))
    draw_wrapped(cv, 1330, 520, "One DFS fills the array. Time: O(V + E).", 30, 510, MUTED, False, a=ctx.p("lin", 0.5))
    finish(ctx)


TOPO_CODE = [
    "def topological_sort(graph):",
    "    visited = set()",
    "    order = []",
    "",
    "    def visit(v):",
    "        visited.add(v)",
    "        for w in graph[v]:",
    "            if w not in visited:",
    "                visit(w)",
    "        order.append(v)",
    "",
    "    for v in graph:",
    "        if v not in visited:",
    "            visit(v)",
    "    order.reverse()",
    "    return order",
]
TOPO_CARD = CodeCard(TOPO_CODE, size=28, lh=43, y_off=34, x_off=100)


def scene_code(ctx):
    boxes = [(10, "order.append(v)", ACCENT_DARK, "app"), (15, "order.reverse()", GREEN, "rev"),
             (12, "for v in graph:", BLUE, "outer"), (7, "for w in graph[v]:", PURPLE, "kids")]
    TOPO_CARD.draw(ctx, boxes=boxes, title="TOPOLOGICAL SORT, IN PLAIN PYTHON")
    notes_panel(ctx, "READING IT", [
        ("kids", "for w in graph[v]", "every trail out of v: visit the ones not visited yet", PURPLE),
        ("app", "order.append(v)", "v is added only after all its children: in finish order", ACCENT_DARK),
        ("rev", "order.reverse()", "flips the list in place. Same as filling S from the back.", GREEN),
        ("outer", "for v in graph", "start a search at every vertex not yet visited", BLUE)])
    finish(ctx)


def scene_cycle_check(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    rows = [("a", "visited", "marks only", BLUE, "assumes: no cycle"), ("b", "status:  new / active / finished", "the three states", RED, "fails on an active vertex")]
    y = 200
    for cue, head, sub, col, tail in rows:
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 220, 26, fill=WHITE, outline=col, width=5, a=a)
        cv.text(120, y + 30, head, 44, col, True, a=a)
        cv.text(120, y + 100, sub, 30, MUTED, False, a=a)
        cv.text(120, y + 148, tail, 36, INK, True, a=a)
        y += 260
    panel_card(ctx, "BOOK: PDF p.251")
    draw_wrapped(cv, 1330, 190, "If the graph might have a cycle, use the three-state version from the last video, and fail gracefully when an edge leads to an active vertex.",
                 29, 510, INK, False, a=ctx.p("b", 0.5))
    draw_wrapped(cv, 1330, 520, "If we already know the graph is acyclic, plain marking is enough.", 29, 510, MUTED, False, a=ctx.p("a", 0.5))
    finish(ctx)


def scene_implicit(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    order = H.POST
    ps = {v: ctx.p(f"p{i + 1}", 0.4) for i, v in enumerate(order)}
    GV.draw(ctx, marked={v: p for v, p in ps.items()}, estyle={})
    for v, p in ps.items():
        if p > 0:
            x, y = T_POS[v]
            badge(cv, x + 38, y - 40, order.index(v) + 1, p, ACCENT_DARK, r=18, size=20)
    panel_card(ctx, "BOOK: 'IMPLICIT' TOPOLOGICAL SORT")
    draw_wrapped(cv, 1330, 190, "Often the sorted list is not the goal. We want to do something at each vertex, in order.", 28, 510, INK, False)
    cv.rrect(1316, 340, 1854, 560, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=ctx.p("proc", 0.5))
    cv.text(1344, 362, "process each vertex", 32, ACCENT_DARK, True, a=ctx.p("proc", 0.5))
    cv.text(1344, 412, "when its search ends", 32, ACCENT_DARK, True, a=ctx.p("proc", 0.5))
    draw_wrapped(cv, 1344, 468, "= reverse topological order", 30, 480, INK, True, a=ctx.p("proc", 0.5))
    draw_wrapped(cv, 1330, 620, "No array needed: Process(v) replaces 'append v'.", 28, 510, MUTED, False, a=ctx.p("noarr", 0.5))
    chips(cv, 1330, 740, [v for v in order if ps[v] > 0.5], w=160, h=36, per_row=3, size=20)
    finish(ctx)


GV_L = GraphView({v: ((p[0] - 520) * 0.5 + 330, (p[1] - 470) * 0.6 + 520) for v, p in T_POS.items()}, T_EDGES, directed=True, r=26, label_size=15)
GV_R = GraphView({v: ((p[0] - 520) * 0.5 + 940, (p[1] - 470) * 0.6 + 520) for v, p in T_POS.items()},
                 [(b, a) for a, b in T_EDGES], directed=True, r=26, label_size=15)


def scene_rev(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    a = ctx.p("rev", 0.6)
    cv.text(330, 270, "G", 44, INK, True, anchor="mm")
    GV_L.draw(ctx)
    cv.text(940, 270, "rev(G)", 44, ACCENT_DARK, True, anchor="mm", a=a)
    GV_R.draw(ctx, edge_alpha=a, vfade={v: max(a, 0.001) for v in T_POS})
    ss = ctx.p("src", 0.5)
    tag(cv, GV_L.pos["Start"][0] + 6, GV_L.pos["Start"][1] - 48, "source", GREEN, a=ss, size=22)
    tag(cv, GV_R.pos["Start"][0] + 6, GV_R.pos["Start"][1] - 48, "sink", PURPLE, a=ss * a, size=22)
    tag(cv, GV_L.pos["Summit"][0], GV_L.pos["Summit"][1] - 48, "sink", PURPLE, a=ss, size=22)
    tag(cv, GV_R.pos["Summit"][0], GV_R.pos["Summit"][1] - 48, "source", GREEN, a=ss * a, size=22)
    panel_card(ctx, "FORWARD ORDER: BOOK PDF p.252")
    draw_wrapped(cv, 1330, 190, "To process vertices in forward topological order: run depth-first search on rev(G), every edge reversed.", 29, 510, INK, False, a=a)
    draw_wrapped(cv, 1330, 400, "A reversed cycle is still a cycle, so the reversal of a DAG is a DAG. Every source of G becomes a sink of rev(G).", 28, 510, MUTED, False, a=ss)
    draw_wrapped(cv, 1330, 660, "Reversing a graph takes O(V + E) time.", 30, 510, ACCENT_DARK, True, a=ctx.p("lin", 0.5))
    finish(ctx)


def scene_footnote(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    a, b = ctx.p("one", 0.5), ctx.p("two", 0.5)
    cv.text(640, 170, "reverse of G's postorder", 30, BLUE, True, anchor="mm", a=a)
    n1 = n2 = 0
    if a > 0:
        _, n1 = draw_line(ctx, H.TOPO, H.TRAIL, y=330, a=a, r=36, size=18, x0=120, x1=1160, good=BLUE)
    cv.text(640, 560, "a postorder of rev(G)", 30, ACCENT_DARK, True, anchor="mm", a=b)
    if b > 0:
        _, n2 = draw_line(ctx, H.REV_TOPO_OF_G, H.TRAIL, y=720, a=b, r=36, size=18, x0=120, x1=1160, good=GREEN)
    panel_card(ctx, "BOOK: FOOTNOTE 3, PDF p.252")
    cv.text(1330, 190, "both are topological orders:", 28, MUTED, True, a=b)
    cv.text(1330, 240, "0 backward edges each", 36, GREEN, True, a=b)
    c = ctx.p("diff", 0.5)
    draw_wrapped(cv, 1330, 370, "Pine, Ridge, Creek  vs  Pine, Creek, Ridge. The two orders are different.", 29, 510, INK, True, a=c)
    draw_wrapped(cv, 1330, 560, "A postordering of rev(G) is not necessarily the reversal of a postordering of G, though both are topological orderings of G.", 27, 510, MUTED, False, a=c)
    finish(ctx)


# ================================================================ part B: DP (6.4)
ST_POS = {i: (110 + i * 152, 520) for i in range(8)}
ST_EDGES = [(i, i + 1, 0) for i in range(7)] + [(i, i + 2, -190) for i in range(6)]
GV_ST = GraphView(ST_POS, ST_EDGES, directed=True, r=40, label_size=36)
STONES = {i: [j for j in (i + 1, i + 2) if j <= 7] for i in range(8)}
WAYS = {7: 1, 6: 1}
for _i in range(5, -1, -1):
    WAYS[_i] = WAYS[_i + 1] + WAYS[_i + 2]


def river(ctx):
    cv = ctx.cv
    stage(ctx, "river")
    cv.rrect(40, 430, 1248, 640, 22, fill=(196, 224, 246))


def scene_dep(ctx):
    river(ctx)
    cv = ctx.cv
    r1, r2 = ctx.p("rec", 0.5), ctx.p("dep", 0.5)
    es = {GV_ST.key(2, 3): (ACCENT, 11, r2), GV_ST.key(2, 4): (ACCENT, 11, r2)}
    GV_ST.draw(ctx, rings={2: (BLUE, r2)}, estyle={k: v for k, v in es.items() if v[2] > 0.02})
    cv.text(640, 230, "ways(i)  =  ways(i + 1)  +  ways(i + 2)", 44, INK, True, anchor="mm", a=r1)
    cv.text(640, 330, "a recurrence from the frog video", 28, MUTED, False, anchor="mm", a=r1)
    chars.frog(cv, 110, 482, 0.85, a=r1)
    panel_card(ctx, "DEPENDENCY GRAPH  (PDF p.252)")
    draw_wrapped(cv, 1330, 190, "A vertex for every subproblem. An edge from one subproblem to another if evaluating the first needs the second.", 28, 510, INK, False, a=r2)
    draw_wrapped(cv, 1330, 470, "Here the dependency graph is the stepping-stone graph itself.", 28, 510, ACCENT_DARK, True, a=ctx.p("same", 0.5))
    draw_wrapped(cv, 1330, 650, "It must be acyclic, or the plain recursion would never halt.", 28, 510, RED, True, a=ctx.p("acyc", 0.5))
    finish(ctx)


def scene_memo_dfs(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    rows = [("m1", "value[x] is undefined", "v is unmarked", BLUE),
            ("m2", "start evaluating x", "PreVisit(v)", GREEN),
            ("m3", "evaluate every subproblem y of x", "DFS(w) for every edge v → w", ACCENT_DARK),
            ("m4", "finish computing value[x]", "PostVisit(v)", PURPLE)]
    cv.text(260, 160, "memoized recursion", 30, MUTED, True, anchor="mm")
    cv.text(900, 160, "depth-first search", 30, MUTED, True, anchor="mm")
    y = 200
    for cue, l, r, col in rows:
        a = ctx.p(cue, 0.5)
        cv.rrect(60, y, 520, y + 130, 22, fill=WHITE, outline=col, width=4, a=a)
        draw_wrapped(cv, 86, y + 26, l, 30, 410, INK, True, a=a, lead=1.2)
        cv.arrow((540, y + 65), (640, y + 65), col, 8, a=a, head=26)
        cv.rrect(660, y, 1220, y + 130, 22, fill=WHITE, outline=col, width=4, a=a)
        draw_wrapped(cv, 686, y + 26, r, 30, 510, INK, True, a=a, lead=1.2)
        y += 160
    panel_card(ctx, "BOOK: FIGURE 6.10, PDF p.253")
    draw_wrapped(cv, 1330, 190, "Memoized recursion is depth-first search. Depth-first search is memoized recursion.", 34, 510, ACCENT_DARK, True)
    draw_wrapped(cv, 1330, 480, "A vertex is marked when its value has been computed.", 29, 510, INK, False, a=ctx.p("mk", 0.5))
    draw_wrapped(cv, 1330, 620, "PreVisit and PostVisit stand in for the real value computation.", 29, 510, MUTED, False, a=ctx.p("pp", 0.5))
    finish(ctx)


def scene_dp_post(ctx):
    river(ctx)
    cv = ctx.cv
    order = [7, 6, 5, 4, 3, 2, 1, 0]
    t0 = ctx.cue("go")
    shown = {}
    for i, n in enumerate(order):
        a = ctx.ramp(t0 + 0.75 * i, t0 + 0.75 * i + 0.4) if t0 is not None else 0.0
        if a > 0:
            shown[n] = a
    cur = None
    for n in order:
        if n in shown and shown[n] < 1.0:
            cur = n
    GV_ST.draw(ctx, rings={cur: (BLUE, 1.0)} if cur is not None else None)
    for n, a in shown.items():
        x, y = ST_POS[n]
        badge(cv, x, y + 78, WAYS[n], a)
    cv.text(640, 250, "evaluate in postorder: children before parents", 36, INK, True, anchor="mm")
    cv.text(640, 760, "7   6   5   4   3   2   1   0", 36, ACCENT_DARK, True, anchor="mm", a=ctx.p("go", 0.4))
    cv.text(640, 810, "reverse topological order  =  postorder", 28, MUTED, False, anchor="mm", a=ctx.p("go", 0.4))
    panel_card(ctx, "BOOK: FIGURE 6.11, PDF p.253")
    draw_wrapped(cv, 1330, 190, "Dynamic programming is evaluating every subproblem in reverse topological order.", 30, 510, INK, True)
    draw_wrapped(cv, 1330, 400, "Every dynamic programming algorithm is equivalent to a postorder traversal of the dependency graph of its recurrence.", 28, 510,
                 ACCENT_DARK, True, a=ctx.p("every", 0.5))
    finish(ctx)


def scene_grid(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    n, cell, ox, oy = 5, 128, 280, 220
    t0 = ctx.cue("fill")
    for i in range(n):
        for j in range(n):
            x, y = ox + j * cell, oy + i * cell
            idx = i * n + j
            a = ctx.ramp(t0 + 0.14 * idx, t0 + 0.14 * idx + 0.2) if t0 is not None else 0.0
            cv.rrect(x + 6, y + 6, x + cell - 6, y + cell - 6, 14, fill=mix(WHITE, ACCENT_SOFT, a), outline=GRAY, width=3)
            cv.text(x + cell / 2, y + cell / 2, f"{i},{j}", 28, INK, True, anchor="mm")
    h = ctx.p("one", 0.5)
    ci, cj = 3, 3
    hx, hy = ox + cj * cell + cell / 2, oy + ci * cell + cell / 2
    if h > 0:
        for (di, dj) in ((0, -1), (-1, 0), (-1, -1)):
            tx, ty = ox + (cj + dj) * cell + cell / 2, oy + (ci + di) * cell + cell / 2
            cv.arrow((hx + (tx - hx) * 0.28, hy + (ty - hy) * 0.28), (hx + (tx - hx) * 0.78, hy + (ty - hy) * 0.78), ACCENT, 7, a=h, head=22)
        cv.circle(hx, hy, 60, outline=BLUE, width=6, a=h)
    panel_card(ctx, "BOOK: FIGURE 6.12, PDF p.254")
    draw_wrapped(cv, 1330, 190, "Edit distance: each subproblem (i, j) needs its left, upper, and diagonal neighbors.", 29, 510, INK, False, a=h)
    draw_wrapped(cv, 1330, 440, "The dependency graph is a regular grid. So the evaluation order is hard-wired as nested loops: no topological sort at run time.", 28, 510,
                 ACCENT_DARK, True, a=ctx.p("loops", 0.5))
    draw_wrapped(cv, 1330, 760, "The book calls this reverse topological order the evaluation order.", 27, 510, MUTED, False, a=ctx.p("eval", 0.5))
    finish(ctx)


def scene_diffs(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    rows = [("d1", "The graph is implicit", "no adjacency list in memory: the recurrence encodes the edges. That is a minor difference, if each subproblem can be listed in constant time.", BLUE),
            ("d2", "The graph is regular", "so we can skip the topological sort and write nested loops.", GREEN),
            ("d3", "Irregular graphs?", "use depth-first search directly, as in the next example.", ACCENT_DARK)]
    y = 160
    for cue, head, body, col in rows:
        a = ctx.p(cue, 0.5)
        cv.rrect(70, y, 1190, y + 220, 26, fill=WHITE, outline=col, width=4, a=a)
        cv.text(110, y + 26, head, 44, col, True, a=a)
        draw_wrapped(cv, 110, y + 100, body, 30, 1040, INK, False, a=a)
        y += 250
    panel_card(ctx, "DP VS TOPOLOGICAL SORT")
    draw_wrapped(cv, 1330, 190, "Two differences. Both are small.", 34, 510, ACCENT_DARK, True)
    finish(ctx)


# ---------------------------------------------------------------- longest path
def scene_problem(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    GV.draw(ctx, show_weights=True, rings={"Start": (BLUE, 1.0), "Summit": (ORANGE, 1.0)})
    tag(cv, T_POS["Start"][0], T_POS["Start"][1] + 78, "s", BLUE, size=26)
    tag(cv, T_POS["Summit"][0], T_POS["Summit"][1] + 78, "t", ORANGE, size=26)
    panel_card(ctx, "LONGEST PATH  (PDF pp.253-254)")
    a, b = ctx.p("prob", 0.5), ctx.p("np", 0.5)
    draw_wrapped(cv, 1330, 190, "Find the path of maximum total weight from s to t in a weighted directed graph.", 29, 510, INK, True, a=a)
    cv.rrect(1316, 440, 1854, 640, 18, fill=(253, 232, 232), outline=RED, width=4, a=b)
    cv.text(1344, 464, "in general graphs", 28, MUTED, True, a=b)
    cv.text(1344, 504, "NP-hard", 52, RED, True, a=b)
    cv.text(1344, 570, "(a reduction from the traveling salesman problem)", 22, MUTED, False, a=b)
    cv.rrect(1316, 670, 1854, 850, 18, fill=(228, 246, 236), outline=GREEN, width=4, a=ctx.p("easy", 0.5))
    cv.text(1344, 694, "if the graph is a DAG", 28, MUTED, True, a=ctx.p("easy", 0.5))
    cv.text(1344, 736, "linear time", 52, GREEN, True, a=ctx.p("easy", 0.5))
    finish(ctx)


def scene_recurrence(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    cv.text(80, 190, "LLP(v)  =  length of the longest path from v to t", 36, INK, True, a=ctx.p("def", 0.5))
    a1, a2, a3 = ctx.p("base", 0.5), ctx.p("rec", 0.5), ctx.p("neg", 0.5)
    cv.rrect(80, 270, 1180, 420, 26, fill=WHITE, outline=BLUE, width=5, a=a1)
    cv.text(120, 310, "LLP(v) = 0", 56, BLUE, True, a=a1)
    cv.text(700, 322, "if v = t", 40, MUTED, True, a=a1)
    cv.rrect(80, 450, 1180, 640, 26, fill=WHITE, outline=ACCENT, width=5, a=a2)
    cv.text(120, 480, "LLP(v) = max over every edge v → w of", 36, ACCENT_DARK, True, a=a2)
    cv.text(120, 550, "length(v → w) + LLP(w)", 56, ACCENT_DARK, True, a=a2)
    cv.rrect(80, 670, 1180, 830, 26, fill=WHITE, outline=RED, width=5, a=a3)
    cv.text(120, 700, "no edges out, and v is not t:", 32, INK, True, a=a3)
    cv.text(120, 760, "max of nothing = −∞", 50, RED, True, a=a3)
    panel_card(ctx, "THE RECURRENCE")
    draw_wrapped(cv, 1330, 190, "Its dependency graph is the input graph itself: LLP(v) depends on LLP(w) exactly when v → w is an edge.", 29, 510, INK, False, a=ctx.p("dep", 0.5))
    draw_wrapped(cv, 1330, 520, "So a depth-first search of G, from s, evaluates it in O(V + E) time.", 29, 510, ACCENT_DARK, True, a=ctx.p("dfs", 0.5))
    finish(ctx)


def scene_run(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    log = H.LOG
    vals = {"Summit": 0}
    shown = {"Summit": 1.0}
    cur = None
    for i, (v, cands, best) in enumerate(log):
        t = ctx.cue(f"v{i + 1}")
        ok = t is not None and ctx.t >= t
        ctx.sig.append(1 if ok else 0)
        if ok:
            vals[v] = best
            shown[v] = ctx.ramp(t, t + 0.5)
            cur = (v, cands, best, t)
    es = {}
    if cur:
        v, cands, best, t = cur
        for w, ln, lw, c in cands:
            es[GV.key(v, w)] = (ACCENT if c == best else BLUE, 11, 1.0)
    GV.draw(ctx, show_weights=True, estyle=es, rings={cur[0]: (BLUE, 1.0)} if cur else None)
    for v, a in shown.items():
        x, y = T_POS[v]
        badge(cv, x, y - 82, vals[v], a, color=GREEN, size=28)
    panel_card(ctx, "BEST SCORE FROM EACH JUNCTION")
    cv.text(1330, 170, "Summit:  0", 30, INK, True, True)
    if cur:
        v, cands, best, t = cur
        cv.text(1330, 240, f"computing {v}", 30, ACCENT_DARK, True)
        y = 290
        for w, ln, lw, c in cands:
            win = c == best
            cv.rrect(1318, y - 6, 1852, y + 44, 10, fill=ACCENT_SOFT if win else PAPER, outline=ACCENT if win else PANEL_LINE, width=3)
            cv.text(1334, y + 4, f"via {w}:  {ln} + {lw} = {c}", 26, INK, True, True)
            y += 62
        cv.text(1330, y + 14, f"best = {best}", 40, GREEN, True)
    finish(ctx)


LP_CODE = [
    "def longest_path(graph, length, s, t):",
    "    best = {}",
    "",
    "    def go(v):",
    "        if v == t:",
    "            return 0",
    "        if v not in best:",
    '            best[v] = float("-inf")',
    "            for w in graph[v]:",
    "                best[v] = max(best[v], length[(v, w)] + go(w))",
    "        return best[v]",
    "",
    "    return go(s)",
]
LP_CARD = CodeCard(LP_CODE, size=29, lh=50, y_off=34, x_off=100, rect=(40, 126, 1246, 906))


def scene_lp_code(boxes, notes):
    def scene(ctx):
        LP_CARD.draw(ctx, boxes=boxes, title="THE BOOK'S LongestPath, IN PYTHON")
        notes_panel(ctx, "READING IT", notes)
        finish(ctx)
    return scene


def scene_route(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    r = H.ROUTE
    es = {}
    steps = [("Start", "Pine"), ("Pine", "Creek"), ("Creek", "Falls"), ("Falls", "Summit")]
    for i, (u, w) in enumerate(steps):
        a = ctx.p(f"r{i + 1}", 0.5)
        if a > 0:
            es[GV.key(u, w)] = (GREEN, 15, a)
    GV.draw(ctx, show_weights=True, estyle=es, marked={v: ctx.p(f"r{i + 1}", 0.5) for i, v in enumerate(r[1:])})
    panel_card(ctx, "THE MOST SCENIC ROUTE")
    cv.text(1330, 190, "19 scenery points", 44, GREEN, True, a=ctx.p("r4", 0.5))
    cv.text(1330, 270, "Start → Pine → Creek", 30, INK, True, a=ctx.p("r2", 0.5))
    cv.text(1330, 316, "→ Falls → Summit", 30, INK, True, a=ctx.p("r3", 0.5))
    cv.text(1330, 400, "3 + 5 + 7 + 4 = 19", 38, ACCENT_DARK, True, a=ctx.p("r4", 0.5))
    cv.rrect(1316, 520, 1854, 740, 18, fill=PAPER, outline=ORANGE, width=3, a=ctx.p("extra", 0.5))
    cv.text(1344, 540, "an extra, not in the book", 24, ORANGE, True, a=ctx.p("extra", 0.5))
    draw_wrapped(cv, 1344, 586, "To get the route, and not just its length, remember which edge gave the maximum at each junction.", 27, 480, INK, False,
                 a=ctx.p("extra", 0.5))
    finish(ctx)


DP_CODE = [
    "def longest_path_dp(graph, length, t, postorder):",
    "    best = {}",
    "    for v in postorder:",
    "        if v == t:",
    "            best[v] = 0",
    "        else:",
    '            best[v] = float("-inf")',
    "            for w in graph[v]:",
    "                best[v] = max(best[v], length[(v, w)] + best[w])",
    "    return best",
]
DP_CARD = CodeCard(DP_CODE, size=27, lh=44, y_off=34, x_off=100, rect=(40, 126, 1246, 640))


def scene_dp_table(ctx):
    cv = ctx.cv
    boxes = [(3, "for v in postorder:", BLUE, "loop"), (9, "best[w]", GREEN, "lookup")]
    DP_CARD.draw(ctx, boxes=boxes, title="THE SAME TABLE, BY DYNAMIC PROGRAMMING")
    cv.rrect(40, 660, 1246, 906, 26, fill=WHITE, outline=PANEL_LINE, width=3)
    cv.text(70, 676, "table, filled in postorder", 22, MUTED, True)
    t0 = ctx.cue("fill")
    for i, (v, val) in enumerate(H.DP):
        a = ctx.ramp(t0 + 0.8 * i, t0 + 0.8 * i + 0.4) if t0 is not None else 0.0
        x = 70 + i * 168
        cv.rrect(x, 720, x + 156, 880, 16, fill=ACCENT_SOFT if a > 0.5 else PAPER, outline=ACCENT if a > 0.5 else GRAY, width=3)
        cv.text(x + 78, 756, v, 24, INK, True, anchor="mm")
        cv.text(x + 78, 830, str(val), 54, ACCENT, True, anchor="mm", a=a)
    notes_panel(ctx, "READING IT", [
        ("loop", "for v in postorder", "children always come before parents: so best[w] is ready when we need it", BLUE),
        ("lookup", "best[w]", "a plain lookup. No recursion, no cache check.", GREEN),
        ("same", "same table, same order", "memoized recursion and this loop finish the vertices in the same order", ACCENT_DARK)])
    finish(ctx)


def scene_recap(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    cards = [("c1", "Topological order", "reverse the postorder of a depth-first search"),
             ("c2", "Process at the finish", "reverse order needs no array; forward order: search rev(G)"),
             ("c3", "Memoization is a DFS", "of the dependency graph, which must be acyclic"),
             ("c4", "Dynamic programming is a postorder", "so longest path in a DAG takes O(V + E)")]
    y = 150
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(150, y + 75, 34, fill=ACCENT, a=a)
        cv.text(150, y + 74, str(i + 1), 38, WHITE, True, anchor="mm", a=a)
        cv.text(215, y + 22, head, 38, ACCENT_DARK, True, a=a)
        cv.text(215, y + 86, sub, 27, INK, False, a=a)
        y += 174
    cv.text(630, 868, "Pause: say each of these four in your own words.", 30, BLUE, True, anchor="mm", a=ctx.p("try", 0.5))
    finish(ctx)
