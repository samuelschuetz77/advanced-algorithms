"""Video 05 scenes: the one-way-door maze, the clock, intervals, edge types, cycles."""
from __future__ import annotations

import math

import chars
import mazelog as M
from dfslog import dfs
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, RED, WHITE, clamp, ease, lerp, mix,
)
from graphview import GraphView
from widgets import (
    CodeCard, PANEL, chrome, draw_wrapped, notes_panel, panel_card, predict_chip, tag, wrap,
)

ORANGE = (234, 140, 36)
GOLD = (214, 160, 32)
PURPLE = (140, 80, 200)
TYPE_COL = {"tree": INK, "forward": GREEN, "back": RED, "cross": ORANGE}

POS = {"A": (150, 520), "B": (450, 300), "C": (450, 740), "D": (760, 300), "F": (760, 740),
       "E": (1070, 300), "G": (1070, 740)}
EDGES = [(u, w, 0) for u, ws in M.MAZE.items() for w in ws]
BULGE = {("A", "E"): 140, ("B", "E"): -150, ("E", "B"): -150, ("C", "G"): -150, ("F", "C"): -150}
EDGES = [(u, w, BULGE.get((u, w), 0)) for u, w, _ in EDGES]
GV = GraphView(POS, EDGES, directed=True, r=44, label_size=40)


def stage(ctx):
    cv = ctx.cv
    cv.rrect(30, 112, 1258, 916, 28, fill=(238, 246, 238), outline=(212, 226, 212), width=3)
    for (x, y, w, h) in [(60, 150, 70, 40), (1160, 150, 70, 40), (60, 850, 70, 40), (1160, 850, 70, 40),
                         (600, 140, 80, 34), (600, 860, 80, 34)]:
        cv.rrect(x, y, x + w, y + h, 12, fill=(214, 232, 210))


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def state_at(k):
    state, pre, post, stack, last, clock = {}, {}, {}, [], None, 0
    for e in M.EVENTS[:k]:
        if e["kind"] == "start":
            state[e["v"]] = "active"
            pre[e["v"]] = e["clock"]
            stack.append(e["v"])
            clock = e["clock"]
        elif e["kind"] == "finish":
            state[e["v"]] = "finished"
            post[e["v"]] = e["clock"]
            stack.remove(e["v"])
            clock = e["clock"]
        last = e
    return state, pre, post, stack, last, clock


def badge_num(cv, x, y, n, color, a=1.0):
    cv.circle(x, y, 17, fill=color, a=a)
    cv.text(x, y - 1, str(n), 20, WHITE, True, anchor="mm", a=a)


def thread_and_ada(ctx, stack, gold_a=1.0):
    """Draw the thread along the active path, a ball at the start, and Ada at the current room."""
    cv = ctx.cv
    for u, w in zip(stack, stack[1:]):
        cv.poly_line(GV.pts(u, w), GOLD, 11, a=0.9 * gold_a)
    return


def ada(ctx, v, a=1.0, scale=0.62):
    x, y = POS[v]
    chars.person(ctx.cv, x - 62, y + 38, scale, shirt=ACCENT, hat=(60, 100, 60), a=a)


def ball(ctx, a=1.0):
    x, y = POS["A"]
    cv = ctx.cv
    cv.circle(x - 78, y + 62, 24, fill=GOLD, outline=(160, 110, 10), width=3, a=a)
    cv.arc = None
    cv.line((x - 96, y + 56), (x - 58, y + 70), (160, 110, 10), 3, a)
    cv.line((x - 92, y + 74), (x - 62, y + 52), (160, 110, 10), 3, a)


def legend(ctx, y=880, a=1.0):
    cv = ctx.cv
    x = 70
    for name in ("tree", "forward", "back", "cross"):
        cv.line((x, y), (x + 50, y), TYPE_COL[name], 8, a)
        cv.text(x + 62, y, name, 24, INK, True, anchor="lm", a=a)
        x += 62 + cv.text_w(name, 24, True) + 40


