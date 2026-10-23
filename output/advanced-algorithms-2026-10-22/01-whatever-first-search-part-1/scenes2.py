"""Scenes for beats from Part 2 onward (token pile, rules, trace, parents, why, code, recap)."""
from __future__ import annotations

import math

import trace_check
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, EDGES, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED,
    PANEL_LINE, PAPER, POS, R_VERT, RED, WHITE, YELLOW, clamp, edge_pts, ease, lerp, mix, point_along,
)
from scenes import finish, soil, sprite_at, walker
from widgets import (
    PANEL, draw_graph, draw_wrapped, ekey, glossary, panel_card, rules_panel, tag, token_pill, wrap, wrinkles,
)

ALLKNOWN = ("vertex", "edge", "graph", "reachability", "mark")
ORANGE = (234, 140, 36)

LOG: list = []
trace_check.whatever_first_search(trace_check.graph, "S", show=False, log=LOG)
MARK_ORDER = [s["current"] for s in LOG if s["new"]]
PARENT = LOG[-1]["parent_after"]


def tk(p):
    return f"({p[0] if p[0] else 'nobody'}, {p[1]})"


def mid(u, v, f=0.5):
    return point_along(edge_pts(u, v), f)


def mini_pill(ctx, u, v, label, a=1.0, hi=True, strike=False, w=128, f=0.5, dy=0):
    x, y = mid(u, v, f)
    token_pill(ctx.cv, x - w / 2, y - 15 + dy, label, a, hi, strike, w)


def edge_hl(src, color=BLUE, width=10, a=1.0):
    return {ekey(*k): (color, width, a) for k in src}


# ==================================================================== PART 2
def scene_three(ctx):
    soil(ctx)
    th = ctx.p("three", 0.5)
    es = {ekey("S", x): (mix(LINE, BLUE, th), 6 + 4 * th, 1.0) for x in "ABC"}
    draw_graph(ctx, marked={"S": 1.0}, estyle=es)
    sprite_at(ctx, *POS["S"], scale=1.15)
    glossary(ctx, known=ALLKNOWN, new={})
    finish(ctx)


def big_pile(ctx, items, title="TOKEN PILE", note=None, note_cue=None):
    """items: [(label, cue or None)] in insertion order; newest drawn on top."""
    cv = ctx.cv
    panel_card(ctx, title)
    cv.text(1316, 170, "newest on top", 22, MUTED, True)
    y = 222
    for label, cue in reversed(items):
        a = ctx.p(cue, 0.4) if cue else 1.0
        if a > 0:
            slide = (1 - a) * -30
            token_pill(cv, 1330, y + slide, label, a, hi=(label == items[-1][0]), w=330, h=56, fs=34)
        y += 72
    if note:
        a = ctx.p(note_cue, 0.5) if note_cue else 1.0
        draw_wrapped(cv, 1330, 700, note, 28, 500, MUTED, False, a=a)


def scene_tokens(ctx):
    soil(ctx)
    t = [ctx.p("t1", 0.4), ctx.p("t2", 0.4), ctx.p("t3", 0.4)]
    es = {}
    for x, a in zip("ABC", t):
        es[ekey("S", x)] = (mix(LINE, ACCENT, a), 6 + 5 * a, 1.0)
    draw_graph(ctx, marked={"S": 1.0}, estyle=es)
    for x, a in zip("ABC", t):
        if a > 0:
            mini_pill(ctx, "S", x, f"(S, {x})", a, f=0.55)
    sprite_at(ctx, *POS["S"], scale=1.15)
    big_pile(ctx, [("(S, A)", "t1"), ("(S, B)", "t2"), ("(S, C)", "t3")],
             note="Mole-rats can't really read, so just pretend.", note_cue="ro")
    finish(ctx)


def scene_bag(ctx):
    soil(ctx)
    es = {ekey("S", x): (ACCENT, 11, 1.0) for x in "ABC"}
    draw_graph(ctx, marked={"S": 1.0}, estyle=es)
    for x in "ABC":
        mini_pill(ctx, "S", x, f"(S, {x})", 1.0, f=0.55)
    sprite_at(ctx, *POS["S"], scale=1.15)
    big_pile(ctx, [("(S, A)", None), ("(S, B)", None), ("(S, C)", None)])
    a = ctx.p("bag", 0.5)
    cv = ctx.cv
    if a > 0:
        cv.rrect(1330, 480, 1850, 640, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=a)
        cv.text(1360, 500, "the book calls this pile a", 28, INK, False, a=a)
        cv.text(1360, 542, "bag", 60, BLUE, True, a=a)
    finish(ctx)


