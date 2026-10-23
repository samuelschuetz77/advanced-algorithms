# Transcript: Whatever-First Search, Part 1: The Mole-Rat Colony

Voice: Ava (en-US-AvaMultilingualNeural). Cue markers and phonetic markup removed.

## 01 · 0:00 · Meet Wrinkles

Meet Wrinkles, a naked mole-rat worker. Her colony is a maze of chambers joined by tunnels. Mathematicians draw a maze like this as a graph. Each chamber is a dot, called a vertex. Each tunnel is a line, called an edge.

## 02 · 0:17 · The question

Wrinkles is in the nest, vertex S. Her job is to find every chamber she can reach by following tunnels. That question has a name: reachability. And one burrow over here was cut off by a cave-in, so she will never reach it. Pause, and think. How would Wrinkles check every chamber?

## 03 · 0:43 · Her first idea

Wrinkles' first idea: follow any tunnel. At the next chamber, follow any tunnel again. Watch. Round and round. She never remembers where she has been.

## 04 · 0:55 · A better idea: a scent mark

Naked mole-rats know their colony by smell, so Wrinkles has a better idea. The first time she arrives at a chamber, she leaves a scent mark. In graph words, she marks the vertex. If she arrives at a marked vertex, she knows: been here, nothing new, turn around.

## 05 · 1:16 · One more problem

But a scent mark is not enough. At the nest, three tunnels lead out of vertex S, and Wrinkles can only walk down one. What happens to the other two? Pause. How does she remember them?

## 06 · 1:33 · A pile of tokens

So Wrinkles carries a pile of tokens. Each token reminds her of one tunnel she has not walked yet. It is stamped with the two chambers that tunnel connects. Mole-rats cannot really read, so just pretend.

## 07 · 1:48 · The pile has a name

All the tokens go into one pile. The book calls this pile a bag. It is just somewhere to put things in, and take things out.

## 08 · 1:57 · A token is a pair

Each token is a pair: the vertex she came from, and the vertex it leads to. In code, we will call these two things came_from, and current. In a few minutes, you will see why we keep both.

## 09 · 2:11 · The four rules

The whole method is four rules. Rule one: start with a single token that says: came from nobody, leads to the nest.

## 10 · 2:20 · The four rules

Rule two: as long as the pile is not empty, take one token out.

## 11 · 2:26 · The four rules

Rule three: look at the vertex that token leads to. If it has no mark yet, mark it. Remember who sent her. That is its parent. Then add a new token for every edge leaving that vertex.

## 12 · 2:41 · The four rules

Rule four: if the vertex is already marked, throw the token away. There is nothing new to do.

## 13 · 2:48 · The book's name for it

That is the entire algorithm. The book calls it whatever-first search, because we have not said which token to take out of the pile. Today, we always take the newest one. Next video, we will see what changes if you choose differently. And if you open the book, here is the translation of its letters. The letter s is the start. The bag is our token pile. The letter p is came_from. The letter v is current. And w is a neighbor.

## 14 · 3:18 · Run it on the colony

Let us run it on the colony. Seven vertices, twelve edges. Each vertex keeps a list of its neighbors, and adds tokens in list order. So the last neighbor in the list ends up on top of the pile.

## 15 · 3:33 · Step 1

Start with one token: nobody to S. Take it out. S has no mark, so mark S. Its parent is nobody. S has three edges, so add three tokens: S to A, S to B, and S to C.

## 16 · 3:50 · Which token comes out?

Now the pile has three tokens. We always take the newest one. Which one is it?

## 17 · 4:01 · Step 2

It is S to C, the last one we added. Take it out. C is new, so mark C. Its parent is S. C has four edges, to A, B, F, and back to S, so four tokens go on top.

## 18 · 4:16 · Step 3: a useless token

Newest token: C to S. But S already has a mark. Throw it away.

## 19 · 4:23 · Step 4

Next, C to F. F is new. Mark it, parent C. F has three edges, to C, D, and E, so three tokens go on top.

## 20 · 4:34 · Step 5

The newest is F to E. E is new. Mark it, parent F. E has edges to B, D, and F. Three more tokens.

## 21 · 4:44 · Step 6

Now E to F. F is already marked. Throw it away.

## 22 · 4:50 · Step 7

Next, E to D. D is new. Mark it, parent E. D has edges to A, E, and F. Three more tokens.

## 23 · 5:00 · Steps 8 and 9

D to F: F is marked. Throw it away. D to E: E is marked. Throw that one away too.

## 24 · 5:09 · Step 10: predict

