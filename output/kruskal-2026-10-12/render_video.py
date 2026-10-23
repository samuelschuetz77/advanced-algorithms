"""Render the October 12 Kruskal lesson from scene-synced narration MP3s.

Requires Pillow and FFmpeg. Run after placing 01-mst.mp3 ... 08-elegant.mp3
in voice/. The graph coordinates and edges trace the Google Docs class image.
The unlabeled C-E edge is assigned cost 17; typography and crowded label
positions are cleaned up for legibility.
"""

from __future__ import annotations

import json
import math
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SCENES = json.loads((ROOT / "narration.json").read_text(encoding="utf-8"))
VOICE = ROOT / "voice"
CLIPS = ROOT / "clips"
W, H, FPS = 1280, 720, 12

INK = "#183045"
MUTED = "#65788a"
BG = "#eef4f4"
WHITE = "#ffffff"
TEAL = "#00a896"
TEAL_DARK = "#007e75"
GOLD = "#f2ad45"
RED = "#dc6472"
PALE = "#e0e9eb"
NAVY = "#102536"

FONT_DIR = Path("C:/Windows/Fonts")


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    name = "CascadiaMono.ttf" if mono else ("segoeuib.ttf" if bold else "segoeui.ttf")
    path = FONT_DIR / name
    if not path.exists() and mono:
        path = FONT_DIR / "consola.ttf"
    return ImageFont.truetype(str(path), size)


F_TITLE = font(37, True)
F_SUB = font(22)
F_SMALL = font(17)
F_SMALL_BOLD = font(18, True)
F_WEIGHT = font(20, True)
F_NODE = font(25, True)
F_CODE = font(20, mono=True)
F_CODE_SMALL = font(17, mono=True)
F_CAPTION = font(22, True)

# Directly transcribed from the class drawing (917 x 659 image).
SOURCE_POS = {
    "A": (59, 513), "B": (243, 271), "C": (463, 498), "D": (522, 86),
    "E": (657, 229), "F": (834, 381), "G": (819, 86), "H": (665, 472),
}
POS = {v: (int(76 + x * .86), int(116 + y * .86)) for v, (x, y) in SOURCE_POS.items()}
EDGES = [
    ("B", "C", 1), ("A", "C", 3), ("C", "H", 4), ("A", "B", 5),
    ("H", "F", 6), ("E", "F", 7), ("G", "F", 8), ("D", "E", 9),
    ("D", "G", 10), ("E", "G", 11), ("C", "E", 17),
]
BASE_TREE = [("B", "C"), ("A", "C"), ("C", "H"), ("H", "F"),
             ("E", "F"), ("G", "F"), ("D", "E")]

# Offsets move crowded labels away from their edges, especially E--G at 11.
OFFSETS = {
    1: (15, -15), 3: (0, 22), 4: (0, 22), 5: (-17, 0),
    6: (16, 20), 7: (18, -12), 8: (23, 0), 9: (-22, 8),
    10: (0, -24), 11: (22, -17), 17: (29, 1),
}

VERTICES = tuple(sorted(SOURCE_POS))
COMPONENT_COLORS = {
    "A": "#d8874c", "B": TEAL_DARK, "C": "#5586ba", "D": "#8568b6",
    "E": "#c15e78", "F": "#558870", "G": "#a07835", "H": "#6675a8",
}


def forest_state(accepted):
    """Replay union by size to show the same representatives as the Python solution."""
    parent = {v: v for v in VERTICES}
    size = {v: 1 for v in VERTICES}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for u, v in accepted:
        a, b = find(u), find(v)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    roots = {v: find(v) for v in VERTICES}
    groups = {}
    for v, root in roots.items():
        groups.setdefault(root, []).append(v)
    return roots, sorted(groups.items(), key=lambda item: item[1][0])