def scene_pair(ctx):
    soil(ctx)
    cv = ctx.cv
    fa, ta = ctx.p("from", 0.4), ctx.p("to", 0.4)
    es = {ekey("S", "A"): (BLUE, 11, 1.0)}
    draw_graph(ctx, marked={"S": 1.0}, estyle=es, rings={"S": (BLUE, fa), "A": (BLUE, ta)})
    ax, ay = POS["S"]
    bx, by = POS["A"]
    cv.arrow((ax + 28, ay - 34), (bx - 30, by + 30), BLUE, 6, a=0.9, head=22)
    sprite_at(ctx, *POS["S"], scale=1.15)
    tag(cv, ax, ay + 78, "from", BLUE, a=max(fa, 0.0))
    tag(cv, bx + 70, by - 44, "to", BLUE, a=max(ta, 0.0))
    panel_card(ctx, "ONE TOKEN IS A PAIR")
    pa = ctx.p("pair", 0.4)
    labels = [("came_from", "S", fa, 1330), ("current", "A", ta, 1610)]
    for name, val, a, x0 in labels:
        lit = a > 0.5
        cv.text(x0 + 120, 190, name, 30, ACCENT_DARK if lit else MUTED, True, True, anchor="ma")
        cv.rrect(x0, 240, x0 + 240, 400, 24, fill=ACCENT_SOFT if lit else WHITE,
                 outline=ACCENT if lit else GRAY, width=5)
        cv.text(x0 + 120, 320, val, 96, INK, True, anchor="mm")
    cv.text(1585, 330, ",", 90, INK, True, anchor="mm")
    draw_wrapped(cv, 1330, 450, "the vertex she came from, and the vertex the tunnel leads to", 30, 500, INK, False)
    draw_wrapped(cv, 1330, 560, "Why keep both? You'll see in a few minutes.", 28, 500, MUTED, False)
    finish(ctx)


def rule_scene(n):
    def scene(ctx):
        soil(ctx)
        cv = ctx.cv
        cue = f"r{n + 1}"
        rules_panel(ctx, n, cue, prior=tuple(range(n)))
        if n == 0:
            a = ctx.p(cue, 0.5)
            draw_graph(ctx, rings={"S": (BLUE, a)})
            sprite_at(ctx, *POS["S"], scale=1.15)
            token_pill(cv, 205, 592, "(nobody, S)", a, True, False, 190, 34, 24)
        elif n == 1:
            a = ctx.p(cue, 0.6)
            draw_graph(ctx, marked={})
            cv.text(70, 818, "TOKEN PILE  (oldest left, newest right)", 22, MUTED, True)
            labels = ["(S, A)", "(S, B)", "(S, C)"]
            for i, lb in enumerate(labels):
                top = i == 2
                token_pill(cv, 70 + i * 170 + (a * 90 if top else 0), 858, lb, 1.0, top, False, 150, 38, 26)
            cv.text(790, 877, "take one out", 32, ACCENT_DARK, True, anchor="lm", a=a)
            sprite_at(ctx, *POS["S"], scale=1.15)
        elif n == 2:
            mk = ctx.p("mk", 0.5)
            par = ctx.p("par", 0.5)
            ev = ctx.p("ev", 0.5)
            es = {ekey("S", x): (mix(LINE, ACCENT, ev), 6 + 4 * ev, 1.0) for x in "ABC"}
            draw_graph(ctx, marked={"S": mk}, estyle=es, rings={"S": (BLUE, 1.0)})
            sprite_at(ctx, *POS["S"], scale=1.15)
            token_pill(cv, 205, 592, "(nobody, S)", 1.0, True, False, 190, 34, 24)
            tag(cv, POS["S"][0] - 60, POS["S"][1] + 128, "parent: nobody", ACCENT_DARK, a=par, size=24)
            tev = ctx.cue("ev")
            for i, x in enumerate("ABC"):
                a = ctx.ramp(tev + 0.18 * i, tev + 0.18 * i + 0.3) if tev is not None else 0.0
                if a > 0:
                    mini_pill(ctx, "S", x, f"(S, {x})", a, f=0.55)
        else:
            tp = ctx.p("r4", 0.5)
            thr = ctx.p("throw", 0.4)
            draw_graph(ctx, marked={"S": 1.0}, rings={"S": (BLUE, 1.0)},
                       estyle={ekey("C", "S"): (BLUE, 10, 1.0)})
            sprite_at(ctx, *POS["C"], scale=1.0)
            mini_pill(ctx, "C", "S", "(C, S)", tp, True, thr > 0.5, f=0.62, dy=-34)
            tag(cv, POS["S"][0] - 20, POS["S"][1] - 112, "already marked!", RED, a=tp, size=24)
        finish(ctx)
    return scene


def scene_translate(ctx):
    soil(ctx)
    cv = ctx.cv
    draw_graph(ctx, marked={"S": 1.0})
    cv.rrect(30, 112, 1258, 916, 28, fill=WHITE, a=0.88)
    rules_panel(ctx, 3, None, prior=(0, 1, 2, 3), all_dim=True)
    cv.rrect(180, 170, 1100, 880, 30, fill=WHITE, outline=ACCENT, width=4)
    cv.text(640, 200, "THE BOOK'S LETTERS, IN OUR WORDS", 30, ACCENT_DARK, True, anchor="ma")
    rows = [("s", "start", "the vertex we begin from", "t_s"),
            ("bag", "the token pile", "to_visit in the code", "t_bag"),
            ("p", "came_from", "the vertex that sent the token", "t_p"),
            ("v", "current", "the vertex the token leads to", "t_v"),
            ("w", "neighbor", "a vertex joined to current by an edge", "t_w")]
    y = 330
    for letter, ours, gloss, cue in rows:
        a = ctx.p(cue, 0.4)
        cv.text(260, y, letter, 56, BLUE, True, True, anchor="lm", a=a)
        cv.text(380, y, "=", 48, MUTED, True, anchor="lm", a=a)
        cv.text(450, y - 22, ours, 40, INK, True, anchor="lm", a=a)
        cv.text(450, y + 22, gloss, 26, MUTED, False, anchor="lm", a=a)
        y += 112
    finish(ctx)


