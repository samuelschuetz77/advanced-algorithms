# First-Week Prerequisites

Two source lists, then a priority-merged list weighted against what Project 1
(due Thu 9/3) actually requires. Sources: `big-ideas-and-review.md` (professor,
via Canvas) and the JEA textbook Preface (`Reading for Prep/JEA - Algorithms
textbook (Erickson).pdf`, pg 5-6).

## List 1 — Professor's recommendations (Canvas "Ideas to Review")

- Python — math and testing basics
- Computational problems: arithmetic, sorting, searching
- Binary addition and multiplication
- Sequential search
- Binary search
- Selection sort and insertion sort
- Asymptotic notation (Big O, etc.)
- Proofs (especially by induction)
- Python: class basics and benchmarking
- Python: generators, comprehensions, and decorators
- Trees and graphs
- Abstract Data Types (unordered/ordered sets and dictionaries, priority queues)
- Fundamental Data Structures (hash tables, AVL trees, binary heaps)

## List 2 — Book's recommendations (JEA Preface, "Prerequisites")

- Discrete math: algebra, log identities, naive set theory, Boolean algebra,
  first-order predicate logic, sets/functions/equivalences/partial orders,
  modular arithmetic, recursive definitions, trees/graphs (as abstract objects)
- Proof techniques: direct, indirect, contradiction, exhaustive case analysis,
  induction (especially strong/structural)
- Iterative programming concepts: variables, conditionals, loops, records,
  indirection, subroutines, recursion (fluency in *some* language, not
  necessarily Python)
- Fundamental ADTs: scalars, sequences, vectors, sets, stacks, queues,
  maps/dictionaries, ordered maps, priority queues
- Fundamental data structures: arrays, linked lists, BSTs, a balanced-BST
  variant, hash tables, binary heaps
- Fundamental computational problems: arithmetic, sorting, searching,
  enumeration, tree traversal
- Fundamental algorithms: elementary algorism, sequential search, binary
  search, sorting (selection/insertion/merge/heap/quick/radix), BFS/DFS
- Elementary algorithm analysis: asymptotic notation (o, O, Θ, Ω, ω),
  loops→sums, recursive calls→recurrences, evaluating sums/recurrences
- Mathematical maturity: abstraction, formal/recursive definitions, inductive
  proofs, spotting nonsense arguments

## List 3 — Priority order, weighted by Project 1

Project 1 ("Sorting," due Thu 9/3, 24 pts) requires: implementing 6 specific
sorts (bubble, selection, insertion, recursive merge, recursive/random-pivot
in-place quick, counting) with `pytest` tests, a Big O correctness/complexity
self-check on each, and a `pandas`/`seaborn` empirical benchmark + plot. That
deadline is what breaks ties below — items feeding it directly are ranked
above items that matter for the course generally but aren't due this week.

1. **The 6 sorting algorithms themselves** (bubble, selection, insertion,
   merge, quick, counting) — the literal deliverable. On both lists in part
   (professor names selection/insertion/binary-search-adjacent search;
   book names all 6 sort variants plus radix/heap).
2. **Asymptotic notation / Big O** — required for Project 1's self-check
   ("analyze your implementation to ensure it achieves the theoretical Big O
   properties... be prepared for this on an exam") and is the single most
   book-referenced topic (~230 mentions) — everything downstream leans on it.
3. **Recursion** (book's "iterative programming concepts") — merge sort and
   quick sort are explicitly required *recursive*; without this, 2 of the 6
   algorithms are blocked outright, not just harder.
4. **pytest fluency + benchmarking/plotting (pandas, seaborn)** — both
   explicitly required for Project 1 Part 1 (tests) and Part 2 (benchmark +
   plot); professor's list calls these out directly ("Python — math and
   testing basics," "class basics and benchmarking").
5. **Proofs, especially induction** — needed to actually back up the Big O
   self-check in #2 with real reasoning rather than guessing; book leans on
   induction constantly (2nd-most-referenced topic after asymptotic notation).
6. **Sequential search / binary search** — on both lists, foundational, but
   not part of Project 1's 6 algorithms directly — useful review, not
   blocking this week's deadline.
7. **Discrete math basics** (logs, set theory, Boolean algebra, modular
   arithmetic) — book prerequisite, but background/ongoing rather than
   something Project 1 exercises directly this week.
8. **Trees, graphs, ADTs (stacks/queues/priority queues), hash tables/AVL
   trees/binary heaps** — on both lists, but the course doesn't reach graph
   material until ~week 8 (per `course-schedule.md`); lowest urgency for
   *this* week specifically, even though it'll matter a lot later.
9. **Python generators/comprehensions/decorators** — professor's list wants
   this, but the book itself never uses Python at all (language-agnostic
   pseudocode) and Project 1 doesn't strictly require these features to
   pass — nice-to-have fluency, not a blocker.

Bottom line: if time is tight this week, 1-4 are what actually gate turning
in Project 1 on time; 5 strengthens the analysis you're required to be
"prepared to do... on an exam"; 6-9 matter for the course as a whole but
aren't this week's fire.
