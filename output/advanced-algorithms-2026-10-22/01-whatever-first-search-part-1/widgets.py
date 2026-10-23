"""Reusable drawing pieces: chrome, subtitles, the Colony graph, panels."""
from __future__ import annotations

import math

from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BAND, BLUE, BLUE_SOFT, EDGES, GRAY, GRAY_SOFT, GREEN, H, INK, LINE,
    MUTED, PANEL_LINE, PAPER, PINK, POS, R_VERT, RED, W, WHITE, YELLOW, Canvas, NullCanvas, clamp, ease,
    edge_pts, font, lerp, mix, point_along, sprite,
)

TOP = 96
BAND_Y = 930
PANEL = (1290, 118, 1880, 906)
SERIES = "GRAPH SEARCH  ·  VIDEO 1 OF 6"
TITLE = "Whatever-First Search, Part 1"


class Ctx:
    """Everything a scene needs to draw one frame at local time t."""

    def __init__(self, cv, t, beat):
        self.cv = cv
        self.t = t
        self.b = beat
        self.cues = beat["cues"]
        self.sig = []

    def cue(self, name):
        return self.cues.get(name)

    def p(self, name, dur=0.4):
        c = self.cues.get(name)
        v = 0.0 if c is None else ease(clamp((self.t - c) / dur))
        self.sig.append(round(v, 3))
        return v

    def reached(self, name):
        c = self.cues.get(name)
        r = c is not None and self.t >= c
        self.sig.append(1 if r else 0)
        return r

    def ramp(self, t0, t1):
        v = clamp((self.t - t0) / max(1e-6, (t1 - t0)))
        self.sig.append(round(v, 3))
        return v

    def pulse(self, name, dur=1.0):
        c = self.cues.get(name)
        if c is None:
            v = 0.0
        else:
            x = clamp((self.t - c) / dur)
            v = math.sin(math.pi * x)
        self.sig.append(round(v, 3))
        return v

    def blink(self, name, period=0.9):
        """Looping 0..1 pulse that starts at a cue and never stops."""
        c = self.cues.get(name)
        if c is None or self.t < c:
            self.sig.append(0)
            return 0.0
        v = 0.5 - 0.5 * math.cos(2 * math.pi * (self.t - c) / period)
        self.sig.append(round(v, 3))
        return v


# ---------------------------------------------------------------- text utils
def wrap(text, size, width, bold=False, mono=False):
    f = font(size, bold, mono)
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if f.getlength(trial) / 2 <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(cv, x, y, text, size, width, color=INK, bold=False, mono=False, lead=1.3, a=1.0, anchor="la"):
    lines = wrap(text, size, width, bold, mono)
    for i, ln in enumerate(lines):
        cv.text(x, y + i * size * lead, ln, size, color, bold, mono, anchor, a)
    return len(lines) * size * lead


# ---------------------------------------------------------------- chrome
def chrome(ctx):
    cv, b = ctx.cv, ctx.b
    cv.rrect(0, 0, W, TOP, 0, fill=WHITE)
    cv.rrect(0, 0, W, 8, 0, fill=ACCENT)
    cv.line((0, TOP), (W, TOP), PANEL_LINE, 2)
    cv.text(48, 26, SERIES, 24, ACCENT, True)
    cv.text(48, 54, TITLE, 30, INK, True)
    cv.text(W / 2, 30, b.get("topic", ""), 34, INK, True, anchor="ma")
    if b.get("book"):
        s = b["book"]
        w = cv.text_w(s, 26, True) + 44
        cv.rrect(W - 48 - w, 28, W - 48, 70, 21, fill=BLUE_SOFT, outline=BLUE, width=2)
        cv.text(W - 48 - w / 2, 49, s, 26, BLUE, True, anchor="mm")
    # caption band
    cv.rrect(0, BAND_Y, W, H, 0, fill=BAND)
    subtitles(ctx)


def subtitles(ctx):
    cv, b, t = ctx.cv, ctx.b, ctx.t
    chunks = b["chunks"]
    ci = -1
    for i, ch in enumerate(chunks):
        if t >= ch["t0"] - 0.04:
            ci = i
    wi = -1
    if ci >= 0:
        for k in ch_words(chunks[ci]):
            if t >= b["words"][k]["t0"]:
                wi = k
    ctx.sig.append((ci, wi))
    if ci < 0:
        return
    ch = chunks[ci]
    size = 46
    lines = ch["lines"]
    total_h = len(lines) * 62
    y0 = BAND_Y + (H - BAND_Y - total_h) / 2 + 2
    for li, line_words in enumerate(lines):
        widths = [cv.text_w(b["words"][k]["disp"], size, True) for k in line_words]
        space = cv.text_w(" ", size, True)
        total = sum(widths) + space * (len(widths) - 1)
        x = W / 2 - total / 2
        for k, wd in zip(line_words, widths):
            word = b["words"][k]
            if k == wi:
                col = YELLOW
            elif t >= word["t0"]:
                col = WHITE
            else:
                col = (140, 150, 168)
            cv.text(x, y0 + li * 62, word["disp"], size, col, True)
            x += wd + space