# ---------------------------------------------------------------- panels
def bars_panel(ctx, k, hl=None, show_lists=True, title="ACTIVE INTERVALS"):
    cv = ctx.cv
    state, pre, post, stack, last, clock = state_at(k)
    panel_card(ctx, None)
    cv.text(1318, 134, title + f"   (clock: {clock})", 20, MUTED, True)
    x0, per = 1372, 34
    order = M.RES["pre_order"]
    for t in range(1, 15):
        cv.text(x0 + (t - 0.5) * per, 176, str(t), 15, GRAY, True, anchor="mm")
    for i, v in enumerate(order):
        y = 196 + i * 44
        cv.text(1340, y + 16, v, 24, INK, True, anchor="mm")
        cv.line((x0, y + 34), (x0 + 14 * per, y + 34), GRAY_SOFT, 2)
        if v in pre:
            end = post.get(v, clock)
            on = hl and v in hl
            col = (RED if on else (ACCENT if v in post else BLUE))
            cv.rrect(x0 + (pre[v] - 1) * per + 3, y + 2, x0 + end * per - 3, y + 30, 8, fill=col)
            cv.text(x0 + (pre[v] - 0.5) * per, y + 16, str(pre[v]), 16, WHITE, True, anchor="mm")
            if v in post:
                cv.text(x0 + (post[v] - 0.5) * per, y + 16, str(post[v]), 16, WHITE, True, anchor="mm")
    if show_lists:
        cv.text(1318, 520, "STARTED (preorder)", 20, MUTED, True)
        for i, v in enumerate(sorted(pre, key=pre.get)):
            x = 1330 + i * 70
            cv.rrect(x, 548, x + 60, 586, 19, fill=BLUE_SOFT, outline=BLUE, width=3)
            cv.text(x + 30, 567, v, 24, INK, True, anchor="mm")
        cv.text(1318, 618, "FINISHED (postorder)", 20, MUTED, True)
        for i, v in enumerate(sorted(post, key=post.get)):
            x = 1330 + i * 70
            cv.rrect(x, 646, x + 60, 684, 19, fill=ACCENT_SOFT, outline=ACCENT, width=3)
            cv.text(x + 30, 665, v, 24, INK, True, anchor="mm")
        cv.text(1318, 716, "THE THREAD (active rooms)", 20, MUTED, True)
        cv.text(1330, 746, "  →  ".join(stack) if stack else "(empty)", 30, GOLD, True)
    return state, pre, post, stack, last, clock


def maze_draw(ctx, k, show_types=False, hl_edges=None, flash_t=None, thread=True, decorate=True):
    cv = ctx.cv
    state, pre, post, stack, last, clock = state_at(k)
    es, fills, rings, marked = {}, {}, {}, {}
    seen = {}
    for e in M.EVENTS[:k]:
        if e["kind"] == "edge":
            seen[(e["u"], e["v"])] = e["etype"]
    for (u, w), et in seen.items():
        es[GV.key(u, w)] = (TYPE_COL[et] if show_types or et == "tree" else LINE, 9 if et == "tree" else 7, 1.0)
    if show_types:
        for (u, w) in M.ETYPE:
            if (u, w) not in seen:
                es[GV.key(u, w)] = (LINE, 6, 0.35)
    for v, s in state.items():
        if s == "active":
            fills[v] = (BLUE, 0.28)
            rings[v] = (BLUE, 1.0)
        else:
            marked[v] = 1.0
    if hl_edges:
        for (u, w, col) in hl_edges:
            es[GV.key(u, w)] = (col, 14, 1.0)
    if thread and stack:
        thread_and_ada(ctx, stack)
    GV.draw(ctx, marked=marked, fills=fills, rings=rings, estyle=es)
    if decorate:
        for v, (x, y) in POS.items():
            if v in pre:
                badge_num(cv, x - 36, y - 40, pre[v], BLUE)
            if v in post:
                badge_num(cv, x + 36, y - 40, post[v], ACCENT_DARK)
    return state, pre, post, stack, last, clock


