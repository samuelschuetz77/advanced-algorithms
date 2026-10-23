"""Video 02 beats (metro-map version). Narration markup: [[cue]]word  {display|spoken}  (~ = space in spoken)."""
import widgets
import scenes as S

widgets.CONFIG.update(series="GRAPH SEARCH  ·  VIDEO 2 OF 6", title="Whatever-First Search, Part 2")

B1 = "JEA 5.5 · PDF p.219"


def rel(anchor, pairs):
    """extra cues: for (step, offset) -> take/do/push cues relative to `anchor`."""
    out = []
    for n, off in pairs:
        out += [(f"take{n}", anchor, off), (f"do{n}", anchor, off + 0.3), (f"push{n}", anchor, off + 0.5)]
    return out


QUEUE_RUN1_X = [("do2", "take2", 0.3), ("push2", "take2", 0.55), ("do3", "take3", 0.3), ("push3", "take3", 0.55),
                ("do4", "take4", 0.3), ("push4", "take4", 0.55)]
QRUN2 = []
for _n, _off in zip((5, 6), (-1.7, -0.9)):
    QRUN2 += rel("take7", [(_n, _off)])
QRUN2 += [("do7", "take7", 0.3), ("push7", "take7", 0.55)]
QRUN2 += rel("take7", [(8, 0.6), (9, 1.2), (10, 1.8), (11, 2.4)])
QRUN2 += [("do12", "take12", 0.3), ("push12", "take12", 0.55)]
QRUN3 = rel("take19", [(n, -0.55 * (19 - n)) for n in range(13, 19)])
QRUN3 += [("do19", "take19", 0.3), ("push19", "take19", 0.55)]
QRUN3 += rel("take19", [(n, 0.6 * (n - 19)) for n in range(20, 26)])