def ch_words(chunk):
    return [k for line in chunk["lines"] for k in line]


# ---------------------------------------------------------------- predict
def predict_chip(ctx):
    b = ctx.b
    if not b.get("predict"):
        return
    cv, t = ctx.cv, ctx.t
    q0 = ctx.cues.get("q", b["pause_start"])
    a = ease(clamp((t - q0) / 0.35))
    ctx.sig.append(round(a, 3))
    if a <= 0:
        return
    x0, y0, x1, y1 = 150, 800, 1130, 912
    cv.rrect(x0, y0, x1, y1, 26, fill=WHITE, outline=ACCENT, width=4, a=a)
    cv.text(x0 + 150, y0 + 18, "PAUSE AND PREDICT", 24, ACCENT, True, a=a)
    draw_wrapped(cv, x0 + 150, y0 + 52, b["predict"], 34, 780, INK, True, a=a, lead=1.2)
    left = clamp(1 - (t - b["pause_start"]) / max(0.01, b["pause_len"])) if t >= b["pause_start"] else 1.0
    ctx.sig.append(round(left, 3))
    cx, cy = x0 + 70, (y0 + y1) / 2
    cv.circle(cx, cy, 40, fill=PAPER, outline=GRAY, width=6, a=a)
    # countdown arc approximated with a polygon wedge
    pts = [(cx, cy)]
    n = max(2, int(60 * left))
    for i in range(n + 1):
        ang = -math.pi / 2 + 2 * math.pi * left * i / n
        pts.append((cx + 33 * math.cos(ang), cy + 33 * math.sin(ang)))
    if left > 0.01:
        cv.polygon(pts, ACCENT, a=a)
    secs = math.ceil(left * b["pause_len"] - 1e-6)
    cv.text(cx, cy, str(max(0, secs)), 34, INK if left < 0.5 else WHITE, True, anchor="mm", a=a)


# ---------------------------------------------------------------- graph
def ekey(u, v):
    return tuple(sorted((u, v)))


def draw_graph(ctx, marked=None, rings=None, estyle=None, qmarks=0.0, vis=None, show_cave=True,
               cave_shake=0.0, edge_vis=None, badges=None, labels=True, vfade=None):
    """marked: {v: 0..1}; rings: {v: (color, alpha)}; estyle: {(u,v): (color,width,alpha)}"""
    cv = ctx.cv
    marked = marked or {}
    rings = rings or {}
    estyle = estyle or {}
    badges = badges or {}
    vfade = vfade or {}
    if show_cave:
        shake = math.sin(ctx.t * 40) * 4 * cave_shake
        x0, y0, x1, y1 = 1050 + shake, 330, 1225 + shake, 735
        cv.rrect(x0, y0, x1, y1, 30, fill=(240, 236, 228), outline=GRAY, width=3)
        for (bx, by, r) in [(1090, 700, 20), (1140, 708, 26), (1195, 698, 19), (1115, 676, 15), (1170, 680, 17)]:
            cv.circle(bx + shake, by, r, fill=(150, 142, 130), outline=(110, 104, 94), width=2)
        cv.text((x0 + x1) / 2, 342, "cut off", 22, MUTED, True, anchor="ma")
    for (a, b, _bulge) in EDGES:
        key = ekey(a, b)
        col, wd, al = estyle.get(key, (LINE, 6, 1.0))
        if edge_vis is not None and key in edge_vis:
            al *= edge_vis[key]
        pts = edge_pts(a, b)
        cv.poly_line(pts, col, wd, al)
    for v, (x, y) in POS.items():
        mf = marked.get(v, 0.0)
        fa = vfade.get(v, 1.0)
        fill = mix(WHITE, ACCENT, mf)
        ring_col = mix(INK, ACCENT_DARK, mf)
        cv.circle(x, y, R_VERT, fill=fill, outline=ring_col, width=5, a=fa)
        if labels:
            cv.text(x, y - 1, v, 40, mix(INK, WHITE, mf), True, anchor="mm", a=fa)
        if v in rings:
            col, al = rings[v]
            cv.circle(x, y, R_VERT + 12, outline=col, width=7, a=al)
        if v in badges:
            kind, al = badges[v]
            if kind == "x":
                cv.circle(x + 30, y - 30, 17, fill=RED, a=al)
                cv.line((x + 23, y - 37), (x + 37, y - 23), WHITE, 5, al)
                cv.line((x + 37, y - 37), (x + 23, y - 23), WHITE, 5, al)
    if qmarks > 0:
        for v, (x, y) in POS.items():
            if v != "S":
                qx, qy = (x + 60, y) if v in ("X", "Y") else (x + 40, y - 52)
                cv.text(qx, qy, "?", 38, MUTED, True, anchor="mm", a=qmarks * 0.9)