def rr(d: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def centered(d, xy, label, fnt, fill):
    box = d.textbbox((0, 0), str(label), font=fnt)
    d.text((xy[0] - (box[2] - box[0]) / 2, xy[1] - (box[3] - box[1]) / 2 - box[1]),
           str(label), font=fnt, fill=fill)


def wrap_pixels(d, text, fnt, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if d.textlength(candidate, font=fnt) > max_width and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def edge_key(u, v):
    return frozenset((u, v))


def draw_graph(d, *, accepted=(), focus=None, rejected=None, hypothetical=False,
               pulse=0.0, dim=False):
    rr(d, (31, 128, 913, 614), 26, WHITE, PALE, 2)
    roots, _ = forest_state(accepted)
    accepted_keys = {edge_key(*e) for e in accepted}
    focus_key = edge_key(*focus) if focus else None
    rejected_key = edge_key(*rejected) if rejected else None
    active_nodes = set()
    for u, v in accepted:
        active_nodes.update((u, v))

    for u, v, weight in EDGES:
        key = edge_key(u, v)
        color = "#c3d1d4" if not dim else "#d5e0e1"
        width = 3
        if key in accepted_keys:
            color, width = COMPONENT_COLORS[roots[u]], 7
        if key == focus_key:
            color, width = GOLD, 9
        if key == rejected_key:
            color, width = RED, 7
        x1, y1 = POS[u]
        x2, y2 = POS[v]
        d.line((x1, y1, x2, y2), fill=color, width=width, joint="curve")

    for u, v, weight in EDGES:
        x1, y1 = POS[u]
        x2, y2 = POS[v]
        dx, dy = OFFSETS[weight]
        x = (x1 + x2) / 2 + dx
        y = (y1 + y2) / 2 + dy
        shown = 6 if hypothetical and weight == 9 else weight
        key = edge_key(u, v)
        fill = NAVY if key not in accepted_keys else COMPONENT_COLORS[roots[u]]
        if key == focus_key:
            fill = "#a96414"
        if key == rejected_key:
            fill = "#a43c4d"
        digits = len(str(shown))
        rr(d, (x - 17 - digits * 3, y - 17, x + 17 + digits * 3, y + 17),
           10, fill)
        centered(d, (x, y), shown, F_WEIGHT, WHITE)

    for vertex, (x, y) in POS.items():
        highlighted = focus and vertex in focus
        rejected_node = rejected and vertex in rejected
        if highlighted or rejected_node:
            radius = 31 + 5 * math.sin(pulse * math.pi) ** 2
            color = "#ffda9b" if highlighted else "#fac5ca"
            d.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)
        fill = WHITE
        outline = COMPONENT_COLORS[roots[vertex]]
        if highlighted:
            outline = "#ae6a1a"
        if rejected_node:
            outline = "#a43c4d"
        d.ellipse((x-23, y-23, x+23, y+23), fill=fill, outline=outline, width=4)
        centered(d, (x, y), vertex, F_NODE, INK)

    if rejected:
        # A red cross makes the rejected candidate unambiguous.
        u, v = rejected
        x, y = (POS[u][0] + POS[v][0]) / 2, (POS[u][1] + POS[v][1]) / 2
        d.line((x-13, y-13, x+13, y+13), fill=RED, width=5)
        d.line((x-13, y+13, x+13, y-13), fill=RED, width=5)


def base_canvas(scene, i, duration, t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 98), fill=NAVY)
    d.text((34, 20), "KRUSKAL’S ALGORITHM", font=F_TITLE, fill=WHITE)
    d.text((36, 68), "MST  /  OCTOBER 12, 2026 CLASS NOTES", font=F_SMALL, fill="#a7c3c7")
    d.text((949, 28), f"{i+1:02d} / {len(SCENES):02d}", font=font(25, True), fill=GOLD)
    rr(d, (34, 106, 1246, 114), 4, "#d8e5e5")
    rr(d, (34, 106, int(34 + 1212 * (i + min(t/duration, 1)) / len(SCENES)), 114), 4, TEAL)
    return im, d


