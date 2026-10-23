"""Reusable drawing pieces: chrome, subtitles, the Colony graph, panels."""
from __future__ import annotations

import math

from engine import (
    ACCENT, ACCENT_DARK, ACCENT_SOFT, BAND, BLUE, BLUE_SOFT, GRAY, GRAY_SOFT, GREEN, H, INK, LINE, MUTED,
    PANEL_LINE, PAPER, PINK, RED, W, WHITE, YELLOW, Canvas, NullCanvas, clamp, ease, font, lerp, mix,
)

TOP = 96
BAND_Y = 930
PANEL = (1290, 118, 1880, 906)
CONFIG = {"series": "GRAPH SEARCH", "title": ""}


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
    cv.text(48, 26, CONFIG["series"], 24, ACCENT, True)
    cv.text(48, 54, CONFIG["title"], 30, INK, True)
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


# ---------------------------------------------------------------- shared panels
def panel_card(ctx, title, rect=PANEL):
    cv = ctx.cv
    x0, y0, x1, y1 = rect
    cv.rrect(x0, y0, x1, y1, 24, fill=WHITE, outline=PANEL_LINE, width=3)
    if title:
        cv.text(x0 + 28, y0 + 20, title, 24, MUTED, True)
    return rect


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


def notes_panel(ctx, title, notes, rect=PANEL):
    """notes: [(cue, head, body, color)] cards that appear on their cue. Cards size to their text."""
    cv = ctx.cv
    panel_card(ctx, title, rect)
    width = rect[2] - rect[0] - 100
    y = rect[1] + 50
    for cue, head, body, color in notes:
        a = ctx.p(cue, 0.4) if cue else 1.0
        lines = wrap(body, 27, width)
        h = 84 + len(lines) * 33
        if a > 0:
            size = min(40, int(width / (0.56 * max(1, len(head)))))
            cv.rrect(rect[0] + 26, y, rect[2] - 26, y + h, 18, fill=PAPER, outline=color, width=4, a=a)
            cv.text(rect[0] + 54, y + 16, head, size, color, True, True, a=a)
            draw_wrapped(cv, rect[0] + 54, y + 70, body, 27, width, INK, False, lead=1.22, a=a)
        y += h + 14


def values_strip(ctx, title, rows, y0=700):
    cv = ctx.cv
    cv.line((1330, y0 - 14), (1840, y0 - 14), PANEL_LINE, 3)
    cv.text(1330, y0, title, 22, MUTED, True)
    for i, (k, v) in enumerate(rows):
        cv.text(1330, y0 + 36 + i * 38, f"{k} = {v}", 26, INK, True, True)


class CodeCard:
    """Python code on a white card. Boxes are found by substring, so no hand-counted columns."""

    def __init__(self, lines, rect=(40, 126, 1246, 906), size=34, lh=54, x_off=110, y_off=24, numbers=True):
        self.lines, self.rect, self.size, self.lh = lines, rect, size, lh
        self.x_off, self.y_off, self.numbers = x_off, y_off, numbers

    def draw(self, ctx, hl=(), boxes=(), tags=(), dim=None, title=None):
        """hl: [(line_no, cue|None)] bands; boxes: [(line_no, substring, color, cue|None)];
        tags: [(line_no, text, color, cue)]; dim: set of line numbers to fade."""
        cv = ctx.cv
        x0, y0, x1, y1 = self.rect
        cv.rrect(x0, y0, x1, y1, 26, fill=WHITE, outline=PANEL_LINE, width=3)
        if title:
            cv.text(x0 + 28, y0 + 14, title, 22, MUTED, True)
        cw = cv.text_w("M", self.size, False, True)
        top = y0 + self.y_off + (26 if title else 0)
        tx = x0 + self.x_off
        for ln, cue in hl:
            a = ctx.p(cue, 0.35) if cue else 1.0
            y = top + (ln - 1) * self.lh
            cv.rrect(x0 + 18, y - 6, x1 - 18, y + self.lh - 8, 12, fill=BLUE_SOFT, a=a)
        for i, line in enumerate(self.lines):
            y = top + i * self.lh
            fade = 0.35 if dim and (i + 1) in dim else 1.0
            if self.numbers:
                cv.text(tx - 36, y + 4, str(i + 1), 26, GRAY, True, True, anchor="ra", a=fade)
            cv.text(tx, y, line, self.size, INK, False, True, a=fade)
        for ln, sub, color, cue in boxes:
            a = ctx.p(cue, 0.35) if cue else 1.0
            line = self.lines[ln - 1]
            c0 = line.index(sub)
            y = top + (ln - 1) * self.lh
            cv.rrect(tx + c0 * cw - 4, y - 4, tx + (c0 + len(sub)) * cw + 4, y + self.size + 10, 8,
                     outline=color, width=4, a=a)
        for ln, text, color, cue in tags:
            a = ctx.p(cue, 0.35)
            y = top + (ln - 1) * self.lh
            cv.text(x1 - 30, y + 8, text, 26, color, True, anchor="ra", a=a)
