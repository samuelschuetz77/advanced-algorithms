"""Video 03 scenes: counting paths with a frog, a diamond, and a hiking map."""
from __future__ import annotations

import math

import chars
import pathlog as P
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, RED, WHITE, clamp, ease, lerp, mix, point_along,
)
from graphview import GraphView
from motion import walk
from widgets import (
    CodeCard, PANEL, chrome, draw_wrapped, notes_panel, panel_card, predict_chip, tag, token_pill,
)

PURPLE = (140, 80, 200)
ORANGE = (234, 140, 36)

# ---------------------------------------------------------------- graphs
STONE_POS = {i: (110 + i * 152, 520) for i in range(8)}
STONE_EDGES = [(i, i + 1, 0) for i in range(7)] + [(i, i + 2, -190) for i in range(6)]
GV_ST = GraphView(STONE_POS, STONE_EDGES, directed=True, r=40, label_size=36)
STONE_VAL = {n: P.paths(P.STONES, n, 7) for n in range(8)}

D_POS = {"a": (300, 520), "b": (640, 320), "c": (640, 720), "d": (940, 520), "e": (1160, 520)}
D_EDGES = [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d", "e")]
GV_D = GraphView(D_POS, D_EDGES, directed=True, r=48, label_size=44)

T_POS = {"Start": (150, 520), "Pine": (420, 520), "Creek": (690, 330), "Ridge": (690, 710),
         "Meadow": (950, 330), "Falls": (950, 710), "Summit": (1150, 520)}
T_EDGES = [(u, v) for u, vs in P.TRAIL.items() for v in vs]
GV_T = GraphView(T_POS, T_EDGES, directed=True, r=50, label_size=24)
T_VAL = dict(P.finish_order(P.TRAIL, "Start", "Summit"))
T_COL = {"Start": (95, 105, 125), "Pine": (46, 140, 90), "Creek": BLUE, "Ridge": (150, 100, 40),
         "Meadow": ACCENT, "Falls": (0, 150, 170), "Summit": PURPLE}


def stage(ctx, kind="plain"):
    cv = ctx.cv
    bg = {"plain": (244, 246, 250), "river": (238, 246, 252), "trail": (238, 246, 236)}[kind]
    cv.rrect(30, 112, 1258, 916, 28, fill=bg, outline=(220, 226, 234), width=3)
    if kind == "river":
        cv.rrect(40, 430, 1248, 640, 22, fill=(196, 224, 246))
        for k in range(6):
            x = 120 + k * 200
            cv.line((x, 610), (x + 70, 610), (170, 205, 236), 4)
            cv.line((x + 90, 460), (x + 160, 460), (170, 205, 236), 4)
    if kind == "trail":
        for k, (cx, cy, rx, ry) in enumerate([(640, 520, 560, 320), (640, 520, 420, 230), (640, 520, 270, 130)]):
            cv.ellipse(cx, cy, rx, ry, outline=(214, 230, 210), width=3)


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def badge(cv, x, y, val, a=1.0, color=ACCENT, r=26, size=30):
    cv.circle(x, y, r, fill=WHITE, outline=color, width=4, a=a)
    cv.text(x, y - 1, str(val), size, color, True, anchor="mm", a=a)


# ---------------------------------------------------------------- stones
def stone_line(n):
    if n == 7:
        return "stone 7:  done = 1"
    if n == 6:
        return "stone 6:  one hop = 1"
    return f"stone {n}:  {STONE_VAL[n + 1]} + {STONE_VAL[n + 2]} = {STONE_VAL[n]}"


def stones_scene(known=(), cues=(), hook=False, rule_cue=None):
    def scene(ctx):
        cv = ctx.cv
        stage(ctx, "river")
        shown = {n: 1.0 for n in known}
        es = {}
        for n, cue in cues:
            a = ctx.p(cue, 0.4)
            if a > 0:
                shown[n] = a
            pl = ctx.pulse(cue, 1.6)
            if pl > 0:
                for c in (n + 1, n + 2):
                    if c <= 7:
                        es[GV_ST.key(n, c)] = (BLUE, 9, pl)
        hop_a = ctx.p("hop", 0.5) if hook else 0.0
        rings = {}
        if hook:
            sp = ctx.pulse("stone", 1.2)
            rings = {i: (BLUE, sp) for i in range(8)}
            if hop_a > 0:
                for k in GV_ST.edges:
                    es[GV_ST.key(k[0], k[1])] = (mix(LINE, ACCENT, hop_a), 6 + 2 * hop_a, 1.0)
        GV_ST.draw(ctx, estyle=es, rings=rings)
        for n, a in shown.items():
            x, y = STONE_POS[n]
            badge(cv, x, y + 76, STONE_VAL[n], a)
        # frog: waits on stone 0; hops 0->2->3 in the hook
        if hook:
            t0 = ctx.cue("hop") or 0
            wps = [(t0, 0), (t0 + 0.4, 0), (t0 + 1.2, 2), (t0 + 1.6, 2), (t0 + 2.2, 3)] if ctx.cue("hop") else [(0, 0), (1, 0)]
            x, y, flip, mv = walk(ctx, GV_ST, wps, hop=60)
        else:
            x, y = STONE_POS[0]
        chars.frog(cv, x, y - 38, 0.9)
        # panel
        panel_card(ctx, "WAYS TO FINISH, FROM EACH STONE")
        yy = 180
        lines = [(n, None) for n in known] + list(cues)
        for n, cue in lines:
            a = 1.0 if cue is None else ctx.p(cue, 0.4)
            if a > 0:
                cv.text(1330, yy, stone_line(n), 30, INK if cue is None else ACCENT_DARK, True, True, a=a)
                yy += 46
        if rule_cue:
            ra = ctx.p(rule_cue, 0.5)
            cv.rrect(1316, 640, 1854, 880, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=ra)
            cv.text(1344, 662, "the rule", 26, MUTED, True, a=ra)
            draw_wrapped(cv, 1344, 704, "ways from a stone = ways from one ahead + ways from two ahead", 32, 480,
                         ACCENT_DARK, True, a=ra, lead=1.2)
        finish(ctx)
    return scene


def scene_general(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    items = [("dag", "A DAG: arrows, and no cycles", 40, INK), ("base", "paths(s, t) = 1      if s is t", 44, BLUE),
             ("rec", "paths(s, t) = sum of paths(child, t)      otherwise", 44, ACCENT_DARK)]
    y = 230
    for cue, text, size, col in items:
        a = ctx.p(cue, 0.5)
        cv.text(80, y, text, size, col, True, a=a)
        y += 140
    cv.text(80, 160, "COUNTING PATHS FROM s TO t", 26, MUTED, True)
    panel_card(ctx, "WORDS")
    notes = [("dag", "DAG", "directed acyclic graph: every edge is an arrow, and no path loops back", BLUE),
             ("base", "base case", "standing on the target counts as exactly one path: the empty one", GREEN),
             ("rec", "children", "the vertices that s points to", ACCENT_DARK)]
    yy = 180
    for cue, head, body, col in notes:
        a = ctx.p(cue, 0.5)
        cv.rrect(1316, yy, 1854, yy + 180, 20, fill=PAPER, outline=col, width=4, a=a)
        cv.text(1344, yy + 14, head, 36, col, True, a=a)
        draw_wrapped(cv, 1344, yy + 70, body, 27, 490, INK, False, a=a)
        yy += 200
    finish(ctx)


# ---------------------------------------------------------------- diamond
def diamond_scene(known=(), cues=(), paths=False, ring=None):
    vals = {v: P.paths(P.DIAMOND, v, "e") for v in "abcde"}

    def scene(ctx):
        cv = ctx.cv
        stage(ctx, "plain")
        shown = {v: 1.0 for v in known}
        for v, cue in cues:
            a = ctx.p(cue, 0.4)
            if a > 0:
                shown[v] = a
        es = {}
        p1, p2 = ctx.p("p1", 0.5), ctx.p("p2", 0.5)
        if paths:
            for (u, v) in (("a", "b"), ("b", "d"), ("d", "e")):
                es[GV_D.key(u, v)] = (ACCENT, 12, p1)
            for (u, v) in (("a", "c"), ("c", "d")):
                es[GV_D.key(u, v)] = (BLUE, 12, p2)
            es = {k: v for k, v in es.items() if v[2] > 0.02}
        GV_D.draw(ctx, estyle=es, rings={ring: (BLUE, 1.0)} if ring else None)
        for v, a in shown.items():
            x, y = D_POS[v]
            badge(cv, x, y - 82, vals[v], a, size=32, r=28)
        panel_card(ctx, "PATHS FROM A TO E")
        cv.text(1330, 190, "A → E", 56, INK, True)
        a = ctx.p("a", 0.4)
        cv.text(1330, 270, "2 paths", 90, ACCENT, True, a=a)
        cv.text(1330, 420, "A  B  D  E", 40, ACCENT_DARK, True, a=p1)
        cv.text(1330, 480, "A  C  D  E", 40, BLUE, True, a=p2)
        finish(ctx)
    return scene


def diamond_events():
    ev = []

    def go(v, depth):
        ev.append(("call", v, depth, None))
        if v == "e":
            val = 1
        else:
            val = sum(go(c, depth + 1) for c in P.DIAMOND[v])
        ev.append(("ret", v, depth, val))
        return val
    go("a", 0)
    return ev


DEV = diamond_events()


def scene_diamond_rec(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    t0 = ctx.cue("go") or 0.0
    per = 0.62
    k = int(clamp((ctx.t - t0) / per, 0, len(DEV))) if ctx.cue("go") and ctx.t >= t0 else 0
    ctx.sig.append(k)
    cur, es, vals = None, {}, {}
    for i in range(k):
        kind, v, depth, val = DEV[i]
        cur = v if kind == "call" else cur
        if kind == "ret":
            vals[v] = val
    # edges of the live call stack
    stack = []
    for i in range(k):
        kind, v, depth, val = DEV[i]
        if kind == "call":
            stack = stack[:depth] + [v]
        else:
            stack = stack[:depth]
    for u, v in zip(stack, stack[1:]):
        es[GV_D.key(u, v)] = (BLUE, 12, 1.0)
    GV_D.draw(ctx, estyle=es, rings={stack[-1]: (BLUE, 1.0)} if stack else None)
    for v, val in vals.items():
        x, y = D_POS[v]
        badge(cv, x, y - 82, val, 1.0, size=32, r=28)
    panel_card(ctx, "THE CALLS, IN ORDER")
    y = 176
    again = ctx.p("again", 0.4)
    for i in range(k):
        kind, v, depth, val = DEV[i]
        txt = f"nested({v})" if kind == "call" else f"return {val}"
        col = INK if kind == "call" else GREEN
        calls_so_far = sum(1 for j in range(i + 1) if DEV[j][0] == "call" and DEV[j][1] == "d")
        hi = kind == "call" and v == "d" and calls_so_far == 2 and again > 0
        if hi:
            cv.rrect(1318, y - 6, 1850, y + 36, 10, fill=ACCENT_SOFT, outline=ACCENT, width=3)
        cv.text(1334 + depth * 36, y, ("→ " if kind == "call" else "← ") + txt, 28, ACCENT_DARK if hi else col, True, True)
        y += 45
    finish(ctx)


# ---------------------------------------------------------------- trail
def scene_trail_intro(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    GV_T.draw(ctx, rings={"Start": (BLUE, ctx.pulse("q", 1.5))})
    chars.person(cv, 150, 450, 0.9, shirt=ACCENT, hat=(60, 100, 60))
    panel_card(ctx, "THE HIKING MAP")
    cv.text(1330, 190, "7 junctions", 46, INK, True)
    cv.text(1330, 260, "12 one-way trails", 46, INK, True)
    cv.text(1330, 330, "all uphill: no cycles", 30, MUTED, False)
    cv.text(1330, 450, "routes from", 32, MUTED, True)
    cv.text(1330, 500, "Start to Summit?", 38, INK, True)
    cv.text(1330, 590, "?", 140, ACCENT, True)
    finish(ctx)


def layout_tree(tree, cached=False):
    nodes = []

    def rec(t, depth, parent):
        if cached:
            name, hit, kids = t
        else:
            name, kids = t
            hit = False
        idx = len(nodes)
        nodes.append({"name": name, "depth": depth, "parent": parent, "hit": hit, "kids": []})
        if parent is not None:
            nodes[parent]["kids"].append(idx)
        for k in kids:
            rec(k, depth + 1, idx)
    rec(tree, 0, None)
    leaves = [0]

    def assign(i):
        n = nodes[i]
        if not n["kids"]:
            n["xi"] = leaves[0]
            leaves[0] += 1
        else:
            for k in n["kids"]:
                assign(k)
            n["xi"] = sum(nodes[k]["xi"] for k in n["kids"]) / len(n["kids"])
    assign(0)
    return nodes, leaves[0]


NAIVE_NODES, NAIVE_LEAVES = layout_tree(P.naive_tree(P.TRAIL, "Start", "Summit"))
CACHED_NODES, CACHED_LEAVES = layout_tree(P.cached_tree(P.TRAIL, "Start", "Summit"), cached=True)


def draw_calltree(ctx, nodes, leaves, t0, per, hl=None, x0=70, x1=1220, y0=210, dy=150, r=30, show_hits=True):
    cv = ctx.cv
    pos = []
    for n in nodes:
        pos.append((x0 + (n["xi"] + 0.5) / leaves * (x1 - x0), y0 + n["depth"] * dy))
    seen = 0
    for i, n in enumerate(nodes):
        a = ctx.ramp(t0 + per * i, t0 + per * i + 0.25) if t0 is not None else 0.0
        dim = 1.0 if (hl is None or n["name"] in hl) else 0.25
        if a > 0.02:
            seen += 1 if a > 0.5 else 0
            if n["parent"] is not None:
                cv.line(pos[n["parent"]], pos[i], GRAY, 4, a * dim)
    for i, n in enumerate(nodes):
        a = ctx.ramp(t0 + per * i, t0 + per * i + 0.25) if t0 is not None else 0.0
        if a <= 0.02:
            continue
        dim = 1.0 if (hl is None or n["name"] in hl) else 0.25
        x, y = pos[i]
        col = T_COL[n["name"]]
        if n["hit"]:
            cv.circle(x, y, r, fill=WHITE, outline=col, width=4, a=a * dim)
            cv.text(x, y, n["name"][:3], 17, col, True, anchor="mm", a=a * dim)
            cv.text(x, y + r + 18, "hit", 18, GREEN, True, anchor="mm", a=a * dim)
        else:
            cv.circle(x, y, r, fill=col, outline=INK, width=3, a=a * dim)
            cv.text(x, y, n["name"][:3], 18, WHITE, True, anchor="mm", a=a * dim)
        if hl and n["name"] in hl:
            cv.circle(x, y, r + 9, outline=RED, width=5, a=a)
    return seen


def scene_trail_naive(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    t0 = ctx.cue("go")
    seen = draw_calltree(ctx, NAIVE_NODES, NAIVE_LEAVES, t0, 0.3) if t0 is not None else 0
    panel_card(ctx, "PLAIN RECURSION")
    cv.text(1330, 190, "calls made:", 30, MUTED, True)
    cv.text(1330, 240, str(seen), 150, ACCENT, True)
    cv.text(1330, 450, "junctions on the map:", 28, MUTED, True)
    cv.text(1330, 495, "7", 64, INK, True)
    finish(ctx)


def scene_dups(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    m, f = ctx.p("meadow", 0.4), ctx.p("falls", 0.4)
    hl = None
    if f > 0.5:
        hl = {"Falls"}
    elif m > 0.5:
        hl = {"Meadow"}
    draw_calltree(ctx, NAIVE_NODES, NAIVE_LEAVES, -100.0, 0.0, hl=hl)
    panel_card(ctx, "WORK REPEATED")
    cv.text(1330, 200, "Meadow:", 44, ACCENT_DARK, True, a=max(m, 0.3))
    cv.text(1330, 260, f"asked {P.times_called(P.naive_tree(P.TRAIL, 'Start', 'Summit'), 'Meadow')} times", 44, INK, True, a=m)
    cv.text(1330, 380, "Falls:", 44, (0, 150, 170), True, a=max(f, 0.3))
    cv.text(1330, 440, f"asked {P.times_called(P.naive_tree(P.TRAIL, 'Start', 'Summit'), 'Falls')} times", 44, INK, True, a=f)
    draw_wrapped(cv, 1330, 580, "Every time, the answer is 1, recomputed from scratch.", 30, 500, MUTED, False, a=f)
    finish(ctx)


def scene_memo(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    t0 = ctx.cue("tree")
    hit = ctx.p("hit", 0.5)
    seen = draw_calltree(ctx, CACHED_NODES, CACHED_LEAVES, t0, 0.42, r=32) if t0 is not None else 0
    panel_card(ctx, "WITH A CACHE")
    cv.text(1330, 190, "calls made:", 30, MUTED, True)
    cv.text(1330, 240, str(seen), 150, GREEN, True)
    hits = sum(1 for n in CACHED_NODES if n["hit"])
    cv.text(1330, 450, "of them cache hits:", 28, MUTED, True, a=hit)
    cv.text(1330, 495, str(hits), 64, GREEN, True, a=hit)
    cv.text(1330, 600, "plain recursion: 24", 30, ACCENT_DARK, True, a=hit)
    finish(ctx)


def scene_table(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    order = list(T_VAL.items())
    GV_T.draw(ctx, rings={v: (BLUE, ctx.pulse(f"c{i + 1}", 1.0)) for i, (v, _) in enumerate(order)})
    for i, (v, val) in enumerate(order):
        a = ctx.p(f"c{i + 1}", 0.4)
        x, y = T_POS[v]
        if a > 0:
            badge(cv, x, y - 80, val, a, size=32, r=28)
    panel_card(ctx, "THE CACHE (a table)")
    yy = 180
    for i, (v, val) in enumerate(order):
        a = ctx.p(f"c{i + 1}", 0.4)
        cv.rrect(1316, yy, 1854, yy + 80, 14, fill=PAPER, outline=ACCENT if a > 0.5 else PANEL_LINE, width=3, a=max(a, 0.2) if a > 0 else 0)
        if a > 0:
            cv.text(1342, yy + 40, f"'{v}'", 36, INK, True, True, anchor="lm", a=a)
            cv.text(1620, yy + 40, "→", 36, MUTED, True, anchor="mm", a=a)
            cv.text(1830, yy + 40, str(val), 44, ACCENT, True, True, anchor="rm", a=a)
        yy += 92
    finish(ctx)


def scene_cost(ctx):
    stage(ctx, "trail")
    cv = ctx.cv
    v, e, c, big = ctx.p("v", 0.4), ctx.p("e", 0.4), ctx.p("calls", 0.4), ctx.p("big", 0.5)
    GV_T.draw(ctx, marked={k: v for k in P.TRAIL})
    panel_card(ctx, "COUNTING THE WORK")
    cv.text(1330, 190, "junctions computed:", 28, MUTED, True, a=v)
    cv.text(1330, 230, "7  (once each)", 48, INK, True, a=v)
    cv.text(1330, 330, "trails looked at:", 28, MUTED, True, a=e)
    cv.text(1330, 370, "12  (once each)", 48, INK, True, a=e)
    cv.text(1330, 470, "calls in total:", 28, MUTED, True, a=c)
    cv.text(1330, 510, "1 + 12 = 13", 48, GREEN, True, a=c)
    cv.rrect(1316, 640, 1854, 800, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=big)
    cv.text(1585, 720, "O(V + E)", 70, BLUE, True, anchor="mm", a=big)
    finish(ctx)


# ---------------------------------------------------------------- code
CODE = [
    "from functools import cache",
    "",
    "def count_paths(graph, s, t):",
    "    @cache",
    "    def nested(s):",
    "        if (s == t):",
    "            return 1",
    "        return sum(nested(child) for child in graph[s])",
    "    return nested(s)",
]
CARD = CodeCard(CODE, size=32, lh=58, y_off=30)
LONG = CodeCard(["total = 0", "for child in graph[s]:", "    total = total + nested(child)", "return total"],
                rect=(1290, 540, 1880, 800), size=26, lh=48, x_off=40, numbers=False, y_off=22)


def code_scene(hl=(), boxes=(), notes=(), title="notes", longhand=False):
    def scene(ctx):
        CARD.draw(ctx, hl=[(ln, cue) for ln, cue in hl], boxes=boxes, title="YOUR count_paths")
        notes_panel(ctx, title, list(notes), rect=(1290, 118, 1880, 520 if longhand else 906))
        if longhand and ctx.reached("long"):
            LONG.draw(ctx, title="THE SAME, LONGHAND")
        finish(ctx)
    return scene


def scene_decorator(ctx):
    boxes = [(4, "@cache", ACCENT_DARK, "at")]
    CARD.draw(ctx, hl=[(4, "at")], boxes=boxes, title="YOUR count_paths")
    cv = ctx.cv
    panel_card(ctx, "WHAT @cache ADDS")
    cv.text(1330, 190, "a table of answers", 34, INK, True, a=ctx.p("wrap", 0.5))
    a1, a2 = ctx.p("wrap", 0.5), ctx.p("again", 0.5)
    cv.rrect(1316, 260, 1854, 440, 20, fill=PAPER, outline=BLUE, width=4, a=a1)
    cv.text(1344, 280, "first call:  nested('d')", 28, BLUE, True, True, a=a1)
    cv.text(1344, 330, "runs the function", 28, INK, False, a=a1)
    cv.text(1344, 376, "writes   'd' → 1", 28, GREEN, True, True, a=a1)
    cv.rrect(1316, 470, 1854, 650, 20, fill=PAPER, outline=GREEN, width=4, a=a2)
    cv.text(1344, 490, "second call:  nested('d')", 28, GREEN, True, True, a=a2)
    cv.text(1344, 540, "finds   'd' → 1", 28, INK, False, a=a2)
    cv.text(1344, 586, "skips the function", 28, ACCENT_DARK, True, a=a2)
    finish(ctx)


def scene_sum_trace(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    seq = [("t1", ["a", "b", "d", "e"]), ("t2", ["d", "b"]), ("t3", ["c"]), ("t4", ["c"]), ("t5", ["a"])]
    vals = {"e": 1, "d": 1, "b": 1, "c": 1, "a": 2}
    shown = {}
    es = {}
    rings = {}
    t1, t2, t3, t4, t5 = (ctx.p(c, 0.4) for c, _ in seq)
    if t1 > 0:
        for u, v in (("a", "b"), ("b", "d"), ("d", "e")):
            es[GV_D.key(u, v)] = (BLUE, 11, t1)
        rings = {"e": (BLUE, 1.0)}
    if t1 > 0.5:
        shown["e"] = t1
    if t2 > 0:
        shown["d"] = t2
        if t2 > 0.5:
            shown["b"] = t2
        rings = {"b": (BLUE, 1.0)}
    if t3 > 0:
        for u, v in (("a", "c"), ("c", "d")):
            es[GV_D.key(u, v)] = (BLUE, 11, t3)
        rings = {"d": (GREEN, 1.0)}
    if t4 > 0:
        shown["c"] = t4
        rings = {"c": (BLUE, 1.0)}
    if t5 > 0:
        shown["a"] = t5
        rings = {"a": (BLUE, 1.0)}
    GV_D.draw(ctx, estyle=es, rings=rings)
    for v, a in shown.items():
        x, y = D_POS[v]
        badge(cv, x, y - 82, vals[v], a, size=32, r=28)
    panel_card(ctx, "THE CACHE")
    yy = 180
    for v in ["e", "d", "b", "c", "a"]:
        a = shown.get(v, 0.0)
        if a > 0:
            cv.rrect(1316, yy, 1854, yy + 76, 14, fill=PAPER, outline=ACCENT, width=3, a=a)
            cv.text(1342, yy + 38, f"'{v}'", 36, INK, True, True, anchor="lm", a=a)
            cv.text(1620, yy + 38, "→", 36, MUTED, True, anchor="mm", a=a)
            cv.text(1830, yy + 38, str(vals[v]), 44, ACCENT, True, True, anchor="rm", a=a)
        yy += 88
    hit = ctx.p("t4", 0.4)
    if hit > 0:
        tag(cv, 1585, 640, "cache hit on 'd'", GREEN, a=hit, size=32)
    finish(ctx)


def scene_e_to_a(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    GV_D.draw(ctx, rings={"e": (BLUE, ctx.p("e", 0.4))})
    cv.text(D_POS["e"][0], D_POS["e"][1] + 90, "start here", 26, BLUE, True, anchor="mm", a=ctx.p("e", 0.4))
    cv.text(D_POS["a"][0], D_POS["a"][1] + 90, "target", 26, ORANGE, True, anchor="mm", a=ctx.p("e", 0.4))
    panel_card(ctx, "count_paths(g, 'e', 'a')")
    a = ctx.p("e", 0.4)
    cv.text(1330, 200, "'e' is not 'a'", 34, INK, True, a=a)
    cv.text(1330, 260, "and graph['e'] is  [ ]", 34, INK, True, a=a)
    cv.text(1330, 340, "sum of nothing", 32, MUTED, True, a=a)
    cv.text(1330, 420, "0", 150, RED, True, a=a)
    finish(ctx)


CYC_POS = {"a": (330, 520), "b": (730, 320), "c": (730, 720)}
GV_C = GraphView(CYC_POS, [("a", "b"), ("b", "c"), ("c", "a")], directed=True, r=56, label_size=48)


def scene_cycle(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    t0 = ctx.cue("go") or 0.0
    k = int(clamp((ctx.t - t0) / 0.45, 0, 14)) if ctx.cue("go") and ctx.t >= t0 else 0
    ctx.sig.append(k)
    order = ["a", "b", "c"]
    cur = order[(k - 1) % 3] if k else None
    err = ctx.p("err", 0.5)
    es = {GV_C.key(order[i % 3], order[(i + 1) % 3]): (RED, 10, 1.0) for i in range(min(k, 3))}
    GV_C.draw(ctx, estyle=es, rings={cur: (BLUE, 1.0)} if cur and err < 0.5 else None)
    panel_card(ctx, "THE CALL STACK")
    y = 176
    for i in range(max(0, min(k, 14) - 11), min(k, 14)):
        cv.text(1330, y, f"nested({order[i % 3]})", 28, INK, True, True)
        y += 40
    if k >= 14 or err > 0:
        cv.rrect(1316, 700, 1854, 880, 20, fill=(253, 232, 232), outline=RED, width=4, a=max(err, 0.0))
        cv.text(1585, 790, "RecursionError", 46, RED, True, anchor="mm", a=err)
    finish(ctx)


LADDER_CODE = ["ladder = {i: [i + 1, i + 2] for i in range(60)} | {60: [], 61: []}"]
LADDER_CARD = CodeCard(LADDER_CODE, rect=(40, 126, 1246, 420), size=28, lh=56, numbers=False, x_off=40, y_off=40)


def scene_ladder_code(ctx):
    boxes = [(1, "i: [i + 1, i + 2]", BLUE, "comp"), (1, "for i in range(60)", ACCENT_DARK, "comp"),
             (1, "|", RED, "bar"), (1, "{60: [], 61: []}", GREEN, "bar")]
    LADDER_CARD.draw(ctx, boxes=boxes, title="THE LAB'S LADDER")
    cv = ctx.cv
    stage_rect = (40, 450, 1246, 906)
    cv.rrect(40, 450, 1246, 906, 26, fill=(238, 246, 252), outline=PANEL_LINE, width=3)
    # tiny picture of the first stones
    small = {i: (140 + i * 140, 760) for i in range(8)}
    sg = GraphView(small, [(i, i + 1, 0) for i in range(7)] + [(i, i + 2, -120) for i in range(6)], directed=True, r=34,
                   label_size=30)
    a = ctx.p("comp", 0.5)
    sg.draw(ctx, edge_alpha=a)
    cv.text(640, 520, "stone i can hop to  i + 1  and  i + 2", 32, INK, True, anchor="mm", a=a)
    cv.text(1196, 760, "…60", 30, MUTED, True, anchor="mm", a=a)
    notes_panel(ctx, "READING THE LINE", [
        ("comp", "{ i: [...] for i in ... }", "a dictionary comprehension: for each i from 0 to 59, a key i with the list [i + 1, i + 2]", BLUE),
        ("bar", "dict | dict", "the bar merges two dictionaries. Here it adds stones 60 and 61, which have no hops.", RED)])
    finish(ctx)


def scene_ladder_num(ctx):
    cv = ctx.cv
    stage(ctx, "river")
    big = ctx.p("big", 0.6)
    cv.text(640, 230, "ways to cross 60 stones", 36, MUTED, True, anchor="mm", a=big)
    cv.text(640, 340, "2,504,730,781,961", 88, ACCENT, True, anchor="mm", a=big)
    fib = ctx.p("fib", 0.6)
    cv.text(640, 470, "1   1   2   3   5   8   13   21   34   55   ...", 38, INK, True, True, anchor="mm", a=fib)
    cv.text(640, 540, "each number = the two before it added together", 28, MUTED, False, anchor="mm", a=fib)
    chars.frog(cv, 640, 760, 1.4)
    panel_card(ctx, "FIBONACCI, AGAIN")
    draw_wrapped(cv, 1330, 190, "These are the Fibonacci numbers from the dynamic programming reading.", 32, 500, INK, True, a=fib)
    finish(ctx)


def ladder_rows():
    rows = []
    for n in (5, 10, 20, 40, 60):
        ladder = {i: [i + 1, i + 2] for i in range(n)} | {n: [], n + 1: []}
        cached = P.count(P.cached_tree(ladder, 0, n))
        rows.append((n, P.ladder_paths(n), P.naive_calls_ladder(n), cached))
    return rows


LADDER_ROWS = ladder_rows()


def scene_ladder_cost(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    ca = ctx.p("cache", 0.5)
    hdr = ["stones", "ways", "plain calls", "cached calls"]
    xs = [140, 330, 700, 1040]
    for x, h in zip(xs, hdr):
        cv.text(x, 180, h, 28, MUTED, True, anchor="lm")
    y = 240
    for n, ways, naive, cached in LADDER_ROWS:
        hi = n == 60
        if hi:
            cv.rrect(60, y - 10, 1230, y + 70, 16, fill=ACCENT_SOFT, outline=ACCENT, width=3)
        cv.text(xs[0], y + 30, str(n), 36, INK, True, anchor="lm")
        cv.text(xs[1], y + 30, f"{ways:,}", 34, INK, True, anchor="lm")
        cv.text(xs[2], y + 30, f"{naive:,}", 34, RED, True, anchor="lm")
        cv.text(xs[3], y + 30, str(cached), 34, GREEN, True, anchor="lm", a=ca if hi else 1.0)
        y += 96
    cv.text(640, 780, "at ten million calls a second, 8 trillion calls take over nine days", 30, RED, True, anchor="mm")
    cv.text(640, 840, "121 calls take a fraction of a millisecond", 34, GREEN, True, anchor="mm", a=ca)
    panel_card(ctx, "PLAIN vs CACHED")
    cv.text(1330, 200, "plain:", 32, RED, True)
    cv.text(1330, 246, "grows like Fibonacci", 30, INK, False)
    cv.text(1330, 340, "cached:", 32, GREEN, True, a=ca)
    cv.text(1330, 386, "1 + E calls  =  2n + 1", 30, INK, False, a=ca)
    finish(ctx)


def scene_dp_link(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    rows = [("m1", "a vertex", "a subproblem  (a call)", BLUE), ("m2", "an edge  u → v", "computing u needs v", ACCENT_DARK),
            ("m3", "marking a vertex", "its answer is cached", GREEN),
            ("m4", "the post-visit", "compute the value, last", PURPLE)]
    y = 160
    for cue, a_, b_, col in rows:
        a = ctx.p(cue, 0.5)
        cv.rrect(70, y, 1210, y + 150, 24, fill=WHITE, outline=col, width=4, a=a)
        cv.text(110, y + 26, "depth-first search:", 24, MUTED, True, a=a)
        cv.text(110, y + 66, a_, 40, col, True, a=a)
        cv.arrow((560, y + 75), (640, y + 75), col, 7, a=a, head=24)
        cv.text(690, y + 26, "memoized recursion:", 24, MUTED, True, a=a)
        cv.text(690, y + 66, b_, 36, INK, True, a=a)
        y += 178
    panel_card(ctx, "BOOK: FIGURE 6.10, PDF p.253")
    draw_wrapped(cv, 1330, 190, "Memoized recursion is depth-first search. Depth-first search is memoized recursion.", 34, 500, ACCENT_DARK, True)
    finish(ctx)


def scene_recap(ctx):
    cv = ctx.cv
    stage(ctx, "plain")
    cards = [("c1", "paths(s, t)", "1 if s is t, else the sum over the children"),
             ("c2", "Plain recursion repeats work", "24 calls on a 7-junction map"),
             ("c3", "A cache answers each vertex once", "so the time is O(V + E)"),
             ("c4", "Answers come out children first", "next: topological order")]
    y = 150
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(150, y + 75, 34, fill=ACCENT, a=a)
        cv.text(150, y + 74, str(i + 1), 38, WHITE, True, anchor="mm", a=a)
        cv.text(215, y + 22, head, 40, ACCENT_DARK, True, a=a)
        cv.text(215, y + 86, sub, 28, INK, False, a=a)
        y += 174
    chars.frog(cv, 1100, 880, 1.0, a=ctx.p("c4", 0.5))
    finish(ctx)
