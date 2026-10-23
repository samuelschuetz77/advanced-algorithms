"""A reusable graph drawing: positions + edges, optional arrows, weights, name labels."""
from __future__ import annotations

import math

from engine import (
    ACCENT, ACCENT_DARK, BLUE, GRAY, INK, LINE, MUTED, RED, WHITE, bezier, clamp, mix, point_along,
)


class GraphView:
    def __init__(self, pos, edges, directed=False, r=44, label_size=30, labels=None, weights=None):
        """pos: {v: (x, y)}; edges: [(u, v)] or [(u, v, bulge)]; bulge bends the edge sideways."""
        self.pos = {v: tuple(p) for v, p in pos.items()}
        self.edges = [(e[0], e[1], e[2] if len(e) > 2 else 0) for e in edges]
        self.directed = directed
        self.r = r
        self.label_size = label_size
        self.labels = labels or {}
        self.weights = weights or {}

    # ---- geometry --------------------------------------------------------
    def key(self, u, v):
        return (u, v) if self.directed else tuple(sorted((u, v)))

    def _def(self, u, v):
        for a, b, bulge in self.edges:
            if (a, b) == (u, v):
                return a, b, bulge, False
            if not self.directed and (b, a) == (u, v):
                return a, b, bulge, True
        raise KeyError((u, v))

    def pts(self, u, v, trim=None, n=200):
        """Polyline from u to v (trimmed to the vertex circles)."""
        a, b, bulge, rev = self._def(u, v)
        p0, p1 = self.pos[a], self.pos[b]
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        if bulge:
            dx, dy = p1[0] - p0[0], p1[1] - p0[1]
            L = math.hypot(dx, dy) or 1
            ctrl = (mx - dy / L * bulge, my + dx / L * bulge)
        else:
            ctrl = (mx, my)
        pts = bezier(p0, ctrl, p1, n)
        if rev:
            pts.reverse()
        t = self.r if trim is None else trim
        if t:
            s, e = self.pos[u], self.pos[v]
            inner = [p for p in pts if math.hypot(p[0] - s[0], p[1] - s[1]) >= t
                     and math.hypot(p[0] - e[0], p[1] - e[1]) >= t]
            pts = inner or pts
        return pts

    def mid(self, u, v, f=0.5):
        return point_along(self.pts(u, v), f)

    def full(self, u, v):
        return self.pts(u, v, trim=0)

    # ---- drawing ---------------------------------------------------------
    def draw(self, ctx, marked=None, fills=None, rings=None, estyle=None, badges=None, vfade=None,
             show_weights=False, edge_alpha=1.0, label_color=None):
        """marked {v: 0..1 accent fill}; fills {v: (color, 0..1)}; rings {v: (color, alpha)};
        estyle {key: (color, width, alpha)}; badges {v: ('x', alpha)}."""
        cv = ctx.cv
        marked, fills, rings = marked or {}, fills or {}, rings or {}
        estyle, badges, vfade = estyle or {}, badges or {}, vfade or {}
        for a, b, _ in self.edges:
            k = self.key(a, b)
            col, wd, al = estyle.get(k, (LINE, 6, 1.0))
            pts = self.pts(a, b)
            if self.directed:
                head = 12 + wd * 1.6
                # pull the line back so the arrow tip touches the vertex ring
                cut = []
                acc = 0.0
                for i in range(len(pts) - 1, 0, -1):
                    acc += math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1])
                    if acc >= head * 0.8:
                        cut = pts[:i]
                        break
                cv.poly_line(cut or pts, col, wd, al * edge_alpha)
                tip = pts[-1]
                back = pts[max(0, len(pts) - 12)]
                ang = math.atan2(tip[1] - back[1], tip[0] - back[0])
                left = (tip[0] - head * math.cos(ang - 0.42), tip[1] - head * math.sin(ang - 0.42))
                right = (tip[0] - head * math.cos(ang + 0.42), tip[1] - head * math.sin(ang + 0.42))
                cv.polygon([tip, left, right], col, al * edge_alpha)
            else:
                cv.poly_line(pts, col, wd, al * edge_alpha)
        if show_weights and self.weights:
            for (a, b), w in self.weights.items():
                x, y = self.mid(a, b, 0.5)
                cv.circle(x, y, 19, fill=WHITE, outline=GRAY, width=2)
                cv.text(x, y - 1, str(w), 22, INK, True, anchor="mm")
        for v, (x, y) in self.pos.items():
            mf = marked.get(v, 0.0)
            fa = vfade.get(v, 1.0)
            fill = mix(WHITE, ACCENT, mf)
            ring_col = mix(INK, ACCENT_DARK, mf)
            txt = mix(INK, WHITE, mf)
            if v in fills:
                col, f = fills[v]
                fill = mix(fill, col, f)
                ring_col = mix(ring_col, mix(col, INK, 0.35), f)
                txt = mix(txt, WHITE if sum(col) < 600 else INK, f)
            if label_color and v in label_color:
                txt = label_color[v]
            cv.circle(x, y, self.r, fill=fill, outline=ring_col, width=5, a=fa)
            label = self.labels.get(v, str(v))
            size = min(self.label_size, int(self.r * 2 * 0.68 / max(1, 0.56 * len(label))))
            cv.text(x, y - 1, label, size, txt, True, anchor="mm", a=fa)
            if v in rings:
                col, al = rings[v]
                cv.circle(x, y, self.r + 12, outline=col, width=7, a=al)
            if v in badges:
                kind, al = badges[v]
                if kind == "x":
                    cv.circle(x + self.r * 0.75, y - self.r * 0.75, 17, fill=RED, a=al)
                    cx, cy = x + self.r * 0.75, y - self.r * 0.75
                    cv.line((cx - 7, cy - 7), (cx + 7, cy + 7), WHITE, 5, al)
                    cv.line((cx + 7, cy - 7), (cx - 7, cy + 7), WHITE, 5, al)