def sidebar(d, kicker, heading, body_lines, *, cost=None, badge=None):
    rr(d, (935, 128, 1249, 614), 25, WHITE, PALE, 2)
    d.text((957, 151), kicker.upper(), font=F_SMALL_BOLD, fill=TEAL_DARK)
    lines = wrap_pixels(d, heading, font(26, True), 270)
    y = 185
    for line in lines:
        d.text((957, y), line, font=font(26, True), fill=INK)
        y += 33
    y += 15
    for text in body_lines:
        for line in wrap_pixels(d, text, F_SUB, 270):
            d.text((957, y), line, font=F_SUB, fill=INK)
            y += 30
        y += 12
    if cost is not None:
        rr(d, (956, 529, 1228, 590), 15, NAVY)
        d.text((973, 542), "SELECTED COST", font=F_SMALL_BOLD, fill="#a7c3c7")
        d.text((1164, 532), str(cost), font=font(39, True), fill=WHITE)
    if badge:
        rr(d, (957, 538, 1227, 583), 12, "#fff0d9")
        centered(d, (1092, 560), badge, F_SMALL_BOLD, "#9b6217")


def forest_chips(d, groups, top):
    x, y = 956, top
    for root, vertices in groups:
        label = "{" + ",".join(vertices) + "}"
        width = max(58, int(d.textlength(label, font=F_SMALL_BOLD)) + 22)
        if x + width > 1228:
            x, y = 956, y + 35
        rr(d, (x, y, x + width, y + 29), 10, "#f2f6f6", COMPONENT_COLORS[root], 2)
        centered(d, (x + width/2, y + 14), label, F_SMALL_BOLD, COMPONENT_COLORS[root])
        x += width + 8


def forest_sidebar(d, *, step, candidate, before, after, keep, cost, hypothetical=False):
    rr(d, (935, 128, 1249, 614), 25, WHITE, PALE, 2)
    kicker = f"{'WHAT IF' if hypothetical else 'CLASS'}  /  EDGE {step}"
    d.text((956, 149), kicker, font=F_SMALL_BOLD, fill=TEAL_DARK)
    u, v, weight = candidate
    d.text((956, 183), f"{u}-{v}  /  cost {weight}", font=font(27, True), fill=INK)
    roots_before, _ = forest_state(before)
    d.text((956, 235), "FIND BEFORE", font=F_SMALL_BOLD, fill=MUTED)
    d.text((956, 260), f"find({u}) = {roots_before[u]}", font=F_CODE, fill=INK)
    d.text((956, 286), f"find({v}) = {roots_before[v]}", font=F_CODE, fill=INK)
    decision = f"KEEP  /  union({u}, {v})" if keep else "SKIP  /  same root"
    decision_color = "#e2f5ed" if keep else "#fff0f0"
    decision_ink = TEAL_DARK if keep else "#a43c4d"
    rr(d, (956, 326, 1228, 366), 11, decision_color)
    centered(d, (1092, 346), decision, F_SMALL_BOLD, decision_ink)
    _, groups = forest_state(after)
    d.text((956, 390), f"FOREST AFTER  /  {len(groups)} TREES", font=F_SMALL_BOLD, fill=MUTED)
    forest_chips(d, groups, 420)
    rr(d, (956, 536, 1228, 590), 13, NAVY)
    d.text((973, 553), "SELECTED COST", font=F_SMALL_BOLD, fill="#a7c3c7")
    d.text((1172, 540), str(cost), font=font(36, True), fill=WHITE)


def forest_summary_sidebar(d, *, kicker, heading, accepted, lines, cost=None):
    rr(d, (935, 128, 1249, 614), 25, WHITE, PALE, 2)
    d.text((956, 151), kicker.upper(), font=F_SMALL_BOLD, fill=TEAL_DARK)
    d.text((956, 187), heading, font=font(26, True), fill=INK)
    y = 239
    for line in lines:
        for wrapped in wrap_pixels(d, line, F_SMALL, 268):
            d.text((956, y), wrapped, font=F_SMALL, fill=INK)
            y += 25
        y += 11
    _, groups = forest_state(accepted)
    d.text((956, 390), f"FOREST  /  {len(groups)} TREES", font=F_SMALL_BOLD, fill=MUTED)
    forest_chips(d, groups, 420)
    if cost is not None:
        rr(d, (956, 536, 1228, 590), 13, NAVY)
        d.text((973, 553), "SELECTED COST", font=F_SMALL_BOLD, fill="#a7c3c7")
        d.text((1172, 540), str(cost), font=font(36, True), fill=WHITE)