def dfs_run(lo, hi, show_types=True, flash=0.9):
    def scene(ctx):
        cv = ctx.cv
        stage(ctx)
        k, times = lo, []
        for i in range(lo, hi):
            t = ctx.cue(f"e{i}")
            ok = t is not None and ctx.t >= t
            ctx.sig.append(1 if ok else 0)
            if ok:
                k, times = i + 1, times + [t]
        last = M.EVENTS[k - 1] if k > 0 else None
        hl = None
        if last and last["kind"] == "edge" and times and ctx.t - times[-1] < flash:
            hl = [(last["u"], last["v"], TYPE_COL[last["etype"]])]
        state, pre, post, stack, last, clock = maze_draw(ctx, k, show_types=show_types, hl_edges=hl)
        cur = stack[-1] if stack else (last["v"] if last and last["kind"] == "finish" else "A")
        ada(ctx, cur)
        if k == 0:
            ball(ctx)
        if hl:
            x0, y0 = POS[last["u"]]
            x1, y1 = POS[last["v"]]
            tag(cv, (x0 + x1) / 2, (y0 + y1) / 2 - 40, f"{last['etype']} edge", TYPE_COL[last["etype"]], size=26)
        legend(ctx)
        bars_panel(ctx, k)
        finish(ctx)
    return scene


def ev_cues(spec):
    out = []
    for anchor, first, count, per, off in spec:
        for j in range(count):
            out.append((f"e{first + j}", anchor, off + per * j))
    return out


# ---------------------------------------------------------------- A: story, clock, states
def scene_hook(ctx):
    stage(ctx)
    cv = ctx.cv
    r, d = ctx.pulse("rooms", 1.4), ctx.pulse("doors", 1.4)
    es = {GV.key(u, w): (mix(LINE, ACCENT, d), 6 + 3 * d, 1.0) for u, w, _ in GV.edges}
    GV.draw(ctx, rings={v: (BLUE, r) for v in POS}, estyle=es)
    ada(ctx, "A")
    ball(ctx)
    legend(ctx, a=0.0)
    panel_card(ctx, "THE MAZE")
    cv.text(1330, 190, "7 rooms", 46, INK, True)
    cv.text(1330, 260, "12 one-way doors", 46, INK, True)
    draw_wrapped(cv, 1330, 340, "Ada starts in room A, with a ball of thread.", 32, 500, MUTED, False)
    a = ctx.p("thread", 0.5)
    cv.rrect(1316, 480, 1854, 700, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=a)
    cv.text(1344, 504, "depth-first search", 30, ACCENT_DARK, True, a=a)
    draw_wrapped(cv, 1344, 556, "is that thread: always a way back to where it started", 30, 480, INK, False, a=a)
    finish(ctx)


def scene_clock(ctx):
    stage(ctx)
    cv = ctx.cv
    en, lv = ctx.p("enter", 0.5), ctx.p("leave", 0.5)
    GV.draw(ctx, marked={"A": lv}, fills={"A": (BLUE, 0.28 * en * (1 - lv))}, rings={"A": (BLUE, en)})
    if en > 0:
        badge_num(cv, POS["A"][0] - 36, POS["A"][1] - 40, 1, BLUE, a=en)
    if lv > 0:
        badge_num(cv, POS["A"][0] + 36, POS["A"][1] - 40, 14, ACCENT_DARK, a=lv)
    ada(ctx, "A")
    legend(ctx, a=0.0)
    panel_card(ctx, "TWO STAMPS PER ROOM")
    cv.rrect(1316, 180, 1854, 420, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=en)
    cv.text(1344, 204, "first time in", 30, BLUE, True, a=en)
    cv.text(1344, 256, "starting time", 40, INK, True, a=en)
    cv.text(1344, 316, "preorder number", 30, MUTED, False, a=en)
    cv.text(1344, 360, "clock + 1, then write it", 26, MUTED, False, a=en)
    cv.rrect(1316, 450, 1854, 690, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=lv)
    cv.text(1344, 474, "leaving for good", 30, ACCENT_DARK, True, a=lv)
    cv.text(1344, 526, "finishing time", 40, INK, True, a=lv)
    cv.text(1344, 586, "postorder number", 30, MUTED, False, a=lv)
    cv.text(1344, 630, "clock + 1, then write it", 26, MUTED, False, a=lv)
    finish(ctx)