D to A. A is new, so mark A, parent D. A has four edges, so four tokens go on top: to B, C, D, and S. Only one of those vertices is still unmarked. Which token will lead Wrinkles to it, and how many will she throw away first?

## 25 · 5:34 · Steps 11 to 14

The answer: three get thrown away. A to S, A to D, and A to C. Then A to B. B is new, so mark B. Its parent is A. That is the seventh vertex. Every vertex Wrinkles can reach now has a mark. But the pile is not empty.

## 26 · 5:55 · Steps 15 to 25: the pile drains

Eleven tokens are left, and every one leads to a marked vertex. So rule four, over and over. Throw it away, throw it away. Watch the pile drain. The last two tokens, S to B and S to A, have been waiting at the bottom since step one. Their vertices got marked a different way, so they are stale. We never dig through the pile to remove old tokens. We just ignore them when they come out. Zero tokens. We are done.

## 27 · 6:25 · The answer, and a count

The marked vertices are S, A, B, C, D, E, and F. X and Y never got a mark. That is the answer: from the nest, Wrinkles can reach seven chambers, and she can never reach the cut-off burrow. And look at the count. Twenty-five tokens in all: one to start, and two for each of the twelve edges, one from each end. Only seven were useful. We will use that count in the next video.

## 28 · 6:54 · Why keep the pair?

Remember the pair on each token? Here is why. Ask vertex B: who is your parent? A. Ask A? D. Ask D? E. Then F, then C, then S. Keep asking, and Wrinkles walks right back to the nest.

## 29 · 7:12 · The parents form a tree

Now draw only the parent edges. Six of them, one fewer than the seven vertices. They form a tree: one long, skinny path from the nest. The book says depth-first trees are usually long and skinny. And every marked vertex hangs from the nest by exactly one route.

## 30 · 7:32 · Promise 1: it stops

Three promises. First, it always stops. A vertex is marked only once, and only a marked vertex adds tokens. So the pile cannot keep growing forever.

## 31 · 7:45 · Promise 2: nothing unreachable

Second, it never marks a vertex she cannot reach. Every token is added by a marked vertex, along a real edge. So every marked vertex has a chain of parents leading back to the nest.

## 32 · 8:00 · Promise 3: every reachable vertex

Third, it marks every vertex she can reach. Pick any reachable vertex, call it the target, and take a shortest route to it. The nest, then a few vertices, then the target.

## 33 · 8:13 · Promise 3: the dominoes

S gets marked, so it adds a token for the next vertex on the route. That token cannot vanish, and the search only stops when the pile is empty, so the token gets taken out. At that moment the vertex is already marked, or it gets marked now. Either way, it is marked.

## 34 · 8:32 · Promise 3: induction

Then it adds the token for the next one. Each vertex knocks over the next. Mathematicians call this induction on distance. It is the proof of Lemma five point one, and now you can read it.

## 35 · 8:45 · The four rules, as Python

Here are the four rules as Python. Rule one is line two. Rule two is the while loop. Rule three is everything inside the if. And rule four is what is missing: if the vertex is already marked, the if is false, and nothing runs.

## 36 · 9:03 · Reading line two

Line two. Square brackets make a list: that is our pile. Inside is one pair. Round brackets glue two values together. The first is None, which means nobody. The second is start.

## 37 · 9:18 · Reading line six

Line six. Pop takes the last item out of the list: our newest token, a pair. The two names on the left of the equals sign, with a comma between them, split that pair. The first value goes into came_from. The second goes into current. That is called unpacking.

## 38 · 9:37 · Sets, dictionaries, and the loop

A set remembers which vertices have a mark, and answers, is this one in here, very quickly. The curly brackets on line four make a dictionary: look up a vertex, get its parent. The loop adds one token per neighbor. Look at the double round brackets. The inner pair is the token. The outer ones belong to append.

## 39 · 9:59 · What it returns

The function returns the parents table. Its keys are exactly the marked vertices, the answer to reachability. And its values are the tree.

## 40 · 10:10 · You have already written this

One more connection. In class you wrote build_topo_from. That is this same idea, written with recursion. There is no written pile, because Python's own call stack is the pile. The order of the neighbors can come out flipped, but the idea is the same.

## 41 · 10:27 · Recap

Let us retell it. Scent marks stop her circling. A pile of tokens remembers the tunnels she has not walked yet. And the parents form a tree back to the nest. Pause, and run the four rules on the graph from page one of your notes. Next time: what changes when the pile is a queue, or a priority queue.
