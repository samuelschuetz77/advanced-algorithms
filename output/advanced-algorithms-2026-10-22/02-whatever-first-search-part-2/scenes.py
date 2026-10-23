"""Video 02 scenes: the metro map, three piles, one-way tracks, flood fill."""
from __future__ import annotations

import math

import chars
import metrolog as R
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, RED, WHITE, YELLOW, clamp, ease, lerp, mix, point_along,
)
from graphview import GraphView
from widgets import (
    CodeCard, PANEL, chrome, draw_wrapped, notes_panel, panel_card, predict_chip, tag, token_pill, wrap,
)

ORANGE = (234, 140, 36)
PURPLE = (140, 80, 200)
DAY_COL = [ACCENT, BLUE, GREEN, PURPLE]

GV = GraphView(R.POS, R.FRIENDS, r=46, label_size=28)
GVD = GraphView(R.POS, R.ONE_WAY, directed=True, r=46, label_size=28)


def _xf(p, s=0.62, ox=40, oy=480):
    return (ox + (p[0] - 100) * s, oy + (p[1] - 520) * s)


POS2 = {v: _xf(p) for v, p in R.POS.items()}
POS2.update({"Mill": (960, 380), "Nest": (850, 640), "Oak": (1090, 640)})
GV2 = GraphView(POS2, R.FRIENDS + R.FERRY, r=40, label_size=24)


def stops_label(n):
    return "start" if n == 0 else ("1 stop" if n == 1 else f"{n} stops")


def stage(ctx):
    cv = ctx.cv
    cv.rrect(30, 112, 1258, 916, 28, fill=(240, 245, 252), outline=(214, 224, 238), width=3)
    for y in range(160, 916, 48):
        cv.line((48, y), (1240, y), (226, 234, 246), 2)


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def bubbles(ctx, gv, marked, scale=0.6):
    """A small flag on every visited station."""
    cv = ctx.cv
    for v, p in marked.items():
        if p > 0.02:
            x, y = gv.pos[v]
            fx, top = x + gv.r * 0.5, y - gv.r - 28
            cv.line((fx, top), (fx, y - gv.r + 6), INK, 3, a=p)
            cv.polygon([(fx, top), (fx + 26, top + 9), (fx, top + 18)], ACCENT, a=p)


def train(cv, x, y, a=1.0):
    cv.rrect(x - 30, y - 16, x + 30, y + 16, 9, fill=BLUE, outline=INK, width=2, a=a)
    cv.rrect(x - 21, y - 9, x - 7, y + 3, 3, fill=WHITE, a=a)
    cv.rrect(x + 5, y - 9, x + 19, y + 3, 3, fill=WHITE, a=a)
    cv.circle(x - 15, y + 18, 6, fill=INK, a=a)
    cv.circle(x + 15, y + 18, 6, fill=INK, a=a)


def schedule(anchor, start, stop, per, offset=0.0):
    """extra_cues for steps start..stop: take at anchor+k*per, do 0.25 later (and push 0.5 later)."""
    out = []
    for k, n in enumerate(range(start, stop + 1)):
        t = offset + k * per
        out += [(f"take{n}", anchor, t), (f"do{n}", anchor, t + 0.25), (f"push{n}", anchor, t + 0.45)]
    return out


# ---------------------------------------------------------------- search view
def search_panel(ctx, mode, take, pile, palpha, marked, stale=None):
    cv = ctx.cv
    panel_card(ctx, None)
    cv.rrect(1316, 138, 1854, 268, 20, fill=PAPER, outline=PANEL_LINE, width=3)
    cv.text(1338, 148, "TAKE THE " + ("NEWEST" if mode == "stack" else "OLDEST") + " TOKEN", 20, MUTED, True)
    if take is None:
        cv.text(1338, 190, "—", 40, GRAY, True, True)
    else:
        s, a_do = take
        cv.text(1338, 172, f"({s['came_from'] or 'nobody'}, {s['current']})", 38, INK, True, True)
        if a_do > 0:
            if s["new"]:
                msg, col = f"{s['current']} is new: mark it", ACCENT_DARK
            else:
                msg, col = f"{s['current']} already visited: throw it away", RED
            cv.text(1338, 224, msg, 25, col, True, a=a_do)
    cv.text(1330, 282, "TOKEN PILE", 20, MUTED, True)
    cv.text(1850, 282, "newest on top", 20, MUTED, False, anchor="ra")
    shown = [(t, a) for t, a in zip(pile, palpha) if a > 0]
    y = 306
    if not shown:
        cv.text(1330, y + 2, "(empty)", 26, GRAY, True, True)
    n = len(shown)
    for rank, (tok, a) in enumerate(reversed(shown)):
        nxt = (rank == 0) if mode == "stack" else (rank == n - 1)
        token_pill(cv, 1330, y, f"({tok[0] or 'nobody'}, {tok[1]})", a, hi=nxt, w=250, h=26, fs=21)
        if nxt:
            cv.text(1596, y + 13, "← next out", 21, ACCENT_DARK, True, anchor="lm", a=a)
        if stale and tok in stale:
            cv.text(1596, y + 13, "stale", 21, ORANGE, True, anchor="lm", a=a)
        y += 29
    cv.text(1330, 700, "VISITED", 20, MUTED, True)
    for i, v in enumerate(R.PEOPLE):
        col, row = i % 4, i // 4
        x0, y0 = 1330 + col * 128, 726 + row * 52
        mf = marked.get(v, 0.0)
        cv.rrect(x0, y0, x0 + 118, y0 + 42, 21, fill=mix(WHITE, ACCENT, mf), outline=mix(GRAY, ACCENT_DARK, mf), width=3)
        cv.text(x0 + 59, y0 + 21, v, 24, mix(MUTED, WHITE, mf), True, anchor="mm")