def scene_states(ctx):
    stage(ctx)
    cv = ctx.cv
    k = 10  # after finish D: E, D finished; A, B active; C, F, G new
    state, pre, post, stack, last, clock = maze_draw(ctx, k, show_types=False)
    ada(ctx, stack[-1])
    legend(ctx, a=0.0)
    cv.text(1070, 880, "", 20, INK)
    panel_card(ctx, "THREE STATES")
    rows = [("n", "new", "Ada has never entered it", WHITE, INK), ("a", "active", "entered, not yet left for good", BLUE_SOFT, BLUE),
            ("f", "finished", "left for good", ACCENT, ACCENT_DARK)]
    y = 180
    for cue, name, body, fill, col in rows:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 150, 20, fill=PAPER, outline=col, width=4, a=a)
        cv.circle(1372, y + 75, 32, fill=fill, outline=col, width=5, a=a)
        cv.text(1426, y + 28, name, 38, col, True, a=a)
        draw_wrapped(cv, 1426, y + 80, body, 26, 400, INK, False, a=a)
        y += 170
    p = ctx.p("path", 0.5)
    cv.rrect(1316, 700, 1854, 880, 20, fill=(252, 244, 220), outline=GOLD, width=4, a=p)
    draw_wrapped(cv, 1344, 722, "the active rooms always form one path: the thread", 31, 480, (130, 90, 10), True, a=p)
    tag(cv, 300, 880, "the thread: A → B", GOLD, a=p, size=26)
    finish(ctx)


# ---------------------------------------------------------------- B: orders and intervals
def scene_orders(ctx):
    stage(ctx)
    cv = ctx.cv
    k = len(M.EVENTS)
    maze_draw(ctx, k, show_types=False, thread=False)
    legend(ctx, a=0.0)
    panel_card(ctx, "TWO ORDERINGS")
    a1, a2 = ctx.p("pre", 0.5), ctx.p("post", 0.5)
    cv.text(1330, 190, "by starting time", 28, BLUE, True, a=a1)
    for i, v in enumerate(M.RES["pre_order"]):
        x = 1330 + i * 70
        cv.rrect(x, 232, x + 60, 280, 24, fill=BLUE_SOFT, outline=BLUE, width=3, a=a1)
        cv.text(x + 30, 256, v, 30, INK, True, anchor="mm", a=a1)
    cv.text(1330, 330, "a preorder", 36, BLUE, True, a=a1)
    cv.text(1330, 450, "by finishing time", 28, ACCENT_DARK, True, a=a2)
    for i, v in enumerate(M.RES["post_order"]):
        x = 1330 + i * 70
        cv.rrect(x, 492, x + 60, 540, 24, fill=ACCENT_SOFT, outline=ACCENT, width=3, a=a2)
        cv.text(x + 30, 516, v, 30, INK, True, anchor="mm", a=a2)
    cv.text(1330, 590, "a postorder", 36, ACCENT_DARK, True, a=a2)
    a3 = ctx.p("diff", 0.5)
    draw_wrapped(cv, 1330, 700, "A different order of doors, or a different start, gives different ones.", 30, 500, MUTED, False, a=a3)
    finish(ctx)


def scene_intervals(ctx):
    stage(ctx)
    cv = ctx.cv
    k = len(M.EVENTS)
    c1, c2 = ctx.p("nest", 0.5), ctx.p("apart", 0.5)
    hl = []
    if c1 > 0.5:
        hl = ["B", "D", "E"]
    if c2 > 0.5:
        hl = ["B", "C"]
    es = {}
    for v, p in M.RES["parent"].items():
        es[GV.key(p, v)] = (INK, 9, 1.0)
    fills = {v: (RED, 0.35) for v in hl}
    GV.draw(ctx, estyle=es, fills=fills, marked={v: 1.0 for v in POS if v not in hl})
    legend(ctx, a=0.0)
    bars_panel(ctx, k, hl=set(hl), show_lists=False, title="BARS (Figure 6.4 style)")
    cv.text(1330, 560, "any two bars:", 28, MUTED, True, a=c1)
    cv.text(1330, 604, "nested", 44, RED, True, a=c1)
    cv.text(1330, 664, "or completely apart", 44, BLUE, True, a=c2)
    anc = ctx.p("anc", 0.5)
    draw_wrapped(cv, 1330, 740, "B's bar contains D's and E's: B is their ancestor in the thread tree.", 28, 500, INK, False, a=anc)
    finish(ctx)


