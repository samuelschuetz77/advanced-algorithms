"""Simple characters drawn from primitives (no image files). Anchor (x, y) = feet / bottom center."""
from __future__ import annotations

import math

from engine import ACCENT, ACCENT_DARK, BLUE, INK, WHITE

SKIN = (240, 196, 160)
GREEN = (84, 170, 92)
GREEN_DARK = (46, 120, 58)


def person(cv, x, y, scale=1.0, shirt=BLUE, hair=(60, 40, 30), hat=None, a=1.0, flip=False, wave=0.0):
    s = scale
    d = -1 if flip else 1
    # legs
    cv.line((x - 10 * s, y - 38 * s), (x - 12 * s, y), INK, 7 * s, a)
    cv.line((x + 10 * s, y - 38 * s), (x + 12 * s, y), INK, 7 * s, a)
    # body
    cv.rrect(x - 22 * s, y - 92 * s, x + 22 * s, y - 34 * s, 14 * s, fill=shirt, a=a)
    # arms (one waves)
    cv.line((x - 22 * s, y - 84 * s), (x - 36 * s, y - 56 * s), shirt, 9 * s, a)
    ay = y - 84 * s - 24 * s * wave
    cv.line((x + 22 * s, y - 84 * s), (x + 38 * s * d, ay), shirt, 9 * s, a)
    # head
    cv.circle(x, y - 114 * s, 24 * s, fill=SKIN, outline=(200, 150, 120), width=2, a=a)
    cv.rrect(x - 25 * s, y - 142 * s, x + 25 * s, y - 120 * s, 12 * s, fill=hair, a=a)
    cv.circle(x - 8 * s * d, y - 112 * s, 3 * s, fill=INK, a=a)
    cv.circle(x + 8 * s * d, y - 112 * s, 3 * s, fill=INK, a=a)
    cv.line((x - 7 * s, y - 102 * s), (x + 7 * s, y - 102 * s), (150, 80, 70), 3 * s, a)
    if hat:
        cv.rrect(x - 30 * s, y - 138 * s, x + 30 * s, y - 130 * s, 4 * s, fill=hat, a=a)
        cv.rrect(x - 20 * s, y - 160 * s, x + 20 * s, y - 136 * s, 8 * s, fill=hat, a=a)


def frog(cv, x, y, scale=1.0, flip=False, a=1.0, squash=0.0):
    s = scale
    d = -1 if flip else 1
    h = 34 * s * (1 - 0.25 * squash)
    cv.ellipse(x, y - h, 46 * s, h, fill=GREEN, outline=GREEN_DARK, width=3, a=a)
    cv.ellipse(x - 4 * s * d, y - h * 0.55, 30 * s, h * 0.5, fill=(200, 235, 180), a=a)
    for ex in (-18, 18):
        cv.circle(x + ex * s * d + 8 * s * d, y - 2 * h + 6 * s, 14 * s, fill=GREEN, outline=GREEN_DARK, width=3, a=a)
        cv.circle(x + ex * s * d + 10 * s * d, y - 2 * h + 6 * s, 7 * s, fill=WHITE, a=a)
        cv.circle(x + ex * s * d + 12 * s * d, y - 2 * h + 6 * s, 3.5 * s, fill=INK, a=a)
    cv.line((x - 36 * s, y - 6 * s), (x - 56 * s, y), GREEN_DARK, 8 * s, a)
    cv.line((x + 36 * s, y - 6 * s), (x + 56 * s, y), GREEN_DARK, 8 * s, a)
    cv.line((x + 8 * s * d, y - h * 0.9), (x + 28 * s * d, y - h * 0.8), GREEN_DARK, 3 * s, a)


def bubble(cv, x, y, text="!", scale=1.0, color=ACCENT, a=1.0):
    """Speech bubble whose tail points down at (x, y)."""
    s = scale
    w, h = 66 * s, 50 * s
    cv.rrect(x - w / 2, y - h - 18 * s, x + w / 2, y - 18 * s, 18 * s, fill=color, a=a)
    cv.polygon([(x - 10 * s, y - 20 * s), (x + 10 * s, y - 20 * s), (x, y - 2 * s)], color, a)
    cv.text(x, y - 18 * s - h / 2, text, int(34 * s), WHITE, True, anchor="mm", a=a)


def clock_face(cv, x, y, r, t, a=1.0):
    """A small clock; t is a number that advances the minute hand."""
    cv.circle(x, y, r, fill=WHITE, outline=INK, width=4, a=a)
    for i in range(12):
        ang = math.pi * 2 * i / 12 - math.pi / 2
        cv.line((x + r * 0.82 * math.cos(ang), y + r * 0.82 * math.sin(ang)),
                (x + r * 0.95 * math.cos(ang), y + r * 0.95 * math.sin(ang)), INK, 2, a)
    ang = math.pi * 2 * (t % 12) / 12 - math.pi / 2
    cv.line((x, y), (x + r * 0.7 * math.cos(ang), y + r * 0.7 * math.sin(ang)), ACCENT_DARK, 5, a)
    cv.circle(x, y, 5, fill=INK, a=a)
