"""Video 03 beats. Narration markup: [[cue]]word  {display|spoken}  (~ = space in spoken)."""
import widgets
import scenes as S

widgets.CONFIG.update(series="GRAPH SEARCH  ·  VIDEO 3 OF 6", title="Class Lab: count_paths")

BEATS = [
    # ------------------------------------------------------------ A: counting by hand
    dict(id="hook", topic="Meet Hopper", scene=S.stones_scene(hook=True), pause=6.0,
         predict="How many different ways?",
         narration=("Meet Hopper, a frog. Hopper wants to cross a river on eight stepping stones, numbered zero to seven. "
                    "Each hop goes forward one stone, or two. Drawn as a graph, each [[stone]]stone is a vertex, and each "
                    "[[hop]]hop is an arrow, a directed edge. [[q]]How many different ways can Hopper get from stone zero "
                    "to stone seven?")),
    dict(id="back7", topic="Count backward from the far bank", scene=S.stones_scene(cues=[(7, "s7"), (6, "s6"), (5, "s5")]),
         narration=("Let us count backward, from the far bank. [[s7]]From stone seven, Hopper is done. That is one way: do "
                    "nothing. [[s6]]From stone six, one way: hop one. [[s5]]From stone five, two ways: hop one, then one more, "
                    "or hop two, straight to the bank.")),
    dict(id="rule", topic="The pattern", scene=S.stones_scene(known=(7, 6, 5), cues=[(4, "s4"), (3, "s3")], rule_cue="rule"),
         narration=("[[rule]]See the pattern? The ways from a stone are the ways from the stone one ahead, plus the ways from "
                    "the stone two ahead, because those are the only first hops. [[s4]]Stone four: two plus one is three. "
                    "[[s3]]Stone three: three plus two is five.")),
    dict(id="finish21", topic="Twenty-one ways",
         scene=S.stones_scene(known=(7, 6, 5, 4, 3), cues=[(2, "s2"), (1, "s1"), (0, "s0")], rule_cue="rule0"),
         narration=("Keep going. [[s2]]Eight. [[s1]]Thirteen. [[s0]]And from stone zero, twenty-one ways. [[rule0]]Every count "
                    "used only the counts of the stones it can hop to.")),
    dict(id="general", topic="Counting paths in general", scene=S.scene_general,
         narration=("In any graph, this is called counting paths. The graph must be a [[dag]]DAG: a directed acyclic graph, "
                    "meaning arrows, and no cycles. To count the paths from {s|S} to {t|T}: [[base]]if {s|S} is {t|T}, there "
                    "is one path, the empty one. [[rec]]Otherwise, add up the counts of {s|S}'s children. The children are the "
                    "vertices that {s|S} points to.")),
    dict(id="diamond", topic="The graph from your lab",
         scene=S.diamond_scene(known=("e", "d"), cues=[("b", "b"), ("c", "c"), ("a", "a")], paths=True),
         narration=("Here is the graph from your class lab. Vertex {A} points to {B} and {C}. {B} and {C} both point to {D}. "
                    "{D} points to {E}. How many paths from {A} to {E}? [[b]]From {B} to {E}: one. [[c]]From {C} to {E}: one. "
                    "[[a]]So from {A}: two. [[p1]]One path goes {A}, {B}, {D}, {E}. [[p2]]The other goes {A}, {C}, {D}, {E}.")),
    dict(id="diamond_rec", topic="How the code asks", scene=S.scene_diamond_rec, min_len=15.0,
         narration=("The code asks these questions in a different order. [[go]]To count from {A}, it asks {B}. {B} asks {D}. "
                    "{D} asks {E}, and {E} answers one. {D} answers one. {B} answers one. Then {A} asks {C}, and {C} asks {D} "
                    "all over again. {D} has to ask {E} all over again. [[again]]The same question, twice. Seven calls, for "
                    "five vertices.")),
    # ------------------------------------------------------------ B: the explosion and the fix
    dict(id="trail_intro", topic="A bigger map", scene=S.scene_trail_intro, pause=5.0,
         predict="How many routes?",
         narration=("That repeat is harmless here. On a bigger map, it explodes. This is a hiking map: seven junctions, "
                    "twelve one-way trails, all uphill. [[q]]How many different routes lead from Start to Summit?")),
    dict(id="trail_naive", topic="Plain recursion", scene=S.scene_trail_naive, min_len=14.0,
         narration=("Plain recursion asks each child, and each child asks its own children, with no memory. [[go]]Watch the "
                    "calls pile up. Twenty-four calls, for a map with seven junctions.")),
    dict(id="dups", topic="The repeats", scene=S.scene_dups,
         narration=("Look at the repeats. [[meadow]]Meadow is asked five times. [[falls]]Falls is asked four times. Every "
                    "time, the answer is one, recomputed from scratch.")),
    dict(id="memo", topic="The fix: a cache", book="JEA 6.4 · PDF p.252", scene=S.scene_memo, min_len=14.0,
         narration=("The fix: write each answer down the first time, and look it up after. That is called memoization, and the "
                    "table is a cache. [[tree]]Here is the same search with a cache. [[hit]]Whenever a junction was already "
                    "answered, it is a cache hit: read the table, and stop there.")),
    dict(id="table", topic="The cache filling in", scene=S.scene_table,
         narration=("Here is the table filling in. [[c1]]Summit: one. [[c2]]Meadow: one. [[c3]]Falls: one. [[c4]]Creek: two. "
                    "[[c5]]Ridge: two. [[c6]]Pine: five. [[c7]]Start: nine. Nine routes. Each junction was finished only after "
                    "all of its children.")),
    dict(id="cost", topic="How much work?", scene=S.scene_cost,
         narration=("Count the work. [[v]]Each junction is computed once: seven. [[e]]Each trail is looked at once, when its "
                    "starting junction is computed: twelve. [[calls]]So there are thirteen calls: one for the start, plus one "
                    "per trail. [[big]]That is V plus E: linear time.")),
    # ------------------------------------------------------------ C: your code, line by line
    dict(id="code_import", topic="Your code: the import",
         scene=S.code_scene(hl=[(1, None)], boxes=[(1, "cache", S.ACCENT_DARK, None)],
                            notes=[("import", "from ... import", "borrow one tool from a module", S.BLUE),
                                   ("tool", "functools", "a toolbox that comes with Python. cache is one tool in it.",
                                    S.ACCENT_DARK)]),
         narration=("Now your code. [[import]]The first line: from functools import cache. [[tool]]Functools is a toolbox "
                    "that comes with Python, and cache is one tool in it.")),
    dict(id="code_def", topic="Your code: the outline",
         scene=S.code_scene(hl=[], boxes=[(3, "def count_paths(graph, s, t):", S.BLUE, "def"),
                                          (9, "return nested(s)", S.GREEN, "ret")],
                            notes=[("def", "count_paths(graph, s, t)", "the graph, a start s, and a target t", S.BLUE),
                                   ("ret", "return nested(s)", "start the whole search, from s", S.GREEN)]),
         narration=("[[def]]Def {count_paths|count~paths} takes the graph, a start {s|S}, and a target {t|T}. [[ret]]The last "
                    "line, return nested of {s|S}, starts the whole search from the start.")),
    dict(id="decorator", topic="Your code: @cache", scene=S.scene_decorator,
         narration=("[[at]]The line above the inner def is at cache. The at sign means: wrap the function underneath. "
                    "[[wrap]]The wrapped function keeps a table of answers. The first time it sees an input, it runs, and writes "
                    "the answer down. [[again]]The next time it sees the same input, it skips the function, and returns what is "
                    "written.")),
    dict(id="closure", topic="Your code: a function inside a function",
         scene=S.code_scene(hl=[], boxes=[(5, "def nested(s):", S.ACCENT_DARK, "nested"), (8, "graph", S.BLUE, "gg"),
                                          (6, "t", S.RED, "tt"), (5, "(s)", S.GREEN, "shadow")],
                            notes=[("nested", "nested", "a function defined inside another function", S.ACCENT_DARK),
                                   ("gg", "graph, t", "nested can read them from outside", S.BLUE),
                                   ("tt", "a fresh cache",
                                    "a new nested is built on every call to count_paths, so t never changes inside one",
                                    S.RED),
                                   ("shadow", "(s)", "a new variable: this call's vertex", S.GREEN)]),
         narration=("[[nested]]Nested is a function inside a function, so it can read [[gg]]graph and [[tt]]{t|T} from "
                    "outside. A new nested is built every time {count_paths|count~paths} is called, so its table starts empty "
                    "each time. That is why the table can be keyed by {s|S} alone, even though the answer depends on {t|T}: "
                    "inside one call, {t|T} never changes. [[shadow]]The {s|S} in the parentheses is a fresh variable: this "
                    "call's vertex.")),
    dict(id="code_base", topic="Your code: the base case",
         scene=S.code_scene(hl=[], boxes=[(6, "if (s == t):", S.BLUE, "base"), (7, "return 1", S.GREEN, "one")],
                            notes=[("base", "if (s == t)", "we are standing on the target", S.BLUE),
                                   ("one", "return 1", "exactly one path: the empty path. The parentheses are optional.",
                                    S.GREEN)]),
         narration=("[[base]]If {s|S} equals {t|T}, [[one]]return one. Arriving at the target is exactly one path, the empty "
                    "path. The parentheses around the comparison are optional.")),
    dict(id="sum1", topic="Your code: the densest line",
         scene=S.code_scene(hl=[(8, None)], boxes=[(8, "graph[s]", S.BLUE, "g")],
                            notes=[("g", "graph[s]", "the list of children of s. At vertex a in the diamond: ['b', 'c']",
                                    S.BLUE)]),
         narration=("Now the densest line. Return sum of nested of child, for child in graph of {s|S}. Take it apart. "
                    "[[g]]Graph of {s|S} is the list of children of {s|S}. At vertex {A} in the diamond, that is {B} and {C}.")),
    dict(id="sum2", topic="Your code: the loop inside",
         scene=S.code_scene(hl=[(8, None)], boxes=[(8, "for child in graph[s]", S.ACCENT_DARK, "for"),
                                                   (8, "nested(child)", S.GREEN, "nc")],
                            notes=[("for", "for child in graph[s]", "go through that list, one child at a time",
                                    S.ACCENT_DARK),
                                   ("nc", "nested(child)", "the count for that child", S.GREEN)]),
         narration=("[[for]]For child in graph of {s|S} means: go through that list, one child at a time. [[nc]]Nested of "
                    "child is the count for that child. Together they produce one number for each child. Wrapped in "
                    "parentheses like this, it is called a generator expression.")),
    dict(id="sum3", topic="Your code: sum",
         scene=S.code_scene(hl=[(8, None)], boxes=[(8, "sum(", S.RED, "sum")],
                            notes=[("sum", "sum( ... )", "adds up the numbers. sum of nothing is 0.", S.RED),
                                   ("nothing", "no children", "nothing to add, so the answer is 0", S.GREEN)],
                            longhand=True),
         narration=("[[sum]]Sum adds those numbers up. [[nothing]]If {s|S} has no children, there is nothing to add, and the "
                    "sum of nothing is zero. [[long]]Here is the same thing written longhand: a total that starts at zero, a "
                    "loop, and a return.")),
    dict(id="trace", topic="Run it on the diamond", scene=S.scene_sum_trace,
         narration=("Run it on the diamond. [[t1]]{A} asks {B}, {B} asks {D}, {D} asks {E}, and {E} returns one. [[t2]]{D} is "
                    "stored. {B} is stored. [[t3]]Then {A} asks {C}, and {C} asks {D}. [[t4]]A cache hit: one, instantly. {C} is "
                    "stored. [[t5]]And {A} adds one plus one: two.")),
    dict(id="e_to_a", topic="Your third test", scene=S.scene_e_to_a,
         narration=("Your third test asks for {E} to {A}. [[e]]Nested of {E}: {E} is not {A}, and {E} has no children, so the "
                    "sum of nothing is zero. Zero paths.")),
    dict(id="cycle", topic="One rule: no cycles", book="JEA 6.4 · PDF p.252", scene=S.scene_cycle, min_len=17.0,
         narration=("One rule: no cycles. Suppose vertex {A} pointed to vertex {B}, {B} to {C}, and {C} back to {A}. [[go]]Then nested of "
                    "{A} would call {B}, which calls {C}, which calls {A} again, forever. [[err]]Python gives up with a "
                    "recursion error. That is why the graph must be acyclic. In the book's words, the dependency graph of a "
                    "recurrence must have no cycles.")),
    # ------------------------------------------------------------ D: the ladder
    dict(id="ladder_code", topic="Your last test: sixty stones", scene=S.scene_ladder_code,
         narration=("Now your last test: sixty stepping stones, hop one or two. The test builds the graph in one line. "
                    "[[comp]]For i in range sixty, make a key i, with the list i plus one, i plus two. [[bar]]The vertical "
                    "bar merges two dictionaries, here adding stones sixty and sixty-one, which have no hops.")),
    dict(id="ladder_num", topic="How many ways?", scene=S.scene_ladder_num,
         narration=("How many ways? [[big]]Two trillion, five hundred four billion, seven hundred thirty million, seven "
                    "hundred eighty-one thousand, nine hundred sixty-one. [[fib]]Those are Fibonacci numbers, like the ones "
                    "from the dynamic programming reading: each count is the sum of the two ahead.")),
    dict(id="ladder_cost", topic="Plain versus cached", scene=S.scene_ladder_cost,
         narration=("Plain recursion would make over eight trillion calls. At ten million calls a second, that is more than "
                    "nine days. [[cache]]With the cache: one hundred twenty-one calls. A fraction of a millisecond.")),
    dict(id="dp_link", topic="Memoization is depth-first search", book="JEA 6.4 · PDF p.253", scene=S.scene_dp_link,
         narration=("This is memoization, and it is depth-first search in disguise. [[m1]]Each junction is a vertex. [[m2]]Each "
                    "call that needs another is an edge. [[m3]]Storing an answer is marking. [[m4]]Computing the value happens "
                    "after the children, at the post-visit. The book puts it in one line: memoized recursion is depth-first "
                    "search of the dependency graph.")),
    dict(id="recap", topic="Recap", scene=S.scene_recap,
         narration=("To recap. [[c1]]Paths from {s|S} to {t|T}: one if {s|S} is {t|T}, otherwise the sum over the children. "
                    "[[c2]]Plain recursion repeats work. [[c3]]A cache answers each vertex once, so the time is V plus E. "
                    "[[c4]]And the answers come out children first. Next video: the other half of your lab, topological "
                    "order.")),
]