def scene_lemma(ctx):
    stage(ctx)
    cv = ctx.cv
    k = len(M.EVENTS)
    es = {GV.key(p, v): (INK, 9, 1.0) for v, p in M.RES["parent"].items()}
    hl = ctx.p("l1", 0.4)
    GV.draw(ctx, estyle=es, fills={"B": (BLUE, 0.35), "E": (RED, 0.35)}, marked={v: 1.0 for v in POS if v not in ("B", "E")})
    tag(cv, POS["B"][0], POS[ "B"][1] - 80, "u = B", BLUE, size=26)
    tag(cv, POS["E"][0], POS["E"][1] - 80, "v = E", RED, size=26)
    legend(ctx, a=0.0)
    panel_card(ctx, "LEMMA 6.1  (PDF p.248)")
    rows = [("l1", "1", "u is an ancestor of v", "in the thread tree"),
            ("l2", "2", "u's bar contains v's", "u.pre ≤ v.pre < v.post ≤ u.post"),
            ("l3", "3", "u is active when v starts", "B is on the thread when E starts"),
            ("l4", "4", "a path of all-new rooms", "B → D → E, before B starts")]
    y = 176
    for cue, n, head, sub in rows:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 150, 18, fill=PAPER, outline=ACCENT, width=3, a=a)
        cv.circle(1362, y + 46, 24, fill=ACCENT, a=a)
        cv.text(1362, y + 45, n, 28, WHITE, True, anchor="mm", a=a)
        cv.text(1404, y + 22, head, 28, ACCENT_DARK, True, a=a)
        draw_wrapped(cv, 1404, y + 70, sub, 24, 430, MUTED, False, a=a)
        y += 166
    cv.text(1330, 850, "all four say the same thing", 30, BLUE, True, a=ctx.p("same", 0.5))
    finish(ctx)


# ---------------------------------------------------------------- C: four edge types
def scene_types_intro(ctx):
    stage(ctx)
    cv = ctx.cv
    k = len(M.EVENTS)
    maze_draw(ctx, k, show_types=True, thread=False, decorate=False)
    legend(ctx)
    panel_card(ctx, "WHEN ADA TRIES A DOOR  u → v")
    rows = [("t1", "tree", "v is new", TYPE_COL["tree"]), ("t2", "back", "v is active", TYPE_COL["back"]),
            ("t3", "forward", "v is finished, below u", TYPE_COL["forward"]), ("t4", "cross", "v is finished, elsewhere", TYPE_COL["cross"])]
    y = 176
    for cue, name, body, col in rows:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 150, 20, fill=PAPER, outline=col, width=5, a=a)
        cv.text(1344, y + 24, name, 40, col, True, a=a)
        cv.text(1344, y + 88, body, 30, INK, False, a=a)
        y += 170
    finish(ctx)


def edge_scene(kind, cue_edges, explain, ex_edge, extra=None):
    def scene(ctx):
        stage(ctx)
        cv = ctx.cv
        k = len(M.EVENTS)
        a = ctx.p("go", 0.5)
        hl = [(u, w, TYPE_COL[kind]) for (u, w) in cue_edges] if a > 0.2 else None
        maze_draw(ctx, k, show_types=True, hl_edges=hl, thread=False, decorate=False)
        legend(ctx)
        panel_card(ctx, f"{kind.upper()} EDGES")
        cv.text(1330, 190, f"{ex_edge[0]} → {ex_edge[1]}", 64, TYPE_COL[kind], True, a=a)
        draw_wrapped(cv, 1330, 290, explain, 31, 500, INK, False, a=a)
        if extra:
            extra(ctx)
        finish(ctx)
    return scene


