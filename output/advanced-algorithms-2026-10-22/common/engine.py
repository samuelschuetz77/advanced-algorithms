"""Drawing engine shared by all videos in this series.

All coordinates are 1920x1080 "1x" pixels. Everything is drawn at 2x and
downsampled so lines and circles are anti-aliased. Every drawing call accepts an
alpha `a` (0..1).
"""
from __future__ import annotations

import math

from PIL import Image, ImageDraw, ImageFont

W, H, SS = 1920, 1080, 2
FONT_DIR = "C:/Windows/Fonts/"

PAPER = (248, 246, 240)
INK = (27, 36, 51)
MUTED = (104, 116, 132)
LINE = (122, 132, 148)
ACCENT = (214, 90, 49)
ACCENT_DARK = (160, 58, 24)
ACCENT_SOFT = (252, 228, 215)
BLUE = (37, 99, 235)
BLUE_SOFT = (219, 232, 254)
GREEN = (22, 150, 90)
RED = (214, 54, 62)
GRAY = (178, 184, 194)
GRAY_SOFT = (232, 234, 238)
WHITE = (255, 255, 255)
PANEL_LINE = (222, 224, 230)
BAND = (22, 30, 44)
YELLOW = (255, 214, 102)
PINK = (238, 160, 172)

_font_cache: dict = {}


def font(size, bold=False, mono=False):
    key = (size, bold, mono)
    if key not in _font_cache:
        if mono:
            name = "consolab.ttf" if bold else "consola.ttf"
        else:
            name = "segoeuib.ttf" if bold else "segoeui.ttf"
        _font_cache[key] = ImageFont.truetype(FONT_DIR + name, int(round(size * SS)))
    return _font_cache[key]


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))


def ease(v):
    v = clamp(v)
    return v * v * (3 - 2 * v)


def lerp(a, b, t):
    return a + (b - a) * t


def mix(c0, c1, t):
    return tuple(int(round(lerp(c0[i], c1[i], t))) for i in range(3))