# ==================================================================== PART 3
def scene_map(ctx):
    soil(ctx)
    cv = ctx.cv
    draw_graph(ctx, marked={})
    ca = ctx.p("v7", 0.4)
    ea = ctx.p("e12", 0.4)
    cv.rrect(60, 130, 470, 186, 18, fill=WHITE, outline=PANEL_LINE, width=3)
    cv.text(84, 142, "7 vertices", 30, INK, True, a=max(ca, 0.25))
    cv.text(284, 142, "12 edges", 30, INK, True, a=max(ea, 0.25))
    panel_card(ctx, "EACH VERTEX'S NEIGHBOR LIST")
    last = ctx.p("last", 0.5)
    lists = {"S": ["A", "B", "C"], "A": ["B", "C", "D", "S"], "B": ["A", "C", "E", "S"],
             "C": ["A", "B", "F", "S"], "D": ["A", "E", "F"], "E": ["B", "D", "F"], "F": ["C", "D", "E"]}
    y = 196
    for v, ns in lists.items():
        cv.text(1330, y, f"{v}:", 40, INK, True, True)
        x = 1400
        for i, n in enumerate(ns):
            hi = (i == len(ns) - 1) and last > 0
            if hi:
                cv.rrect(x - 6, y - 2, x + 50, y + 50, 12, fill=ACCENT_SOFT, outline=ACCENT, width=3, a=last)
            cv.text(x + 22, y + 24, n, 36, ACCENT_DARK if hi else INK, True, True, anchor="mm")
            x += 70
        y += 66
    cv.text(1330, y + 2, "X: Y     Y: X", 30, MUTED, True, True)
    cv.text(1330, y + 40, "(the cut-off burrow)", 22, MUTED, False)
    sprite_at(ctx, *POS["S"], scale=1.15)
    finish(ctx)


def trace_panel(ctx, take, pile, palpha, marked, stale):
    cv = ctx.cv
    panel_card(ctx, None)
    # take card
    cv.rrect(1316, 138, 1854, 268, 20, fill=PAPER, outline=PANEL_LINE, width=3)
    cv.text(1338, 148, "TAKE THE NEWEST TOKEN", 20, MUTED, True)
    if take is None:
        cv.text(1338, 190, "—", 40, GRAY, True, True)
    else:
        s, a_do = take
        cv.text(1338, 174, tk((s["came_from"], s["current"])), 40, INK, True, True)
        if a_do > 0:
            if s["new"]:
                parent = s["came_from"] if s["came_from"] else "nobody"
                msg, col = f"{s['current']} is new: mark {s['current']}, parent {parent}", ACCENT_DARK
            else:
                msg, col = f"{s['current']} is already marked: throw it away", RED
            cv.text(1338, 226, msg, 25, col, True, a=a_do)
    # pile
    cv.text(1330, 282, "TOKEN PILE", 20, MUTED, True)
    cv.text(1850, 282, "newest on top", 20, MUTED, False, anchor="ra")
    y = 310
    shown = [(tok, a) for tok, a in zip(pile, palpha) if a > 0]
    if not shown:
        cv.text(1330, y + 4, "(empty)", 26, GRAY, True, True)
    for rank, (tok, a) in enumerate(reversed(shown)):
        is_stale = stale and tok in (("S", "A"), ("S", "B"))
        token_pill(cv, 1330, y, tk(tok), a, hi=(rank == 0 and not stale) or is_stale, w=240)
        if is_stale:
            cv.text(1584, y + 15, "stale", 22, ORANGE, True, anchor="lm", a=a)
        y += 33
    # marked row
    cv.text(1330, 676, "MARKED", 20, MUTED, True)
    for i, v in enumerate("SABCDEF"):
        cx = 1356 + i * 70
        mf = marked.get(v, 0.0)
        cv.circle(cx, 736, 27, fill=mix(WHITE, ACCENT, mf), outline=mix(GRAY, ACCENT_DARK, mf), width=4)
        cv.text(cx, 735, v, 28, mix(MUTED, WHITE, mf), True, anchor="mm")
    # parents
    cv.text(1330, 786, "PARENT OF", 20, MUTED, True)
    for i, v in enumerate(MARK_ORDER):
        if marked.get(v, 0.0) > 0.99:
            col, row = i % 4, i // 4
            par = PARENT[v] or "nobody"
            cv.text(1330 + col * 140, 820 + row * 40, f"{v} ← {par}", 22, INK, True, True)


