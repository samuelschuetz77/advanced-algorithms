"""Video 01 beats: narration text (with cue markers) and which scene animates it.

Narration markup:
  [[cue]]word   -> cue fires when `word` starts being spoken
  {S}           -> shown as S, spoken "ess" (phonetic letters, see pipeline.PHON)
  {a|b}         -> shown as a, spoken as b  (use ~ for a space inside b)
"""
import scenes as P1
import scenes2 as P2

BOOK_5_5 = "JEA 5.5 · PDF p.217"

# extra cues for the long "drain" beat: tokens 15..23 leave every 0.55 s, then the last two
DRAIN_EXTRA = []
for _i, _n in enumerate(range(15, 24)):
    DRAIN_EXTRA.append((f"take{_n}", "drain", 0.55 * _i))
    DRAIN_EXTRA.append((f"do{_n}", "drain", 0.55 * _i + 0.25))
DRAIN_EXTRA += [("take24", "s2", 0.0), ("do24", "s2", 0.3), ("take25", "s2", 0.95), ("do25", "s2", 1.25)]

BEATS = [
    # ------------------------------------------------------------------ Part 1
    dict(id="meet", topic="Meet Wrinkles", scene=P1.scene_1,
         narration=("[[w]]Meet Wrinkles, a naked mole-rat worker. Her colony is a maze of [[chambers]]chambers joined by "
                    "[[tunnels]]tunnels. Mathematicians draw a maze like this as a [[graph]]graph. Each chamber is a dot, "
                    "called a [[vertex]]vertex. Each tunnel is a line, called an [[edge]]edge.")),
    dict(id="question", topic="The question", book=BOOK_5_5, scene=P1.scene_2, pause=5.0,
         predict="How would Wrinkles check every chamber?",
         narration=("Wrinkles is in the nest, [[nest]]vertex {S}. Her job is to find every chamber she can reach by "
                    "[[follow]]following tunnels. That question has a name: [[reach]]reachability. And one burrow over here "
                    "was cut off by a [[cave]]cave-in, so she will never reach it. [[q]]Pause, and think. How would "
                    "Wrinkles check every chamber?")),
    dict(id="circles", topic="Her first idea", scene=P1.scene_3, min_len=11.0,
         narration=("Wrinkles' first idea: follow any tunnel. At the next chamber, follow any tunnel again. [[go]]Watch. "
                    "Round and round. She never remembers where she has been.")),
    dict(id="marks", topic="A better idea: a scent mark", scene=P1.scene_4,
         narration=("Naked mole-rats know their colony by smell, so Wrinkles has a better idea. The first time she "
                    "arrives at a chamber, she leaves a [[scent]]scent mark. In graph words, she [[marks]]marks the vertex. "
                    "If she arrives at a marked vertex, she knows: been here, nothing new, [[turn]]turn around.")),
    # ------------------------------------------------------------------ Part 2
    dict(id="three", topic="One more problem", scene=P2.scene_three, pause=4.0,
         predict="How does she remember them?",
         narration=("But a scent mark is not enough. At the nest, [[three]]three tunnels lead out of vertex {S}, and "
                    "Wrinkles can only walk down one. What happens to the other two? [[q]]Pause. How does she remember them?")),
    dict(id="tokens", topic="A pile of tokens", scene=P2.scene_tokens,
         narration=("So Wrinkles carries a pile of [[t1]]tokens. Each token reminds her of one [[t2]]tunnel she has not "
                    "walked yet. It is [[t3]]stamped with the two chambers that tunnel connects. [[ro]]Mole-rats cannot "
                    "really read, so just pretend.")),
    dict(id="bag", topic="The pile has a name", book="JEA 5.5 · PDF p.218", scene=P2.scene_bag,
         narration=("All the tokens go into one pile. The book calls this pile a [[bag]]bag. It is just somewhere to put "
                    "things in, and take things out.")),
    dict(id="pair", topic="A token is a pair", scene=P2.scene_pair,
         narration=("Each token is a [[pair]]pair: the vertex she [[from]]came from, and the vertex it leads [[to]]to. "
                    "In code, we will call these two things {came_from|came~from}, and current. In a few minutes, "
                    "you will see why we keep both.")),
    dict(id="rule1", topic="The four rules", scene=P2.rule_scene(0),
         narration="The whole method is four rules. [[r1]]Rule one: start with a single token that says: came from nobody, leads to the nest."),
    dict(id="rule2", topic="The four rules", scene=P2.rule_scene(1),
         narration="[[r2]]Rule two: as long as the pile is not empty, take one token out."),
    dict(id="rule3", topic="The four rules", scene=P2.rule_scene(2),
         narration=("[[r3]]Rule three: look at the vertex that token leads to. If it has no [[mk]]mark yet, mark it. "
                    "Remember who sent her. That is its [[par]]parent. Then add a new token for [[ev]]every edge leaving "
                    "that vertex.")),
    dict(id="rule4", topic="The four rules", scene=P2.rule_scene(3),
         narration=("[[r4]]Rule four: if the vertex is already marked, [[throw]]throw the token away. There is nothing "
                    "new to do.")),
    dict(id="translate", topic="The book's name for it", book="JEA 5.5 · PDF p.218", scene=P2.scene_translate,
         narration=("That is the entire algorithm. The book calls it whatever-first search, because we have not said "
                    "which token to take out of the pile. Today, we always take the newest one. Next video, we will see "
                    "what changes if you choose differently. And if you open the book, here is the translation of its "
                    "letters. [[t_s]]The letter s is the start. [[t_bag]]The bag is our token pile. [[t_p]]The letter p is "
                    "{came_from|came~from}. [[t_v]]The letter v is current. [[t_w]]And w is a neighbor.")),
    # ------------------------------------------------------------------ Part 3
    dict(id="map", topic="Run it on the colony", scene=P2.scene_map,
         narration=("Let us run it on the colony. Seven [[v7]]vertices, twelve [[e12]]edges. Each vertex keeps a list of "
                    "its neighbors, and adds tokens in list order. So the [[last]]last neighbor in the list ends up on top "
                    "of the pile.")),
    dict(id="step1", topic="Step 1", scene=P2.trace_scene([1]),
         narration=("Start with one token: [[take]]nobody to {S}. Take it out. {S} has no mark, so [[do]]mark {S}. Its "
                    "parent is nobody. {S} has three edges, so [[push]]add three tokens: {S} to {A}, {S} to {B}, and "
                    "{S} to {C}.")),
    dict(id="predict1", topic="Which token comes out?", scene=P2.trace_scene([], idle_after=1), pause=4.0,
         predict="Which token comes out next?",
         narration="Now the pile has three tokens. We always take the newest one. [[q]]Which one is it?"),
    dict(id="step2", topic="Step 2", scene=P2.trace_scene([2]),
         narration=("It is {S} to {C}, the last one we added. [[take]]Take it out. {C} is new, so [[do]]mark {C}. Its "
                    "parent is {S}. {C} has four edges, to {A}, {B}, {F}, and back to {S}, so [[push]]four tokens go on top.")),
    dict(id="step3", topic="Step 3: a useless token", scene=P2.trace_scene([3]),
         narration="[[take]]Newest token: {C} to {S}. But {S} already has a mark. [[do]]Throw it away."),
    dict(id="step4", topic="Step 4", scene=P2.trace_scene([4]),
         narration=("[[take]]Next, {C} to {F}. {F} is new. [[do]]Mark it, parent {C}. {F} has three edges, to {C}, {D}, "
                    "and {E}, so [[push]]three tokens go on top.")),
    dict(id="step5", topic="Step 5", scene=P2.trace_scene([5]),
         narration=("[[take]]The newest is {F} to {E}. {E} is new. [[do]]Mark it, parent {F}. {E} has edges to {B}, {D}, "
                    "and {F}. [[push]]Three more tokens.")),
    dict(id="step6", topic="Step 6", scene=P2.trace_scene([6]),
         narration="[[take]]Now {E} to {F}. {F} is already marked. [[do]]Throw it away."),
    dict(id="step7", topic="Step 7", scene=P2.trace_scene([7]),
         narration=("[[take]]Next, {E} to {D}. {D} is new. [[do]]Mark it, parent {E}. {D} has edges to {A}, {E}, and {F}. "
                    "[[push]]Three more tokens.")),
    dict(id="step89", topic="Steps 8 and 9", scene=P2.trace_scene([8, 9]),
         narration=("[[take8]]{D} to {F}: {F} is marked. [[do8]]Throw it away. [[take9]]{D} to {E}: {E} is marked. "
                    "[[do9]]Throw that one away too.")),
    dict(id="step10", topic="Step 10: predict", scene=P2.trace_scene([10]), pause=5.0,
         predict="Which token is the first useful one?",
         narration=("[[take]]{D} to {A}. {A} is new, so [[do]]mark {A}, parent {D}. {A} has four edges, so [[push]]four "
                    "tokens go on top: to {B}, {C}, {D}, and {S}. Only one of those vertices is still unmarked. [[q]]Which "
                    "token will lead Wrinkles to it, and how many will she throw away first?")),
    dict(id="step1114", topic="Steps 11 to 14", scene=P2.trace_scene([11, 12, 13, 14]),
         extra_cues=[("do11", "take11", 0.5), ("do12", "take12", 0.5), ("do13", "take13", 0.5)],
         narration=("The answer: three get thrown away. [[take11]]{A} to {S}, [[take12]]{A} to {D}, and [[take13]]{A} to "
                    "{C}. [[take14]]Then {A} to {B}. {B} is new, so [[do14]]mark {B}. Its parent is {A}. That is the "
                    "seventh vertex. Every vertex Wrinkles can reach now has a mark. [[push14]]But the pile is not empty.")),
    dict(id="drain", topic="Steps 15 to 25: the pile drains", scene=P2.trace_scene(list(range(15, 26)), stale_cue="s1"),
         extra_cues=DRAIN_EXTRA, min_len=0.0,
         narration=("Eleven tokens are left, and every one leads to a marked vertex. [[drain]]So rule four, over and over. "
                    "Throw it away, throw it away. Watch the pile drain. [[s1]]The last two tokens, {S} to {B} and {S} to "
                    "{A}, have been waiting at the bottom since step one. Their vertices got marked a different way, so "
                    "they are stale. We never dig through the pile to remove old tokens. We just ignore them when they "
                    "come out. [[s2]]Zero tokens. We are done.")),
    dict(id="answer", topic="The answer, and a count", book=BOOK_5_5.replace("217", "219"), scene=P2.scene_answer,
         narration=("The marked vertices are {S}, {A}, {B}, {C}, {D}, {E}, and {F}. [[xy]]{X} and {Y} never got a mark. "
                    "That is the answer: from the nest, Wrinkles can reach [[seven]]seven chambers, and she can never reach "
                    "the cut-off burrow. And look at the [[count]]count. Twenty-five tokens in all: [[one]]one to start, and "
                    "[[two]]two for each of the twelve edges, one from each end. Only seven were useful. We will use that "
                    "count in the next video.")),
    # ------------------------------------------------------------------ Part 4
    dict(id="parents", topic="Why keep the pair?", scene=P2.scene_parents,
         narration=("Remember the pair on each token? Here is why. [[b]]Ask vertex {B}: who is your parent? {A}. [[a]]Ask "
                    "{A}? {D}. [[d]]Ask {D}? {E}. [[e]]Then {F}, [[f]]then {C}, [[c]]then {S}. Keep asking, and Wrinkles "
                    "[[back]]walks right back to the nest.")),
    dict(id="tree", topic="The parents form a tree", book="Lemma 5.1 · PDF p.218", scene=P2.scene_tree,
         narration=("Now draw only the [[par]]parent edges. Six of them, one fewer than the seven vertices. They form a "
                    "[[tree]]tree: one long, skinny path from the nest. The book says depth-first trees are usually long "
                    "and skinny. And every marked vertex hangs from the nest by exactly one route.")),
    # ------------------------------------------------------------------ Part 5
    dict(id="stops", topic="Promise 1: it stops", scene=P2.scene_stops,
         narration=("Three promises. First, it always stops. A vertex is marked [[once]]only once, and only a marked "
                    "vertex adds tokens. So the pile cannot keep growing forever.")),
    dict(id="never", topic="Promise 2: nothing unreachable", scene=P2.scene_never,
         narration=("Second, it never marks a vertex she cannot reach. Every token is added by a marked vertex, along a "
                    "real edge. So [[c1]]every marked vertex has a chain [[c2]]of parents [[c3]]leading back [[c4]]to the nest.")),
    dict(id="route", topic="Promise 3: every reachable vertex", scene=P2.scene_route_setup,
         narration=("Third, it marks every vertex she can reach. Pick any reachable vertex, call it the target, and take "
                    "a [[route]]shortest route to it. The nest, then a few vertices, then the target.")),
    dict(id="dominoes1", topic="Promise 3: the dominoes", scene=P2.scene_dominoes_1,
         narration=("[[s]]{S} gets marked, so it adds a [[tok]]token for the next vertex on the route. That token cannot "
                    "vanish, and the search only stops when the pile is empty, so the token [[out]]gets taken out. At that "
                    "moment the vertex is already marked, or it gets marked now. [[either]]Either way, it is marked.")),
    dict(id="dominoes2", topic="Promise 3: induction", book="Lemma 5.1 · PDF pp.218-219", scene=P2.scene_dominoes_2,
         narration=("Then it [[next]]adds the token for the next one. Each vertex [[knock]]knocks over the next. "
                    "Mathematicians call this [[ind]]induction on distance. It is the proof of Lemma five point one, and "
                    "now you can read it.")),
    # ------------------------------------------------------------------ Part 6
    dict(id="code_all", topic="The four rules, as Python", scene=P2.scene_code_all,
         narration=("Here are the four rules as Python. [[l2]]Rule one is line two. [[l5]]Rule two is the while loop. "
                    "[[l7]]Rule three is everything inside the if. [[l_else]]And rule four is what is missing: if the "
                    "vertex is already marked, the if is false, and nothing runs.")),
    dict(id="code_l2", topic="Reading line two", scene=P2.scene_code_l2,
         narration=("[[l2]]Line two. [[sq]]Square brackets make a list: that is our pile. Inside is one pair. [[rd]]Round "
                    "brackets glue two values together. The first is [[none]]None, which means nobody. The second is "
                    "[[start]]start.")),
    dict(id="code_l6", topic="Reading line six", scene=P2.scene_code_l6,
         narration=("[[l6]]Line six. [[pop]]Pop takes the last item out of the list: our newest token, a pair. [[names]]The "
                    "two names on the left of the equals sign, with a comma between them, split that pair. The first value "
                    "goes into {came_from|came~from}. The second goes into current. That is called [[unp]]unpacking.")),
    dict(id="code_sets", topic="Sets, dictionaries, and the loop", scene=P2.scene_code_sets,
         narration=("A [[set]]set remembers which vertices have a mark, and answers, is this one in here, very quickly. "
                    "The [[curly]]curly brackets on line four make a dictionary: look up a vertex, get its parent. The "
                    "[[loop]]loop adds one token per neighbor. Look at the [[dbl]]double round brackets. The inner pair is "
                    "the token. The outer ones belong to append.")),
    dict(id="code_ret", topic="What it returns", scene=P2.scene_code_return,
         narration=("The function [[ret]]returns the parents table. Its [[keys]]keys are exactly the marked vertices, the "
                    "answer to reachability. And its [[values]]values are the tree.")),
    dict(id="recursion", topic="You have already written this", scene=P2.scene_recursion,
         narration=("One more connection. In class you wrote {build_topo_from|build~topo~from}. That is this [[g1]]same "
                    "idea, [[g2]]written with [[g3]]recursion. There is no written pile, because Python's own "
                    "[[nopile]]call stack is the pile. The order of the neighbors can come out flipped, but the idea is "
                    "the same.")),
    # ------------------------------------------------------------------ Part 7
    dict(id="recap", topic="Recap", scene=P2.scene_recap,
         narration=("Let us retell it. [[c1]]Scent marks stop her circling. [[c2]]A pile of tokens remembers the tunnels "
                    "she has not walked yet. [[c3]]And the parents form a tree back to the nest. [[try]]Pause, and run the "
                    "four rules on the graph from page one of your notes. Next time: what changes when the pile is a "
                    "queue, or a priority queue.")),
]