def footer(d, scene, t, duration):
    # Sentence-level captions are paced to the actual segment duration.
    p = t / max(duration, .1)
    scene_index = SCENES.index(scene)
    sync_captions = {
        2: ["Initially, each vertex is its own tree in the forest.",
            "B–C, cost 1: different roots, so union creates {B,C}.",
            "A–C, cost 3: different roots, so union adds A.",
            "C–H, cost 4: union adds H to the first tree.",
            "A–B, cost 5: same root, so skip; the forest stays put."],
        3: ["H–F, cost 6: union adds F to the large tree.",
            "E–F, cost 7: union adds E.",
            "G–F, cost 8: union adds G.",
            "D–E, cost 9: union leaves one tree, total 38.",
            "Stop after seven edges; weights 10, 11, and 17 are not needed."],
        4: ["Reset after the cost-5 rejection; change D–E from 9 to 6.",
            "Hypothetical D–E costs 6: union creates a second tree.",
            "H–F also costs 6: union grows the first tree.",
            "E–F, cost 7: union bridges those two trees.",
            "G–F, cost 8: one tree remains, total 35."],
    }
    if scene_index in sync_captions:
        captions = sync_captions[scene_index]
        index = phase_for(scene_index, p)
        lines = wrap_pixels(d, captions[index], F_CAPTION, 1195)
    else:
        sentences = []
        import re
        for sentence in re.split(r"(?<=[.!?])\s+", scene["text"]):
            if sentence.strip():
                sentences.append(sentence.strip())
        weights = [max(15, len(s)) for s in sentences]
        cumulative = 0
        index = len(sentences) - 1
        pos = p * sum(weights)
        for j, weight in enumerate(weights):
            cumulative += weight
            if pos < cumulative:
                index = j
                break
        lines = wrap_pixels(d, sentences[index], F_CAPTION, 1195)
    d.rectangle((0, 628, W, H), fill=NAVY)
    d.text((34, 638), scene["title"].upper(), font=F_SMALL_BOLD, fill=GOLD)
    if len(lines) > 2:
        lines = lines[:2]
    for j, line in enumerate(lines):
        d.text((34, 663 + j*26), line, font=F_CAPTION, fill=WHITE)


def selected_until(sequence, phase):
    return sequence[:max(0, phase)]


def phase_for(index, p):
    cuts = {
        2: (.13, .32, .48, .63),
        3: (.22, .40, .56, .80),
        4: (.23, .45, .65, .83),
    }[index]
    return sum(p >= cut for cut in cuts)


