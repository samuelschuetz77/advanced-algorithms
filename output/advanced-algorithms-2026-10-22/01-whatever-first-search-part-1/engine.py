"""Drawing engine for the advanced-algorithms videos.

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


# ---- Wrinkles the naked mole-rat -----------------------------------------
_sprite_hi = None
_sprite_cache: dict = {}


def _make_sprite_hi():
    u = 4  # draw at 4x of a 140x90 base
    img = Image.new("RGBA", (140 * u, 90 * u), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    dark = (205, 118, 134, 255)
    body = (240, 166, 178, 255)
    belly = (250, 200, 208, 255)
    d.line([(16 * u, 52 * u), (8 * u, 60 * u), (6 * u, 68 * u)], fill=dark, width=3 * u, joint="curve")
    for fx in (34, 52, 82, 98):
        d.ellipse([(fx - 7) * u, 68 * u, (fx + 9) * u, 80 * u], fill=(226, 140, 156, 255), outline=dark, width=2 * u // 2)
    d.ellipse([8 * u, 28 * u, 100 * u, 76 * u], fill=body, outline=dark, width=2 * u // 2 + 1)
    d.ellipse([22 * u, 52 * u, 88 * u, 74 * u], fill=belly)
    for x0 in (30, 44, 58, 72):
        d.arc([(x0 - 6) * u, 32 * u, (x0 + 12) * u, 70 * u], 255, 105, fill=dark, width=2 * u // 2 + 1)
    for tx in (117, 125):
        d.rounded_rectangle([tx * u, 56 * u, (tx + 6) * u, 71 * u], radius=2 * u, fill=(255, 255, 255, 255), outline=(150, 150, 150, 255), width=u // 2)
    d.ellipse([84 * u, 24 * u, 126 * u, 70 * u], fill=body, outline=dark, width=2 * u // 2 + 1)
    d.ellipse([108 * u, 38 * u, 136 * u, 64 * u], fill=body, outline=dark, width=2 * u // 2 + 1)
    d.ellipse([98 * u, 22 * u, 108 * u, 32 * u], fill=(226, 140, 156, 255), outline=dark, width=u // 2)
    d.ellipse([125 * u, 43 * u, 134 * u, 52 * u], fill=(120, 60, 76, 255))
    d.ellipse([108 * u, 38 * u, 115 * u, 45 * u], fill=(20, 20, 30, 255))
    d.ellipse([110 * u, 39 * u, 112 * u, 41 * u], fill=(255, 255, 255, 255))
    return img


def sprite(scale=1.0, flip=False, tilt=0.0):
    """Wrinkles as an SS-scaled RGBA image, ~140x90 at scale 1."""
    global _sprite_hi
    if _sprite_hi is None:
        _sprite_hi = _make_sprite_hi()
    key = (round(scale, 2), flip, round(tilt, 1))
    if key not in _sprite_cache:
        im = _sprite_hi
        if flip:
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        if tilt:
            im = im.rotate(tilt, resample=Image.BICUBIC, expand=True)
        w, h = int(140 * SS * scale), int(90 * SS * scale * im.size[1] / (90 * 4))
        w = int(im.size[0] / 4 * SS * scale)
        h = int(im.size[1] / 4 * SS * scale)
        _sprite_cache[key] = im.resize((max(1, w), max(1, h)), Image.LANCZOS)
    return _sprite_cache[key]


# ---- the Colony graph -----------------------------------------------------
POS = {
    "S": (300, 520),
    "A": (520, 290), "B": (520, 520), "C": (520, 750),
    "D": (880, 290), "E": (880, 520), "F": (880, 750),
    "X": (1135, 410), "Y": (1135, 650),
}
# (u, v, bulge) ; bulge is the sideways offset of a quadratic curve control point
EDGES = [
    ("S", "A", 0), ("S", "B", 0), ("S", "C", 0),
    ("A", "B", 0), ("B", "C", 0), ("A", "C", -710),
    ("A", "D", 0), ("B", "E", 0), ("C", "F", 0),
    ("D", "E", 0), ("E", "F", 0), ("D", "F", 260),
    ("X", "Y", 0),
]
R_VERT = 40
NEIGHBORS = {
    "S": ["A", "B", "C"], "A": ["B", "C", "D", "S"], "B": ["A", "C", "E", "S"],
    "C": ["A", "B", "F", "S"], "D": ["A", "E", "F"], "E": ["B", "D", "F"],
    "F": ["C", "D", "E"], "X": ["Y"], "Y": ["X"],
}


def _edge_def(u, v):
    for a, b, bulge in EDGES:
        if (a, b) == (u, v):
            return (a, b, bulge, False)
        if (b, a) == (u, v):
            return (a, b, bulge, True)
    raise KeyError((u, v))


def edge_pts(u, v, n=240, trim=R_VERT):
    """Polyline for edge u->v (trimmed to the vertex circles)."""
    a, b, bulge, rev = _edge_def(u, v)
    p0, p1 = POS[a], POS[b]
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    if bulge:
        ctrl = (mx + bulge, my)
    else:
        ctrl = (mx, my)
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t * t * p1[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t * t * p1[1]
        pts.append((x, y))
    if rev:
        pts.reverse()
    if trim:
        def inside(pt, c):
            return math.hypot(pt[0] - c[0], pt[1] - c[1]) < trim
        start = POS[u]
        end = POS[v]
        pts = [p for p in pts if not inside(p, start) and not inside(p, end)] or pts
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


def full_edge_pts(u, v):
    """Edge polyline from vertex center to vertex center (for walkers)."""
    return edge_pts(u, v, trim=0)