def trace_scene(steps, idle_after=None, stale_cue=None, extra_sprite=None):
    def scene(ctx):
        cv = ctx.cv
        soil(ctx)
        multi = len(steps) > 1

        def cn(base, n):
            return f"{base}{n}" if multi else base

        if steps:
            first = steps[0]
            pile = list(LOG[first - 1]["pile_before"])
            marked_names = LOG[first - 2]["marked_after"] if first > 1 else []
            prev_new = None
            for s in LOG[:first - 1]:
                if s["new"]:
                    prev_new = s["current"]
        else:
            pile = list(LOG[idle_after - 1]["pile_after"])
            marked_names = LOG[idle_after - 1]["marked_after"]
            prev_new = marked_names[-1]
        palpha = [1.0] * len(pile)
        marked = {v: 1.0 for v in marked_names}
        rings, estyle, badges = {}, {}, {}
        take = None
        wps = [(0.0, prev_new or "S")]
        cur_v = prev_new or "S"
        for n in steps:
            s = LOG[n - 1]
            t_take = ctx.cues.get(cn("take", n))
            took = t_take is not None and ctx.t >= t_take
            ctx.sig.append(1 if took else 0)
            if not took:
                break
            pile.pop()
            palpha.pop()
            a_do = ctx.p(cn("do", n), 0.4)
            take = (s, a_do)
            rings, estyle, badges = {}, {}, {}
            rings[s["current"]] = (BLUE, 1.0)
            if s["came_from"]:
                estyle[ekey(s["came_from"], s["current"])] = (BLUE, 10, 1.0)
            if s["new"]:
                marked[s["current"]] = a_do
                if s["current"] != cur_v:
                    t0 = max(t_take, wps[-1][0])
                    wps.append((t0, cur_v))
                    wps.append((t0 + 0.7, s["current"]))
                    cur_v = s["current"]
            else:
                badges[s["current"]] = ("x", a_do)
            t_push = ctx.cues.get(cn("push", n))
            for k, tok in enumerate(s["added"]):
                a = 0.0 if t_push is None else ctx.ramp(t_push + 0.12 * k, t_push + 0.12 * k + 0.3)
                pile.append(tok)
                palpha.append(a)
        # a fully-taken beat: tokens added by earlier steps in this beat are already in `pile`
        draw_graph(ctx, marked=marked, rings=rings, estyle=estyle, badges=badges)
        x, y, flip, moving = walker(ctx, wps) if len(wps) > 1 else (*POS[wps[0][1]], False, False)
        sprite_at(ctx, x, y, flip=flip, scale=1.0)
        stale = bool(stale_cue) and ctx.reached(stale_cue)
        trace_panel(ctx, take, pile, palpha, marked, stale)
        finish(ctx)
    return scene


def scene_answer(ctx):
    soil(ctx)
    cv = ctx.cv
    xy = ctx.p("xy", 0.5)
    marked = {v: 1.0 for v in "SABCDEF"}
    draw_graph(ctx, marked=marked, badges={"X": ("x", xy), "Y": ("x", xy)})
    sprite_at(ctx, *POS["B"], scale=1.0)
    panel_card(ctx, "THE ANSWER")
    sv = ctx.ramp(0.3, 0.8)
    cv.text(1330, 184, "Reachable from S:", 28, MUTED, True, a=max(sv, 0.0))
    cv.text(1330, 228, "S  A  B  C  D  E  F", 50, ACCENT_DARK, True, True, a=sv)
    cv.text(1330, 304, "Not reachable:", 28, MUTED, True, a=xy)
    cv.text(1330, 348, "X  Y", 50, RED, True, True, a=xy)
    ca = ctx.p("count", 0.5)
    cv.text(1330, 450, "TOKENS TAKEN", 22, MUTED, True, a=ca)
    one, two = ctx.p("one", 0.4), ctx.p("two", 0.4)
    cv.text(1330, 490, "25", 90, INK, True, a=ca)
    cv.text(1470, 520, "=  1", 54, ACCENT_DARK, True, a=one)
    cv.text(1580, 520, "+  2 × 12", 54, BLUE, True, a=two)
    if ca > 0:
        w = 520
        cv.rrect(1330, 640, 1330 + w, 700, 12, fill=GRAY_SOFT, a=ca)
        cv.rrect(1330, 640, 1330 + w * 7 / 25, 700, 12, fill=ACCENT, a=ca)
        cv.text(1330 + w * 7 / 25 / 2, 670, "7 useful", 22, WHITE, True, anchor="mm", a=ca)
        cv.text(1330 + w * (7 + 18 / 2) / 25, 670, "18 thrown away", 22, MUTED, True, anchor="mm", a=ca)
    finish(ctx)


# ==================================================================== PART 4
PATH_ASK = [("B", "A", "b"), ("A", "D", "a"), ("D", "E", "d"), ("E", "F", "e"), ("F", "C", "f"), ("C", "S", "c")]


def scene_parents(ctx):
    soil(ctx)
    cv = ctx.cv
    marked = {v: 1.0 for v in "SABCDEF"}
    es, rings = {}, {}
    cur = None
    for u, v, cue in PATH_ASK:
        a = ctx.p(cue, 0.4)
        if a > 0:
            es[ekey(u, v)] = (BLUE, 11, 1.0)
            cur = (u, v)
    if cur:
        rings[cur[0]] = (BLUE, 1.0)
        if ctx.reached("back"):
            rings = {"S": (BLUE, 1.0)}
    draw_graph(ctx, marked=marked, estyle=es, rings=rings)
    sx, sy = POS[cur[0]] if cur else POS["B"]
    sprite_at(ctx, sx, sy, scale=1.0)
    panel_card(ctx, "WHO IS YOUR PARENT?")
    rows = ["B", "A", "D", "E", "F", "C", "S"]
    cues = {"B": "b", "A": "a", "D": "d", "E": "e", "F": "f", "C": "c", "S": "back"}
    y = 168
    for v in rows:
        lit = ctx.reached(cues[v])
        par = PARENT[v] or "nobody"
        cv.rrect(1316, y, 1854, y + 84, 16, fill=ACCENT_SOFT if lit else PAPER, outline=ACCENT if lit else PANEL_LINE,
                 width=3)
        cv.text(1360, y + 42, v, 52, INK, True, True, anchor="lm")
        cv.text(1470, y + 42, "←", 52, MUTED, True, anchor="lm")
        cv.text(1560, y + 42, par, 52 if par != "nobody" else 40, ACCENT_DARK if lit else GRAY, True, True, anchor="lm")
        y += 96
    finish(ctx)