def search_scene(mode, steps, idle_after=None, tree=True, days=False, stale_cue=None, graph_log=None,
                 gv=GV, tele_anim=True):
    log = graph_log or (R.STACK if mode == "stack" else R.QUEUE)
    first_depth = log[-1]["depth"]

    def scene(ctx):
        cv = ctx.cv
        stage(ctx)
        multi = len(steps) > 1

        def cn(base, n):
            return f"{base}{n}" if multi else base

        if steps:
            f = steps[0]
            pile = list(log[f - 1]["pile_before"])
            marked_names = log[f - 2]["marked_after"] if f > 1 else []
        else:
            pile = list(log[idle_after - 1]["pile_after"])
            marked_names = log[idle_after - 1]["marked_after"]
        palpha = [1.0] * len(pile)
        marked = {v: 1.0 for v in marked_names}
        latest, take, rings, estyle, badges = None, None, {}, {}, {}
        tele = None
        for n in steps:
            s = log[n - 1]
            t_take = ctx.cues.get(cn("take", n))
            took = t_take is not None and ctx.t >= t_take
            ctx.sig.append(1 if took else 0)
            if not took:
                break
            pile.pop(s["idx"])
            palpha.pop(s["idx"])
            a_do = ctx.p(cn("do", n), 0.4)
            take = (s, a_do)
            rings, badges = {}, {}
            estyle_tmp = {}
            rings[s["current"]] = (BLUE, 1.0)
            if s["came_from"]:
                estyle_tmp[gv.key(s["came_from"], s["current"])] = (BLUE, 10, 1.0)
                if tele_anim and ctx.t - t_take < 0.5:
                    tele = (s["came_from"], s["current"], ctx.ramp(t_take, t_take + 0.45))
            latest = (s, estyle_tmp)
            if s["new"]:
                marked[s["current"]] = a_do
            else:
                badges[s["current"]] = ("x", a_do)
            t_push = ctx.cues.get(cn("push", n))
            for k, tok in enumerate(s["added"]):
                a = 0.0 if t_push is None else ctx.ramp(t_push + 0.1 * k, t_push + 0.1 * k + 0.25)
                pile.append(tok)
                palpha.append(a)
        parents = log[-1]["parent_after"]
        es = {}
        if tree:
            for v, p in marked.items():
                par = parents.get(v)
                if par and p > 0.02:
                    col = DAY_COL[min(first_depth.get(v, 0), 3)] if days else ACCENT
                    es[gv.key(par, v)] = (col, 11, p)
        if latest:
            for k, val in latest[1].items():
                es[k] = val
        fills = None
        if days:
            fills = {v: (DAY_COL[min(first_depth.get(v, 0), 3)], p) for v, p in marked.items()}
            gv.draw(ctx, fills=fills, rings=rings, estyle=es, badges=badges)
        else:
            gv.draw(ctx, marked=marked, rings=rings, estyle=es, badges=badges)
        if days:
            for v, p in marked.items():
                if p > 0.5:
                    x, y = gv.pos[v]
                    cv.text(x, y + gv.r + 24, stops_label(first_depth.get(v, 0)), 22,
                            DAY_COL[min(first_depth.get(v, 0), 3)], True, anchor="mm", a=p)
        bubbles(ctx, gv, marked)
        if tele:
            u, v, f = tele
            x, y = point_along(gv.full(u, v), ease(f))
            train(cv, x, y)
        stale = {("Arch", "Bay"), ("Arch", "Cove")} if (stale_cue and ctx.reached(stale_cue)) else None
        search_panel(ctx, mode, take, pile, palpha, marked, stale)
        finish(ctx)
    return scene


# ---------------------------------------------------------------- part A: cost
def scene_recap(ctx):
    stage(ctx)
    GV.draw(ctx)
    panel_card(ctx, "LAST TIME: THE THREE-LINE ALGORITHM")
    cv = ctx.cv
    cards = [("c1", "take a token", "from the pile"), ("c2", "if its vertex is new", "mark it, remember its parent"),
             ("c3", "add a token", "for every edge out of it")]
    y = 180
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 150, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=a)
        cv.circle(1368, y + 75, 28, fill=ACCENT, a=a)
        cv.text(1368, y + 74, str(i + 1), 32, WHITE, True, anchor="mm", a=a)
        cv.text(1418, y + 30, head, 32, ACCENT_DARK, True, a=a)
        cv.text(1418, y + 80, sub, 27, INK, False, a=a)
        y += 176
    finish(ctx)


def scene_world(ctx):
    stage(ctx)
    cv = ctx.cv
    b = ctx.p("start", 0.5)
    GV.draw(ctx, rings={"Arch": (BLUE, ctx.pulse("start", 1.0))})
    bubbles(ctx, GV, {"Arch": b}, 0.9)
    panel_card(ctx, "STORY WORD  →  GRAPH WORD")
    rows = [("w1", "station", "vertex"), ("w2", "track", "edge"), ("w3", "visited", "marked"),
            ("w4", "a track to try", "token (from, to)"), ("w5", "the station you came from", "parent")]
    y = 180
    for cue, a_, b_ in rows:
        a = ctx.p(cue, 0.4)
        cv.rrect(1316, y, 1854, y + 118, 18, fill=PAPER, outline=ACCENT if a > 0.5 else PANEL_LINE, width=3, a=a)
        cv.text(1342, y + 14, a_, 28, MUTED, True, a=a)
        cv.text(1342, y + 58, b_, 40, ACCENT_DARK, True, a=a)
        y += 134
    finish(ctx)


def scene_predict(ctx):
    stage(ctx)
    GV.draw(ctx)
    bubbles(ctx, GV, {"Arch": 1.0}, 0.9)
    panel_card(ctx, "THE METRO MAP")
    cv = ctx.cv
    cv.text(1330, 200, "7 stations", 46, INK, True)
    cv.text(1330, 270, "12 tracks", 46, INK, True)
    cv.text(1330, 360, "tokens ever written?", 34, MUTED, True)
    cv.text(1330, 420, "?", 120, ACCENT, True)
    finish(ctx)


def arrow_pair(ctx, u, v, a1, a2, color=ACCENT, off=15):
    """Two parallel arrows between u and v, one each way."""
    cv = ctx.cv
    (x0, y0), (x1, y1) = GV.pos[u], GV.pos[v]
    L = math.hypot(x1 - x0, y1 - y0) or 1
    nx, ny = -(y1 - y0) / L, (x1 - x0) / L
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    r = GV.r + 6
    if a1 > 0.02:
        cv.arrow((x0 + ux * r + nx * off, y0 + uy * r + ny * off), (x1 - ux * r + nx * off, y1 - uy * r + ny * off),
                 color, 5, a=a1, head=20)
    if a2 > 0.02:
        cv.arrow((x1 - ux * r - nx * off, y1 - uy * r - ny * off), (x0 + ux * r - nx * off, y0 + uy * r - ny * off),
                 color, 5, a=a2, head=20)


