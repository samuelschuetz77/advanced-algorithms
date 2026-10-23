# Video 01: Whatever-First Search, Part 1 — The Naked Mole-Rat Colony

Status: BUILT (see README.md). This file is the design draft; the final narration is `storyboard.py` / `transcript.md`. Part 1 follows the approved v4; Parts 2 to 7 were converted to the same balance (graph words in the narration, Wrinkles acting on the graph). Optional beat 32 (reverse order) was cut.
Voice: **Ava** (`en-US-AvaMultilingualNeural`, rate -4%), chosen by Samuel.
Target length: about 10 minutes (42 beats, about 1,350 spoken words plus pauses). Beat B30 is optional and can be cut for time.
Framework: `advanced algorithms/video-framework.md`.

## Objectives (what Samuel can do after watching)
1. Say what "reachability" asks and why we need scent marks (the book's "marks").
2. Explain what the "bag" (the token pile) holds and why each token is a pair.
3. Run the algorithm by hand on a 7-chamber, 12-tunnel colony, including discarded tokens.
4. Explain why it marks every reachable chamber and nothing else, and why the parent links form a tree with exactly one fewer tunnel than chambers.
5. Read the Python version line by line, including the pair and unpacking syntax.

## Prerequisites assumed
None beyond "a map is dots and lines". Everything else is introduced on screen.

## Story and vocabulary map (story word -> book word)
| In the story | Book / code word |
|---|---|
| chamber | vertex |
| tunnel | edge |
| the colony map | graph |
| scent mark (a dab of smell) | mark / `visited` |
| token pile (the worker carries it) | bag / `to_visit` |
| token stamped "from X, to Y" | the pair `(p, v)` / `(came_from, current)` |
| the chamber that sent the token | `parent(v)` / `parent_of[...]` |
| the nest, chamber S | start vertex `s` |

Honest note for the narration: mole-rats cannot read or write. The video says so
once, up front: "pretend each token is stamped with two chamber names."

## Book coverage checklist (JEA 5.5, PDF 217-219)
| Book item | Status |
|---|---|
| Reachability question; undirected: reachable = same component | Covered B05, B29 |
| RecursiveDFS and IterativeDFS are the same algorithm; the stack is visible | Covered B37-B41 |
| WhateverFirstSearch with a "bag" | Covered B06-B14 |
| "Marks each vertex at most once" and "at least once" | Covered B32-B36 |
| Pairs `(p, v)` and `parent(v)` | Covered B09, B30-B31 |
| Lemma 5.1 and proof (induction on distance; parent path leads to s; edges = vertices - 1) | Covered B33-B36 and B31 (picture, not formal symbols) |
| "Depth-first spanning trees are long and skinny" (PDF 219-220) | Covered B31, B30 |
| Tail of 5.4: "all time bounds assume a standard adjacency list" (PDF 217) | Moved to video 02 |
| Analysis `O(V + E T)`, line counts (PDF 219) | Previewed B29 (25 = 2 x 12 + 1); proved in video 02 |
| 5.6 variants, disconnected graphs, directed graphs, 5.7 flood fill | Moved to video 02 |

## Anchor example: "The Colony" (all numbers come from `trace_check.py`)
Twelve tunnels between seven chambers, plus a separate burrow X-Y cut off by a cave-in.
```
S: A, B, C      A: B, C, D, S      B: A, C, E, S      C: A, B, F, S
D: A, E, F      E: B, D, F         F: C, D, E         X: Y      Y: X
```
Tunnels: S-A, S-B, S-C, A-B, A-C, A-D, B-C, B-E, C-F, D-E, D-F, E-F, and X-Y.

Stage layout (a soil cross-section, three columns):
```
                 col 1        col 2
          A  ----------- D          top
        / | \            |   \
  S -- B  |  (arc)       E   (arc) middle
        \ | /            |   /
          C  ----------- F          bottom
```
S (the nest, queen icon) at far left. A, B, C stacked in column 1. D, E, F stacked in column 2. Tunnels A-B and B-C are short vertical segments; A-C is an arc on the left; D-F is an arc on the right; D-E and E-F are short vertical segments. X and Y in a separate cave at the lower right behind a rubble pile labeled "cave-in".
Mole-rat art: a simple pink, wrinkled, hairless cartoon with two buck teeth (a vector sprite drawn in Pillow). A "worker" mole-rat is the walker. No text on the sprite.

Pile rule for this video: take the NEWEST token. A chamber writes its tokens in list order, so the last neighbor in the list ends up on top.

## Visual key (series-wide, see framework section 7)
current = accent ring; marked = filled accent with a scent-dab mark; waiting token = outline; discarded = gray with a strike; parent tunnel = thick accent line.
State panel (right): **TOKEN PILE** (newest on top), **MARKED CHAMBERS**, **PARENTS** table.

---

## Part 1. The problem (v4, graph always on screen, mole-rat always acting, about 1:10)

Design note (Samuel, 10/22): v2 had "too much story, not enough graph"; v3 had
"not enough mole-rat". Rule that resolves both: **the graph is on screen from
the first frame and never leaves; the mole-rat (named Wrinkles) is the character
doing every action on it.** Each new idea gets its story word and its graph word
together once ("chamber, which is a vertex"); after that the narration uses the
graph word and the mole-rat acts it out.

**B01 — Meet Wrinkles and her colony**
Screen: the full Colony graph (S, A to F, 12 edges, plus the X-Y pair) drawn over a faint soil texture. Wrinkles, a naked mole-rat worker, sits on S. Two chips appear side by side as spoken: "chamber = vertex" and "tunnel = edge".
Say: "Meet Wrinkles, a naked mole-rat worker. Her colony is a maze of chambers joined by tunnels. Mathematicians draw a maze like this as a graph. Each chamber is a dot, called a vertex. Each tunnel is a line, called an edge."
Cues: "chambers" pulses every dot, "tunnels" pulses every line, then the chips pair the story word with the graph word.

**B02 — The question (book chip: JEA 5.5, PDF p.217)**
Screen: Wrinkles on S, ringed. Dotted question marks over every other vertex. Rubble drawn on the X-Y burrow.
Say: "Wrinkles is in the nest, vertex S. Her job is to find every chamber she can reach by following tunnels. That question has a name: reachability. And one burrow over here was cut off by a cave-in, so she'll never reach it."
Cues: "following tunnels" draws a faint path from S to D. "reachability" appears as a title. "cave-in" shakes the rubble at X and Y.
**PAUSE AND PREDICT (5 s)** chip: "How would Wrinkles check every chamber?"

**B03 — Her first idea goes wrong**
Screen: Wrinkles walks S, A, B, C, S, A, B, C. A step counter climbs past 20; the looping edges glow red; a small dizzy swirl circles her head.
Say: "Wrinkles' first idea: follow any tunnel. At the next chamber, follow any tunnel again. Watch. Round and round. She never remembers where she's been."
Cue: "round and round" holds the counter running.

**B04 — A better idea: a scent mark**
Screen: Wrinkles enters S, then A, then B; each gets a dab of scent that fills the vertex. At an already-marked vertex she sniffs, then turns back.
Say: "Naked mole-rats know their colony by smell, so Wrinkles has a better idea. The first time she arrives at a chamber, she leaves a scent mark. In graph words, she marks the vertex. If she arrives at a marked vertex, she knows: been here, nothing new, turn around."
Cues: "scent mark" draws the dab; "marks the vertex" fills the dot; "turn around" bounces her back.

## Part 2. The missing piece: the token pile (about 2:15)

**B06 — Three tunnels, one mole-rat**
Screen: the nest S with three arrows out, to A, B, and C. Walker at S.
Say: "But scent marks aren't enough. At the nest, three tunnels lead out. You can only walk down one. What happens to the other two?"
**PAUSE AND PREDICT (4 s)** chip: "How do you not forget them?"

**B07 — Tokens**
Screen: a round root-slice token slides into the right panel, stamped "S to A". Two more join: "S to B", "S to C". A caption: "mole-rats can't write, so pretend each token is stamped with two chamber names".
Say: "Carry tokens. One token for each tunnel you haven't walked yet, stamped with the two chambers it connects. Mole-rats can't actually read, so just pretend."
Cue: "stamped" flashes the two names.

**B08 — The pile has a name (book chip: "bag")**
Screen: the panel is titled TOKEN PILE; a small label says: "the book calls this a bag".
Say: "All your tokens go into one pile. The book calls this pile a bag. We'll call it the token pile. It's just somewhere you can put things in, and take things out."
Cue: "bag" shows the book label once.

**B09 — Each token holds a pair**
Screen: a token zoomed in: two slots, "came_from" and "current". Example: came_from = S, current = A.
Say: "Each token holds two things: the chamber we came from, and the chamber it leads to. A pair. Came from, comma, current. In a few minutes, you'll see why we keep both."
Cues: "came from" lights slot 1; "current" lights slot 2.

**B10 — Rule one**
Screen: four rule cards on the left; card 1 lit: "1. Start the pile with one token: (nobody, start)."
Say: "The whole method is four rules. Rule one: start with a single token that says, came from nobody, leads to the nest."
Cue: "nobody" highlights the NONE.

**B11 — Rule two**
Screen: card 2 lit: "2. While the pile isn't empty: take one token out."
Say: "Rule two: as long as the pile isn't empty, take one token out of it."

**B12 — Rule three**
Screen: card 3 lit: "3. If its chamber has no mark: mark it, remember who sent you, and add a token for every tunnel out."
Say: "Rule three: look at the chamber that token leads to. If it has no scent mark, mark it. Remember who sent you, that's its parent. Then add a new token for every tunnel leaving that chamber."
Cues: "mark it" draws the dab; "parent" highlights the came_from slot; "every tunnel" fans out tokens.

**B13 — Rule four**
Screen: card 4 lit: "4. If its chamber is already marked: throw the token away."
Say: "Rule four: if the chamber is already marked, throw the token away. There's nothing new to do."
Cue: "throw" crosses the token out.

**B14 — The book's name and the missing choice**
Screen: all four rules visible. Banner: "WhateverFirstSearch (JEA 5.5, PDF p.218)". Chips: s = start, bag = token pile, p = came_from, v = current, w = neighbor.
Say: "That's the entire algorithm. The book calls it whatever-first search, because we haven't said which token to take out of the pile. Today, we always take the newest one. Next video, we'll see what changes if you choose differently. And if you open the book, here's the translation of its letters."
Cues: chips appear in order as the translation is mentioned.

## Part 3. Worked example: the Colony (about 3:20)

**B15 — The map**
Screen: the Colony with each chamber's neighbor list in the panel. Count labels: "7 chambers, 12 tunnels".
Say: "Let's run it. Seven chambers, twelve tunnels. Each chamber keeps a list of its neighbors, in this order, and it writes its tokens in that order. The last neighbor in the list ends up on top of the pile."
Cue: "last neighbor" highlights the end of a list.

**B16 — Step 1: start**
Screen: pile = [(nobody, S)]. Take it. S marked; parent of S = nobody. Three tokens added: (S,A), (S,B), (S,C), with (S,C) on top.
Say: "Start with one token, nobody to S. Take it out. S has no mark, so mark S. Its parent is nobody. S has three tunnels, so we add three tokens: S to A, S to B, and S to C."

**B17 — Predict: the newest token**
Screen: the pile, (S,C) on top. Chip.
Say: "Now the pile has three tokens. We take the newest one. Which one is it?"
**PAUSE AND PREDICT (4 s)**
Reveal: "S to C. The last one we added."

**B18 — Step 2**
Screen: take (S,C). C marked; parent S. C's neighbors in order: A, B, F, S, so four tokens land on top: (C,A), (C,B), (C,F), (C,S).
Say: "Take S to C. C is new, so mark C. Its parent is S. C's four tunnels go to A, B, F, and back to S, so four new tokens go on top."

**B19 — Step 3: a useless token**
Screen: take (C,S). S is already marked. Token struck through.
Say: "Newest token: C to S. But S already has a mark. Throw it away."

**B20 — Step 4**
Screen: take (C,F). F marked; parent C. F's neighbors: C, D, E: three tokens.
Say: "Next, C to F. F is new. Mark it, parent C. F has three tunnels, to C, D, and E, so three tokens go on top."

**B21 — Step 5**
Screen: take (F,E). E marked; parent F. E's neighbors: B, D, F: three tokens.
Say: "The newest is F to E. E is new. Mark it, parent F. E's tunnels lead to B, D, and F. Three more tokens."

**B22 — Step 6**
Screen: take (E,F). F is marked; struck.
Say: "Now E to F. F is already marked. Throw it away."

**B23 — Step 7**
Screen: take (E,D). D marked; parent E. D's neighbors: A, E, F: three tokens.
Say: "Next, E to D. D is new. Mark it, parent E. D's tunnels lead to A, E, and F."

**B24 — Steps 8 and 9: two quick discards**
Screen: take (D,F), struck; then (D,E), struck.
Say: "D to F: F is marked. Throw it away. D to E: E is marked. Throw that one away too."

**B25 — Step 10: predict which token is useful**
Screen: take (D,A). A marked; parent D. A's neighbors: B, C, D, S: four tokens on top: (A,B), (A,C), (A,D), (A,S). Only B is unmarked.
Say: "D to A. A is new, so mark A, parent D. A has four tunnels, so four tokens go on top: to B, C, D, and S. Only one of those chambers is still unmarked. Which token will lead us to it, and how many will we throw away first?"
**PAUSE AND PREDICT (5 s)**
Reveal: "A to S, A to D, and A to C get thrown away. Then A to B."

**B26 — Steps 11 to 13**
Screen: (A,S), (A,D), (A,C) each struck in turn.
Say: "A to S: S is marked. Throw it away. A to D: D is marked. Throw it away. A to C: C is marked. Throw it away."

**B27 — Step 14: the last chamber**
Screen: take (A,B). B marked; parent A. All seven chambers now filled. B's four tokens (B,A), (B,C), (B,E), (B,S) added.
Say: "Now A to B. B is new, so mark B. Its parent is A. That's the seventh chamber. Every chamber we can reach now has a mark. But the pile isn't empty."
Cue: "seventh" counts 7 of 7.

**B28 — Steps 15 to 25: the pile drains**
Screen: the remaining 11 tokens fly out one after another, each struck as discarded. The pile counter counts down 11, 10, ... 0. Speed ramps up.
Say: "Eleven tokens are left, and every one leads to a marked chamber. So rule four, over and over. Throw it away, throw it away. Watch the pile drain. Zero tokens. We're done."
Note: one of the discarded tokens is S to A and one is S to B, which sat at the bottom of the pile since step one. They are stale: those chambers got marked a different way. We never dig through the pile to remove old tokens. We just ignore them when they come out.

**B29 — The answer, and a count**
Screen: marked chambers S, C, F, E, D, A, B filled. X and Y gray: "never marked". Then a counter: "tokens taken: 25 = 1 + 24", with the split bar "7 useful | 18 thrown away".
Say: "The marked chambers are S, A, B, C, D, E, and F. X and Y never got a mark. That's the answer to our question: from the nest we can reach seven chambers, and we can't reach the burrow behind the cave-in. And look at the count. Twenty-five tokens in all. One to start, and two for each of the twelve tunnels, one from each end. Only seven were useful. We'll use that count in the next video."
Book chip: "Analysis, PDF p.219: line (⋆⋆) runs at most 2E times".

## Part 4. Why keep the pair? Parents (about 1:00)

**B30 — Ask for a parent**
Screen: the parents table. B pulses. Arrows light in sequence B to A, A to D, D to E, E to F, F to C, C to S.
Say: "Remember the pair on each token? Here's why. Ask chamber B: who's your parent? A. Ask A? D. Ask D? E. Then F, then C, then S. Keep asking, and you walk right back to the nest."
Cues: each answer lights an arrow.

**B31 — A tree appears**
Screen: only the six parent tunnels are drawn thick: S-C, C-F, F-E, E-D, D-A, A-B. The other six tunnels fade. The picture straightens into a long skinny chain with S at the top. Label: "7 chambers, 6 parent tunnels".
Say: "Now draw only the parent tunnels. Six of them, one fewer than the seven chambers. They form a tree, a single long, skinny path from the nest. The book says depth-first trees are usually long and skinny. And every marked chamber hangs from the nest by exactly one route."
Book chip: "Lemma 5.1: the parent edges form a spanning tree of the component (PDF p.218)".

**B32 (optional) — Different order, different tree**
Screen: side by side, the colony with neighbors written in reverse order gives the path S, A, B, C, F, D, E. Caption: "same chambers, different tree".
Say: "If we had listed the neighbors in the opposite order, we'd get a different tree. Same seven chambers marked, but a different path. The shape depends on the order. That it's a tree does not."

## Part 5. Why it works (about 1:15)

**B33 — Promise one: it stops**
Screen: counter "chambers marked: 7 of 9". Each chamber can get a mark once; a stop sign.
Say: "Three promises. First, it always stops. A chamber is marked only once, and only a marked chamber adds tokens. So the pile can't keep growing forever."

**B34 — Promise two: nothing unreachable**
Screen: a token drawn as an arrow from a marked chamber. Then a chain of parent arrows from any marked chamber back to S.
Say: "Second, it never marks a chamber we can't reach. Every token is added by a marked chamber, along a real tunnel. So every marked chamber has a chain of parents leading back to the nest."

**B35 — Promise three: every reachable chamber (setup)**
Screen: a route S to u1 to u2 to v drawn as dominoes standing upright. Label: "a shortest route to v".
Say: "Third, it marks every chamber we can reach. Pick any reachable chamber, call it v, and take a shortest route to it. The nest, then a few chambers, then v."

**B36 — Dominoes, and the proof's name**
Screen: the first domino falls on "S is marked", then each falls as spoken. Final label: "induction on distance from S". Book chip: "Lemma 5.1 and proof, PDF pp. 218 to 219".
Say: "S gets marked, so it adds a token for the next chamber on the route. That token can't vanish, and the search only stops when the pile is empty, so the token gets taken out. At that moment the chamber is already marked, or it gets marked now. Either way, it's marked. Then it adds the token for the next one. Each chamber knocks over the next. Mathematicians call this induction on distance. It's the proof of Lemma five point one, and now you can read it."
Cues: dominoes fall in sync with the sentences.

## Part 6. The code (about 1:30)

Code on screen (12 lines, Python):
```python
def whatever_first_search(graph, start):
    to_visit = [(None, start)]
    visited = set()
    parent_of = {}
    while len(to_visit) > 0:
        came_from, current = to_visit.pop()
        if current not in visited:
            visited.add(current)
            parent_of[current] = came_from
            for neighbor in graph[current]:
                to_visit.append((current, neighbor))
    return parent_of
```
A "values now" strip beside it shows the variables for step 2 of the trace (came_from = S, current = C).

**B37 — The whole thing**
Screen: code appears; each line fades in as its rule is mentioned: rule 1 to line 2, rule 2 to line 5, rule 3 to lines 7 to 11, rule 4 is the missing else.
Say: "Here are the four rules as Python. Rule one is line two. Rule two is the while loop. Rule three is everything inside the if. And rule four is what's missing. If the chamber is already marked, the if is false and nothing runs."

**B38 — Pairs and unpacking**
Screen: highlight line 2, `[(None, start)]`, each symbol labeled. Then line 6, `came_from, current = to_visit.pop()`; values strip shows came_from = S, current = C.
Say: "Line two. Square brackets make a list: that's our pile. Inside is one pair. Round brackets glue two values together. The first is None, which means nobody. The second is start. Line six. Pop takes the last item out of the list: our newest token, a pair. The two names on the left of the equals sign, with a comma between them, split that pair. The first value goes into came_from. The second goes into current. That's called unpacking."

**B39 — Sets, dictionaries, and the loop**
Screen: line 3 `set()`, line 4 `{}`, line 7 `not in`, then lines 10 and 11.
Say: "A set remembers which chambers have a mark, and answers, is this one in here, very quickly. The curly brackets on line four make a dictionary: look up a chamber, get its parent. The loop adds one token per neighbor. Look at the double round brackets. The inner pair is the token. The outer ones belong to append."

**B40 — The return value**
Screen: the `parent_of` table appears: {S: None, C: S, F: C, E: F, D: E, A: D, B: A}.
Say: "The function returns the parents table. Its keys are exactly the marked chambers, the answer to reachability. And its values are the tree."

**B41 — You've already written this**
Screen: left, the iterative code; right, six lines of recursive DFS (`def visit(current): if current not in visited: visited.add(current); for neighbor in graph[current]: visit(neighbor)`). Matching lines highlighted pairwise. Samuel's `build_topo_from` from `mini-lab.py` appears briefly as the same shape with two extra lines.
Say: "One more connection. In class you wrote build topo from. That's this same idea, written with recursion. There's no written pile, because Python's own call stack is the pile. The order of the neighbors can come out flipped, but the idea is the same."

## Part 7. Recap (about 0:30)

**B42 — Retell it**
Screen: three cards: "scent marks stop the circles", "a pile of tokens remembers the tunnels we haven't walked", "the parents form a tree". Then: "Try it: run the four rules on the page-one graph from your 10/19 notes."
Say: "Let's retell it. Scent marks stop us circling. A pile of tokens remembers the tunnels we haven't walked yet. And the parents form a tree back to the nest. Pause, and run the four rules on the graph from page one of your notes. Next time: what changes when the pile is a queue, or a priority queue."

---

## Review questions for Samuel
1. Is the mole-rat story (marks, tokens) the right tone, or do you want less story and more graph?
2. The trace is slow for 14 steps, then fast for 11. Too long, or good?
3. B32 (different order, different tree): keep or cut?
4. Anything in the book section (PDF 217 to 219) you want explained more slowly?