def scene_tree(ctx):
    soil(ctx)
    cv = ctx.cv
    par = ctx.p("par", 0.6)
    tree_edges = {ekey(PARENT[v], v) for v in PARENT if PARENT[v]}
    es = {}
    for (a, b, _) in EDGES:
        k = ekey(a, b)
        if k in tree_edges:
            es[k] = (mix(LINE, ACCENT, par), 6 + 7 * par, 1.0)
        else:
            es[k] = (LINE, 6, 1.0 - 0.75 * par)
    draw_graph(ctx, marked={v: 1.0 for v in "SABCDEF"}, estyle=es)
    sprite_at(ctx, *POS["S"], scale=1.15)
    panel_card(ctx, "THE PARENT TREE")
    ta = ctx.p("tree", 0.6)
    y = 190
    for i, v in enumerate(MARK_ORDER):
        a = clamp(ta * 7 - i * 0.55) if i else ta
        a = ta if i == 0 else clamp(ta * 2 - i * 0.1)
        cv.circle(1500, y + 26, 30, fill=ACCENT, outline=ACCENT_DARK, width=4, a=a)
        cv.text(1500, y + 25, v, 32, WHITE, True, anchor="mm", a=a)
        if i + 1 < len(MARK_ORDER):
            cv.arrow((1500, y + 58), (1500, y + 92), ACCENT_DARK, 5, a=a, head=14)
        y += 90
    cv.text(1590, 330, "7 vertices", 30, INK, True, a=ta)
    cv.text(1590, 372, "6 parent edges", 30, ACCENT_DARK, True, a=ta)
    cv.text(1590, 440, "one long,", 26, MUTED, False, a=ta)
    cv.text(1590, 472, "skinny path", 26, MUTED, False, a=ta)
    finish(ctx)


# ==================================================================== PART 5
PROMISES = [
    ("It always stops.", "A vertex is marked only once, and only marked vertices add tokens."),
    ("It never marks an unreachable vertex.", "Every token is added by a marked vertex, along a real edge."),
    ("It marks every reachable vertex.", "Follow a shortest route and watch the dominoes fall."),
]


def promises_panel(ctx, lit):
    cv = ctx.cv
    panel_card(ctx, "THREE PROMISES")
    y = 168
    for i, (head, sub) in enumerate(PROMISES):
        on = i == lit
        cv.rrect(1316, y, 1854, y + 220, 22, fill=ACCENT_SOFT if on else WHITE, outline=ACCENT if on else PANEL_LINE,
                 width=4 if on else 3, a=1.0 if on else 0.5)
        cv.circle(1366, y + 50, 28, fill=ACCENT if on else GRAY, a=1.0 if on else 0.6)
        cv.text(1366, y + 49, str(i + 1), 32, WHITE, True, anchor="mm")
        draw_wrapped(cv, 1412, y + 22, head, 30, 420, INK, True, lead=1.2, a=1.0 if on else 0.6)
        draw_wrapped(cv, 1350, y + 112, sub, 26, 470, MUTED, False, lead=1.25, a=1.0 if on else 0.6)
        y += 240


def scene_stops(ctx):
    soil(ctx)
    cv = ctx.cv
    draw_graph(ctx, marked={v: 1.0 for v in "SABCDEF"})
    sprite_at(ctx, *POS["B"], scale=1.0)
    a = ctx.p("once", 0.5)
    cv.rrect(60, 130, 470, 186, 18, fill=WHITE, outline=PANEL_LINE, width=3)
    cv.text(84, 140, "marked once each", 30, INK, True)
    promises_panel(ctx, 0)
    finish(ctx)


def scene_never(ctx):
    soil(ctx)
    cv = ctx.cv
    cues = [("D", "E", "c1"), ("E", "F", "c2"), ("F", "C", "c3"), ("C", "S", "c4")]
    es, rings = {}, {}
    cur = "D"
    for u, v, c in cues:
        if ctx.p(c, 0.4) > 0:
            es[ekey(u, v)] = (BLUE, 11, 1.0)
            cur = v
    rings[cur] = (BLUE, 1.0)
    draw_graph(ctx, marked={v: 1.0 for v in "SABCDEF"}, estyle=es, rings=rings)
    sprite_at(ctx, *POS[cur], scale=1.0)
    promises_panel(ctx, 1)
    finish(ctx)


def domino_panel(ctx, falls, title="PROMISE 3: THE DOMINOES"):
    cv = ctx.cv
    panel_card(ctx, title)
    base_y = 560
    xs = [1380, 1545, 1710]
    names = ["S", "B", "E"]
    for i, (x, nm) in enumerate(zip(xs, names)):
        cue = falls[i]
        ang = 0.0
        if cue == "_done":
            ang = 76.0
        elif cue:
            ang = ctx.p(cue, 0.7) * 76
        w, h = 60, 140
        px, py = x + w / 2, base_y
        pts = [(x - w / 2, base_y - h), (x + w / 2, base_y - h), (x + w / 2, base_y), (x - w / 2, base_y)]
        r = math.radians(ang)
        rot = []
        for (qx, qy) in pts:
            dx, dy = qx - px, qy - py
            rot.append((px + dx * math.cos(r) - dy * math.sin(r), py + dx * math.sin(r) + dy * math.cos(r)))
        fallen = ang > 5
        cv.polygon(rot, ACCENT if fallen else WHITE)
        cv.poly_line(rot + [rot[0]], ACCENT_DARK if fallen else INK, 5)
        cv.text(x, base_y + 56, nm, 44, INK, True, anchor="mm")
    cv.text(1330, 700, "each vertex knocks over the next", 28, MUTED, False)