def scene_two_each(ctx):
    stage(ctx)
    cv = ctx.cv
    a1, a2 = ctx.p("t1", 0.5), ctx.p("t2", 0.5)
    es = {GV.key("Arch", "Bay"): (LINE, 6, 0.3)}
    GV.draw(ctx, estyle=es, rings={"Arch": (BLUE, a1), "Bay": (BLUE, a2)})
    arrow_pair(ctx, "Arch", "Bay", a1, a2)
    if a1 > 0.02:
        x, y = GV.pos["Arch"]
        tag(cv, 395, 330, "(Arch, Bay)", ACCENT_DARK, a=a1, size=24)
    if a2 > 0.02:
        tag(cv, 395, 495, "(Bay, Arch)", ACCENT_DARK, a=a2, size=24)
    panel_card(ctx, "ONE TRACK")
    count = (1 if a1 > 0.5 else 0) + (1 if a2 > 0.5 else 0)
    cv.text(1330, 200, "tokens it makes:", 32, MUTED, True)
    cv.text(1330, 250, str(count), 140, ACCENT, True)
    finish(ctx)


def scene_all_edges(ctx):
    stage(ctx)
    cv = ctx.cv
    t0 = ctx.cue("all") or 0.0
    es, count = {}, 0
    for i, (u, v) in enumerate(R.FRIENDS):
        a = ctx.ramp(t0 + 0.42 * i, t0 + 0.42 * i + 0.3)
        if a > 0.02:
            es[GV.key(u, v)] = (ACCENT, 6, 0.3 + 0.7 * a)
        if a > 0.5:
            count += 2
    GV.draw(ctx, estyle=es)
    for i, (u, v) in enumerate(R.FRIENDS):
        a = ctx.ramp(t0 + 0.42 * i, t0 + 0.42 * i + 0.3)
        arrow_pair(ctx, u, v, a, a, off=12)
    panel_card(ctx, "TOKENS FROM TRACKS")
    cv.text(1330, 200, "tracks used:", 30, MUTED, True)
    cv.text(1330, 242, f"{count // 2} of 12", 54, INK, True)
    cv.text(1330, 340, "tokens so far:", 30, MUTED, True)
    cv.text(1330, 382, str(count), 130, ACCENT, True)
    finish(ctx)


def formula_panel(ctx, title, lines):
    """lines: [(cue, text, size, color)] shown one under another."""
    panel_card(ctx, title)
    y = 190
    for cue, text, size, color in lines:
        a = ctx.p(cue, 0.45) if cue else 1.0
        ctx.cv.text(1330, y, text, size, color, True, a=a)
        y += size * 1.7


def scene_plus_one(ctx):
    stage(ctx)
    es = {GV.key(u, v): (ACCENT, 6, 1.0) for u, v in R.FRIENDS}
    GV.draw(ctx, estyle=es)
    for u, v in R.FRIENDS:
        arrow_pair(ctx, u, v, 1.0, 1.0, off=12)
    bubbles(ctx, GV, {"Arch": ctx.p("plus", 0.5)}, 0.9)
    formula_panel(ctx, "COUNTING TOKENS", [
        (None, "24 from edges", 36, INK), ("plus", "+ 1 to start (Arch)", 36, ACCENT_DARK),
        ("total", "= 25 tokens", 48, ACCENT), ("formula", "2E + 1", 96, BLUE), ("eq", "2 × 12 + 1 = 25", 40, INK)])
    finish(ctx)


def scene_cost(ctx):
    stage(ctx)
    cv = ctx.cv
    y = 190
    items = [("one", "Every token is put in the pile once", 40, INK), ("two", "and taken out once.", 40, INK),
             ("three", "One put or one take costs  T", 44, BLUE), ("four", "Total for all tokens:", 40, INK),
             ("five", "(2E + 1) × T   ≈   2E × T", 64, ACCENT)]
    for cue, text, size, color in items:
        a = ctx.p(cue, 0.45)
        cv.text(80, y, text, size, color, True, a=a)
        y += size * 1.9
    panel_card(ctx, "BOOK: PDF p.219")
    cv.text(1330, 190, "the loop over tracks", 28, INK, True)
    cv.text(1330, 230, "runs once per marked vertex", 26, MUTED, False)
    cv.text(1330, 330, "putting tokens in:", 28, INK, True)
    cv.text(1330, 370, "at most 2E times", 26, MUTED, False)
    cv.text(1330, 470, "taking tokens out:", 28, INK, True)
    cv.text(1330, 510, "at most 2E + 1 times", 26, MUTED, False)
    finish(ctx)


def scene_vertices(ctx):
    stage(ctx)
    cv = ctx.cv
    GV.draw(ctx, marked={v: ctx.p("mark", 0.5) for v in R.PEOPLE})
    cv.text(80, 160, "each station is marked once:   + V", 40, ACCENT_DARK, True, a=ctx.p("mark", 0.5))
    formula_panel(ctx, "TOTAL TIME", [("v", "V  +  E × T", 90, BLUE),
                                      ("w", "(the V is the marking)", 28, MUTED),
                                      ("w2", "(the E × T is the tokens)", 28, MUTED)])
    finish(ctx)