def interval_schema(ctx, kind, y0, a=1.0):
    """Tiny bars for u and v showing how their intervals relate (Figure 6.5)."""
    cv = ctx.cv
    spec = {"tree": ((1, 10), (3, 7)), "forward": ((1, 10), (3, 7)), "back": ((3, 7), (1, 10)),
            "cross": ((6, 10), (1, 4))}
    (u0, u1), (v0, v1) = spec[kind]
    x0, per = 1340, 44
    for i, (lab, (s, e), col) in enumerate((("u", (u0, u1), BLUE), ("v", (v0, v1), ACCENT))):
        y = y0 + i * 52
        cv.text(x0 - 6, y + 20, lab, 26, INK, True, anchor="rm", a=a)
        cv.rrect(x0 + 10 + (s - 1) * per, y, x0 + 10 + e * per, y + 40, 10, fill=col, a=a)
    return


def scene_back(ctx):
    base = edge_scene("back", [("E", "B"), ("F", "C")], "v is active: already on the thread. The door loops back up the thread.", ("E", "B"))

    def scene(ctx):
        base(ctx)
    return scene


def scene_impossible(ctx):
    stage(ctx)
    cv = ctx.cv
    maze_draw(ctx, len(M.EVENTS), show_types=True, thread=False, decorate=False)
    legend(ctx)
    panel_card(ctx, "WHAT THE INTERVALS LOOK LIKE")
    rows = [("tree", "u contains v"), ("forward", "u contains v"), ("back", "v contains u"), ("cross", "v is entirely before u")]
    y = 170
    for i, (kind, text) in enumerate(rows):
        a = ctx.p(f"s{i + 1}", 0.45)
        cv.text(1330, y, kind, 28, TYPE_COL[kind], True, a=a)
        cv.text(1850, y, text, 24, MUTED, True, anchor="ra", a=a)
        interval_schema(ctx, kind, y + 36, a=a)
        y += 168
    n = ctx.p("none", 0.5)
    cv.rrect(40, 800, 1246, 906, 22, fill=(253, 246, 232), outline=ORANGE, width=3, a=n)
    draw_wrapped(cv, 70, 820, "A fifth kind, v starting after u has finished, is impossible: Ada tries every door out of u before she leaves it.",
                 28, 1140, INK, True, a=n)
    finish(ctx)


# ---------------------------------------------------------------- D: cycles
def scene_cycle(ctx):
    stage(ctx)
    cv = ctx.cv
    a = ctx.p("loop", 0.5)
    b = ctx.p("fin", 0.5)
    hl = []
    if a > 0.2:
        hl = [("B", "D", RED), ("D", "E", RED), ("E", "B", RED)]
    maze_draw(ctx, len(M.EVENTS), show_types=True, hl_edges=hl, thread=False, decorate=False)
    legend(ctx)
    panel_card(ctx, "A BACK EDGE MEANS A CYCLE")
    cv.text(1330, 190, "B → D → E → B", 54, RED, True, a=a)
    draw_wrapped(cv, 1330, 280, "E → B leads to an active room: the thread loops back on itself.", 30, 500, INK, False, a=a)
    draw_wrapped(cv, 1330, 470, "Doors to finished rooms never prove a cycle.", 32, 500, GREEN, True, a=b)
    finish(ctx)


def scene_finish_times(ctx):
    stage(ctx)
    cv = ctx.cv
    k = len(M.EVENTS)
    maze_draw(ctx, k, show_types=True, thread=False, decorate=True)
    legend(ctx)
    panel_card(ctx, "COMPARE FINISHING TIMES")
    y = 190
    edges = [(u, w) for u, ws in M.MAZE.items() for w in ws]
    shown = ctx.p("tab", 0.5)
    for i, (u, w) in enumerate(edges):
        back = M.POST[u] < M.POST[w]
        if back:
            cv.rrect(1318, y - 4, 1850, y + 36, 8, fill=(253, 232, 232), outline=RED, width=2, a=shown)
        cv.text(1334, y, f"{u} → {w}", 26, INK, True, True, a=shown)
        cv.text(1560, y, f"post {M.POST[u]:>2} {'<' if back else '>'} {M.POST[w]:>2}", 26, RED if back else MUTED, True, True, a=shown)
        y += 40
    f = ctx.p("rule", 0.5)
    draw_wrapped(cv, 1330, 700, "If an edge u → v has u.post < v.post, there is a cycle. In a DAG, every edge has u.post > v.post.", 28, 500,
                 RED, True, a=f)
    finish(ctx)