def scene_route_setup(ctx):
    soil(ctx)
    cv = ctx.cv
    rt = ctx.p("route", 0.6)
    es = {ekey("S", "B"): (mix(LINE, BLUE, rt), 6 + 5 * rt, 1.0), ekey("B", "E"): (mix(LINE, BLUE, rt), 6 + 5 * rt, 1.0)}
    draw_graph(ctx, estyle=es, rings={"S": (BLUE, rt), "E": (ORANGE, rt)})
    sprite_at(ctx, *POS["S"], scale=1.15)
    cv.text(POS["E"][0], POS["E"][1] + 66, "target", 28, ORANGE, True, anchor="ma", a=rt)
    cv.text(POS["S"][0], POS["S"][1] + 66, "start", 28, BLUE, True, anchor="ma", a=rt)
    domino_panel(ctx, [None, None, None])
    finish(ctx)


def scene_dominoes_1(ctx):
    soil(ctx)
    cv = ctx.cv
    s0 = ctx.p("s", 0.5)
    tok = ctx.p("tok", 0.4)
    out = ctx.p("out", 0.4)
    ei = ctx.p("either", 0.5)
    es = {ekey("S", "B"): (BLUE, 11, 1.0), ekey("B", "E"): (BLUE, 11, 1.0)}
    draw_graph(ctx, marked={"S": s0, "B": ei}, estyle=es, rings={"S": (BLUE, 1.0), "E": (ORANGE, 1.0)})
    sprite_at(ctx, *POS["S"], scale=1.15)
    if tok > 0:
        x, y = mid("S", "B", 0.5)
        move = out
        px, py = lerp(x, POS["B"][0] - 52, move), lerp(y - 20, POS["B"][1] - 20, move)
        token_pill(cv, px - 64, py - 15, "(S, B)", tok, True, False, 128)
    domino_panel(ctx, ["s", "either", None])
    finish(ctx)


def scene_dominoes_2(ctx):
    soil(ctx)
    cv = ctx.cv
    nx = ctx.p("next", 0.4)
    kn = ctx.p("knock", 0.5)
    es = {ekey("S", "B"): (BLUE, 11, 1.0), ekey("B", "E"): (BLUE, 11, 1.0)}
    draw_graph(ctx, marked={"S": 1.0, "B": 1.0, "E": kn}, estyle=es, rings={"B": (BLUE, 1.0)})
    sprite_at(ctx, *POS["B"], scale=1.0)
    if nx > 0:
        mini_pill(ctx, "B", "E", "(B, E)", nx, True, False, f=0.5, dy=-26)
    domino_panel(ctx, ["_done", "_done", "knock"])
    ia = ctx.p("ind", 0.5)
    if ia > 0:
        cv.rrect(60, 130, 760, 196, 20, fill=BLUE_SOFT, outline=BLUE, width=4, a=ia)
        cv.text(410, 163, "induction on distance from S", 32, BLUE, True, anchor="mm", a=ia)
    finish(ctx)


# ==================================================================== PART 6
CODE = [
    "def whatever_first_search(graph, start):",
    "    to_visit = [(None, start)]",
    "    visited = set()",
    "    parent_of = {}",
    "    while len(to_visit) > 0:",
    "        came_from, current = to_visit.pop()",
    "        if current not in visited:",
    "            visited.add(current)",
    "            parent_of[current] = came_from",
    "            for neighbor in graph[current]:",
    "                to_visit.append((current, neighbor))",
    "    return parent_of",
]
CODE_X, CODE_Y0, CODE_LH, CODE_FS = 150, 150, 54, 34


def code_card(ctx, lines_hl=(), boxes=(), hl_alpha=1.0, tags=()):
    """lines_hl: [(line_no, cue)] highlight bands; boxes: [(line_no, c0, c1, color, cue)]"""
    cv = ctx.cv
    cv.rrect(40, 126, 1246, 906, 26, fill=WHITE, outline=PANEL_LINE, width=3)
    cw = cv.text_w("M", CODE_FS, False, True)
    for ln, cue in lines_hl:
        a = ctx.p(cue, 0.35) if cue else 1.0
        y = CODE_Y0 + (ln - 1) * CODE_LH
        cv.rrect(58, y - 6, 1228, y + CODE_LH - 8, 12, fill=BLUE_SOFT, a=a * hl_alpha)
    for i, line in enumerate(CODE):
        y = CODE_Y0 + i * CODE_LH
        cv.text(112, y + 4, str(i + 1), 26, GRAY, True, True, anchor="ra")
        cv.text(CODE_X, y, line, CODE_FS, INK, False, True)
    for ln, c0, c1, color, cue in boxes:
        a = ctx.p(cue, 0.35) if cue else 1.0
        y = CODE_Y0 + (ln - 1) * CODE_LH
        cv.rrect(CODE_X + c0 * cw - 4, y - 4, CODE_X + c1 * cw + 4, y + CODE_FS + 10, 8, outline=color, width=4, a=a)
    for ln, text, color, cue in tags:
        a = ctx.p(cue, 0.35)
        y = CODE_Y0 + (ln - 1) * CODE_LH
        cv.text(1210, y + 8, text, 26, color, True, anchor="ra", a=a)