def scene_stackT(ctx):
    stage(ctx)
    cv = ctx.cv
    cv.text(100, 150, "A stack touches only the top", 42, INK, True)
    for i, lb in enumerate(["(East, Gate)", "(Cove, East)", "(Arch, Cove)"]):
        a = ctx.p("top", 0.5) if i == 0 else 1.0
        token_pill(cv, 160, 270 + i * 70, lb, 1.0, hi=(i == 0), w=330, h=56, fs=30)
    tp = ctx.p("top", 0.5)
    cv.arrow((620, 290), (520, 296), ACCENT_DARK, 6, a=tp, head=24)
    cv.text(640, 270, "put and take: one step", 32, ACCENT_DARK, True, a=tp)
    cv.text(640, 316, "however big the pile", 28, MUTED, False, a=tp)
    tt = ctx.p("T", 0.5)
    cv.rrect(100, 540, 1180, 800, 28, fill=WHITE, outline=BLUE, width=4, a=tt)
    cv.text(640, 610, "T is a constant", 46, BLUE, True, anchor="mm", a=tt)
    lo = ctx.p("linear", 0.5)
    cv.text(640, 720, "total time  =  O(V + E)", 70, ACCENT, True, anchor="mm", a=lo)
    panel_card(ctx, "TIME FOR THE WHOLE SEARCH")
    cv.text(1330, 200, "stack:  T = 1", 38, INK, True)
    cv.text(1330, 270, "queue:  T = 1", 38, INK, True)
    cv.text(1330, 340, "so  V + E", 38, ACCENT_DARK, True)
    finish(ctx)


def scene_matrix(ctx):
    stage(ctx)
    cv = ctx.cv
    la = ctx.p("lists", 0.5)
    cv.text(70, 150, "A list of neighbors for each station", 34, INK, True, a=la)
    y = 210
    for v in R.PEOPLE:
        cv.text(80, y, f"{v}:", 32, ACCENT_DARK, True, True, a=la)
        cv.text(230, y, "  ".join(R.G[v]), 30, INK, False, True, a=la)
        y += 56
    ma = ctx.p("matrix", 0.5)
    cv.text(700, 150, "A table of yes / no answers", 34, INK, True, a=ma)
    ox, oy, c = 760, 250, 60
    scan = ctx.ramp(ctx.cue("scan") or 0, (ctx.cue("scan") or 0) + 2.0) if ctx.cue("scan") else 0.0
    for i, a_ in enumerate(R.PEOPLE):
        cv.text(ox - 12, oy + i * c + c / 2, a_[:3], 22, MUTED, True, anchor="rm", a=ma)
        cv.text(ox + i * c + c / 2, oy - 18, a_[:3], 22, MUTED, True, anchor="mm", a=ma)
        for j, b_ in enumerate(R.PEOPLE):
            yes = b_ in R.G[a_]
            lit = (i == 0)
            hl = lit and scan > 0 and (j / 7.0) <= scan
            cv.rrect(ox + j * c + 2, oy + i * c + 2, ox + j * c + c - 2, oy + i * c + c - 2, 8,
                     fill=ACCENT_SOFT if yes else PAPER, outline=ACCENT if hl else PANEL_LINE, width=4 if hl else 2, a=ma)
            if yes:
                cv.circle(ox + j * c + c / 2, oy + i * c + c / 2, 12, fill=ACCENT_DARK, a=ma)
    if scan > 0:
        cv.text(760, 700, "to find Arch's neighbors: check all V cells", 28, ACCENT_DARK, True)
    sq = ctx.p("square", 0.5)
    cv.text(640, 800, "total then grows like V × V", 44, RED, True, anchor="mm", a=sq)
    panel_card(ctx, "WHY THE BOOK USES LISTS")
    draw_wrapped(ctx.cv, 1330, 190, "Every bound in the book assumes the graph is stored as adjacency lists, unless it says otherwise.",
                 29, 500, INK, False)
    cv.text(1330, 470, "PDF p.217", 26, BLUE, True)
    finish(ctx)


# ---------------------------------------------------------------- part B: three piles
def scene_three_rules(ctx):
    stage(ctx)
    cv = ctx.cv
    toks = [5, 2, 9, 4]  # oldest .. newest
    cols = [("STACK", "take the newest", "stack", 4, 3), ("QUEUE", "take the oldest", "queue", 5, 0),
            ("PRIORITY QUEUE", "take the smallest number", "pq", 2, 1)]
    cv.text(640, 150, "one pile, four tokens, numbered 5, 2, 9, 4 (oldest to newest)", 28, MUTED, True, anchor="mm")
    for i, (title, rule, cue, pick, idx) in enumerate(cols):
        x0 = 70 + i * 395
        a = ctx.p(cue, 0.5)
        cv.rrect(x0, 190, x0 + 360, 880, 26, fill=WHITE, outline=ACCENT if a > 0.4 else PANEL_LINE, width=4 if a > 0.4 else 3)
        cv.text(x0 + 180, 220, title, 34, ACCENT_DARK, True, anchor="mm")
        cv.text(x0 + 180, 262, rule, 26, MUTED, False, anchor="mm", a=max(a, 0.25))
        for k, v in enumerate(reversed(toks)):  # newest on top
            y = 320 + k * 110
            chosen = a > 0.02 and v == pick
            cv.rrect(x0 + 60, y, x0 + 300, y + 86, 20, fill=ACCENT_SOFT if chosen else PAPER,
                     outline=ACCENT if chosen else PANEL_LINE, width=5 if chosen else 3)
            cv.text(x0 + 180, y + 43, str(v), 48, INK, True, anchor="mm")
        if a > 0.02:
            k = list(reversed(toks)).index(pick)
            cv.text(x0 + 180, 320 + k * 110 - 22, "next out", 24, ACCENT_DARK, True, anchor="mm", a=a)
    panel_card(ctx, "NEXT OUT")
    cv.text(1330, 200, "stack  → 4", 44, INK, True, a=max(ctx.p("stack", 0.4), 0.25))
    cv.text(1330, 290, "queue  → 5", 44, INK, True, a=max(ctx.p("queue", 0.4), 0.25))
    cv.text(1330, 380, "priority queue  → 2", 38, INK, True, a=max(ctx.p("pq", 0.4), 0.25))
    cv.text(1330, 520, "Same algorithm.", 34, ACCENT_DARK, True, a=ctx.p("stack", 0.4))
    cv.text(1330, 568, "Different pile.", 34, ACCENT_DARK, True, a=ctx.p("stack", 0.4))
    finish(ctx)


