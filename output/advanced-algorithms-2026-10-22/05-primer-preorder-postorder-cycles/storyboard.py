"""Video 05 beats. Narration markup: [[cue]]word  {display|spoken}  (~ = space in spoken)."""
import widgets
import scenes as S

widgets.CONFIG.update(series="GRAPH SEARCH  ·  VIDEO 5 OF 6", title="Reading Primer: JEA 6.1 and 6.2")

BLUE, GREEN, RED, ORANGE = S.BLUE, S.GREEN, S.RED, S.ORANGE
ACCENT_DARK = S.ACCENT_DARK

BEATS = [
    # ------------------------------------------------------------ A: the story, the clock, the states
    dict(id="hook", topic="The thread", scene=S.scene_hook,
         narration=("In an old story, Theseus walked into a labyrinth holding a ball of thread, so he could always find his "
                    "way back. Depth-first search is that thread. This maze has seven [[rooms]]rooms, joined by twelve "
                    "one-way [[doors]]doors. Ada will explore it from room {A}, [[thread]]unrolling a thread behind her.")),
    dict(id="clock", topic="Two stamps per room", book="JEA 6.1 · PDF p.246", scene=S.scene_clock,
         narration=("Ada carries a clock. [[enter]]The first time she enters a room, she advances the clock, and writes the "
                    "time on the room. That is the room's starting time, its preorder number. [[leave]]When she leaves a room "
                    "for good, because every door out of it has been tried, she advances the clock again, and writes that: "
                    "its finishing time, its postorder number.")),
    dict(id="states", topic="Three states", book="JEA 6.1 · PDF p.246", scene=S.scene_states,
         narration=("At any moment, every room is in one of three states. [[n]]New: Ada has never entered it. [[a]]Active: "
                    "she has entered it, but not yet left it for good. [[f]]Finished: she has left it for good. "
                    "[[path]]The active rooms always form one single path, from the start to Ada. That is the thread.")),
    # ------------------------------------------------------------ B: the walk
    dict(id="run1", topic="The walk, part one", scene=S.dfs_run(0, 12, show_types=False),
         narration=("[[e0]]Ada enters {A}: clock one. [[e1]]The door to {B} leads to a new room, [[e2]]so she goes: clock two. "
                    "[[e3]]{B} to {D}, [[e4]]clock three. [[e5]]{D} to {E}, [[e6]]clock four. [[e7]]{E} has a door back to {B}, "
                    "but {B} is still on the thread. [[e8]]{E} has no more doors, so {E} is finished: clock five. "
                    "[[e9]]Back in {D}: finished, clock six. [[e10]]Back in {B}: its other door, to {E}, leads to a finished "
                    "room. [[e11]]{B} is finished: clock seven.")),
    dict(id="run2", topic="The walk, part two", scene=S.dfs_run(12, 26, show_types=True),
         narration=("[[e12]]Back at {A}, the next door leads to {C}, [[e13]]a new room: clock eight. [[e14]]{C} to {F}, "
                    "[[e15]]nine. [[e16]]{F} has a door back to {C}, which is on the thread. [[e17]]{F} to {G}, [[e18]]ten. "
                    "[[e19]]{G} has a door to {D}, a finished room, in a branch Ada already completed. [[e20]]{G} is "
                    "finished: eleven. [[e21]]{F} is finished: twelve. [[e22]]Back at {C}: its door to {G} leads to a "
                    "finished room. [[e23]]{C} is finished: thirteen. [[e24]]Back at {A}: the last door, to {E}, also leads "
                    "to a finished room. [[e25]]{A} is finished: fourteen. The walk is over.")),
    dict(id="orders", topic="Two orderings", book="JEA 6.1 · PDF p.246", scene=S.scene_orders,
         narration=("Read the rooms by starting time, [[pre]]{A}, {B}, {D}, {E}, {C}, {F}, {G}. That is a preorder. Read "
                    "them by finishing time, [[post]]{E}, {D}, {B}, {G}, {F}, {C}, {A}. That is a postorder. [[diff]]With a "
                    "different order of doors, or a different starting room, you would get different ones.")),
    dict(id="intervals", topic="Active intervals", book="JEA 6.1 · PDF p.247, Figure 6.4", scene=S.scene_intervals,
         narration=("Draw each room as a bar, from its starting time to its finishing time. Any two bars are either "
                    "[[nest]]nested, one inside the other, or [[apart]]completely apart. [[anc]]And one room's bar contains "
                    "another's exactly when it is an ancestor in the thread tree. The bar for room {B} contains the bars for {D} and {E}.")),
    dict(id="lemma", topic="Four ways to say 'ancestor'", book="Lemma 6.1 · PDF p.248", scene=S.scene_lemma,
         narration=("The book says this in four equivalent ways. [[l1]]One: u is an ancestor of v in the thread tree. "
                    "[[l2]]Two: u's bar contains v's bar. [[l3]]Three: when v starts, u is active. [[l4]]Four: just before u "
                    "starts, there is a path from u to v through rooms that are all new. [[same]]All four mean the same thing.")),
    # ------------------------------------------------------------ C: four kinds of door
    dict(id="types_intro", topic="Four kinds of door", book="JEA 6.1 · PDF p.247", scene=S.scene_types_intro,
         narration=("Now classify the doors. When Ada tries a door from u to v, there are four cases, depending on v's state "
                    "at that moment. [[t1]]If v is new, it is a tree edge. [[t2]]If v is active, it is a back edge. [[t3]]If v "
                    "is finished and below u, it is a forward edge. [[t4]]If v is finished, and somewhere else, it is a cross "
                    "edge.")),
    dict(id="tree", topic="Tree edges", scene=S.edge_scene("tree", [("A", "B"), ("B", "D"), ("D", "E"), ("A", "C"), ("C", "F"), ("F", "G")],
                                                           "v is new, so Ada walks through, and the door joins the thread tree. Six doors are tree edges.", ("A", "B")),
         narration=("[[go]]A tree edge: v is new, so Ada walks through, and the door joins the thread tree. {A} to {B} is a "
                    "tree edge. So are five more.")),
    dict(id="back", topic="Back edges", scene=S.edge_scene("back", [("E", "B"), ("F", "C")],
                                                           "v is active: already on the thread. The door loops back up the thread. Two doors are back edges.", ("E", "B")),
         narration=("[[go]]A back edge: v is active, already on the thread. {E} to {B}: {B} is on the thread, so this door "
                    "loops back up it. {F} to {C} does the same. Two doors are back edges.")),
    dict(id="forward", topic="Forward edges", scene=S.edge_scene("forward", [("B", "E"), ("C", "G"), ("A", "E")],
                                                                 "v is finished, and it is below u: Ada already reached it by another route. Three doors are forward edges.", ("B", "E")),
         narration=("[[go]]A forward edge: v is finished, and it is below u. {B} to {E}: Ada already reached {E} through {D}. "
                    "{C} to {G} and {A} to {E} are the same. Three doors are forward edges.")),
    dict(id="cross", topic="Cross edges", scene=S.edge_scene("cross", [("G", "D")],
                                                             "v is finished, and not below u: it sits in a branch that Ada completed earlier. One door is a cross edge.", ("G", "D")),
         narration=("[[go]]A cross edge: v is finished, and not below u. {G} to {D}: {D} sits in a branch that Ada completed "
                    "before she even entered {G}'s branch. One door is a cross edge.")),
    dict(id="impossible", topic="What the bars look like", book="JEA 6.1 · PDF p.247, Figure 6.5", scene=S.scene_impossible,
         narration=("What do the bars look like? [[s1]]For a tree edge, u's bar contains v's. [[s2]]For a forward edge, the "
                    "same. [[s3]]For a back edge, v's bar contains u's. [[s4]]For a cross edge, v's bar is entirely before u's. "
                    "[[none]]A fifth kind, with v starting after u has finished, is impossible, because Ada tries every door out "
                    "of u before she leaves it.")),
    # ------------------------------------------------------------ D: cycles
    dict(id="cycle", topic="A back edge means a cycle", book="JEA 6.2 · PDF p.249", scene=S.scene_cycle,
         narration=("Here is the key fact. If any door leads to an active room, the maze has a cycle. [[loop]]The thread "
                    "runs from {B} down to {E}, and the door from {E} back to {B} closes the loop. [[fin]]But doors to "
                    "finished rooms never prove a cycle.")),
    dict(id="finish_times", topic="The same test, with finishing times", book="JEA 6.2 · PDF p.249", scene=S.scene_finish_times,
         narration=("There is a second way to see it, with finishing times. [[tab]]Here is every door, with the two finishing "
                    "times. For a back edge, the room it points to is still active when u finishes, so it finishes later. "
                    "[[rule]]If an edge u to v has u finishing before v, there is a cycle. In a DAG, every edge has u finishing "
                    "after v.")),
    dict(id="code_intro", topic="The algorithm in Python", book="JEA 6.2 · PDF p.249, Figure 6.7", scene=S.code_scene(
        hl=[(2, None), (3, None), (4, None)], boxes=[(2, "status = {}", BLUE, "d"), (4, 'status[v] = "new"', GREEN, "n")],
        notes=[("d", "status = {}", "an empty dictionary: room → state", BLUE),
               ("n", 'status[v] = "new"', "the for loop sets every room to new, before anything starts", GREEN)]),
         narration=("Now the algorithm, in Python. It keeps a status for every room. [[d]]First, an empty dictionary. [[n]]A "
                    "loop sets every room's status to new.")),
    dict(id="code_visit", topic="Visiting a room", scene=S.code_scene(
        hl=[], boxes=[(6, "def visit(v):", BLUE, "a"), (7, 'status[v] = "active"', ACCENT_DARK, "b"),
                      (8, "for w in graph[v]:", GREEN, "c")],
        notes=[("a", "def visit(v)", "a function inside a function, like before: one call per room", BLUE),
               ("b", 'status[v] = "active"', "the moment Ada enters: v goes on the thread", ACCENT_DARK),
               ("c", "for w in graph[v]", "every door out of v", GREEN)]),
         narration=("[[a]]Visit is a function inside a function, one call per room. [[b]]The moment Ada enters v, its status "
                    "becomes active. [[c]]Then, for each door out of v, to a room w, look at w's status.")),
    dict(id="code_checks", topic="The three cases", scene=S.code_scene(
        hl=[], boxes=[(9, 'if status[w] == "active":', RED, "a"), (10, "return False", RED, "b"),
                      (11, 'if status[w] == "new":', BLUE, "c"), (12, "if visit(w) == False:", ACCENT_DARK, "d"),
                      (13, "return False", ACCENT_DARK, "e")],
        notes=[("a", 'status[w] == "active"', "a back edge: the door leads onto the thread", RED),
               ("b", "return False", "so there is a cycle. Stop, and say so.", RED),
               ("c", 'status[w] == "new"', "a tree edge: go there", BLUE),
               ("d", "visit(w) == False", "if that visit found a cycle deeper down...", ACCENT_DARK),
               ("e", "return False", "...pass the bad news up", ACCENT_DARK)]),
         narration=("[[a]]If w is active, that is a back edge. [[b]]Return False: there is a cycle. [[c]]If w is new, that is "
                    "a tree edge, so [[d]]visit it. And if that visit comes back False, a cycle was found deeper down, "
                    "[[e]]so return False too. If w is finished, do nothing: it can never prove a cycle.")),
    dict(id="code_finish", topic="Leaving the room", scene=S.code_scene(
        hl=[], boxes=[(14, 'status[v] = "finished"', GREEN, "a"), (15, "return True", GREEN, "b")],
        notes=[("a", 'status[v] = "finished"', "every door tried: Ada leaves for good", GREEN),
               ("b", "return True", "no cycle was found below this room", GREEN)]),
         narration=("[[a]]When every door out of v has been tried, v becomes finished. [[b]]And visit returns True: no cycle "
                    "was found at or below this room.")),
    dict(id="code_outer", topic="The outer loop", scene=S.code_scene(
        hl=[], boxes=[(17, "for v in graph:", BLUE, "a"), (18, 'if status[v] == "new":', GREEN, "b"),
                      (19, "if visit(v) == False:", RED, "c"), (21, "return True", GREEN, "d")],
        notes=[("a", "for v in graph", "try every room as a starting point", BLUE),
               ("b", 'status[v] == "new"', "skip rooms an earlier walk already covered", GREEN),
               ("c", "visit(v) == False", "any cycle anywhere: answer False", RED),
               ("d", "return True", "every room covered, no back edge found: it is a DAG", GREEN)]),
         narration=("The outer loop. [[a]]Try every room as a starting point. [[b]]Skip the ones an earlier walk already "
                    "covered. [[c]]If any walk finds a cycle, the answer is False. [[d]]If every room is covered and no back "
                    "edge was found, return True: the graph is a DAG.")),
    dict(id="run_cycle", topic="Run it on the maze", scene=S.scene_run_cycle, min_len=15.0,
         narration=("Run it on the maze. [[go]]Visit {A}: active. Visit {B}. Visit {D}. Visit {E}. Now {E}'s door leads to "
                    "{B}, and {B}'s status is active. Return False, right away: the maze has a cycle. It never even looks at "
                    "the rest.")),
    dict(id="dag", topic="Without the back edges", book="JEA 6.2 · PDF p.249", scene=S.scene_dag,
         narration=("[[rm]]Remove the two back edges, {E} to {B} and {F} to {C}. Ten doors are left. [[true]]Now no door ever "
                    "leads to an active room, and the function returns True. This is a DAG. [[src]]A room with no doors in is a "
                    "source: here, room {A}. [[snk]]A room with no doors out is a sink: here, room {E}. [[every]]Every DAG has at least "
                    "one source and one sink.")),
    dict(id="dfsall", topic="Starting everywhere", book="JEA 6.1 · PDF p.245", scene=S.scene_dfsall,
         narration=("One more detail. If we start a walk from every room in turn, skipping the ones already entered, the "
                    "number of separate trees depends on the order. [[one]]Start at {A}: one tree. [[two]]Start at {G} first, "
                    "and the first walk is stuck after {G}, {D}, {E}, {B}. Then {A} starts a second tree. [[any]]In a directed "
                    "graph, even a connected one, the count can be anything from one to V.")),
    dict(id="recap", topic="Recap", scene=S.scene_recap,
         narration=("To recap. [[c1]]Every room gets two stamps from one clock. [[c2]]Every room is new, active, or finished, "
                    "and the active rooms are the thread. [[c3]]Every door is a tree, forward, back, or cross edge. [[c4]]A "
                    "back edge, an edge to an active room, means a cycle. [[next]]Next: topological sort, and dynamic "
                    "programming, sections six point three and six point four.")),
]