BEATS = [
    # ---------------------------------------------------------------- A: what does it cost?
    dict(id="recap", topic="Last time", scene=S.scene_recap,
         narration=("Last time, we ran one short algorithm on a graph. [[c1]]Take a token from the pile. [[c2]]If its "
                    "vertex is new, mark it. [[c3]]Then add a token for every edge leaving that vertex. Today we ask two "
                    "questions. How long does that take? And what happens if we change the pile?")),
    dict(id="world", topic="A new example: a metro map", scene=S.scene_world,
         narration=("Here is a city metro map. Each [[w1]]station is a vertex, and each [[w2]]track between two stations is "
                    "an edge. [[start]]You begin at Arch. A station counts as [[w3]]visited the first time you arrive "
                    "there. Every track you could still try is a [[w4]]token: from which station, to which. And the "
                    "station you arrived from is that station's [[w5]]parent.")),
    dict(id="predict_count", topic="A guess", scene=S.scene_predict, pause=6.0,
         predict="How many tokens, in total?",
         narration=("Before we count anything, guess. The map has twelve tracks. [[q]]How many tokens get put in the "
                    "pile in total, counting every track you could ever try?")),
    dict(id="two_each", topic="One track", book=B1, scene=S.scene_two_each,
         narration=("Look at one track, between Arch and Bay. When you arrive at Arch, [[t1]]you add a token to try this "
                    "track toward Bay. When you arrive at Bay, [[t2]]you add a token to try it back toward Arch. So every "
                    "track makes two tokens, one from each end.")),
    dict(id="all_edges", topic="All twelve tracks", scene=S.scene_all_edges,
         narration="Do that for all twelve tracks, [[all]]one after another, and we get twenty-four tokens."),
    dict(id="plus_one", topic="Counting tokens", scene=S.scene_plus_one,
         narration=("Add the one token we start with, [[plus]]at Arch. [[total]]Twenty-five tokens in all. [[formula]]Two "
                    "times E, plus one. [[eq]]Two times twelve, plus one, is twenty-five. That is exactly the count from "
                    "last time.")),
    dict(id="cost", topic="The cost of tokens", book=B1, scene=S.scene_cost,
         narration=("[[one]]Every token is put in the pile once, [[two]]and taken out once. [[three]]Call the time for one "
                    "put, or one take, T. [[four]]Then all the tokens together cost [[five]]about two E times T.")),
    dict(id="vertices", topic="Marking costs too", scene=S.scene_vertices,
         narration=("Each station is also [[mark]]marked only once, which adds about V more work. So the total time is "
                    "[[v]]V plus E times T. [[w]]The V is the marking. [[w2]]The E times T is the tokens.")),
    dict(id="stackT", topic="With a stack", scene=S.scene_stackT,
         narration=("With a stack, a put or a take only touches [[top]]the top of the pile, so [[T]]T is a constant, "
                    "however big the pile gets. The total is V plus E. [[linear]]We call that linear time.")),
    dict(id="matrix", topic="One warning", book="JEA 5.4 · PDF p.217", scene=S.scene_matrix,
         narration=("One warning. The book assumes the map is stored as [[lists]]a list of neighbors for each station. "
                    "If it were stored as [[matrix]]a table of yes or no answers, [[scan]]finding one station's neighbors "
                    "would mean checking every cell in a row, V steps each time, and the total would grow like "
                    "[[square]]V times V.")),
    # ---------------------------------------------------------------- B: three piles
    dict(id="three_rules", topic="One pile, three rules", book="JEA 5.5 · PDF p.218", scene=S.scene_three_rules,
         narration=("Now the pile. The proof only needed somewhere to put tokens in and take tokens out. It never said "
                    "which one to take. Here is one pile with four numbered tokens. [[stack]]Take the newest, and that is a "
                    "stack. [[queue]]Take the oldest, and that is a queue. [[pq]]Take the smallest number, and that is a "
                    "priority queue.")),
    dict(id="names", topic="Three searches", scene=S.scene_names,
         narration=("Same algorithm, three behaviors. [[n1]]A stack gives depth-first search. [[n2]]A queue gives "
                    "breadth-first search. [[n3]]A priority queue gives best-first search. Let us run the first two on the "
                    "metro map.")),
    dict(id="stack_run", topic="The stack: depth-first", scene=S.search_scene("stack", list(range(1, 26))),
         extra_cues=S.schedule("go", 1, 25, 0.42), min_len=19.0,
         narration=("First, the stack. The newest token always goes first. [[go]]Watch how deep it goes. From Arch, ride to "
                    "Dock, then Fort, then Gate, then East, then Cove, and last of all, Bay.")),
    dict(id="stack_tree", topic="The stack's tree", scene=S.scene_stack_tree,
         narration=("The came-from links form one long, skinny chain, six tracks deep. [[friend]]Bay is right next to "
                    "Arch, yet [[ben]]in this tree, the route to Bay passes through five other stations.")),
    dict(id="predict_queue", topic="Now the queue", scene=S.search_scene("queue", [], idle_after=1, days=True), pause=4.0,
         predict="Which token comes out first?",
         narration=("Now the queue. From Arch, three tokens are in the pile. This time we take the oldest token. "
                    "[[q]]Which one comes out first?")),
    dict(id="queue_run1", topic="The queue: one stop away", scene=S.search_scene("queue", [2, 3, 4], days=True),
         extra_cues=QUEUE_RUN1_X,
         narration=("Arch to Bay, the oldest. [[take2]]Bay is new. Then Arch to Cove, [[take3]]Cove is new. Then Arch to "
                    "Dock, [[take4]]Dock is new. Every station next to Arch is reached before we go any further. Those are "
                    "one stop away.")),
    dict(id="queue_run2", topic="The queue: two stops away", scene=S.search_scene("queue", list(range(5, 13)), days=True),
         extra_cues=QRUN2,
         narration=("Now the tokens from Bay, Cove, and Dock. Most lead to stations already visited, so they are thrown "
                    "away. [[take7]]Bay to East: East is new. Most of Cove's tokens are thrown away. But [[take12]]Cove to "
                    "Fort: Fort is new. East and Fort are two stops from Arch.")),
    dict(id="queue_run3", topic="The queue: three stops away", scene=S.search_scene("queue", list(range(13, 26)), days=True),
         extra_cues=QRUN3,
         narration=("Next come Dock's tokens, and then East's. Most are thrown away. At last, [[take19]]East to Gate: Gate "
                    "is new, the final station. Three stops. Everything left in the pile is thrown away.")),
    dict(id="queue_tree", topic="Two trees", book="Figure 5.12 · PDF p.220", scene=S.scene_queue_tree,
         narration=("The queue gives a short, bushy tree. Every station is at most three stops from Arch. [[q]]Put it next "
                    "to the stack's tree, and the difference is clear: depth six, against depth three.")),
    dict(id="shortest", topic="Why the queue is special", scene=S.scene_shortest,
         narration=("That is no accident. Each round reaches one stop further, so the number of stops at which a station "
                    "is first reached is the fewest tracks between it and Arch. [[route]]Bay: one stop. [[gus]]Gate: three "
                    "stops, and no route is shorter. [[claim]]Breadth-first search finds the routes with the fewest stops. "
                    "Depth-first search does not.")),
    dict(id="pq", topic="Best-first search", book="JEA 5.6 · PDF pp.220-221", scene=S.scene_pq,
         narration=("The third rule puts a number on every track, [[w]]say, the minutes of travel, and always takes the "
                    "smallest. That is best-first search. [[a]]With the track times as the numbers, it builds a minimum "
                    "spanning tree: that is {Jarník's|Yarnik's} algorithm, which most people call Prim's. [[b]]With the "
                    "time so far as the number, it finds the fastest routes on a weighted map: that is "
                    "{Dijkstra's|Dikestra's} algorithm. [[time]]A priority queue costs a little more per token, so the "
                    "time is V plus E log E. [[later]]Later chapters return to both.")),
    # ---------------------------------------------------------------- C: three more situations
    dict(id="disc1", topic="Problem: a second network", book="JEA 5.6 · PDF p.221", scene=S.scene_disc1,
         narration=("A new problem. Across the water, a separate ferry network has three stations: Mill, Nest, and Oak. "
                    "They connect only to each other. [[run]]Your search from Arch visits the whole metro, and the pile "
                    "empties. The search stops. [[never]]Mill, Nest, and Oak are never visited.")),
    dict(id="wrapper", topic="The loop around the search", scene=S.scene_wrapper,
         narration=("To reach everywhere, add a loop. [[w1]]Go through every station. [[w2]]If a station has not been "
                    "visited yet, it belongs to a new network. [[w3]]Count it, and start a fresh search from there.")),
    dict(id="wrapper_code", topic="The loop in Python", scene=S.scene_wrapper_code,
         narration=("In Python. [[c_set]]A set called visited remembers which stations we have seen. [[c_zero]]Networks "
                    "starts at zero. [[c_for]]For each station in the graph, [[c_not]]if the station is not in visited, "
                    "[[c_add]]we found a new network, so add one, [[c_call]]and run the search from that station, which "
                    "fills in visited.")),
    dict(id="count_result", topic="Counting the networks", book="JEA 5.6 · PDF pp.221-222", scene=S.scene_count_result,
         narration=("Run it. [[g1]]Arch starts network one, and marks seven stations. [[g2]]Mill starts network two, and "
                    "marks three. Two networks. Every vertex and every edge is still visited only once, so even with the "
                    "loop, [[lin]]it is still V plus E. The same loop counts the networks for free.")),
    dict(id="dir1", topic="Directed graphs", book="JEA 5.6 · PDF p.223", scene=S.scene_dir1,
         narration=("Now make some tracks one-way. [[ex]]An arrow from Arch to Bay means trains only run from Arch to Bay. "
                    "[[same]]The search code does not change at all. A marked station just adds a token for each arrow "
                    "leaving it.")),
    dict(id="dir2", topic="Run it from Arch", scene=S.scene_dir2,
         narration=("Run it from Arch. [[run]]Bay, Cove, East, and Fort can all be reached. [[never]]Dock and Gate cannot, "
                    "even though they are on the map, because no arrow leads into them. [[sym]]Reachability is no longer "
                    "symmetric.")),
    dict(id="dir_tree", topic="The tree of what Arch reaches", book="JEA 5.6 · PDF p.223", scene=S.scene_dir_tree,
         narration=("The came-from arrows still form a tree, [[tree]]pointing away from Arch. [[notspan]]But it is a tree of "
                    "only the stations Arch can reach, not a spanning tree of the whole map. [[all]]Stacks, queues, and "
                    "priority queues all still work.")),
    dict(id="flood1", topic="Paint bucket as a graph", book="JEA 5.7 · PDF p.224", scene=S.scene_flood1,
         narration=("One more use. The paint bucket in a drawing program. Each [[pa]]pixel is a vertex, and two neighboring "
                    "pixels [[pb]]with the same color share an edge. [[edges]]Those edges form a graph on the pixels. "
                    "[[click]]Click a pixel, and the bucket must recolor everything reachable from it. [[pc]]That is "
                    "reachability again.")),
    dict(id="flood2", topic="Recolor as we mark", scene=S.scene_flood2,
         narration=("So we run a search from the clicked pixel, and [[fill]]recolor each pixel the moment it is marked. "
                    "[[other]]The other blob of the same color is untouched, because no chain of same-colored neighbors "
                    "leads to it.")),
    dict(id="flood3", topic="A reduction", book="JEA 5.7 · PDF p.224", scene=S.scene_flood3,
         narration=("This is called a reduction. We solve the paint bucket problem by calling reachability as a black box. "
                    "[[r1]]A grid of n by n pixels has n squared vertices, [[r2]]and at most two n squared edges, so "
                    "[[r3]]the search runs in n squared time. [[black]]All that matters about the search is what it promises, "
                    "not how it works.")),
    dict(id="recap2", topic="Recap", scene=S.scene_recap2,
         narration=("Let us retell it. [[c1]]About two E plus one tokens, so a stack or queue search is linear. [[c2]]Swap "
                    "the pile, and you swap the search. [[c3]]Loop over every station, to cover every network. [[c4]]Arrows "
                    "change who can be reached, not the code. [[next]]Next time: counting paths, from class.")),
]
