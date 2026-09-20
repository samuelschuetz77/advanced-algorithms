# Study Guide — Big O, Sorting, and Data Structures

- **Type:** Canvas page (study guide, not graded directly — prep for [[Quiz - Big O]])
- **Canvas link:** https://snow.instructure.com/courses/1254074/pages/study-guide-big-o?module_item_id=34814098

Use this guide to prepare for the Quiz - Big O review quiz. Work through each section actively: close your notes, try to explain the idea out loud or on paper, and only check materials when you are genuinely stuck.

## 1. Asymptotic Notation

**Core idea:** We use O, Ω, and Θ to describe how a function grows as n gets large, ignoring constants and lower-order terms.

**Be able to:**
- Write the formal definition of f = O(g): there exist positive constants c and N such that f(n) ≤ c·g(n) for all n > N.
- Explain why O is an upper bound, Ω is a lower bound, and Θ requires both.
- Classify quickly: given f and g, determine whether f = O(g), g = O(f), or both (Θ).
- Recognize equivalent phrasings: f(n)/g(n) ≤ c for sufficiently large n ⟺ f = O(g).

**Practice prompts:**
- Is n^1.01 = O(n·(log n)^10)? Why or why not? (Hint: polynomials always beat polylogarithmic factors eventually.)
- Is 100n ∈ O(n)? Is n ∈ O(100n)? Is 100n ∈ Θ(n)?
- If f = O(g) and g = O(h), must f = O(h)? What property of O does this reflect?
- True or false: n^3 ∈ O(n^2).

## 2. Analyzing Code for Runtime

**Core idea:** Count how many times the dominant operation executes as a function of n.

**Be able to:**
- Look at a nested loop and determine whether the loops combine multiplicatively (independent nested ranges) or additively (sequential blocks).
- Analyze a recursive function by writing its recurrence and solving it (even informally via a recursion tree).
- Identify the dominant term in an expression like n^2 + 100n + 42.

**Practice prompts:**
- Outer loop 0 to n, inner loop i+1 to n. Total iterations? Θ?
- A recursive function calls itself twice on input size n/2, O(1) work per call. Runtime? (Draw the recursion tree.)
- Three sequential for loops, each running n times. Θ(n) or Θ(n^3)?

## 3. Sorting Lower Bound

**Core idea:** Any comparison-based sorting algorithm must make at least Ω(n log n) comparisons in the worst case.

**Be able to:**
- State the lower bound argument: n! possible orderings; each comparison cuts the space in half; so at least log₂(n!) comparisons are needed.
- Explain when algorithms beat this bound: counting sort and radix sort are not comparison-based — they exploit the structure of integer keys.

**Practice prompts:**
- Selection sort always makes exactly n(n-1)/2 comparisons. Can it ever beat Θ(n^2) on a nearly-sorted input? Why or why not?
- Why can merge sort achieve Θ(n log n) but not do better? How does this relate to the lower bound?

## 4. Data Structures — Choosing the Right Tool

**Core idea:** Different data structures provide different operation guarantees. Choosing the right one is a prerequisite for efficient algorithm design.

**Be able to match operations to structures:**
- Insert + extract-min in O(log n) → binary min-heap
- Insert + look up by key in O(1) expected → hash table
- In-order traversal + successor/predecessor in O(log n) → balanced BST
- FIFO access → queue; LIFO access → stack

**Know the runtimes:**
- Build-heap: Θ(n)
- Heap push/pop: Θ(log n)
- Heap find-min: Θ(1)
- Hash table expected lookup: Θ(1)

**Be able to explain trade-offs:** heap vs. balanced BST; when a sorted array beats either.

**Practice prompts:**
- Repeatedly find and remove the smallest element from a dynamic collection — which structure, what runtime?
- Check whether an element exists in a collection as fast as possible — which structure?
- Why is building a heap from an unsorted array Θ(n) rather than Θ(n log n)?

## 5. Gut-Check Questions

- Can you look at any 10-line Python function and immediately state its Θ runtime?
- Can you identify whether "2^n = O(3^n)" is true and explain why?
- If someone needs fast insert and fast find-min, can you immediately name the right data structure?
- Can you explain in one sentence why dropping constants in Big-O is valid?

## How to Study

1. Do the quiz cold — no notes, no references. See where you struggle.
2. For each mistake, revisit the relevant section above and rework the practice prompts.
3. Explain concepts out loud. If you can explain why n^1.01 dominates n·(log n)^10 to a friend, you understand it.
4. Practice with code: write a short function, predict its runtime, then verify by counting operations on a few inputs.

See also [[Quiz - Big O]] for the graded quiz this guide preps for.