def draw_graph_scene(d, index, p, t):
    if index == 0:
        count = min(len(EDGES), max(0, int(p * (len(EDGES)+3))))
        draw_graph(d, dim=count < len(EDGES))
        sidebar(d, "The problem", "Connect every vertex", [
            "No cycles. Seven edges for eight vertices.",
            "Minimize the sum of chosen edge weights.",
            "C-E is assigned cost 17 for this video."
        ], badge="TREE = V − 1 EDGES")
    elif index == 1:
        focus_list = [("B", "C"), ("A", "C"), ("C", "H"), ("A", "B")]
        focus = focus_list[min(3, int(p*4))]
        draw_graph(d, focus=focus, pulse=(t*1.6)%1)
        forest_summary_sidebar(d, kicker="Kruskal's rule", heading="Cheapest first",
            accepted=[], lines=["Sort all edges by weight.",
                "Different find roots: union.", "Same find root: skip cycle."])
    elif index == 2:
        phase = phase_for(index, p)
        seq = BASE_TREE[:3]
        accepted = seq[:min(phase, 3)]
        focus = [None, ("B", "C"), ("A", "C"), ("C", "H"), None][phase]
        rejected = ("A", "B") if phase == 4 else None
        draw_graph(d, accepted=accepted, focus=focus, rejected=rejected, pulse=(t*1.5)%1)
        if phase == 0:
            forest_summary_sidebar(d, kicker="Initial state", heading="Eight singleton trees",
                accepted=[], lines=["Every vertex starts in its own set.",
                    "Selected edges: none.", "Next candidate: B-C, cost 1."], cost=0)
        else:
            candidates = [("B", "C", 1), ("A", "C", 3),
                          ("C", "H", 4), ("A", "B", 5)]
            before = seq[:phase-1] if phase < 4 else seq
            forest_sidebar(d, step=phase, candidate=candidates[phase-1],
                           before=before, after=accepted, keep=phase < 4,
                           cost=[1, 4, 8, 8][phase-1])
    elif index == 3:
        phase = phase_for(index, p)
        seq = BASE_TREE
        accepted = seq[:min(7, 3+phase+1)]
        focus = seq[3+phase] if phase < 4 else None
        rejected = None
        draw_graph(d, accepted=accepted, focus=focus, rejected=rejected, pulse=(t*1.4)%1)
        if phase < 4:
            candidates = [("H", "F", 6), ("E", "F", 7),
                          ("G", "F", 8), ("D", "E", 9)]
            forest_sidebar(d, step=phase+5, candidate=candidates[phase],
                           before=seq[:3+phase], after=accepted, keep=True,
                           cost=[14, 21, 29, 38][phase])
        else:
            forest_summary_sidebar(d, kicker="Class result", heading="One spanning tree",
                accepted=accepted, lines=["Seven edges connect all eight vertices.",
                    "10, 11, and 17 are unnecessary."], cost=38)
    elif index == 4:
        phase = phase_for(index, p)
        alternate = BASE_TREE[:3] + [("D", "E"), ("H", "F"), ("E", "F"), ("G", "F")]
        accepted = alternate[:min(7, 3+phase)]
        focus = alternate[2+phase] if phase > 0 else None
        draw_graph(d, accepted=accepted, focus=focus, hypothetical=True, pulse=(t*1.5)%1)
        if phase == 0:
            forest_summary_sidebar(d, kicker="What if", heading="D-E: 9 to 6",
                accepted=accepted, lines=["Start after the cost-5 cycle skip.",
                    "Four singleton trees remain.", "Next candidate: D-E, cost 6."], cost=8)
        else:
            candidates = [("D", "E", 6), ("H", "F", 6),
                          ("E", "F", 7), ("G", "F", 8)]
            forest_sidebar(d, step=phase+4, candidate=candidates[phase-1],
                           before=alternate[:2+phase], after=accepted, keep=True,
                           cost=[14, 20, 27, 35][phase-1], hypothetical=True)
    elif index == 5:
        phase = min(2, int(p*3))
        focus = [("B", "C"), ("A", "B"), ("D", "E")][phase]
        accepted = BASE_TREE[:3] if phase == 1 else BASE_TREE[:1]
        rejected = ("A", "B") if phase == 1 else None
        draw_graph(d, accepted=accepted, focus=None if rejected else focus, rejected=rejected,
                   pulse=(t*1.5)%1)
        messages = [
            ("Local choice", "Consider the lightest edge next."),
            ("Feasible choice", "Reject an edge that closes a cycle."),
            ("Safe choice", "A lightest crossing edge has an exchange proof."),
        ]
        head, line = messages[phase]
        sidebar(d, "Greedy hallmarks", head, [line, "Commit now; never backtrack.",
                 "The cut property proves optimality."], badge="NO PROBABILITIES NEEDED")


NAIVE = [
    "def edge_cost(edge):",
    "    cost, start, end = edge",
    "    return cost",
    "",
    "def kruskal_naive(vertices, edges):",
    "    group = {}",
    "    for vertex in vertices:",
    "        group[vertex] = vertex",
    "    tree = []",
    "    for cost, start, end in sorted(",
    "            edges, key=edge_cost):",
    "        if group[start] == group[end]:",
    "            continue",
    "        old_group = group[end]",
    "        new_group = group[start]",
    "        for vertex in vertices:",
    "            if group[vertex] == old_group:",
    "                group[vertex] = new_group",
    "        tree.append((cost, start, end))",
    "        if len(tree) == len(vertices) - 1:",
    "            break",
    "    return tree",
]