def notes_panel(ctx, title, notes):
    """notes: [(cue, head, body, color)]"""
    cv = ctx.cv
    panel_card(ctx, title)
    y = 168
    for cue, head, body, color in notes:
        a = ctx.p(cue, 0.4)
        if a > 0:
            cv.rrect(1316, y, 1854, y + 164, 18, fill=PAPER, outline=color, width=4, a=a)
            cv.text(1344, y + 14, head, 40, color, True, True, a=a)
            draw_wrapped(cv, 1344, y + 72, body, 27, 490, INK, False, lead=1.22, a=a)
        y += 178


def values_strip(ctx, title, rows, y0=700):
    cv = ctx.cv
    cv.line((1330, y0 - 14), (1840, y0 - 14), PANEL_LINE, 3)
    cv.text(1330, y0, title, 22, MUTED, True)
    for i, (k, v) in enumerate(rows):
        cv.text(1330, y0 + 36 + i * 38, f"{k} = {v}", 26, INK, True, True)


def scene_code_all(ctx):
    n = sum(1 for c in ("l2", "l5", "l7", "l_else") if ctx.reached(c))
    lit = max(0, n - 1)
    bands = {0: [2], 1: [5], 2: [7, 8, 9, 10, 11], 3: [7]}
    hl = [(ln, None) for ln in bands[lit]] if n else []
    tags = [(2, "rule 1", ACCENT_DARK, "l2"), (5, "rule 2", ACCENT_DARK, "l5"), (7, "rule 3", ACCENT_DARK, "l7"),
            (12, "rule 4: no else needed", ACCENT_DARK, "l_else")]
    code_card(ctx, hl, tags=tags)
    if n:
        rules_panel(ctx, lit, ["l2", "l5", "l7", "l_else"][lit], prior=tuple(range(lit)))
    else:
        rules_panel(ctx, -1, None, prior=(), all_dim=True)
    finish(ctx)


def soil_free(ctx):
    pass


def scene_code_l2(ctx):
    boxes = [(2, 15, 16, BLUE, "sq"), (2, 29, 30, BLUE, "sq"), (2, 16, 17, ACCENT, "rd"), (2, 28, 29, ACCENT, "rd"),
             (2, 17, 21, GREEN, "none"), (2, 23, 28, RED, "start")]
    code_card(ctx, [(2, "l2")], boxes)
    notes = [("sq", "[ ]", "square brackets make a list: our pile", BLUE),
             ("rd", "( )", "round brackets glue two values into a pair", ACCENT_DARK),
             ("none", "None", "means nobody", GREEN),
             ("start", "start", "the vertex we begin from", RED)]
    notes_panel(ctx, "READING LINE 2", notes)
    finish(ctx)


def scene_code_l6(ctx):
    boxes = [(6, 29, 43, ACCENT, "pop"), (6, 8, 26, BLUE, "names")]
    code_card(ctx, [(6, "l6")], boxes)
    notes = [("pop", "pop()", "takes the last item out of the list: the newest token, a pair", ACCENT_DARK),
             ("names", "a, b = pair", "the comma splits the pair into two names. This is called unpacking.", BLUE)]
    notes_panel(ctx, "READING LINE 6", notes)
    if ctx.reached("names"):
        values_strip(ctx, "VALUES NOW (step 2 of our trace)", [("came_from", "'S'"), ("current", "'C'")], y0=700)
    else:
        values_strip(ctx, "BEFORE THE POP", [("to_visit", "[(S,A),(S,B),(S,C)]")], y0=700)
    finish(ctx)


def scene_code_sets(ctx):
    boxes = [(3, 14, 19, GREEN, "set"), (4, 16, 18, ACCENT, "curly"), (7, 19, 25, RED, "set"),
             (11, 31, 32, ACCENT, "dbl"), (11, 51, 52, ACCENT, "dbl"), (11, 32, 51, BLUE, "dbl")]
    hl = [(10, "loop"), (11, "loop")]
    code_card(ctx, hl, boxes)
    notes = [("set", "set()", "remembers which vertices have a mark. 'Is it in here?' is very fast.", GREEN),
             ("curly", "{ }", "a dictionary: look up a vertex, get its parent", ACCENT_DARK),
             ("loop", "for ...", "adds one token for every neighbor", BLUE),
             ("dbl", "(( , ))", "the inner pair is the token. The outer brackets belong to append.", ACCENT_DARK)]
    notes_panel(ctx, "THE REST OF THE LINES", notes)
    finish(ctx)