def scene_names(ctx):
    stage(ctx)
    cv = ctx.cv
    rows = [("n1", "stack", "depth-first search", "long, skinny tree", ACCENT),
            ("n2", "queue", "breadth-first search", "short, bushy tree; shortest routes", BLUE),
            ("n3", "priority queue", "best-first search", "spanning trees and shortest paths on weighted graphs", GREEN)]
    y = 170
    for cue, pile, name, what, col in rows:
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 200, 28, fill=WHITE, outline=col, width=5, a=a)
        cv.text(120, y + 28, f"pile = {pile}", 34, MUTED, True, a=a)
        cv.arrow((520, y + 100), (620, y + 100), col, 8, a=a, head=26)
        cv.text(660, y + 40, name, 44, col, True, a=a)
        draw_wrapped(cv, 660, y + 108, what, 27, 480, INK, False, a=a, lead=1.15)
        y += 232
    panel_card(ctx, "BOOK: PDF pp.219-221")
    draw_wrapped(cv, 1330, 190, "The algorithm is called whatever-first search because the proof never needed to know which token comes out.",
                 29, 500, INK, False)
    finish(ctx)


# ---------------------------------------------------------------- trees
def tree_layout(parent, depth, order, x0, x1, y0, dy, zig=0):
    levels = {}
    for v in order:
        levels.setdefault(depth[v], []).append(v)
    pos = {}
    for d, vs in levels.items():
        n = len(vs)
        for i, v in enumerate(vs):
            x = x0 + (x1 - x0) * (i + 1) / (n + 1)
            if zig:
                x += zig * (1 if d % 2 else -1)
            pos[v] = (x, y0 + d * dy)
    return pos


def draw_tree(ctx, parent, pos, color, alpha_of=None, r=34, hl_path=None, hl_color=RED):
    cv = ctx.cv
    for v, p in parent.items():
        if p:
            a = alpha_of(v) if alpha_of else 1.0
            on = hl_path and v in hl_path and p in hl_path
            cv.line(pos[p], pos[v], hl_color if on else color, 9 if on else 7, a)
    for v, (x, y) in pos.items():
        a = alpha_of(v) if alpha_of else 1.0
        on = hl_path and v in hl_path
        cv.circle(x, y, r, fill=hl_color if on else color, outline=INK, width=3, a=a)
        cv.text(x, y, v, 20 if len(v) > 3 else 24, WHITE, True, anchor="mm", a=a)


def scene_stack_tree(ctx):
    stage(ctx)
    cv = ctx.cv
    order = R.STACK[-1]["marked_after"]
    pos = tree_layout(R.STACK_PARENT, R.STACK_DEPTH, order, 120, 620, 190, 100, zig=70)
    pb = ctx.p("ben", 0.6)
    path = ["Arch", "Dock", "Fort", "Gate", "East", "Cove", "Bay"] if pb > 0.3 else None
    draw_tree(ctx, R.STACK_PARENT, pos, ACCENT, hl_path=set(path) if path else None)
    for v in order:
        cv.text(pos[v][0] - 54, pos[v][1], f"depth {R.STACK_DEPTH[v]}", 22, MUTED, True, anchor="rm")
    # Bay is Arch's direct friend
    fa = ctx.p("friend", 0.5)
    if fa > 0:
        cv.poly_line([(pos["Arch"][0] + 34, pos["Arch"][1]), (900, pos["Arch"][1]), (900, pos["Bay"][1]),
                      (pos["Bay"][0] + 34, pos["Bay"][1])], GREEN, 6, a=fa, dash=(16, 10))
        tag(cv, 900, 500, "but Bay is right next to Arch!", GREEN, a=fa, size=28)
    panel_card(ctx, "THE STACK'S TREE")
    cv.text(1330, 200, "depth 6", 100, ACCENT, True)
    cv.text(1330, 330, "one long chain", 36, INK, True)
    cv.text(1330, 400, "the route to Bay:", 30, MUTED, True, a=pb)
    cv.text(1330, 446, "6 tracks", 46, RED, True, a=pb)
    finish(ctx)


def scene_queue_tree(ctx):
    stage(ctx)
    cv = ctx.cv
    so = R.STACK[-1]["marked_after"]
    qo = R.QUEUE[-1]["marked_after"]
    p1 = tree_layout(R.STACK_PARENT, R.STACK_DEPTH, so, 60, 560, 200, 98, zig=60)
    p2 = tree_layout(R.QUEUE_PARENT, R.QUEUE_DEPTH, qo, 660, 1240, 200, 196)
    cv.text(310, 150, "STACK", 30, ACCENT_DARK, True, anchor="mm")
    cv.text(950, 150, "QUEUE", 30, BLUE, True, anchor="mm")
    draw_tree(ctx, R.STACK_PARENT, p1, ACCENT, r=30)
    draw_tree(ctx, R.QUEUE_PARENT, p2, BLUE, r=34, alpha_of=lambda v: ctx.p("q", 0.6))
    if ctx.p("q", 0.6) > 0:
        for d in range(4):
            cv.text(1250, 200 + d * 196, stops_label(d), 24, MUTED, True, anchor="rm", a=ctx.p("q", 0.6))
    panel_card(ctx, "BOOK: FIGURE 5.12, PDF p.220")
    cv.text(1330, 200, "stack:  depth 6", 40, ACCENT_DARK, True)
    cv.text(1330, 270, "queue:  depth 3", 40, BLUE, True, a=ctx.p("q", 0.5))
    draw_wrapped(cv, 1330, 380, "Depth-first trees are long and skinny. Breadth-first trees are short and bushy.", 29, 500,
                 INK, False, a=ctx.p("q", 0.5))
    finish(ctx)