NAIVE_COMPARE = NAIVE[4:]

ELEGANT = [
    "def kruskal_union_find(vertices, edges):",
    "    groups = DisjointSet(vertices)",
    "    tree = []",
    "    for cost, start, end in sorted(",
    "            edges, key=edge_cost):",
    "        if groups.union(start, end):",
    "            tree.append((cost, start, end))",
    "            if len(tree) == len(vertices) - 1:",
    "                break",
    "    return tree",
]


def code_panel(d, box, title, subtitle, lines, *, spacing=22, text_size=17):
    rr(d, box, 22, WHITE, PALE, 2)
    x1, y1, x2, y2 = box
    d.text((x1+22, y1+14), title, font=font(24, True), fill=INK)
    d.text((x1+22, y1+48), subtitle, font=F_SMALL, fill=MUTED)
    y = y1+82
    fnt = font(text_size, mono=True)
    for line in lines:
        d.text((x1+24, y), line, font=fnt, fill=INK)
        y += spacing


def draw_dsu_explainer(d, p):
    rr(d, (34, 128, 1246, 614), 25, WHITE, PALE, 2)
    d.text((57, 151), "WHAT DISJOINTSET DOES", font=font(29, True), fill=INK)
    d.text((58, 193), "Initially: every vertex points to itself, and every tree has size 1.",
           font=F_SUB, fill=MUTED)
    left_color = "#e7f5f1" if p < .58 else "#f4f8f8"
    right_color = "#e7f5f1" if p >= .58 else "#f4f8f8"
    rr(d, (56, 239, 621, 583), 20, left_color)
    rr(d, (644, 239, 1224, 583), 20, right_color)
    d.text((79, 257), "find(vertex): locate its tree", font=font(22, True), fill=TEAL_DARK)
    d.text((79, 292), "After early merges, links lead to root B.", font=F_SMALL, fill=INK)
    nodes = {"B": (350, 418), "A": (163, 366), "C": (173, 479),
             "F": (526, 365), "H": (528, 473)}
    for vertex in ("A", "C", "F", "H"):
        x, y = nodes[vertex]
        bx, by = nodes["B"]
        d.line((x, y, bx, by), fill=TEAL, width=4)
    for vertex, (x, y) in nodes.items():
        d.ellipse((x-25, y-25, x+25, y+25), fill=WHITE, outline=TEAL_DARK, width=4)
        centered(d, (x, y), vertex, F_NODE, INK)
    d.text((78, 525), "find(A) = B", font=font(23, True, mono=True), fill=TEAL_DARK)
    d.text((256, 532), "Compression saves shorter paths.", font=F_SMALL, fill=INK)

    d.text((667, 257), "union(start, end): join trees", font=font(22, True), fill=TEAL_DARK)
    d.text((667, 292), "Cost-6 hypothetical, before E-F.", font=F_SMALL, fill=INK)
    d.text((667, 334), "find(E) = D     find(F) = B", font=font(21, mono=True), fill=INK)
    d.text((667, 364), "Attach the smaller tree under the larger.", font=F_SMALL, fill=INK)
    rr(d, (674, 392, 895, 437), 13, "#e4f5f0", TEAL_DARK, 2)
    centered(d, (784, 414), "{A,B,C,F,H}", F_SMALL_BOLD, TEAL_DARK)
    d.text((905, 400), "+", font=font(29, True), fill=INK)
    rr(d, (947, 392, 1071, 437), 13, "#f0eaf9", COMPONENT_COLORS["D"], 2)
    centered(d, (1009, 414), "{D,E}", F_SMALL_BOLD, COMPONENT_COLORS["D"])
    d.text((674, 458), "union(E, F)  →  True: accept E-F", font=font(21, True), fill=TEAL_DARK)
    rr(d, (674, 497, 1083, 541), 13, "#e4f5f0", TEAL_DARK, 2)
    centered(d, (879, 519), "{A,B,C,D,E,F,H}", F_SMALL_BOLD, TEAL_DARK)
    d.text((674, 551), "Same root? False: skip the cycle.", font=F_SMALL, fill=INK)