def wrinkles(ctx, x, y, flip=False, scale=1.0, tilt=0.0, a=1.0, dizzy=0.0, sniff=0.0):
    cv = ctx.cv
    if isinstance(cv, NullCanvas):
        return
    sp = sprite(scale, flip, tilt)
    cx, cy = x, y - 58 * scale
    cv.paste(sp, cx, cy, a)
    if dizzy > 0:
        for i in range(3):
            ang = ctx.t * 7 + i * 2.1
            cv.circle(cx + (8 if not flip else -8) + 30 * math.cos(ang) * scale,
                      cy - 40 * scale + 9 * math.sin(ang) * scale, 5, fill=BLUE, a=dizzy)
    if sniff > 0:
        for i in range(3):
            off = (60 + i * 12) * (1 if not flip else -1)
            cv.line((cx + off * scale, cy - 6 * scale + (i - 1) * 9 * scale),
                    (cx + (off + 14 * (1 if not flip else -1)) * scale, cy - 6 * scale + (i - 1) * 9 * scale),
                    MUTED, 3, sniff)


def at_vertex(v, dy=0):
    x, y = POS[v]
    return x + 6, y - R_VERT + 6 + dy


# ---------------------------------------------------------------- panels
def panel_card(ctx, title, rect=PANEL):
    cv = ctx.cv
    x0, y0, x1, y1 = rect
    cv.rrect(x0, y0, x1, y1, 24, fill=WHITE, outline=PANEL_LINE, width=3)
    if title:
        cv.text(x0 + 28, y0 + 20, title, 24, MUTED, True)
    return rect


def glossary(ctx, known, new):
    """known: terms shown fully; new: {term: cue_name} that appear on a cue. Slots fill in order."""
    cv = ctx.cv
    panel_card(ctx, "WORDS WE'VE MET")
    defs = {
        "vertex": "a dot  (a chamber)",
        "edge": "a line  (a tunnel)",
        "graph": "vertices + edges",
        "reachability": "which vertices can you reach?",
        "mark": "a \"been here\" flag on a vertex",
    }
    slots = [t for t in known]
    slots += sorted(new, key=lambda t: ctx.cues.get(new[t], 1e9))
    y = 168
    for term in slots:
        is_new = term in new
        a = ctx.p(new[term], 0.45) if is_new else 1.0
        if a > 0:
            cv.rrect(1316, y, 1854, y + 118, 18, fill=ACCENT_SOFT if is_new else PAPER,
                     outline=ACCENT if is_new else PANEL_LINE, width=3, a=a)
            cv.text(1344, y + 12, term, 36, ACCENT_DARK, True, a=a)
            cv.text(1344, y + 66, defs[term], 28, INK, False, a=a)
        y += 130


RULES = [
    "Start the pile with one token: (nobody, start).",
    "While the pile isn't empty: take one token out.",
    "If its vertex has no mark: mark it, remember its parent, add a token for every edge out of it.",
    "If its vertex is already marked: throw the token away.",
]


def rules_panel(ctx, lit, cue=None, prior=(), all_dim=False):
    """Show the four rules. `prior` rules are fully visible; rule `lit` fades in at `cue`
    and is highlighted; any other rule is a faint placeholder."""
    cv = ctx.cv
    panel_card(ctx, "THE FOUR RULES")
    y = 180
    pa = ctx.p(cue, 0.4) if cue else 1.0
    for i, txt in enumerate(RULES):
        is_lit = (i == lit) and not all_dim
        if i in prior:
            a = 1.0
        elif i == lit:
            a = max(pa, 0.18)
        else:
            a = 0.18
        h = 158
        cv.rrect(1316, y, 1854, y + h, 20, fill=ACCENT_SOFT if is_lit else WHITE,
                 outline=ACCENT if is_lit else PANEL_LINE, width=4 if is_lit else 3, a=a)
        cv.circle(1362, y + 42, 26, fill=ACCENT if is_lit else GRAY, a=a)
        cv.text(1362, y + 41, str(i + 1), 30, WHITE, True, anchor="mm", a=a)
        draw_wrapped(cv, 1404, y + 20, txt, 27, 430, INK, is_lit, a=a, lead=1.25)
        y += h + 12


def token_pill(cv, x, y, label, a=1.0, hi=False, strike=False, w=250, h=30, fs=22):
    cv.rrect(x, y, x + w, y + h, h / 2, fill=ACCENT_SOFT if hi else WHITE,
             outline=ACCENT if hi else GRAY, width=3 if hi else 2, a=a)
    cv.text(x + w / 2, y + h / 2, label, fs, INK, True, True, anchor="mm", a=a)
    if strike:
        cv.line((x + 18, y + h / 2), (x + w - 18, y + h / 2), RED, 3, a)


def tag(cv, x, y, text, color, a=1.0, size=26):
    """Small white label pill centered at x, y."""
    w = cv.text_w(text, size, True) + 28
    cv.rrect(x - w / 2, y - size * 0.8, x + w / 2, y + size * 0.8, size * 0.8, fill=WHITE, outline=color, width=3, a=a)
    cv.text(x, y, text, size, color, True, anchor="mm", a=a)
