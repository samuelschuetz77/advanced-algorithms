"""Move a character along graph edges: waypoints [(time, vertex)] -> (x, y, flip, moving)."""
import math

from engine import ease, point_along


def walk(ctx, gv, wps, hop=0.0):
    t = ctx.t
    x, y = gv.pos[wps[0][1]]
    flip, moving = False, False
    if t >= wps[0][0]:
        x, y = gv.pos[wps[-1][1]]
        for (t0, v0), (t1, v1) in zip(wps, wps[1:]):
            if t0 <= t < t1:
                if v0 == v1:
                    x, y = gv.pos[v0]
                else:
                    f = (t - t0) / (t1 - t0)
                    x, y = point_along(gv.full(v0, v1), ease(f))
                    y -= math.sin(math.pi * f) * hop
                    flip = gv.pos[v1][0] < gv.pos[v0][0]
                    moving = True
                break
            if t >= t1:
                x, y = gv.pos[v1]
                flip = gv.pos[v1][0] < gv.pos[v0][0] if v0 != v1 else flip
    ctx.sig.append((round(x), round(y), flip))
    return x, y, flip, moving
