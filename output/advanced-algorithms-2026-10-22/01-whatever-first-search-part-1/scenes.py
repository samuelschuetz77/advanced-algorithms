"""Video 01 scenes: animation code for every beat.

Narration markup:
  [[cue]]word   -> cue fires when `word` starts being spoken
  {S}           -> shown as S, spoken "ess" (phonetic letters, see pipeline.PHON)
  {a|b}         -> shown as a, spoken as b
"""
from __future__ import annotations

import math
import random

import trace_check
from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, INK, LINE, MUTED, PANEL_LINE,
    PAPER, POS, R_VERT, RED, WHITE, clamp, ease, full_edge_pts, lerp, mix, point_along,
)
from widgets import (
    Ctx, chrome, draw_graph, draw_wrapped, ekey, glossary, panel_card, predict_chip, rules_panel, token_pill,
    wrinkles, wrap,
)

# ------------------------------------------------------------------ shared
TOPIC_MEET = "Meet Wrinkles"
random.seed(7)
SPECKS = [(random.uniform(45, 1245), random.uniform(125, 910), random.uniform(2.5, 6.5)) for _ in range(70)]


def soil(ctx):
    cv = ctx.cv
    cv.rrect(30, 112, 1258, 916, 28, fill=(246, 240, 228), outline=(228, 218, 200), width=3)
    for x, y, r in SPECKS:
        cv.circle(x, y, r, fill=(232, 222, 202))


def finish(ctx):
    predict_chip(ctx)
    chrome(ctx)


def walker(ctx, wps):
    """wps: [(time, vertex), ...] sorted by time. Returns (x, y, flip, moving)."""
    t = ctx.t
    x, y = POS[wps[0][1]]
    flip, moving = False, False
    if t >= wps[0][0]:
        x, y = POS[wps[-1][1]]
        for (t0, v0), (t1, v1) in zip(wps, wps[1:]):
            if t0 <= t < t1:
                if v0 == v1:
                    x, y = POS[v0]
                else:
                    f = ease((t - t0) / (t1 - t0))
                    x, y = point_along(full_edge_pts(v0, v1), f)
                    flip = POS[v1][0] < POS[v0][0]
                    moving = True
                break
            if t >= t1:
                x, y = POS[v1]
                flip = POS[v1][0] < POS[v0][0] if v0 != v1 else flip
    ctx.sig.append((round(x), round(y), flip))
    return x, y, flip, moving


def sprite_at(ctx, x, y, flip=False, scale=1.0, a=1.0, **kw):
    wrinkles(ctx, x, y - 10, flip=flip, scale=scale, a=a, **kw)


# ------------------------------------------------------------------ PART 1
def scene_1(ctx):
    cv = ctx.cv
    soil(ctx)
    wp = ctx.pulse("w", 1.2)
    rings = {v: (BLUE, ctx.pulse("chambers", 1.0)) for v in POS}
    estyle = {}
    tp = ctx.pulse("tunnels", 1.0)
    for a, b, _ in __import__("engine").EDGES:
        estyle[ekey(a, b)] = (mix((122, 132, 148), ACCENT, tp), 6 + 3 * tp, 1.0)
    draw_graph(ctx, rings=rings, estyle=estyle)
    sprite_at(ctx, *POS["S"], scale=1.15)
    if wp > 0:
        cv.circle(POS["S"][0] + 10, POS["S"][1] - 72, 92, outline=BLUE, width=6, a=wp * 0.9)
    glossary(ctx, known=(), new={"vertex": "vertex", "edge": "edge", "graph": "graph"})
    finish(ctx)


def scene_2(ctx):
    cv = ctx.cv
    soil(ctx)
    ring = ctx.p("nest", 0.4)
    q = ctx.p("follow", 0.5)
    path_a = ctx.p("follow", 0.9)
    shake = ctx.pulse("cave", 1.2)
    estyle = {ekey("S", "A"): (BLUE, 9, path_a * 0.9 + 0.1 * 0), ekey("A", "D"): (BLUE, 9, path_a * 0.9)}
    estyle = {k: (v[0], v[1], max(v[2], 0.0)) for k, v in estyle.items() if v[2] > 0}
    draw_graph(ctx, rings={"S": (BLUE, ring)}, estyle=estyle, qmarks=q, cave_shake=shake)
    sprite_at(ctx, *POS["S"], scale=1.15)
    glossary(ctx, known=("vertex", "edge", "graph"), new={"reachability": "reach"})
    finish(ctx)


LOOP = ["S", "A", "B", "C"]


def scene_3(ctx):
    cv = ctx.cv
    soil(ctx)
    go = ctx.cue("go") or 0.0
    per = 0.62
    wps = [(go, "S")]
    seq = []
    cur = "S"
    order = ["A", "B", "C", "S"]
    tt = go
    for i in range(40):
        nxt = order[i % 4]
        wps.append((tt + per, nxt))
        tt += per
    t = ctx.t
    steps = int(clamp((t - go) / per, 0, 40)) if t >= go else 0
    ctx.sig.append(steps)
    x, y, flip, moving = walker(ctx, wps)
    loops = clamp((steps - 3) / 3.0, 0, 1)
    ctx.sig.append(round(loops, 2))
    estyle = {}
    for u, v in [("S", "A"), ("A", "B"), ("B", "C"), ("C", "S")]:
        estyle[ekey(u, v)] = (mix(LINE, RED, loops), 6 + 4 * loops, 1.0)
    draw_graph(ctx, estyle=estyle)
    dizzy = clamp((steps - 4) / 3.0, 0, 1)
    sprite_at(ctx, x, y, flip=flip, scale=1.0, dizzy=dizzy)
    # counter
    cv.rrect(60, 130, 330, 200, 18, fill=WHITE, outline=PANEL_LINE, width=3)
    cv.text(84, 148, "steps:", 30, MUTED, True)
    cv.text(310, 164, str(steps), 40, RED if steps > 8 else INK, True, anchor="rm")
    glossary(ctx, known=("vertex", "edge", "graph", "reachability"), new={})
    finish(ctx)


def scene_4(ctx):
    cv = ctx.cv
    soil(ctx)
    ts = ctx.cue("scent") or 0.0
    tm = ctx.cue("turn") or ts + 8.0
    wps = [
        (ts, "S"), (ts + 1.1, "S"),
        (ts + 2.0, "A"), (ts + 2.7, "A"),
        (ts + 3.6, "B"), (ts + 4.4, "B"),
        (tm - 1.0, "B"), (tm, "A"), (tm + 0.55, "A"), (tm + 1.6, "B"),
    ]
    # make sure the times are increasing
    for i in range(1, len(wps)):
        if wps[i][0] < wps[i - 1][0]:
            wps[i] = (wps[i - 1][0], wps[i][1])
    x, y, flip, moving = walker(ctx, wps)
    marked = {
        "S": ctx.ramp(ts + 0.1, ts + 0.6),
        "A": ctx.ramp(ts + 1.9, ts + 2.4),
        "B": ctx.ramp(ts + 3.5, ts + 4.0),
    }
    sn = ctx.pulse("turn", 0.6) if ctx.cue("turn") else 0
    sniff = clamp(ctx.ramp(tm - 0.1, tm + 0.1) - ctx.ramp(tm + 0.5, tm + 0.7), 0, 1)
    ring = {"A": (BLUE, sniff)} if sniff > 0 else {}
    draw_graph(ctx, marked=marked, rings=ring)
    sprite_at(ctx, x, y, flip=flip, scale=1.0, sniff=sniff)
    glossary(ctx, known=("vertex", "edge", "graph", "reachability"), new={"mark": "marks"})
    finish(ctx)


