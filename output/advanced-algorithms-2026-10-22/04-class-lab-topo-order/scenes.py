"""Video 04 scenes: topological order, the dinner DAG, your E graph, your code and its test."""
from __future__ import annotations

import math

import chars
import topolog as T
from dfslog import backward_edges
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, RED, WHITE, clamp, ease, lerp, mix,
)
from graphview import GraphView
from widgets import (
    CodeCard, PANEL, chrome, draw_wrapped, notes_panel, panel_card, predict_chip, tag, wrap,
)

PURPLE = (140, 80, 200)
ORANGE = (234, 140, 36)

# ---------------------------------------------------------------- graph views
G1_POS = {"A": (640, 320), "B": (420, 540), "C": (860, 540), "D": (640, 760)}
GV1 = GraphView(G1_POS, [(u, w) for u, ws in T.G1.items() for w in ws], directed=True, r=48, label_size=44)
G2_POS = {"E": (640, 190), "A": (640, 390), "B": (420, 580), "C": (860, 580), "D": (640, 770)}
GV2 = GraphView(G2_POS, [(u, w) for u, ws in T.G2_E_FIRST.items() for w in ws], directed=True, r=48, label_size=44)
D_POS = {"Shop": (120, 520), "Chop": (330, 520), "Boil": (540, 320), "Fry": (540, 720), "Sauce": (750, 520),
         "Plate": (960, 520), "Eat": (1170, 520)}
GVD = GraphView(D_POS, [(u, w) for u, ws in T.DINNER.items() for w in ws], directed=True, r=46, label_size=26)


D2_POS = dict(D_POS)
D2_POS["Table"] = (1170, 770)
GVD2 = GraphView(D2_POS, [(u, w) for u, ws in T.DINNER2_C1.items() for w in ws], directed=True, r=46, label_size=26)


def stage(ctx, kind="plain"):
    cv = ctx.cv
    bg = {"plain": (244, 246, 250), "kitchen": (252, 247, 238), "morning": (240, 246, 252)}[kind]
    cv.rrect(30, 112, 1258, 916, 28, fill=bg, outline=(224, 228, 236), width=3)
    if kind == "kitchen":
        for y in range(170, 916, 60):
            cv.line((48, y), (1240, y), (246, 238, 222), 2)


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def names_below(ctx, gv, a=1.0):
    for v, (x, y) in gv.pos.items():
        if v in T.TASK:
            if v == "E":
                ctx.cv.text(x + gv.r + 18, y, T.TASK[v], 24, MUTED, True, anchor="lm", a=a)
            else:
                ctx.cv.text(x, y + gv.r + 24, T.TASK[v], 24, MUTED, True, anchor="mm", a=a)


# ---------------------------------------------------------------- line layouts
def line_view(order, graph, x0=110, x1=1170, y=520, r=38, size=30):
    n = len(order)
    pos = {v: (x0 + (x1 - x0) * i / max(1, n - 1), y) for i, v in enumerate(order)}
    idx = {v: i for i, v in enumerate(order)}
    edges = []
    for u in graph:
        for w in graph[u]:
            edges.append((u, w, -(70 + 46 * abs(idx[u] - idx[w]))))
    return GraphView(pos, edges, directed=True, r=r, label_size=size), idx


def draw_line(ctx, order, graph, y=520, a=1.0, r=38, size=30, x0=110, x1=1170, names=None, fwd_color=BLUE):
    gv, idx = line_view(order, graph, x0=x0, x1=x1, y=y, r=r, size=size)
    es = {}
    for u in graph:
        for w in graph[u]:
            back = idx[u] > idx[w]
            es[gv.key(u, w)] = (RED if back else fwd_color, 6, a)
    gv.draw(ctx, estyle=es, vfade={v: a for v in order})
    if names:
        for v, (x, yy) in gv.pos.items():
            ctx.cv.text(x, yy + r + 22, names.get(v, v), 22, MUTED, True, anchor="mm", a=a)
    return gv, len(backward_edges(graph, order))