def scene_shortest(ctx):
    stage(ctx)
    cv = ctx.cv
    fills = {v: (DAY_COL[min(R.QUEUE_DEPTH[v], 3)], 1.0) for v in R.PEOPLE}
    es = {}
    for v, p in R.QUEUE_PARENT.items():
        if p:
            es[GV.key(p, v)] = (DAY_COL[min(R.QUEUE_DEPTH[v], 3)], 11, 1.0)
    pa = ctx.p("route", 0.6)
    if pa > 0:
        for u, v in (("Arch", "Bay"),):
            es[GV.key(u, v)] = (RED, 14, 1.0)
    GV.draw(ctx, fills=fills, estyle=es)
    for v in R.PEOPLE:
        x, y = GV.pos[v]
        cv.text(x, y + GV.r + 24, stops_label(R.QUEUE_DEPTH[v]), 22, DAY_COL[min(R.QUEUE_DEPTH[v], 3)], True, anchor="mm")
    panel_card(ctx, "STOPS = FEWEST TRACKS")
    cv.text(1330, 200, "Bay:  1 stop", 44, BLUE, True, a=pa)
    cv.text(1330, 262, "1 track from Arch", 28, MUTED, False, a=pa)
    cv.text(1330, 360, "Gate:  3 stops", 44, PURPLE, True, a=ctx.p("gus", 0.5))
    cv.text(1330, 422, "no route has fewer than 3", 28, MUTED, False, a=ctx.p("gus", 0.5))
    cv.text(1330, 540, "Queue: shortest routes.", 34, ACCENT_DARK, True, a=ctx.p("claim", 0.5))
    cv.text(1330, 588, "Stack: not guaranteed.", 34, RED, True, a=ctx.p("claim", 0.5))
    finish(ctx)


WEIGHTS = {("Arch", "Bay"): 4, ("Arch", "Cove"): 2, ("Arch", "Dock"): 7, ("Bay", "Cove"): 3, ("Bay", "East"): 6,
           ("Cove", "Dock"): 5, ("Cove", "East"): 4, ("Cove", "Fort"): 8, ("Dock", "Fort"): 3, ("East", "Fort"): 2,
           ("East", "Gate"): 5, ("Fort", "Gate"): 6}
GVW = GraphView(R.POS, R.FRIENDS, r=46, label_size=28, weights=WEIGHTS)


def scene_pq(ctx):
    stage(ctx)
    cv = ctx.cv
    GVW.draw(ctx, show_weights=True)
    cv.text(80, 150, "numbers = minutes of travel", 30, MUTED, True, a=ctx.p("w", 0.5))
    panel_card(ctx, "BEST-FIRST SEARCH")
    notes = [("a", "priority = edge weight", "builds a minimum spanning tree: Jarník's, usually called Prim's", GREEN),
             ("b", "priority = distance so far", "finds shortest routes on a weighted map: Dijkstra's", BLUE)]
    y = 180
    for cue, head, body, col in notes:
        a = ctx.p(cue, 0.5)
        cv.rrect(1316, y, 1854, y + 190, 20, fill=PAPER, outline=col, width=4, a=a)
        cv.text(1344, y + 16, head, 30, col, True, a=a)
        draw_wrapped(cv, 1344, y + 66, body, 28, 490, INK, False, a=a)
        y += 210
    cv.text(1330, 640, "time:  O(V + E log E)", 36, ACCENT_DARK, True, a=ctx.p("time", 0.5))
    cv.text(1330, 690, "(a priority queue is slower than T = 1)", 24, MUTED, False, a=ctx.p("time", 0.5))
    cv.text(1330, 760, "Chapters 7 and 8 return to both.", 26, MUTED, True, a=ctx.p("later", 0.5))
    finish(ctx)


# ---------------------------------------------------------------- part C
def scene_disc1(ctx):
    stage(ctx)
    cv = ctx.cv
    t0 = ctx.cue("run") or 0.0
    order = R.G and R.run(R.G, "Arch", "stack")[-1]["marked_after"]
    marked = {}
    for i, v in enumerate(order):
        marked[v] = ctx.ramp(t0 + 0.5 * i, t0 + 0.5 * i + 0.3)
    nv = ctx.p("never", 0.5)
    GV2.draw(ctx, marked=marked, badges={v: ("x", nv) for v in ("Mill", "Nest", "Oak")},
             rings={"Arch": (BLUE, 1.0)})
    bubbles(ctx, GV2, marked, 0.5)
    cv.text(380, 880, "the metro", 26, MUTED, True, anchor="mm")
    cv.text(970, 880, "the ferry network", 26, MUTED, True, anchor="mm")
    panel_card(ctx, "WHEN THE PILE IS EMPTY")
    cv.text(1330, 200, "the search stops", 40, INK, True)
    cv.text(1330, 260, "after the whole metro", 40, INK, True)
    cv.text(1330, 380, "Mill, Nest, Oak:", 34, RED, True, a=nv)
    cv.text(1330, 430, "never reached", 34, RED, True, a=nv)
    finish(ctx)


GROUP_CODE = [
    "def count_networks(graph):",
    "    visited = set()",
    "    networks = 0",
    "    for station in graph:",
    "        if station not in visited:",
    "            networks = networks + 1",
    "            explore(graph, station, visited)",
    "    return networks",
]
GROUP_CARD = CodeCard(GROUP_CODE, size=36, lh=62)


def scene_wrapper(ctx):
    cv = ctx.cv
    hl = []
    if ctx.reached("w1"):
        hl.append((4, None))
    if ctx.reached("w2"):
        hl = [(5, None)]
    if ctx.reached("w3"):
        hl = [(6, None), (7, None)]
    GROUP_CARD.draw(ctx, hl=hl, title="THE LOOP AROUND THE SEARCH")
    panel_card(ctx, "IN WORDS")
    notes = [("w1", "go through every station", "for each station on the map", BLUE),
             ("w2", "not visited yet?", "then it is in a new network", ACCENT_DARK),
             ("w3", "count it, and search", "run the search from here, marking as we go", GREEN)]
    y = 180
    for cue, head, body, col in notes:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 180, 20, fill=PAPER, outline=col, width=4, a=a)
        cv.text(1344, y + 16, head, 32, col, True, a=a)
        draw_wrapped(cv, 1344, y + 72, body, 28, 490, INK, False, a=a)
        y += 200
    finish(ctx)


def scene_wrapper_code(ctx):
    boxes = [(2, "set()", GREEN, "c_set"), (3, "0", BLUE, "c_zero"), (4, "for station in graph:", BLUE, "c_for"),
             (5, "not in", RED, "c_not"), (6, "networks + 1", ACCENT_DARK, "c_add"),
             (7, "explore(graph, station, visited)", GREEN, "c_call")]
    GROUP_CARD.draw(ctx, boxes=boxes, title="PYTHON")
    notes_panel(ctx, "READING IT", [
        ("c_zero", "networks = 0", "a counter. No network has been found yet.", BLUE),
        ("c_not", "not in", "asks: is this station missing from visited?", RED),
        ("c_call", "explore(...)", "our search, from the last video. It adds every station it marks to visited.", GREEN)])
    finish(ctx)