# ---------------------------------------------------------------- code
CODE = [
    "def is_acyclic(graph):",
    "    status = {}",
    "    for v in graph:",
    '        status[v] = "new"',
    "",
    "    def visit(v):",
    '        status[v] = "active"',
    "        for w in graph[v]:",
    '            if status[w] == "active":',
    "                return False",
    '            if status[w] == "new":',
    "                if visit(w) == False:",
    "                    return False",
    '        status[v] = "finished"',
    "        return True",
    "",
    "    for v in graph:",
    '        if status[v] == "new":',
    "            if visit(v) == False:",
    "                return False",
    "    return True",
]
CARD = CodeCard(CODE, size=25, lh=33, y_off=30, x_off=96)


def code_scene(boxes=(), hl=(), notes=(), title="notes", maze=False):
    def scene(ctx):
        CARD.draw(ctx, hl=hl, boxes=boxes, title="THE BOOK'S IsAcyclic, IN PYTHON")
        notes_panel(ctx, title, list(notes))
        finish(ctx)
    return scene


def scene_run_cycle(ctx):
    stage(ctx)
    cv = ctx.cv
    t0 = ctx.cue("go") or 0.0
    steps = [("A", "new"), ("B", "new"), ("D", "new"), ("E", "new")]
    k = int(clamp((ctx.t - t0) / 1.0, 0, 9)) if ctx.cue("go") else 0
    ctx.sig.append(k)
    path = ["A", "B", "D", "E"][:max(0, min(k, 4))]
    found = k >= 6
    hl = [("E", "B", RED)] if found else None
    stackv = path
    for u, w in zip(path, path[1:]):
        cv.poly_line(GV.pts(u, w), GOLD, 11, a=0.9)
    fills = {v: (BLUE, 0.28) for v in path}
    GV.draw(ctx, fills=fills, rings={v: (BLUE, 1.0) for v in path}, estyle={GV.key("E", "B"): (RED, 14, 1.0)} if found else None)
    if path:
        ada(ctx, path[-1])
    legend(ctx, a=0.0)
    panel_card(ctx, "RUNNING is_acyclic ON THE MAZE")
    lines = ["visit(A):  status A = active", "visit(B):  status B = active", "visit(D):  status D = active",
             "visit(E):  status E = active", "door E → B:  status B is active", "return False"]
    y = 190
    for i, ln in enumerate(lines):
        a = clamp(k - i + 0.0)
        if i == 4:
            a = clamp(k - 4)
        if i == 5:
            a = clamp(k - 5)
        col = RED if i >= 4 else INK
        cv.text(1330, y, ln, 24, col, True, True, a=min(1.0, max(0.0, a)))
        y += 56
    if found:
        cv.rrect(1316, 600, 1854, 760, 20, fill=(253, 232, 232), outline=RED, width=4)
        cv.text(1585, 680, "False: there is a cycle", 40, RED, True, anchor="mm")
    finish(ctx)