# ---------------------------------------------------------------- part A
def scene_g1(ctx):
    stage(ctx, "morning")
    cv = ctx.cv
    cues = {"A": "a", "B": "b", "C": "c", "D": "d"}
    rings = {v: (BLUE, ctx.pulse(c, 1.0)) for v, c in cues.items()}
    es = {}
    pa = ctx.p("arrow", 0.5)
    if pa > 0:
        es[GV1.key("A", "B")] = (ACCENT, 11, pa)
    GV1.draw(ctx, rings=rings, estyle=es)
    names_below(ctx, GV1)
    panel_card(ctx, "FROM YOUR 10/19 NOTES")
    cv.text(1330, 190, "A  shower", 40, INK, True)
    cv.text(1330, 250, "B  get dressed", 40, INK, True)
    cv.text(1330, 310, "C  coffee", 40, INK, True)
    cv.text(1330, 370, "D  leave", 40, INK, True)
    a = ctx.p("arrow", 0.5)
    cv.rrect(1316, 470, 1854, 680, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=a)
    cv.text(1344, 494, "A → B", 46, ACCENT_DARK, True, a=a)
    draw_wrapped(cv, 1344, 560, "shower must come before get dressed", 30, 480, INK, False, a=a)
    finish(ctx)


def scene_layouts(ctx):
    stage(ctx, "morning")
    cv = ctx.cv
    bad, good = ctx.p("bad", 0.5), ctx.p("good", 0.5)
    names = {"A": "shower", "B": "dress", "C": "coffee", "D": "leave"}
    nbad = 0
    if bad > 0:
        _, nbad = draw_line(ctx, ["C", "B", "A", "D"], T.G1, y=330, a=bad, r=44, size=40, x0=200, x1=1080, names=names)
        cv.text(80, 160, "not topological: arrows point backward", 30, RED, True, a=bad)
    ngood = 0
    if good > 0:
        _, ngood = draw_line(ctx, ["A", "B", "C", "D"], T.G1, y=720, a=good, r=44, size=40, x0=200, x1=1080, names=names)
        cv.text(80, 560, "topological: every arrow points the same way", 30, BLUE, True, a=good)
    panel_card(ctx, "BACKWARD ARROWS")
    cv.text(1330, 190, "top row:", 30, MUTED, True, a=bad)
    cv.text(1330, 236, f"{nbad} backward", 54, RED, True, a=bad)
    cv.text(1330, 360, "bottom row:", 30, MUTED, True, a=good)
    cv.text(1330, 406, "0 backward", 54, BLUE, True, a=good)
    d = ctx.p("dag", 0.5)
    cv.rrect(1316, 560, 1854, 800, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=d)
    cv.text(1344, 586, "your note:", 28, MUTED, True, a=d)
    draw_wrapped(cv, 1344, 630, "a DAG always has a topological order", 36, 480, BLUE, True, a=d)
    finish(ctx)


CYC = GraphView({"A": (480, 520), "B": (800, 520)}, [("A", "B", -90), ("B", "A", -90)], directed=True, r=70, label_size=56)


def scene_cycle2(ctx):
    stage(ctx, "morning")
    cv = ctx.cv
    a = ctx.p("cyc", 0.5)
    CYC.draw(ctx, estyle={("A", "B"): (RED, 9, 1.0), ("B", "A"): (RED, 9, 1.0)} if a > 0 else None)
    cv.text(480, 640, "shower", 30, MUTED, True, anchor="mm")
    cv.text(800, 640, "dress", 30, MUTED, True, anchor="mm")
    tag(cv, 640, 330, "dress before shower?", RED, a=a, size=30)
    tag(cv, 640, 760, "shower before dress?", RED, a=a, size=30)
    imp = ctx.p("imp", 0.5)
    cv.text(640, 860, "no order can satisfy both", 44, RED, True, anchor="mm", a=imp)
    panel_card(ctx, "WHY NO CYCLES")
    draw_wrapped(cv, 1330, 190, "If tasks need each other in a loop, no order exists.", 34, 500, INK, True)
    draw_wrapped(cv, 1330, 420, "Without a cycle, an order always exists.", 34, 500, BLUE, True, a=ctx.p("ok", 0.5))
    finish(ctx)