def scene_count_result(ctx):
    stage(ctx)
    cv = ctx.cv
    g1 = [ctx.ramp((ctx.cue("g1") or 0) + 0.4 * i, (ctx.cue("g1") or 0) + 0.4 * i + 0.3) if ctx.cue("g1") else 0
          for i in range(7)]
    g2 = [ctx.ramp((ctx.cue("g2") or 0) + 0.4 * i, (ctx.cue("g2") or 0) + 0.4 * i + 0.3) if ctx.cue("g2") else 0
          for i in range(3)]
    marked = {v: p for v, p in zip(R.PEOPLE, g1)}
    marked.update({v: p for v, p in zip(["Mill", "Nest", "Oak"], g2)})
    fills = {}
    for v, p in marked.items():
        fills[v] = (ACCENT if v in R.PEOPLE else BLUE, p)
    GV2.draw(ctx, fills=fills)
    bubbles(ctx, GV2, marked, 0.5)
    groups = (1 if g1[0] > 0.5 else 0) + (1 if g2[0] > 0.5 else 0)
    panel_card(ctx, "COUNTING NETWORKS")
    cv.text(1330, 190, "networks found:", 32, MUTED, True)
    cv.text(1330, 240, str(groups), 150, ACCENT, True)
    cv.text(1330, 450, "Arch  →  7 stations", 32, ACCENT_DARK, True, a=ctx.p("g1", 0.4))
    cv.text(1330, 500, "Mill  →  3 stations", 32, BLUE, True, a=ctx.p("g2", 0.4))
    cv.text(1330, 620, "still  O(V + E)", 44, GREEN, True, a=ctx.p("lin", 0.5))
    cv.text(1330, 676, "each vertex and edge once", 26, MUTED, False, a=ctx.p("lin", 0.5))
    finish(ctx)


def scene_dir1(ctx):
    stage(ctx)
    cv = ctx.cv
    GVD.draw(ctx, rings={"Arch": (BLUE, ctx.pulse("ex", 1.2))})
    panel_card(ctx, "ONE-WAY TRACKS")
    cv.text(1330, 200, "Arch → Bay", 46, INK, True)
    draw_wrapped(cv, 1330, 270, "Trains run only from Arch to Bay.", 32, 500, MUTED, False)
    a = ctx.p("same", 0.5)
    cv.rrect(1316, 400, 1854, 640, 20, fill=ACCENT_SOFT, outline=ACCENT, width=4, a=a)
    cv.text(1344, 424, "the code does not change", 32, ACCENT_DARK, True, a=a)
    draw_wrapped(cv, 1344, 480, "a marked station adds a token for each arrow leaving it", 28, 480, INK, False, a=a)
    finish(ctx)


def scene_dir2(ctx):
    stage(ctx)
    cv = ctx.cv
    t0 = ctx.cue("run") or 0.0
    order = R.REACHED_DIRECTED
    marked = {v: (ctx.ramp(t0 + 0.7 * i, t0 + 0.7 * i + 0.3) if ctx.cue("run") else 0) for i, v in enumerate(order)}
    nv = ctx.p("never", 0.5)
    GVD.draw(ctx, marked=marked, rings={"Arch": (BLUE, 1.0)},
             badges={"Dock": ("x", nv), "Gate": ("x", nv)})
    bubbles(ctx, GVD, marked, 0.6)
    panel_card(ctx, "FROM ARCH")
    cv.text(1330, 200, "can reach:", 32, MUTED, True)
    cv.text(1330, 250, "Bay  Cove  East  Fort", 38, ACCENT_DARK, True, a=ctx.p("run", 0.4))
    cv.text(1330, 350, "cannot reach:", 32, MUTED, True, a=nv)
    cv.text(1330, 400, "Dock  Gate", 44, RED, True, a=nv)
    draw_wrapped(cv, 1330, 500, "No arrow points into Dock or Gate. Reachability is no longer symmetric.", 28, 500, INK, False,
                 a=ctx.p("sym", 0.5))
    finish(ctx)


def scene_dir_tree(ctx):
    stage(ctx)
    cv = ctx.cv
    par = R.DIRECTED[-1]["parent_after"]
    es = {}
    for v, p in par.items():
        if p:
            es[GVD.key(p, v)] = (ACCENT, 12, 1.0)
    marked = {v: 1.0 for v in R.REACHED_DIRECTED}
    fade = ctx.p("tree", 0.6)
    for k in [GVD.key(a, b) for a, b, _ in GVD.edges]:
        if k not in es:
            es[k] = (LINE, 6, 1.0 - 0.7 * fade)
    GVD.draw(ctx, marked=marked, estyle=es, badges={"Dock": ("x", 1.0), "Gate": ("x", 1.0)})
    panel_card(ctx, "BOOK: PDF p.223")
    draw_wrapped(cv, 1330, 190, "The came-from arrows form a tree pointing away from Arch.", 30, 500, INK, False)
    draw_wrapped(cv, 1330, 330, "It is a tree of the stations Arch can reach, not a spanning tree of the whole map.", 30, 500,
                 RED, True, a=ctx.p("notspan", 0.5))
    draw_wrapped(cv, 1330, 520, "Stacks, queues, and priority queues all still work.", 28, 500, MUTED, False,
                 a=ctx.p("all", 0.5))
    finish(ctx)


# ---------------------------------------------------------------- flood fill
GRID = [
    "..........",
    ".##...RR..",
    ".###..RR..",
    ".##.......",
    "......##..",
    "..R...###.",
    "..........",
]
CELL, GX, GY = 84, 130, 200
COLORS = {".": (255, 255, 255), "#": (96, 150, 214), "R": (222, 96, 96)}


def region(start):
    seen, order, q = {start}, [], [start]
    while q:
        r, c = q.pop(0)
        order.append((r, c))
        for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(GRID) and 0 <= nc < len(GRID[0]) and (nr, nc) not in seen and GRID[nr][nc] == GRID[start[0]][start[1]]:
                seen.add((nr, nc))
                q.append((nr, nc))
    return order


