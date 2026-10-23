"""Video 06 beats. Narration markup: [[cue]]word  {display|spoken}  (~ = space in spoken)."""
import widgets
import scenes as S

widgets.CONFIG.update(series="GRAPH SEARCH  ·  VIDEO 6 OF 6", title="Reading Primer: JEA 6.3 and 6.4")

BLUE, GREEN, RED, ORANGE, PURPLE = S.BLUE, S.GREEN, S.RED, S.ORANGE, S.PURPLE
ACCENT_DARK = S.ACCENT_DARK

BEATS = [
    # ------------------------------------------------------------ A: topological sort (6.3)
    dict(id="def", topic="Topological ordering", book="JEA 6.3 · PDF p.250", scene=S.scene_def,
         narration=("Section six point three starts with a simple idea. Here is the hiking map from the count paths video. "
                    "In a drawing, the trails can point in any direction. A topological ordering rearranges the junctions "
                    "onto a line, so that every trail points forward, from left to right. [[ok]]Watch the junctions slide "
                    "into place. Every arrow now points right. [[bad]]Here is a line-up that fails: some arrows point "
                    "backward. [[formal]]In symbols: for every edge from vertex u to vertex v, u comes before v. [[tot]]The "
                    "book calls this a total order: any two vertices have a definite before and after.")),
    dict(id="cycle", topic="Why a cycle breaks it", book="JEA 6.3 · PDF p.250", scene=S.scene_cycle,
         narration=("Why can a graph with a cycle never have one? Take three tasks: x before y, y before z, and z before x, "
                    "closing the circle. Who goes first? [[x1]]Not task x, because task z must come before it. [[y1]]Not task "
                    "y, because task x must come before it. [[z1]]And not task z, because task y must come before it. "
                    "[[all]]Nobody can go first: every vertex on a cycle has an arrow pointing into it. [[book]]The book says "
                    "it from the other end: the rightmost vertex has an arrow that can only point left. So a cycle rules out "
                    "any topological ordering.")),
    dict(id="goals", topic="One map, two goals", scene=S.scene_goals,
         narration=("To make this concrete, we will keep using the hiking map: seven junctions, "
                    "twelve one-way trails. [[s]]This time, [[score]]every trail has a number: the scenery points you collect "
                    "walking it. We have two goals. [[g1]]First: an order of the junctions that respects every trail. "
                    "[[g2]]Second: the most scenic route from Start to Summit.")),
    dict(id="fill", topic="The book's version: an array filled from the back", book="JEA 6.3 · PDF p.251, Figure 6.9",
         scene=S.scene_fill,
         narration=("First goal. The book's algorithm uses an array S, with one slot per vertex. A clock starts at V, "
                    "which is seven. Run depth-first search, and whenever a vertex finishes, put it in the slot the clock "
                    "points to, then move the clock down. [[f1]]Summit finishes first: it goes in the last slot, S seven. "
                    "[[f2]]Meadow finishes next, into S six. [[f3]]Falls, into S five. [[f4]]Creek, into S four. "
                    "[[f5]]Ridge, into S three. [[f6]]Pine, into S two. [[f7]]And Start finishes last, into S one. "
                    "[[done]]Read the array from left to right, and every trail points to the right.")),
    dict(id="order_check", topic="Check the array", scene=S.scene_order_check,
         narration=("Lay the vertices out in the order of S. [[line]]Start, Pine, Ridge, Creek, Falls, Meadow, Summit. "
                    "[[zero]]All twelve trails point to the right: zero point left. [[lin]]One depth-first search did all of "
                    "it, so the time is V plus E.")),
    dict(id="code", topic="The same thing in Python", scene=S.scene_code,
         narration=("In Python, the simplest version needs no clock. [[kids]]Visit a vertex by visiting every neighbor not "
                    "yet visited. [[app]]Then append the vertex to a list, after all its neighbors. That puts the vertices in "
                    "finish order. [[rev]]The last line reverses the list in place, which is the same as filling the array from "
                    "the back. [[outer]]And an outer loop starts a search from every vertex not yet visited.")),
    dict(id="cycle_check", topic="What if there might be a cycle?", book="JEA 6.3 · PDF p.251", scene=S.scene_cycle_check,
         narration=("This version assumes the graph has no cycle. [[a]]If we already know it is acyclic, plain marking is "
                    "enough. [[b]]If it might have a cycle, use the three-state version from the last video, and fail "
                    "gracefully the moment an edge leads to an active vertex. The book writes that failure as: fail gracefully.")),
    dict(id="implicit", topic="Often, you do not need the list", book="JEA 6.3 · PDF pp.250-252", scene=S.scene_implicit,
         narration=("Often, the sorted list is not the real goal. We want to do something at each vertex, in order. "
                    "[[proc]]Then we can do that something at the end of each vertex's search, which handles the vertices in "
                    "reverse topological order. [[noarr]]No array is needed: the book just renames the post-visit step to "
                    "process. [[p1]]Summit is processed first, [[p2]]then Meadow, [[p3]]Falls, [[p4]]Creek, [[p5]]Ridge, "
                    "[[p6]]Pine, [[p7]]and Start last. Every vertex is processed after everything it points to.")),
    dict(id="rev", topic="Forward order: reverse the graph", book="JEA 6.3 · PDF p.252", scene=S.scene_rev,
         narration=("What if we want the vertices in forward order instead? One way: [[rev]]search the reversal of the graph, "
                    "written rev of G, where every edge is flipped. [[src]]Every source of G becomes a sink of rev of G, and "
                    "the other way round. A reversed cycle is still a cycle, so reversing a DAG gives another DAG. [[lin]]And "
                    "building the reversal takes V plus E time.")),
    dict(id="footnote", topic="Two orders, both correct", book="JEA 6.3 · PDF p.252, footnote 3", scene=S.scene_footnote,
         narration=("There is a subtle point, in the book's footnote. [[one]]Here is the reverse of G's postorder. [[two]]And "
                    "here is a postorder of the reversed graph. Both are topological orderings of G, with zero backward edges. "
                    "[[diff]]But they are different: Ridge and Creek swap places. So a postordering of rev of G is not "
                    "necessarily the reversal of a postordering of G.")),
    # ------------------------------------------------------------ B: memoization and DP (6.4)
    dict(id="dep", topic="Section 6.4: the dependency graph", book="JEA 6.4 · PDF p.252", scene=S.scene_dep,
         narration=("Section six point four. Remember the frog. [[rec]]The ways from stone i is the ways from stone i plus "
                    "one, plus the ways from stone i plus two. [[dep]]The book draws a dependency graph for any recurrence: a "
                    "vertex for every subproblem, and an edge from one subproblem to another, if evaluating the first needs "
                    "the second. [[same]]For the frog, that graph is the stepping-stone graph itself. [[acyc]]And it has to be "
                    "acyclic. Otherwise, the plain recursion would never halt.")),
    dict(id="memo_dfs", topic="Memoization is depth-first search", book="JEA 6.4 · PDF p.253, Figure 6.10", scene=S.scene_memo_dfs,
         narration=("Here is the big claim. Evaluating a recurrence with memoization is exactly the same as a depth-first "
                    "search of the dependency graph. [[m1]]Is the value still undefined? That is the same as: is the vertex "
                    "unmarked. [[m2]]Starting to evaluate is the pre-visit. [[m3]]Evaluating every subproblem it needs is the "
                    "recursive calls along the edges. [[m4]]And finishing the value is the post-visit. [[mk]]A vertex is marked "
                    "when its value has been computed. [[pp]]The pre-visit and post-visit steps stand in for the actual "
                    "arithmetic.")),
    dict(id="dp_post", topic="Dynamic programming is a postorder", book="JEA 6.4 · PDF p.253, Figure 6.11", scene=S.scene_dp_post,
         narration=("Now dynamic programming. It evaluates every subproblem in reverse topological order: each one is considered "
                    "after the subproblems it depends on. [[go]]For the frog, that means stone seven, six, five, down to zero. "
                    "That order is a postorder of the dependency graph. [[every]]So every dynamic programming algorithm is "
                    "equivalent to a postorder traversal of the dependency graph of its recurrence.")),
    dict(id="grid", topic="Why DP uses nested loops", book="JEA 6.4 · PDF pp.253-254, Figure 6.12", scene=S.scene_grid,
         narration=("Most dynamic programming algorithms look different from a topological sort. [[fill]]Take edit distance. "
                    "[[one]]Each subproblem depends on its left, upper, and diagonal neighbors. The dependency graph is a regular "
                    "grid. [[loops]]Because it is so regular, we hard-wire a good order into the algorithm, as nested loops, so "
                    "no topological sort is needed at run time. [[eval]]The book calls that order the evaluation order.")),
    dict(id="diffs", topic="Two small differences", book="JEA 6.4 · PDF p.253", scene=S.scene_diffs,
         narration=("So there are two small differences between most dynamic programming and topological sort. "
                    "[[d1]]First, the dependency graph is implicit. The recurrence encodes the edges, so there is no adjacency "
                    "list in memory. That is minor, as long as we can list each subproblem's children in constant time. "
                    "[[d2]]Second, the graph is usually regular, so nested loops replace the topological sort. "
                    "[[d3]]When the graph is not regular, we can use depth-first search directly.")),
    # ------------------------------------------------------------ longest path
    dict(id="problem", topic="An irregular graph: longest path", book="JEA 6.4 · PDF pp.253-254", scene=S.scene_problem,
         narration=("Here is an irregular graph: the hiking map. [[prob]]The longest path problem asks: given a weighted "
                    "directed graph, a start s and a target t, find the path with the largest total weight. Here, the most "
                    "scenic route. [[np]]In general directed graphs, that problem is NP-hard. [[easy]]But if the graph is "
                    "acyclic, it takes only linear time.")),
    dict(id="recurrence", topic="The recurrence", book="JEA 6.4 · PDF p.254", scene=S.scene_recurrence,
         narration=("[[def]]For any vertex v, let LLP of v be the length of the longest path from v to t. [[base]]If v is "
                    "t, it is zero: you are already there. [[rec]]Otherwise, look at every edge from v to some w. Take the edge's "
                    "length, plus LLP of w, and keep the maximum. [[neg]]If v has no edges out, and is not t, the maximum of "
                    "nothing is minus infinity: there is no route. [[dep]]The dependency graph of this recurrence is the input "
                    "graph itself. [[dfs]]So a depth-first search, memoizing as we go, solves it in V plus E time.")),
    dict(id="run", topic="Run it on the hiking map", scene=S.scene_run,
         narration=("Run it. Summit is the target, so its score is zero. [[v1]]Meadow has one trail, to Summit, worth five. "
                    "Five plus zero is five. [[v2]]Falls has one trail, worth four. Four. [[v3]]Creek has two trails. Via Meadow: "
                    "two plus five is seven. Via Falls: seven plus four is eleven. The best is eleven. [[v4]]Ridge: via Meadow, "
                    "four plus five is nine. Via Falls, three plus four is seven. The best is nine. [[v5]]Pine has three trails. "
                    "Via Creek: five plus eleven is sixteen. Via Ridge: one plus nine is ten. Via Meadow: six plus five is "
                    "eleven. The best is sixteen. [[v6]]Start: via Pine, three plus sixteen is nineteen. Via Creek, four plus "
                    "eleven is fifteen. Via Ridge, two plus nine is eleven. The best is nineteen.")),
    dict(id="lp_setup", topic="The Python: the setup", scene=S.scene_lp_code(
        boxes=[(1, "length", BLUE, "len"), (2, "best = {}", GREEN, "best")],
        notes=[("len", "length", "a dictionary: the pair (v, w) gives the scenery points of the trail from v to w", BLUE),
               ("best", "best = {}", "the cache: it will hold the best score from each vertex", GREEN)]),
         narration=("Now the Python. The function takes the graph, a dictionary called [[len]]length, whose keys are pairs: "
                    "the pair v, w gives the points of the trail from v to w. And the start and the target. "
                    "[[best]]Best is an empty dictionary: the cache.")),
    dict(id="lp_base", topic="The Python: base case and cache check", scene=S.scene_lp_code(
        boxes=[(5, "if v == t:", BLUE, "base"), (6, "return 0", BLUE, "base"), (7, "if v not in best:", GREEN, "memo")],
        notes=[("base", "if v == t: return 0", "standing on the target: zero more points", BLUE),
               ("memo", "if v not in best", "only compute a vertex the first time. After that, skip straight to the return.", GREEN)]),
         narration=("Inside, the helper function go. [[base]]If v is t, return zero. [[memo]]If v is not in best yet, we have "
                    "not computed it. Only then do the work. Otherwise, skip down to the last line, and return what is stored.")),
    dict(id="lp_max", topic="The Python: the maximum", scene=S.scene_lp_code(
        boxes=[(8, 'float("-inf")', RED, "inf"), (9, "for w in graph[v]:", PURPLE, "loop"),
               (10, "length[(v, w)]", BLUE, "key"), (10, "go(w)", GREEN, "go"), (10, "max(", ORANGE, "max")],
        notes=[("inf", 'float("-inf")', "a special number: minus infinity. It is smaller than every other number.", RED),
               ("loop", "for w in graph[v]", "every trail out of v", PURPLE),
               ("key", "length[(v, w)]", "the inner brackets build the pair; the outer ones look it up", BLUE),
               ("go", "go(w)", "the best score from w. Recursive, and cached.", GREEN),
               ("max", "max(a, b)", "the larger of two numbers", ORANGE)]),
         narration=("Now the heart. [[inf]]Start best of v at minus infinity: float of the text minus inf makes a special "
                    "number, smaller than any other, which is the book's maximum of nothing. [[loop]]Then for each trail out "
                    "of v, to a vertex w: [[key]]look up the trail's points, using the pair v, w, [[go]]add go of w, the best "
                    "score from there, [[max]]and keep the larger of that and the best so far.")),
    dict(id="lp_ret", topic="The Python: the answer", scene=S.scene_lp_code(
        boxes=[(11, "return best[v]", GREEN, "ret"), (13, "return go(s)", BLUE, "start")],
        notes=[("ret", "return best[v]", "hand back the stored answer", GREEN),
               ("start", "return go(s)", "start the whole depth-first search from s", BLUE)]),
         narration=("[[ret]]Return best of v. [[start]]And the last line starts everything: return go of s. That is the "
                    "book's LongestPath algorithm. Each vertex is computed once, and each trail is looked at once: V plus E.")),
    dict(id="route", topic="The route, and an extra", scene=S.scene_route,
         extra_cues=[("r1", "r1", 0.0)],
         narration=("The answer is nineteen scenery points. [[r1]]Start to Pine, [[r2]]to Creek, [[r3]]to Falls, "
                    "[[r4]]to Summit: three plus five plus seven plus four. [[extra]]One extra, which is not in the book. The "
                    "algorithm computes the length. To recover the route itself, remember which trail gave the maximum at "
                    "each junction.")),
    dict(id="dp_table", topic="The same answer by dynamic programming", book="JEA 6.4 · PDF p.254", scene=S.scene_dp_table,
         narration=("The book then says: we can turn this into dynamic programming, with a topological sort. Take the finish "
                    "order from the depth-first search, and [[loop]]loop through it. Children always come before parents, so "
                    "when we reach a vertex, [[lookup]]every best of w it needs is already in the table, and no recursion is "
                    "needed. [[fill]]Watch the table fill in: Summit, zero. Meadow, five. Falls, four. Creek, eleven. Ridge, "
                    "nine. Pine, sixteen. Start, nineteen. [[same]]The same table, in the same order, as the memoized version. "
                    "Memoization and dynamic programming are two views of one postorder.")),
    dict(id="recap", topic="Recap", scene=S.scene_recap,
         narration=("To recap sections six point three and six point four. [[c1]]A topological order is the reverse of a "
                    "depth-first search's finishing order. [[c2]]To process in reverse order, process each vertex as it "
                    "finishes. For forward order, search the reversed graph. [[c3]]Memoization is a depth-first search of "
                    "the dependency graph, which must be acyclic. [[c4]]And dynamic programming is a postorder of that same "
                    "graph, so longest path in a DAG takes V plus E time. [[try]]Pause, and say each of those four in your own "
                    "words. That is a good start for your learning log.")),
]