# ---------------------------------------------------------------- part B: dinner
def scene_dinner_intro(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    GVD.draw(ctx, rings={"Shop": (BLUE, ctx.pulse("q", 1.5))})
    chars.person(cv, 120, 440, 0.85, shirt=ACCENT, hat=(250, 250, 250))
    panel_card(ctx, "DINNER")
    cv.text(1330, 190, "7 tasks", 46, INK, True)
    cv.text(1330, 260, "12 rules", 46, INK, True)
    draw_wrapped(cv, 1330, 340, "An arrow means: this task must be finished before that one starts.", 30, 500, MUTED, False)
    cv.text(1330, 520, "a valid order?", 36, INK, True)
    cv.text(1330, 590, "?", 140, ACCENT, True)
    finish(ctx)


def scene_dfs_idea(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    GVD.draw(ctx)
    panel_card(ctx, "THE TRICK")
    cards = [("u1", "reach a task", "start it", BLUE), ("u2", "visit everything it unlocks", "before anything else", ACCENT_DARK),
             ("u3", "only then", "call this task finished", GREEN)]
    y = 180
    for cue, head, sub, col in cards:
        a = ctx.p(cue, 0.5)
        cv.rrect(1316, y, 1854, y + 180, 20, fill=PAPER, outline=col, width=4, a=a)
        cv.text(1344, y + 24, head, 34, col, True, a=a)
        cv.text(1344, y + 84, sub, 30, INK, False, a=a)
        y += 200
    finish(ctx)


# ---------------------------------------------------------------- DFS animation
def dfs_state(res, k):
    state, pre, post, stack, last = {}, {}, {}, [], None
    for e in res["events"][:k]:
        if e["kind"] == "start":
            state[e["v"]] = "active"
            pre[e["v"]] = e["clock"]
            stack.append(e["v"])
        elif e["kind"] == "finish":
            state[e["v"]] = "finished"
            post[e["v"]] = e["clock"]
            stack.remove(e["v"])
        last = e
    return state, pre, post, stack, last


def chips(cv, x0, y0, items, per_row=4, w=118, h=40, color=ACCENT, a=1.0, size=22, gap=10):
    for i, (label, on) in enumerate(items):
        col, row = i % per_row, i // per_row
        x, y = x0 + col * (w + gap), y0 + row * (h + 8)
        cv.rrect(x, y, x + w, y + h, h / 2, fill=ACCENT_SOFT if on else PAPER, outline=color if on else PANEL_LINE, width=3, a=a)
        cv.text(x + w / 2, y + h / 2, label, size, INK, True, anchor="mm", a=a)


def dfs_panel(ctx, res, k, order_names=None, show_rev=False, rev_cue=None):
    cv = ctx.cv
    state, pre, post, stack, last = dfs_state(res, k)
    panel_card(ctx, None)
    cv.text(1318, 134, "ACTIVE (the recursion stack)", 20, MUTED, True)
    cv.line((1316, 160), (1854, 160), PANEL_LINE, 2)
    # stack drawn bottom-up
    base = 452
    for i, v in enumerate(stack):
        y = base - (i + 1) * 46
        cv.rrect(1330, y, 1700, y + 40, 12, fill=BLUE_SOFT, outline=BLUE, width=3)
        cv.text(1350, y + 20, v, 24, INK, True, anchor="lm")
        cv.text(1690, y + 20, f"start {pre[v]}", 20, MUTED, True, anchor="rm")
    if not stack:
        cv.text(1330, 412, "(empty)", 24, GRAY, True, True)
    cv.text(1318, 470, "STARTED (preorder)", 20, MUTED, True)
    chips(cv, 1330, 498, [(f"{v}", True) for v in sorted(pre, key=pre.get)], w=122, h=38, color=BLUE)
    cv.text(1318, 596, "FINISHED (postorder)", 20, MUTED, True)
    chips(cv, 1330, 624, [(f"{v}", True) for v in sorted(post, key=post.get)], w=122, h=38, color=ACCENT)
    if show_rev:
        a = ctx.p(rev_cue, 0.5) if rev_cue else 1.0
        cv.text(1318, 724, "REVERSED  →  topological order", 20, GREEN, True, a=a)
        rev = list(reversed(sorted(post, key=post.get)))
        chips(cv, 1330, 752, [(v, True) for v in rev], w=122, h=38, color=GREEN, a=a)
    return state, pre, post, stack, last


def badge_num(cv, x, y, n, color, a=1.0):
    cv.circle(x, y, 17, fill=color, a=a)
    cv.text(x, y - 1, str(n), 20, WHITE, True, anchor="mm", a=a)


def dfs_scene(res, gv, lo, hi, kind="kitchen", show_rev=False, rev_cue=None, names=False, flash=0.8):
    def scene(ctx):
        cv = ctx.cv
        stage(ctx, kind)
        k = lo
        times = []
        for i in range(lo, hi):
            t = ctx.cue(f"e{i}")
            ok = t is not None and ctx.t >= t
            ctx.sig.append(1 if ok else 0)
            if ok:
                k = i + 1
                times.append(t)
        state, pre, post, stack, last = dfs_state(res, k)
        fills, es, rings = {}, {}, {}
        marked = {}
        for v, s in state.items():
            if s == "active":
                fills[v] = (BLUE, 0.28)
                rings[v] = (BLUE, 1.0)
            else:
                marked[v] = 1.0
        if last and last["kind"] == "edge" and times and ctx.t - times[-1] < flash:
            col = BLUE if last["etype"] == "tree" else ORANGE
            es[gv.key(last["u"], last["v"])] = (col, 12, 1.0)
        for e in res["events"][:k]:
            if e["kind"] == "edge" and e["etype"] == "tree":
                es.setdefault(gv.key(e["u"], e["v"]), (BLUE, 8, 0.55))
        gv.draw(ctx, marked=marked, fills=fills, rings=rings, estyle=es)
        for v, (x, y) in gv.pos.items():
            if v in pre:
                badge_num(cv, x - gv.r * 0.8, y - gv.r * 0.9, pre[v], BLUE)
            if v in post:
                badge_num(cv, x + gv.r * 0.8, y - gv.r * 0.9, post[v], ACCENT_DARK)
        if names:
            names_below(ctx, gv)
        if last and last["kind"] == "edge" and last["etype"] != "tree" and times and ctx.t - times[-1] < flash:
            x0, y0 = gv.pos[last["u"]]
            x1, y1 = gv.pos[last["v"]]
            tag(cv, (x0 + x1) / 2, (y0 + y1) / 2 - 36, "already finished: skip", ORANGE, size=22)
        dfs_panel(ctx, res, k, show_rev=show_rev, rev_cue=rev_cue)
        finish(ctx)
    return scene


def ev_cues(anchor_spec):
    """anchor_spec: [(anchor, first_event, count, per, offset)] -> extra_cues list."""
    out = []
    for anchor, first, count, per, off in anchor_spec:
        for j in range(count):
            out.append((f"e{first + j}", anchor, off + per * j))
    return out


def scene_finish_order(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    post = T.DINNER_DFS["post_order"]
    rev = list(reversed(post))
    a = ctx.p("rev", 0.5)
    la = ctx.p("line", 0.6)
    cv.text(640, 160, "finish order (postorder)", 30, ACCENT_DARK, True, anchor="mm")
    gv, _ = draw_line(ctx, post, T.DINNER, y=330, a=0.0, r=36, size=22)
    for i, v in enumerate(post):
        x = 110 + (1170 - 110) * i / 6
        cv.circle(x, 220, 40, fill=ACCENT_SOFT, outline=ACCENT, width=4)
        cv.text(x, 219, v, 22, INK, True, anchor="mm")
    cv.text(640, 440, "reversed", 30, GREEN, True, anchor="mm", a=a)
    if la > 0:
        _, nb = draw_line(ctx, rev, T.DINNER, y=700, a=la, r=40, size=24, fwd_color=GREEN)
    panel_card(ctx, "REVERSED = TOPOLOGICAL")
    cv.text(1330, 190, "Shop, Chop, Fry,", 34, GREEN, True, a=a)
    cv.text(1330, 240, "Boil, Sauce, Plate, Eat", 34, GREEN, True, a=a)
    cv.text(1330, 360, "12 of 12 arrows", 40, INK, True, a=la)
    cv.text(1330, 410, "point forward", 40, GREEN, True, a=la)
    finish(ctx)


def scene_why(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    d = T.DINNER_DFS
    post, pre = d["post"], d["pre"]
    p1, p2 = ctx.p("w1", 0.5), ctx.p("w2", 0.5)
    es = {}
    if p1 > 0:
        es[GVD.key("Fry", "Sauce")] = (ACCENT, 13, p1)
    if p2 > 0:
        es[GVD.key("Chop", "Boil")] = (GREEN, 13, p2)
    GVD.draw(ctx, marked={v: 1.0 for v in T.DINNER}, estyle=es)
    for v, (x, y) in GVD.pos.items():
        badge_num(cv, x + GVD.r * 0.8, y - GVD.r * 0.9, post[v], ACCENT_DARK)
    panel_card(ctx, "WHY IT WORKS")
    cv.text(1330, 190, "arrow  Fry → Sauce", 34, INK, True, a=p1)
    cv.text(1330, 240, f"Sauce finished at {post['Sauce']}", 30, MUTED, False, a=p1)
    cv.text(1330, 282, f"Fry finished at {post['Fry']}", 30, MUTED, False, a=p1)
    cv.text(1330, 340, f"{post['Fry']} > {post['Sauce']}", 56, ACCENT, True, a=p1)
    cv.text(1330, 450, "arrow  Chop → Boil", 34, INK, True, a=p2)
    cv.text(1330, 500, f"{post['Chop']} > {post['Boil']}", 56, GREEN, True, a=p2)
    a = ctx.p("rule", 0.5)
    cv.rrect(1316, 620, 1854, 880, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=a)
    draw_wrapped(cv, 1344, 650, "For every arrow u → v, v finishes before u. So after reversing, u comes before v.", 31, 480, BLUE, True, a=a)
    finish(ctx)


def scene_preorder_fail(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    pre = T.DINNER_DFS["pre_order"]
    a = ctx.p("pre", 0.5)
    cv.text(640, 160, "start order (preorder)", 30, BLUE, True, anchor="mm", a=a)
    nb = 0
    if a > 0:
        gv, nb = draw_line(ctx, pre, T.DINNER, y=420, a=a, r=40, size=24)
    bk = ctx.p("bad", 0.5)
    if bk > 0:
        x = 110 + (1170 - 110) * 6 / 6
        cv.circle(x, 420, 56, outline=RED, width=6, a=bk)
        tag(cv, 900, 800, "Fry comes last, but must come before Sauce and Plate", RED, a=bk, size=28)
    panel_card(ctx, "PREORDER FAILS")
    cv.text(1330, 190, f"{nb} backward arrows", 40, RED, True, a=bk)
    cv.text(1330, 250, "Fry → Sauce", 34, INK, True, a=bk)
    cv.text(1330, 296, "Fry → Plate", 34, INK, True, a=bk)
    draw_wrapped(cv, 1330, 420, "Preorder is the order tasks start. It is not a topological order.", 32, 500, INK, True, a=bk)
    finish(ctx)


# ---------------------------------------------------------------- part C: the E graph
def scene_e_intro(ctx):
    """Dinner again, plus a second start task: set the table."""
    stage(ctx, "kitchen")
    cv = ctx.cv
    ta, two = ctx.p("t", 0.6), ctx.p("two", 0.5)
    pulse = ctx.pulse("two", 1.4)
    vf = {"Table": ta}
    es = {GVD2.key("Table", "Eat"): (ACCENT, 11, ta)}
    GVD2.draw(ctx, estyle=es, vfade=vf, rings={"Shop": (BLUE, pulse), "Table": (BLUE, pulse * ta)},
              label_color=None)
    tag(cv, D2_POS["Table"][0] - 130, D2_POS["Table"][1], "set the table", ORANGE, a=ta, size=24)
    panel_card(ctx, "A SECOND START TASK")
    cv.text(1330, 190, "set the table", 40, ACCENT_DARK, True, a=ta)
    draw_wrapped(cv, 1330, 250, "nothing has to come before it. Its only arrow leads to Eat.", 30, 510, INK, False, a=ta)
    cv.rrect(1316, 440, 1854, 700, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=two)
    cv.text(1344, 464, "two start tasks", 34, ACCENT_DARK, True, a=two)
    draw_wrapped(cv, 1344, 520, "Shop and Table. A loop over all the tasks could start at either one.", 30, 480, INK, False, a=two)
    finish(ctx)


def scene_compare(ctx):
    stage(ctx, "kitchen")
    cv = ctx.cv
    blocks = [("case 1: the loop starts at Shop", T.CASE1, "c1"), ("case 2: the loop starts at Table", T.CASE2, "c2")]
    y = 140
    for title, res, cue in blocks:
        g = T.DINNER2_C1
        a = ctx.p(cue, 0.5)
        cv.rrect(50, y, 1240, y + 370, 24, fill=WHITE, outline=PANEL_LINE, width=3, a=a)
        cv.text(80, y + 16, title, 30, ACCENT_DARK, True, a=a)
        rows = [("start order", res["pre_order"], BLUE, "bad"), ("finish order", res["post_order"], ACCENT_DARK, None),
                ("reversed finish order", list(reversed(res["post_order"])), GREEN, "good")]
        for j, (lab, order, col, vcue) in enumerate(rows):
            yy = y + 70 + j * 100
            nb = len(backward_edges(g, order))
            va = a * (ctx.p(vcue, 0.5) if vcue else 0.0)
            cv.text(80, yy + 2, lab, 22, MUTED, True, a=a)
            if vcue:
                cv.text(80, yy + 32, f"{nb} backward" if nb else "0 backward", 24, RED if nb else GREEN, True, a=va)
            for i, v in enumerate(order):
                x = 330 + i * 110
                cv.rrect(x, yy, x + 102, yy + 44, 22, fill=WHITE, outline=col, width=4, a=a)
                cv.text(x + 51, yy + 22, v, 20, INK, True, anchor="mm", a=a)
        y += 392
    panel_card(ctx, "BOTH CASES")
    draw_wrapped(cv, 1330, 190, "The start order fails both times.", 34, 510, RED, True, a=ctx.p("bad", 0.5))
    draw_wrapped(cv, 1330, 330, "The reversed finish order works both times.", 34, 510, GREEN, True, a=ctx.p("good", 0.5))
    draw_wrapped(cv, 1330, 500, "They are different orders. Table only has to come before Eat, so it can go early or late.", 30, 510,
                 INK, False, a=ctx.p("diff", 0.5))
    finish(ctx)


CODE = [
    "def topo_order(children):",
    "    pre_order = []",
    "    post_order = []",
    "    visited = set()",
    "    def build_topo_from(node):",
    "        pre_order.append(node)",
    "        visited.add(node)",
    "        for child in children[node]:",
    "            if child not in visited:",
    "                build_topo_from(child)",
    "        post_order.append(node)",
    "",
    "    for node in children:",
    "        if node not in visited:",
    "            build_topo_from(node)",
    "    return pre_order",
]
CARD = CodeCard(CODE, size=27, lh=44, y_off=34, x_off=100)


def code_scene(hl=(), boxes=(), notes=(), title="notes", tags=(), dim=None):
    def scene(ctx):
        CARD.draw(ctx, hl=hl, boxes=boxes, tags=tags, dim=dim, title="YOUR topo_order  (mini-lab.py)")
        notes_panel(ctx, title, list(notes))
        finish(ctx)
    return scene


def scene_code_bug(ctx):
    CARD.draw(ctx, hl=[(16, None)], boxes=[(16, "pre_order", RED, "bug")], title="YOUR topo_order  (mini-lab.py)")
    cv = ctx.cv
    panel_card(ctx, "THE ONE-LINE FIX")
    a, b = ctx.p("bug", 0.5), ctx.p("fix", 0.5)
    cv.rrect(1316, 180, 1854, 300, 18, fill=(253, 232, 232), outline=RED, width=4, a=a)
    cv.text(1344, 206, "return pre_order", 36, RED, True, True, a=a)
    cv.line((1340, 240), (1700, 240), RED, 4, a)
    cv.text(1344, 262, "start order: not topological", 24, RED, False, a=a)
    cv.rrect(1316, 340, 1854, 500, 18, fill=(228, 246, 236), outline=GREEN, width=4, a=b)
    cv.text(1344, 366, "return list(reversed(post_order))", 28, GREEN, True, True, a=b)
    cv.text(1344, 416, "reversed(...) gives the items back to front", 24, INK, False, a=ctx.p("rev1", 0.5))
    cv.text(1344, 452, "list(...) turns that into a list", 24, INK, False, a=ctx.p("rev2", 0.5))
    cv.text(1330, 560, "A change shown here only.", 28, MUTED, True, a=b)
    cv.text(1330, 600, "Your file stays as you wrote it.", 28, MUTED, False, a=b)
    finish(ctx)


TEST_BAD = [
    "def test_topo_order():",
    '    assert topo_order(g, "a", "e") == 2',
    '    assert topo_order(g, "b", "e") == 1',
    '    assert topo_order(g, "e", "a") == 0',
]
TEST_GOOD = [
    "def test_topo_order():",
    '    for graph in [g, {"x": [], "y": ["x"], "z": ["y", "x"]}]:',
    "        order = topo_order(graph)",
    "        assert sorted(order) == sorted(graph)",
    "        assert all(order.index(u) < order.index(w) for u in graph for w in graph[u])",
]
CARD_BAD = CodeCard(TEST_BAD, rect=(40, 126, 1246, 390), size=28, lh=50, y_off=44, x_off=40, numbers=False)
CARD_GOOD = CodeCard(TEST_GOOD, rect=(40, 126, 1246, 440), size=26, lh=52, y_off=44, x_off=40, numbers=False)


def scene_test_bad(ctx):
    CARD_BAD.draw(ctx, boxes=[(2, 'topo_order(g, "a", "e")', RED, "args")], title="YOUR test_topo_order  (a copy of the first test)")
    if ctx.reached("spec"):
        CARD_GOOD2.draw(ctx, title="THE SPEC'S TEST")
    notes_panel(ctx, "THE MISMATCH", [
        ("args", "3 arguments", "topo_order takes one argument, the graph. This call passes three.", RED),
        ("spec", "the spec's test", "checks the order itself, not a number", GREEN)])
    finish(ctx)


CARD_GOOD2 = CodeCard(TEST_GOOD, rect=(40, 440, 1246, 906), size=24, lh=56, y_off=50, x_off=30, numbers=False)


def scene_spec_test(ctx):
    CARD_GOOD3.draw(ctx, boxes=[(4, "sorted(order) == sorted(graph)", BLUE, "s1"),
                                (5, "order.index(u) < order.index(w)", GREEN, "s2"),
                                (5, "for u in graph for w in graph[u]", ACCENT_DARK, "s3"),
                                (5, "all(", RED, "s4")], title="THE SPEC'S TEST")
    notes_panel(ctx, "READING THE TEST", [
        ("s1", "same vertices", "no vertex lost or added", BLUE),
        ("s2", "order.index(u)", "the position of u in the list. The test: u's position is smaller than w's.", GREEN),
        ("s3", "two for loops", "every vertex u, and every child w of u: every arrow", ACCENT_DARK),
        ("s4", "all( ... )", "True only if every single check is True", RED)])
    finish(ctx)


CARD_GOOD3 = CodeCard(TEST_GOOD, rect=(40, 126, 1246, 906), size=24, lh=64, y_off=40, x_off=30, numbers=False)


def scene_run_tests(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    r_bad, r_ok = T.spec_test(T.topo_order_yours), T.spec_test(T.topo_order_fixed)
    a1, a2 = ctx.p("bad", 0.5), ctx.p("fixed", 0.5)
    cv.text(70, 150, "your function, as written", 28, RED, True, a=a1)
    if a1 > 0:
        order = r_bad[0][0]
        draw_line(ctx, order, T.LAB_G, y=330, a=a1, r=36, size=34, x0=170, x1=1090)
        cv.text(640, 440, "c → d points backward: the test fails", 28, RED, True, anchor="mm", a=a1)
    cv.text(70, 520, "with the fix", 28, GREEN, True, a=a2)
    if a2 > 0:
        order = r_ok[0][0]
        draw_line(ctx, order, T.LAB_G, y=700, a=a2, r=36, size=34, x0=170, x1=1090, fwd_color=GREEN)
        cv.text(640, 810, "every arrow points forward: the test passes", 28, GREEN, True, anchor="mm", a=a2)
    panel_card(ctx, "THE SPEC'S TEST")
    cv.text(1330, 190, "graph 1", 30, MUTED, True)
    cv.text(1330, 240, "your function:  FAIL", 40, RED, True, a=a1)
    cv.text(1330, 300, "fixed:  PASS", 40, GREEN, True, a=a2)
    cv.text(1330, 400, "graph 2  (x, y, z)", 30, MUTED, True, a=a2)
    cv.text(1330, 450, f"fixed: {', '.join(r_ok[1][0])}", 36, GREEN, True, a=a2)
    cv.text(1330, 500, "PASS", 40, GREEN, True, a=a2)
    finish(ctx)


def scene_speed(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    items = [("s1", "each task is visited once", BLUE), ("s2", "each arrow is looked at once", ACCENT_DARK),
             ("s3", "total:  O(V + E)", GREEN)]
    y = 220
    for cue, text, col in items:
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1170, y + 150, 26, fill=WHITE, outline=col, width=4, a=a)
        cv.text(130, y + 75, text, 48, col, True, anchor="lm", a=a)
        y += 190
    panel_card(ctx, "ABOUT THE TEST")
    draw_wrapped(cv, 1330, 190, "The test uses order.index, which scans the list. So the test is slower; the function is not.", 30, 500,
                 MUTED, False, a=ctx.p("t", 0.5))
    finish(ctx)


def scene_recap(ctx):
    stage(ctx, "plain")
    cv = ctx.cv
    cards = [("c1", "Topological order", "every arrow points the same way"),
             ("c2", "Reverse the finish order", "of a depth-first search"),
             ("c3", "Preorder is not enough", "it fails whichever task the loop starts at"),
             ("c4", "One change in your code", "return the reversed post_order")]
    y = 150
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(150, y + 75, 34, fill=ACCENT, a=a)
        cv.text(150, y + 74, str(i + 1), 38, WHITE, True, anchor="mm", a=a)
        cv.text(215, y + 22, head, 40, ACCENT_DARK, True, a=a)
        cv.text(215, y + 86, sub, 28, INK, False, a=a)
        y += 174
    cv.text(630, 868, "Next: the book's chapter 6, preorder, postorder, and cycles", 30, BLUE, True, anchor="mm", a=ctx.p("next", 0.5))
    finish(ctx)