CLICK = (2, 2)
FILL_ORDER = region(CLICK)


def draw_grid(ctx, filled=None, edges=0.0, cursor=0.0):
    cv = ctx.cv
    filled = filled or {}
    for r, row in enumerate(GRID):
        for c, ch in enumerate(row):
            x, y = GX + c * CELL, GY + r * CELL
            col = COLORS[ch]
            if (r, c) in filled:
                col = mix(col, ORANGE, filled[(r, c)])
            cv.rrect(x + 2, y + 2, x + CELL - 2, y + CELL - 2, 8, fill=col, outline=(200, 205, 214), width=2)
    if edges > 0:
        for (r, c) in FILL_ORDER:
            for dr, dc in ((0, 1), (1, 0)):
                if (r + dr, c + dc) in FILL_ORDER:
                    p0 = (GX + c * CELL + CELL / 2, GY + r * CELL + CELL / 2)
                    p1 = (GX + (c + dc) * CELL + CELL / 2, GY + (r + dr) * CELL + CELL / 2)
                    cv.line(p0, p1, INK, 6, a=edges)
        for (r, c) in FILL_ORDER:
            cv.circle(GX + c * CELL + CELL / 2, GY + r * CELL + CELL / 2, 12, fill=INK, a=edges)
    if cursor > 0:
        x, y = GX + CLICK[1] * CELL + CELL / 2, GY + CLICK[0] * CELL + CELL / 2
        cv.rrect(x - 40, y - 40, x + 40, y + 40, 12, outline=BLUE, width=6, a=cursor)
        cv.text(x + 60, y + 70, "click", 30, BLUE, True, anchor="mm", a=cursor)


def scene_flood1(ctx):
    stage(ctx)
    cv = ctx.cv
    draw_grid(ctx, edges=ctx.p("edges", 0.6), cursor=ctx.p("click", 0.5))
    panel_card(ctx, "PIXELS AS A GRAPH")
    rows = [("pa", "pixel", "vertex"), ("pb", "same-color neighbors", "edge"), ("pc", "the paint bucket", "reachability")]
    y = 190
    for cue, a_, b_ in rows:
        a = ctx.p(cue, 0.45)
        cv.rrect(1316, y, 1854, y + 150, 18, fill=PAPER, outline=ACCENT, width=3, a=a)
        cv.text(1342, y + 18, a_, 28, MUTED, True, a=a)
        cv.text(1342, y + 70, b_, 44, ACCENT_DARK, True, a=a)
        y += 170
    finish(ctx)


def scene_flood2(ctx):
    stage(ctx)
    cv = ctx.cv
    t0 = ctx.cue("fill") or 0.0
    filled = {}
    for i, rc in enumerate(FILL_ORDER):
        if ctx.cue("fill") is not None:
            p = ctx.ramp(t0 + 0.4 * i, t0 + 0.4 * i + 0.3)
            if p > 0:
                filled[rc] = p
    draw_grid(ctx, filled=filled, edges=0.0, cursor=0.0)
    other = ctx.p("other", 0.5)
    cv.rrect(GX + 6 * CELL - 6, GY + 4 * CELL - 6, GX + 9 * CELL + 6, GY + 6 * CELL + 6, 14, outline=RED, width=5, a=other)
    cv.text(GX + 7.5 * CELL, GY + 6.5 * CELL + 16, "same color, but not connected", 26, RED, True, anchor="mm", a=other)
    done = sum(1 for p in filled.values() if p > 0.5)
    panel_card(ctx, "RECOLOR AS WE MARK")
    cv.text(1330, 200, "pixels filled:", 30, MUTED, True)
    cv.text(1330, 250, f"{done} of {len(FILL_ORDER)}", 64, ORANGE, True)
    draw_wrapped(cv, 1330, 380, "Marked and recolored in the same step, so the color itself is the mark.", 28, 500, INK, False)
    finish(ctx)


def scene_flood3(ctx):
    stage(ctx)
    cv = ctx.cv
    draw_grid(ctx, filled={rc: 1.0 for rc in FILL_ORDER})
    panel_card(ctx, "A REDUCTION  (PDF p.224)")
    rows = [("r1", "n × n pixels", "n² vertices", INK), ("r2", "at most", "2n² edges", INK),
            ("r3", "search time", "O(n²)", ACCENT)]
    y = 190
    for cue, a_, b_, col in rows:
        a = ctx.p(cue, 0.45)
        cv.text(1330, y, a_, 28, MUTED, True, a=a)
        cv.text(1330, y + 40, b_, 52, col, True, a=a)
        y += 130
    draw_wrapped(cv, 1330, 620, "We used reachability as a black box. How the search works is irrelevant; only what it promises.", 27,
                 500, INK, False, a=ctx.p("black", 0.5))
    finish(ctx)


def scene_recap2(ctx):
    stage(ctx)
    cv = ctx.cv
    cards = [("c1", "About 2E + 1 tokens", "so a stack or queue search is linear: O(V + E)"),
             ("c2", "Swap the pile, swap the search", "stack · queue · priority queue"),
             ("c3", "Loop over every station", "to cover every network; count them for free"),
             ("c4", "Arrows change who is reached", "not the code")]
    y = 150
    for i, (cue, head, sub) in enumerate(cards):
        a = ctx.p(cue, 0.5)
        cv.rrect(80, y, 1180, y + 150, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
        cv.circle(150, y + 75, 34, fill=ACCENT, a=a)
        cv.text(150, y + 74, str(i + 1), 38, WHITE, True, anchor="mm", a=a)
        cv.text(215, y + 22, head, 40, ACCENT_DARK, True, a=a)
        cv.text(215, y + 86, sub, 28, INK, False, a=a)
        y += 174
    ta = ctx.p("next", 0.5)
    cv.rrect(80, 860 - 20, 1180, 900, 20, fill=BLUE_SOFT, outline=BLUE, width=3, a=ta)
    cv.text(630, 870, "Next: counting paths, from class", 32, BLUE, True, anchor="mm", a=ta)
    finish(ctx)