def draw_code_scene(d, index, p):
    if index == 6:
        code_panel(d, (34, 128, 913, 614), "01  Readable first solution",
                   "An edge is (cost, start, end); group stores tree labels.",
                   NAIVE, spacing=18, text_size=17)
        if p < .34:
            sidebar(d, "Read the code", "One edge", [
                "(1, B, C) means cost 1 between B and C.",
                "edge_cost returns the cost.",
                "key=edge_cost tells sorted what to compare."
            ], badge="NO LAMBDA OR INDEXING")
        elif p < .67:
            sidebar(d, "Read the code", "Group labels", [
                "group[vertex] = vertex gives each node its own tree.",
                "Equal endpoint labels mean a cycle: skip.",
                "Different labels mean the trees can merge."
            ], badge="ONE LABEL PER VERTEX")
        else:
            sidebar(d, "Read the code", "Merge by scanning", [
                "Change every old group label to the new one.",
                "Each accepted edge may scan all vertices.",
                "Merge work can grow to O(V²)."
            ], badge="CLEAR, BUT SLOWER")
    elif p < .26 or p >= .88:
        code_panel(d, (24, 128, 628, 614), "01  Relabel every vertex",
                   "Same greedy decision · repeated scan", NAIVE_COMPARE,
                   spacing=21, text_size=16)
        code_panel(d, (649, 128, 1255, 614), "02  Union-find",
                   "Same sorted edges · efficient merge", ELEGANT,
                   spacing=25, text_size=17)
        rr(d, (672, 492, 1231, 530), 10, "#e4f5f0")
        d.text((689, 499), "union returns True  →  keep the edge", font=F_SMALL_BOLD, fill=TEAL_DARK)
        rr(d, (672, 539, 1231, 577), 10, "#fff0f0")
        d.text((689, 546), "union returns False  →  skip the cycle", font=F_SMALL_BOLD, fill="#a43c4d")
    else:
        draw_dsu_explainer(d, p)


def render_frame(scene_index, t, duration):
    scene = SCENES[scene_index]
    p = min(1, t / max(duration, .1))
    im, d = base_canvas(scene, scene_index, duration, t)
    if scene_index < 6:
        draw_graph_scene(d, scene_index, p, t)
    else:
        draw_code_scene(d, scene_index, p)
    footer(d, scene, t, duration)
    return im


def duration(path):
    result = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path)
    ], text=True)
    return float(result.strip())


def render_clip(i, scene):
    audio = VOICE / f"{scene['id']}.mp3"
    if not audio.exists():
        raise FileNotFoundError(audio)
    length = duration(audio) + .45
    frames = math.ceil(length * FPS)
    dest = CLIPS / f"{scene['id']}.mp4"
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "pipe:0", "-i", str(audio),
        "-filter_complex", f"[1:a]apad,atrim=duration={length:.3f}[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast",
        "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
        "-t", f"{length:.3f}", "-movflags", "+faststart", str(dest)
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for frame in range(frames):
            im = render_frame(i, frame / FPS, length)
            proc.stdin.write(im.tobytes())
    finally:
        proc.stdin.close()
        code = proc.wait()
    if code:
        raise RuntimeError(f"FFmpeg failed for {dest}: {code}")
    print(f"Rendered {dest.name}: {length:.1f}s", flush=True)
    return dest


def main():
    CLIPS.mkdir(exist_ok=True)
    paths = [render_clip(i, scene) for i, scene in enumerate(SCENES)]
    manifest = CLIPS / "concat.txt"
    manifest.write_text("".join(f"file '{p.name}'\n" for p in paths), encoding="utf-8")
    final = ROOT / "Kruskal - October 12 Class Graph - Revised Code.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", str(manifest), "-c", "copy", "-movflags", "+faststart", str(final)],
                   check=True)
    print(f"Wrote {final}", flush=True)


if __name__ == "__main__":
    main()