def scene_code_return(ctx):
    code_card(ctx, [(12, "ret")], [])
    cv = ctx.cv
    panel_card(ctx, "THE FUNCTION RETURNS parent_of")
    items = [(v, PARENT[v] or "None") for v in MARK_ORDER]
    ka, va = ctx.p("keys", 0.5), ctx.p("values", 0.5)
    y = 180
    for k, v in items:
        cv.text(1380, y, f"'{k}'", 46, BLUE if ka > 0 else INK, True, True, anchor="la")
        cv.text(1480, y, ":", 46, MUTED, True, True, anchor="la")
        cv.text(1530, y, f"'{v}'" if v != "None" else "None", 46, ACCENT_DARK if va > 0 else INK, True, True, anchor="la")
        y += 74
    cv.text(1330, 712, "keys  = the marked vertices", 28, BLUE, True, a=max(ka, 0.2))
    cv.text(1330, 756, "values = the parent tree", 28, ACCENT_DARK, True, a=max(va, 0.2))
    finish(ctx)


def mini_code(cv, x0, y0, lines, size, w, h, title, hl=()):
    cv.rrect(x0, y0, x0 + w, y0 + h, 22, fill=WHITE, outline=PANEL_LINE, width=3)
    cv.text(x0 + 24, y0 + 14, title, 22, MUTED, True)
    cw = cv.text_w("M", size, False, True)
    for i, line in enumerate(lines):
        y = y0 + 60 + i * (size + 20)
        for (ln, c0, c1, color, a) in hl:
            if ln == i and a > 0:
                cv.rrect(x0 + 24 + c0 * cw - 4, y - 3, x0 + 24 + c1 * cw + 4, y + size + 8, 8, fill=mix(WHITE, color, 0.2), outline=color, width=3, a=a)
        cv.text(x0 + 24, y, line, size, INK, False, True)


def scene_recursion(ctx):
    cv = ctx.cv
    left = ["def build_topo_from(node):", "    pre_order.append(node)", "    visited.add(node)",
            "    for child in children[node]:", "        if child not in visited:", "            build_topo_from(child)",
            "    post_order.append(node)"]
    right = ["def visit(current):", "    if current not in visited:", "        visited.add(current)",
             "        for neighbor in graph[current]:", "            visit(neighbor)"]
    g1, g2, g3 = ctx.p("g1", 0.4), ctx.p("g2", 0.4), ctx.p("g3", 0.4)
    hl_l = [(2, 4, 21, GREEN, g1), (3, 4, 32, BLUE, g2), (5, 12, 34, ACCENT, g3)]
    hl_r = [(2, 8, 27, GREEN, g1), (3, 8, 39, BLUE, g2), (4, 12, 27, ACCENT, g3)]
    mini_code(cv, 40, 126, left, 26, 560, 640, "YOUR CODE  (mini-lab.py)", hl_l)
    mini_code(cv, 616, 126, right, 26, 630, 470, "THE SAME IDEA, NO PILE WRITTEN DOWN", hl_r)
    na = ctx.p("nopile", 0.5)
    if na > 0:
        cv.rrect(616, 620, 1246, 760, 22, fill=BLUE_SOFT, outline=BLUE, width=4, a=na)
        cv.text(931, 690, "Python's call stack  =  the pile", 30, BLUE, True, anchor="mm", a=na)
    cv.rrect(40, 790, 1246, 906, 22, fill=PAPER, outline=PANEL_LINE, width=3)
    cv.text(70, 812, "pre_order and post_order are extra bookkeeping on the same walk.", 28, MUTED, True)
    cv.text(70, 856, "The neighbors may come out in flipped order. The idea is the same.", 28, MUTED, False)
    panel_card(ctx, "SAME PIECES, SAME COLORS")
    rows = [("mark it", "visited.add(...)", GREEN, g1), ("for each neighbor", "the for loop", BLUE, g2),
            ("take the next one", "call itself", ACCENT_DARK, g3)]
    y = 180
    for head, sub, col, a in rows:
        cv.rrect(1316, y, 1854, y + 140, 20, fill=PAPER, outline=col, width=4, a=max(a, 0.25))
        cv.text(1344, y + 24, head, 38, col, True, a=max(a, 0.25))
        cv.text(1344, y + 82, sub, 30, INK, False, True, a=max(a, 0.25))
        y += 160
    finish(ctx)


# ==================================================================== PART 7
def scene_recap(ctx):
    soil(ctx)
    cv = ctx.cv
    cards = [("c1", "Scent marks", "stop her circling", "1"),
             ("c2", "A pile of tokens", "remembers the tunnels she hasn't walked", "2"),
             ("c3", "The parents", "form a tree back to the nest", "3")]
    y = 160
    for cue, head, sub, num in cards:
        a = ctx.p(cue, 0.5)
        cv.rrect(110, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(184, y + 75, 36, fill=ACCENT, a=a)
        cv.text(184, y + 74, num, 40, WHITE, True, anchor="mm", a=a)
        cv.text(250, y + 24, head, 46, ACCENT_DARK, True, a=a)
        cv.text(250, y + 88, sub, 32, INK, False, a=a)
        y += 178
    ta = ctx.p("try", 0.5)
    cv.rrect(110, 700, 1180, 880, 26, fill=BLUE_SOFT, outline=BLUE, width=4, a=ta)
    cv.text(150, 724, "TRY IT ON PAPER", 24, BLUE, True, a=ta)
    cv.text(150, 768, "Run the four rules on the graph from page one", 32, INK, True, a=ta)
    cv.text(150, 814, "of your 10/19 notes.", 32, INK, True, a=ta)
    sprite_at(ctx, 1480, 470, scale=2.4)
    cv.text(1550, 620, "Next: what if the pile is a queue?", 30, MUTED, True, anchor="mm", a=ta)
    finish(ctx)
