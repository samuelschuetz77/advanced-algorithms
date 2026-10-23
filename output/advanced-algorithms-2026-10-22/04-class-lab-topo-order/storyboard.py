"""Video 04 beats. Narration markup: [[cue]]word  {display|spoken}  (~ = space in spoken)."""
import widgets
import scenes as S
import topolog as T

widgets.CONFIG.update(series="GRAPH SEARCH  ·  VIDEO 4 OF 6", title="Class Lab: topo_order")

BLUE, GREEN, RED = S.BLUE, S.GREEN, S.RED
ACCENT_DARK = S.ACCENT_DARK

BEATS = [
    # ------------------------------------------------------------ A: your first drawing
    dict(id="g1", topic="From your notes", scene=S.scene_g1,
         narration=("In your notes, you drew this graph, and two ways to lay it out. Let us give it a story: a morning "
                    "routine. [[a]]{A} is shower. [[b]]{B} is get dressed. [[c]]{C} is coffee. [[d]]{D} is leave. "
                    "[[arrow]]An arrow means: this task must come before that one.")),
    dict(id="layouts", topic="Two layouts", scene=S.scene_layouts,
         narration=("Now lay the four tasks on a line. [[bad]]In this order, {C}, {B}, {A}, {D}, three arrows point backward. "
                    "You would drink coffee before showering. [[good]]In this order, {A}, {B}, {C}, {D}, every arrow points the "
                    "same way. That is called a topological order. [[dag]]Your note says: a DAG always has one.")),
    dict(id="cycle2", topic="Why no cycles?", scene=S.scene_cycle2,
         narration=("Why a DAG? Suppose [[cyc]]get dressed had to come before shower, and shower before get dressed. "
                    "[[imp]]No order could satisfy both. With no cycles, [[ok]]an order always exists.")),
    # ------------------------------------------------------------ B: dinner
    dict(id="dinner_intro", topic="A bigger example: dinner", scene=S.scene_dinner_intro, pause=6.0,
         predict="What order works?",
         narration=("A bigger one. Priya is cooking dinner: seven tasks, and twelve rules. An arrow from one task to another "
                    "means the first must be finished before the second starts. [[q]]In what order can Priya do everything?")),
    dict(id="dfs_idea", topic="The trick", scene=S.scene_dfs_idea,
         narration=("Here is a trick, using depth-first search. [[u1]]When you reach a task, start it. [[u2]]Then visit "
                    "everything it unlocks, before anything else. [[u3]]Only then, call this task finished. So a task always "
                    "finishes after everything that depends on it. Watch.")),
    dict(id="dfs_run1", topic="Going down", scene=S.dfs_scene(T.DINNER_DFS, S.GVD, 0, 12),
         extra_cues=S.ev_cues([("go", 0, 12, 1.15, 0.2)]), min_len=17.0,
         narration=("[[go]]Start at Shop. Shop unlocks Chop, so go there. Chop unlocks Boil. Boil unlocks Sauce. Sauce unlocks "
                    "Plate. Plate unlocks Eat. Eat unlocks nothing, so Eat is the first task to finish.")),
    dict(id="dfs_run2", topic="Backing up", scene=S.dfs_scene(T.DINNER_DFS, S.GVD, 12, 16),
         extra_cues=S.ev_cues([("go", 12, 4, 1.9, 0.3)]),
         narration=("[[go]]Now back up. Plate has nothing left, so Plate is finished. Sauce is finished. Back at Boil, its "
                    "other task, Plate, is already finished, so skip it. Boil is finished.")),
    dict(id="dfs_run3", topic="The rest", scene=S.dfs_scene(T.DINNER_DFS, S.GVD, 16, 26),
         extra_cues=S.ev_cues([("go", 16, 10, 1.45, 0.3)]), min_len=19.0,
         narration=("[[go]]Back at Chop. Its next task, Fry, is new, so go there. Fry's tasks, Sauce and Plate, are both "
                    "finished: skip them. Fry is finished. Chop's last task, Sauce, is done too. Chop is finished. Back at "
                    "Shop, Boil and Fry are done. Shop finishes last of all.")),
    dict(id="finish_order", topic="Reverse the finish order", book="JEA 6.3 · PDF p.250", scene=S.scene_finish_order,
         narration=("The finish order is Eat, Plate, Sauce, Boil, Fry, Chop, Shop. That is called the postorder. [[rev]]Reverse "
                    "it: Shop, Chop, Fry, Boil, Sauce, Plate, Eat. [[line]]Lay the tasks out in that order, and all twelve "
                    "arrows point forward.")),
    dict(id="why", topic="Why it works", scene=S.scene_why,
         narration=("Why does it work? Look at the arrow from [[w1]]Fry to Sauce. Sauce finished before Fry did. And at the "
                    "arrow from [[w2]]Chop to Boil: Boil finished before Chop. [[rule]]For every arrow, the task it points to "
                    "finishes first. So when the finish order is reversed, every task comes before the tasks it points to.")),
    dict(id="preorder_fail", topic="What about the start order?", book="JEA 6.1 · PDF p.246", scene=S.scene_preorder_fail,
         narration=("What about the order the tasks start? That is called the preorder: [[pre]]Shop, Chop, Boil, Sauce, Plate, "
                    "Eat, Fry. [[bad]]Look: Fry comes last, but Fry must come before Sauce and Plate. Two arrows point "
                    "backward. The preorder is not a topological order.")),
    # ------------------------------------------------------------ C: your E graph
    dict(id="e_intro", topic="A second start task", scene=S.scene_e_intro,
         narration=("Back to the dinner, with one more detail. Priya also wants to set the table. [[t]]Setting the table has "
                    "nothing before it, and its only arrow leads to Eat. [[two]]Now there are two tasks with nothing before "
                    "them: Shop, and Table. So a loop over all the tasks could start at either one. Let us run both.")),
    dict(id="e_case1", topic="Case one: the loop starts at Shop", scene=S.dfs_scene(T.CASE1, S.GVD2, 0, 29),
         extra_cues=S.ev_cues([("go", 0, 26, 0.24, 0.2), ("late", 26, 3, 1.9, 0.1)]), min_len=15.0,
         narration=("[[go]]Case one: the dictionary lists Shop first. The search runs exactly as before, and Shop finishes. "
                    "[[late]]Then the loop reaches Table, a new task. Its only arrow leads to Eat, which is already "
                    "finished. So Table finishes last of all.")),
    dict(id="e_case2", topic="Case two: the loop starts at Table", scene=S.dfs_scene(T.CASE2, S.GVD2, 0, 29),
         extra_cues=S.ev_cues([("late", 5, 24, 0.24, 0.1)]), min_len=22.0,
         narration=("Case two: the dictionary lists Table first. [[e0]]Table starts. [[e1]]Its arrow leads to Eat, a new task, "
                    "[[e2]]so Eat starts, [[e3]]and finishes at once, since it unlocks nothing. [[e4]]Then Table finishes. "
                    "[[late]]Now the loop reaches "
                    "Shop, and the whole dinner search runs. But Eat is already finished, so every arrow into Eat is skipped.")),
    dict(id="e_compare", topic="Both ways", scene=S.scene_compare,
         narration=("[[c1]]Here are both cases side by side. [[c2]]Case two, below. [[bad]]In both, the start order fails: "
                    "three arrows point backward each time. [[good]]But the reversed finish order is a valid topological "
                    "order in both. [[diff]]They are not the same order. In case one, Table comes first. In case two, Table "
                    "comes late, right before Eat. Both are correct, because Table only has to come before Eat.")),
    # ------------------------------------------------------------ D: your code
    dict(id="code_intro", topic="Your code", scene=S.code_scene(
        hl=[(2, "lists"), (3, "lists"), (4, "lists")], boxes=[],
        notes=[("lists", "three things to remember", "pre_order, post_order, and visited", BLUE),
               ("nested", "a nested function", "build_topo_from does one task: start it, visit its children, finish it", GREEN),
               ("outer", "an outer loop", "tries every node, so every task is covered", ACCENT_DARK)]),
         narration=("Now your code. [[lists]]It keeps three things: the start order, the finish order, and a set of visited "
                    "tasks. [[nested]]A function inside a function, build topo from, handles one task. [[outer]]And an outer "
                    "loop tries every task, so every one is covered.")),
    dict(id="code_nested", topic="A function inside a function", scene=S.code_scene(
        hl=[], boxes=[(5, "def build_topo_from(node):", ACCENT_DARK, "def"), (6, "pre_order", BLUE, "p"),
                      (7, "visited", GREEN, "v"), (11, "post_order", ACCENT_DARK, "q")],
        notes=[("def", "def build_topo_from(node)", "defined inside topo_order", ACCENT_DARK),
               ("p", "pre_order, visited,", "it can read and change them from outside", BLUE),
               ("q", "post_order", "the same lists, shared by every call", GREEN)]),
         narration=("[[def]]{build_topo_from|build~topo~from} is defined inside topo order, like nested was in count paths. "
                    "[[p]]So it can read and change pre order, and visited, [[q]]and post order, from outside. Every call "
                    "shares the same three.")),
    dict(id="code_body", topic="What one call does", scene=S.code_scene(
        hl=[], boxes=[(6, "pre_order.append(node)", BLUE, "p1"), (7, "visited.add(node)", GREEN, "p2"),
                      (8, "for child in children[node]:", ACCENT_DARK, "p3"), (9, "if child not in visited:", RED, "p4"),
                      (10, "build_topo_from(child)", BLUE, "p5"), (11, "post_order.append(node)", ACCENT_DARK, "p6")],
        notes=[("p1", "pre_order.append(node)", "write the task into the start order", BLUE),
               ("p3", "for child in children[node]", "every task this one unlocks", ACCENT_DARK),
               ("p4", "if child not in visited", "skip tasks already started", RED),
               ("p6", "post_order.append(node)", "all children done: write into the finish order", ACCENT_DARK)]),
         narration=("One call, step by step. [[p1]]Write the task into the start order. [[p2]]Mark it visited. [[p3]]For each "
                    "task it unlocks, [[p4]]if that task is not visited yet, [[p5]]go and handle it first. [[p6]]Only after "
                    "all of them are done, write this task into the finish order.")),
    dict(id="code_base", topic="Where is the base case?", scene=S.code_scene(
        hl=[], boxes=[(8, "for child in children[node]:", ACCENT_DARK, "f"), (11, "post_order.append(node)", GREEN, "post")],
        notes=[("f", "no if for the base case", "none is needed", ACCENT_DARK),
               ("post", "falls through", "no children, or all started: the loop does nothing, and the function finishes", GREEN)]),
         narration=("Where is the base case? There is no if for it. [[f]]When a task has no children, or all of them have "
                    "been started, the for loop does nothing. [[post]]The function falls through to post order, and returns. "
                    "That is what your note says: none of the recursive calls happen when all the children have already been "
                    "started.")),
    dict(id="code_outer", topic="The outer loop", scene=S.code_scene(
        hl=[], boxes=[(13, "for node in children:", BLUE, "o1"), (14, "if node not in visited:", RED, "o2"),
                      (15, "build_topo_from(node)", GREEN, "o3")],
        notes=[("o1", "for node in children", "every key of the dictionary, in dictionary order", BLUE),
               ("o2", "if node not in visited", "skip tasks an earlier call already covered", RED),
               ("o3", "build_topo_from(node)", "start a fresh depth-first search here", GREEN)]),
         narration=("The outer loop. [[o1]]For each node in the dictionary, in the order the dictionary lists them, [[o2]]if "
                    "it was not already covered, [[o3]]start a fresh depth-first search from it. That is the loop from the "
                    "earlier videos, and it is why the dictionary order mattered in the two cases.")),
    dict(id="code_bug", topic="The bug", scene=S.scene_code_bug,
         narration=("Now the bug. [[bug]]The last line returns pre order. We just saw that the start order is not a topological "
                    "order. [[fix]]The fix: return the reverse of post order, with list of reversed post order. "
                    "[[rev1]]Reversed hands the items back to front, [[rev2]]and list turns that into a list. This is shown "
                    "here only. Your file stays as you wrote it.")),
    dict(id="test_bad", topic="Your test", scene=S.scene_test_bad,
         narration=("Now your test. [[args]]Your test_topo_order is a copy of the first test. It calls topo order with three "
                    "arguments, but topo order takes only one: the graph. [[spec]]The spec's test is different. It checks the "
                    "order itself.")),
    dict(id="spec_test", topic="Reading the real test", scene=S.scene_spec_test,
         narration=("The real test, line by line. [[s1]]Sorted order equals sorted graph: the same vertices, none lost. "
                    "[[s2]]Order dot index of u is less than order dot index of w. Index gives a position in the list. "
                    "[[s3]]For every vertex u, and every child w of u, [[s4]]all means every one of those checks must be true. "
                    "In other words: every arrow points forward.")),
    dict(id="run_tests", topic="Running it", scene=S.scene_run_tests,
         narration=("Run your function as written. [[bad]]On the first graph it returns {A}, {B}, {D}, {E}, {C}. {C} points to "
                    "{D}, but {C} comes after {D}. The test fails. [[fixed]]With the fix, both graphs pass: {A}, {C}, {B}, "
                    "{D}, {E}, and then {Z}, {Y}, {X}.")),
    dict(id="speed", topic="How fast?", scene=S.scene_speed,
         narration=("How fast is it? [[s1]]Each task is visited once. [[s2]]Each arrow is looked at once. [[s3]]So the function "
                    "runs in V plus E time. [[t]]The test uses index, which scans the list, so the test is slower. The "
                    "function is not.")),
    dict(id="recap", topic="Recap", scene=S.scene_recap,
         narration=("To recap. [[c1]]A topological order puts every arrow pointing the same way. [[c2]]Depth-first search "
                    "gives one: reverse the finish order. [[c3]]The start order is not enough. [[c4]]Your code needs one "
                    "change: return the reversed post order. [[next]]Next: the book's chapter six, preorder, postorder, and "
                    "cycles, in detail.")),
]