class Canvas:
    def __init__(self, bg=PAPER):
        self.img = Image.new("RGBA", (W * SS, H * SS), tuple(bg) + (255,))
        self.d = ImageDraw.Draw(self.img)

    # ---- low level -------------------------------------------------------
    def _draw(self, a, bbox, fn):
        """Run fn(draw, ox, oy) in SS pixel space. bbox is 1x (x0,y0,x1,y1)."""
        if a <= 0.004:
            return
        if a >= 0.996:
            fn(self.d, 0, 0)
            return
        x0, y0, x1, y1 = bbox
        x0, y0 = int(math.floor(x0)) - 2, int(math.floor(y0)) - 2
        x1, y1 = int(math.ceil(x1)) + 2, int(math.ceil(y1)) + 2
        x0c, y0c = max(0, x0), max(0, y0)
        x1c, y1c = min(W, x1), min(H, y1)
        if x1c <= x0c or y1c <= y0c:
            return
        layer = Image.new("RGBA", ((x1c - x0c) * SS, (y1c - y0c) * SS), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        fn(ld, -x0c * SS, -y0c * SS)
        alpha = layer.getchannel("A").point(lambda v: int(v * a))
        layer.putalpha(alpha)
        self.img.alpha_composite(layer, (x0c * SS, y0c * SS))

    @staticmethod
    def _c(color, fill_alpha=255):
        return tuple(color) + (fill_alpha,)

    # ---- shapes ----------------------------------------------------------
    def circle(self, cx, cy, r, fill=None, outline=None, width=0, a=1.0):
        def fn(d, ox, oy):
            d.ellipse(
                [(cx - r) * SS + ox, (cy - r) * SS + oy, (cx + r) * SS + ox, (cy + r) * SS + oy],
                fill=self._c(fill) if fill else None,
                outline=self._c(outline) if outline else None,
                width=int(width * SS),
            )
        self._draw(a, (cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2), fn)

    def ellipse(self, cx, cy, rx, ry, fill=None, outline=None, width=0, a=1.0):
        def fn(d, ox, oy):
            d.ellipse([(cx - rx) * SS + ox, (cy - ry) * SS + oy, (cx + rx) * SS + ox, (cy + ry) * SS + oy],
                      fill=self._c(fill) if fill else None, outline=self._c(outline) if outline else None,
                      width=int(width * SS))
        self._draw(a, (cx - rx - 2, cy - ry - 2, cx + rx + 2, cy + ry + 2), fn)

    def rrect(self, x0, y0, x1, y1, r=16, fill=None, outline=None, width=0, a=1.0):
        def fn(d, ox, oy):
            d.rounded_rectangle(
                [x0 * SS + ox, y0 * SS + oy, x1 * SS + ox, y1 * SS + oy],
                radius=r * SS,
                fill=self._c(fill) if fill else None,
                outline=self._c(outline) if outline else None,
                width=int(width * SS),
            )
        self._draw(a, (x0 - 2, y0 - 2, x1 + 2, y1 + 2), fn)

    def poly_line(self, pts, color, width, a=1.0, dash=None):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        pad = width + 4

        def fn(d, ox, oy):
            seg = [(x * SS + ox, y * SS + oy) for x, y in pts]
            if dash is None:
                d.line(seg, fill=self._c(color), width=int(width * SS), joint="curve")
                for (x, y) in (seg[0], seg[-1]):
                    d.ellipse([x - width * SS / 2, y - width * SS / 2, x + width * SS / 2, y + width * SS / 2],
                              fill=self._c(color))
            else:
                on, off = dash
                for i in range(len(seg) - 1):
                    (xa, ya), (xb, yb) = seg[i], seg[i + 1]
                    L = math.hypot(xb - xa, yb - ya)
                    if L == 0:
                        continue
                    pos = 0.0
                    while pos < L:
                        e = min(L, pos + on * SS)
                        d.line([(xa + (xb - xa) * pos / L, ya + (yb - ya) * pos / L),
                                (xa + (xb - xa) * e / L, ya + (yb - ya) * e / L)],
                               fill=self._c(color), width=int(width * SS))
                        pos += (on + off) * SS

        self._draw(a, (min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad), fn)

    def line(self, p0, p1, color, width, a=1.0, dash=None):
        self.poly_line([p0, p1], color, width, a, dash)

    def polygon(self, pts, fill, a=1.0):
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]

        def fn(d, ox, oy):
            d.polygon([(x * SS + ox, y * SS + oy) for x, y in pts], fill=self._c(fill))
        self._draw(a, (min(xs), min(ys), max(xs), max(ys)), fn)

    def arrow(self, p0, p1, color, width=6, a=1.0, head=20):
        ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
        bx = p1[0] - head * 0.8 * math.cos(ang)
        by = p1[1] - head * 0.8 * math.sin(ang)
        self.line(p0, (bx, by), color, width, a)
        left = (p1[0] - head * math.cos(ang - 0.45), p1[1] - head * math.sin(ang - 0.45))
        right = (p1[0] - head * math.cos(ang + 0.45), p1[1] - head * math.sin(ang + 0.45))
        self.polygon([p1, left, right], color, a)

    # ---- text ------------------------------------------------------------
    def text(self, x, y, s, size=32, color=INK, bold=False, mono=False, anchor="la", a=1.0):
        f = font(size, bold, mono)
        bb = self.d.textbbox((0, 0), s, font=f, anchor=anchor)
        bx = (bb[0] / SS, bb[1] / SS, bb[2] / SS, bb[3] / SS)

        def fn(d, ox, oy):
            d.text((x * SS + ox, y * SS + oy), s, font=f, fill=self._c(color), anchor=anchor)
        self._draw(a, (x + bx[0] - 4, y + bx[1] - 4, x + bx[2] + 4, y + bx[3] + 4), fn)

    def text_w(self, s, size=32, bold=False, mono=False):
        return font(size, bold, mono).getlength(s) / SS

    def paste(self, img, cx, cy, a=1.0):
        """Paste an RGBA image (already at SS scale) centered at 1x cx, cy."""
        w, h = img.size
        pos = (int(cx * SS - w / 2), int(cy * SS - h / 2))
        if a >= 0.996:
            self.img.alpha_composite(img, (max(pos[0], 0), max(pos[1], 0))) if pos[0] >= 0 and pos[1] >= 0 else \
                self.img.alpha_composite(img.crop((max(0, -pos[0]), max(0, -pos[1]), w, h)),
                                         (max(pos[0], 0), max(pos[1], 0)))
        else:
            im = img.copy()
            im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
            self.img.alpha_composite(im, (max(pos[0], 0), max(pos[1], 0)))

    def finish(self):
        return self.img.convert("RGB").resize((W, H), Image.LANCZOS)


class NullCanvas:
    """Used for the dry pass that only collects frame signatures."""
    def __getattr__(self, name):
        if name == "text_w":
            return lambda s, size=32, bold=False, mono=False: font(size, bold, mono).getlength(s) / SS
        return lambda *a, **k: None


def bezier(p0, ctrl, p1, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p1[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p1[1]))
    return pts


def point_along(pts, f):
    """Point at fraction f (0..1) along a polyline."""
    if f <= 0:
        return pts[0]
    if f >= 1:
        return pts[-1]
    seg = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1)]
    total = sum(seg)
    target = f * total
    acc = 0.0
    for i, L in enumerate(seg):
        if acc + L >= target:
            r = (target - acc) / L if L else 0
            return (lerp(pts[i][0], pts[i + 1][0], r), lerp(pts[i][1], pts[i + 1][1], r))
        acc += L
    return pts[-1]