def scene_dag(ctx):
    stage(ctx)
    cv = ctx.cv
    rm = ctx.p("rm", 0.6)
    es = {}
    for (u, w), et in M.ETYPE.items():
        if et == "back":
            es[GV.key(u, w)] = (RED, 8, 1.0 - 0.85 * rm)
        else:
            es[GV.key(u, w)] = (INK if et == "tree" else LINE, 7, 1.0)
    GV.draw(ctx, estyle=es)
    legend(ctx, a=0.0)
    src, snk = ctx.p("src", 0.5), ctx.p("snk", 0.5)
    tag(cv, POS["A"][0], POS["A"][1] + 76, "source", GREEN, a=src, size=26)
    tag(cv, POS["E"][0], POS["E"][1] - 76, "sink", PURPLE, a=snk, size=26)
    panel_card(ctx, "WITHOUT THE BACK EDGES")
    cv.text(1330, 190, "10 doors left", 40, INK, True, a=rm)
    cv.text(1330, 260, "is_acyclic  →  True", 40, GREEN, True, a=ctx.p("true", 0.5))
    cv.rrect(1316, 380, 1854, 520, 18, fill=PAPER, outline=GREEN, width=4, a=src)
    cv.text(1344, 400, "source", 34, GREEN, True, a=src)
    cv.text(1344, 452, "no doors in:  A", 28, INK, False, a=src)
    cv.rrect(1316, 550, 1854, 690, 18, fill=PAPER, outline=PURPLE, width=4, a=snk)
    cv.text(1344, 570, "sink", 34, PURPLE, True, a=snk)
    cv.text(1344, 622, "no doors out:  E", 28, INK, False, a=snk)
    draw_wrapped(cv, 1330, 740, "Every DAG has at least one source and one sink. (PDF p.249)", 28, 500, MUTED, False, a=ctx.p("every", 0.5))
    finish(ctx)


def scene_dfsall(ctx):
    stage(ctx)
    cv = ctx.cv
    res1 = dfs(M.MAZE, roots=["A"])
    res2 = dfs(M.MAZE, roots=["G", "A"] + [v for v in M.MAZE if v not in ("G", "A")])
    a1, a2 = ctx.p("one", 0.5), ctx.p("two", 0.5)
    which = res2 if a2 > 0.5 else res1
    cols = {}
    roots = [v for v in M.MAZE if v not in which["parent"]]
    palette = [ACCENT, BLUE, GREEN]
    root_of = {}
    for v in which["pre_order"]:
        root_of[v] = v if v not in which["parent"] else root_of[which["parent"][v]]
    ordered = []
    for v in which["pre_order"]:
        if root_of[v] == v:
            ordered.append(v)
    fills = {v: (palette[ordered.index(root_of[v]) % 3], 1.0) for v in M.MAZE}
    es = {GV.key(p, v): (palette[ordered.index(root_of[v]) % 3], 10, 1.0) for v, p in which["parent"].items()}
    GV.draw(ctx, fills=fills, estyle=es)
    legend(ctx, a=0.0)
    n_trees = len(roots)
    panel_card(ctx, "DFSAll: START EVERYWHERE")
    cv.text(1330, 190, "start order:", 28, MUTED, True)
    cv.text(1330, 238, "A first" if a2 < 0.5 else "G first, then A", 40, INK, True)
    cv.text(1330, 330, "separate trees:", 28, MUTED, True)
    cv.text(1330, 380, str(n_trees), 130, ACCENT, True)
    draw_wrapped(cv, 1330, 560, "In a directed graph, even a 'connected' one, the count can be anything from 1 to V.", 28, 500, INK, False,
                 a=ctx.p("any", 0.5))
    cv.text(1330, 760, "PDF p.245", 26, BLUE, True, a=ctx.p("any", 0.5))
    finish(ctx)


def scene_recap(ctx):
    stage(ctx)
    cv = ctx.cv
    cards = [("c1", "Two stamps per room", "start time and finish time, from one clock"),
             ("c2", "Three states", "new, active, finished: the active rooms are the thread"),
             ("c3", "Four edge types", "tree, forward, back, cross"),
             ("c4", "A back edge means a cycle", "an edge to an active room")]
    y = 150
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(150, y + 75, 34, fill=ACCENT, a=a)
        cv.text(150, y + 74, str(i + 1), 38, WHITE, True, anchor="mm", a=a)
        cv.text(215, y + 22, head, 40, ACCENT_DARK, True, a=a)
        cv.text(215, y + 86, sub, 28, INK, False, a=a)
        y += 174
    cv.text(630, 868, "Next: topological sort and dynamic programming, sections 6.3 and 6.4", 28, BLUE, True, anchor="mm",
            a=ctx.p("next", 0.5))
    finish(ctx)
