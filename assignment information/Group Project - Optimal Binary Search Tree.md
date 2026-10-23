# Group Project - Optimal Binary Search Tree

- Status: Graded 25/25; submitted 10/10/2026 9:08pm (late) (Canvas, as of 2026-10-20).
- **Status:** Submitted 10/10/2026 at 9:08pm Mountain; late; ungraded.
- **Last synced:** 2026-10-12 via ChatGPT in Chrome; Canvas Grades checked.
- **Canvas link:** https://snow.instructure.com/courses/1254074/assignments/19231864
- **Due:** Fri 10/9/2026, 11:59pm Mountain. Available until 10/10, 11:59pm.
- **Submission:** Python file, three labeled test screenshots, and reflection.
- **Turn-in path:** `../projects or assignments i turn in live here/` (specific file not yet identified).

## Canvas specification and rubric

With a partner, implement and test a top-down dynamic programming solution to Problem 40 from chapter 3 of Jeff Erickson's online textbook (with the additional details and clarifications below). Whatever you submit should be something that you can recreate on paper without other resources (other than basic notes on Python language features).

As usual, use your non-AI-enabled Classwork Profile for this assignment (no AI code generation or completion).

Summary of the Problem and Clarifications

The problem describes a library where books are fetched by a robot.

Books are stored in bins ordered by increasing ISBN---one bin per owned book title, and books are requested, one copy at a time, by submitting the ISBN to the robot, which then follows a binary search tree over the bin indexes to locate the bin with the matching ISBN.
Based on a variety of historical data and current information, the library has a guess as to the expected number of times each bin will be accessed on any particular day, so the binary search can be re-programmed each day to try to minimize total access time over the day. An array of expected bin frequencies for the day are given as part of the problem input.
The robot must start out at bin 0, facing in the "negative" direction (toward the front desk) to receive an ISBN request.
After receiving the ISBN, the robot must move to the root of the pre-programmed binary search tree, but the robot can only move in the direction it is facing. Whenever the robot must change directions it incurs a cost, and the cost_per_rotation is given as part of the problem input.
If facing in the correct direction, the robot can move to a target index which incurs an additional movement cost which is proportional to the distance that the robot must move. The move_cost_per_distance is given as part of the problem input.
Once the robot arrives at the index corresponding to the tree root, it scans the QR-code on the bin which lets the robot know whether the target ISBN is less than, equal to, or greater than the scanned bin. The robot can scan while facing in the negative or positive direction. The cost_per_scan is given as part of the problem input.
If the robot discovers that the scanned bin has the target ISBN, the robot ensures that it is facing in the negative direction and then moves back to index 0 to deliver the book. Otherwise, the robot consults the appropriate left or right child index stored in the pre-programmed binary search tree and prepares to move to that index to continue the search.

Ultimately, the top-level problem is to efficiently find, given a list of item expected frequencies and the three cost parameters, the binary search tree (over bin indexes) that minimizes the total expected cost of all book deliveries during the day. You will build up to this in four main parts, plus a final submission part:

Describe the recursive structure of the problem in words/math
Use backtracking only (no dynamic programming) to compute the minimum possible cost (do not bother to build up the actual tree yet)
Add dynamic programming (via memoization with lru_cache or cache) to compute the minimum possible cost efficiently
Add the bookkeeping necessary to efficiently construct the optimal tree in addition to computing the optimal cost

Part 1 really represents the bulk of the work, but until you put it into correct code, you might not realize that your solution has holes in it, which is why the concrete implementation can be helpful. I also hope that you can appreciate the very fine line between the correct and slow backtracking implementation and the correct and fast implementation that uses memoization.

Part 1 -- Planning your solution

Work the first three provided test cases (below) out by hand and confirm you get the same numbers. If your hand calculation disagrees with the test, sort that out now -- everything after this depends on you having the cost model right.

After you are clear on the parameters and functionality of the top-level function, answer the following questions in your .py file using a combination of English and Math (you don't necessarily need to figure these out in this order):

What is the best name that you can think of for the top-level function that only returns the optimal cost (not-the tree) and what parameters should the function accept and what does the function return? (Be as precise and clear as you can be.)
How can you carve off part of the problem to be solved by a nested, recursive function, and what parameters would be necessary to identify a particular subproblem? Note: the recursive function doesn't need to be given any of the information already available in the top-level function since it already has access to it; rather, the nested function just needs to know what part of the problem it is working on and any context that would impact the cost of solving that part of the problem (e.g. where is the robot traveling from). Of course, since we will be using memoization with a hash table, make sure that you only use hashable parameter types to the nested function.
How will the top-level function use the nested function to solve the top-level problem. (I.e. What nested function calls will the top-level function make to solve the top-level problem?)
(a) What instances of the nested problem are base cases? and (b) What should the nested function return for each base case?
(a) What part of the solution will the nested function directly choose (hint: what should be the root index for the problem subset)? (b) What options will it consider for that choice? (c) How will it determine the cost/value of each candidate (including what recursive calls it will need to make as part of that calculation and how will those results be combined)? and (d) How will it decide how to combine the results for the various options (hint: in this case, you want the option with the smallest cost)?
Part 2 -- Min Cost Backtracking Search

Write optimal_cost_backtracking so that it passes the provided test_backtracking_finds_the_optimal_cost cases, without memoization or any other dynamic programming technique. Regardless of the name you came up with in Part 1, use the names the tests use here: the function optimal_cost_backtracking with parameters frequencies, cost_per_rotation, move_cost_per_distance, and cost_per_scan (the tests pass the costs by name).

Part 3 -- Min Cost Dynamic Programming Search

Copy your part 2 function to optimal_cost_memoized (same parameter names) and add dynamic programming via memoization with the functools.lru_cache or functools.cache decorator on your nested recursive function. (You may need to raise the recursion limit via sys.setrecursionlimit.) It has to get the same answers as part 2 and also finish test_memoized_handles_fifty_bins, which your part 2 function would never finish.

Part 4 -- Return the Optimal Tree

Copy your part 3 function to optimal_tree (same parameter names) and add the bookkeeping to return the optimal binary search tree (as a nested tuple) alongside the minimum cost, as a (cost, tree) pair.

Hints:

When considering the cost of using a binary search tree on a span of bins, notice that every request for a bin in that span must first physically pass through the index at the root of the tree. So when you calculate the rotations, movement, and scan needed to check the root, you will need to know the total frequency of all the indexes in the span.

Nested tuples are great for representing trees—an empty tuple represents an empty tree and a (value, left_tree, right_tree) triple represents a non-empty tree. For this assignment, use the book indices (0, 1, 2, ...) as the values in the tree, not actual ISBNs. For example, the following tree has 10 at the root node, the left subtree has 7 at root and the right subtree has 12 at root, etc.; the node with value 8 doesn't have a left child (if you turn your head sideways to the right, you can kind of see the tree structure):

```python
value, left, right = (10, (7, (3, (1, (0, (), ()),
                                     (2, (), ())),
                                 (5, (4, (), ()),
                                     (6, (), ()))),
                             (8, (),
                                 (9, (), ()))),
                         (12, (11, (), ()),
                              ()))


```

(Note that building the tree (value, left, right) can be done in constant time if left and right are already built since only the references are copied into the tuple rather than having the contents be deep-copied.)

Provided Tests

Each case with a tree listed has exactly one optimal tree, so there is a single right answer to compare against. If you want to create additional classes for your trees rather than just using tuples: make sure that (1) you don't change the big O space or running time and (2) make sure that you only make the minimal changes to the provided tests to accommodate your interface changes.

Tests -- paste these as-is at the bottom of your .py file (click to expand)
```python
# (frequencies, rotation, move, scan, optimal cost, optimal tree)
# Each case has exactly one optimal tree, so the tree is safe to check.
OPTIMAL_BST_CASES = [
    ([5],                3, 1, 2,   10, (0, (), ())),
    ([4, 3],             3, 1, 2,   44, (0, (), (1, (), ()))),
    ([4, 30],            3, 1, 2,  348, (1, (0, (), ()), ())),
    ([1, 1, 1],          3, 1, 2,   30, (0, (), (1, (), (2, (), ())))),
    ([4, 3, 28, 100, 5], 3, 1, 2, 2072, (3, (2, (1, (0, (), ()), ()), ()), (4, (), ()))),
    ([1, 1, 1, 1, 1, 50], 7, 2, 1, 1940,
     (5, (4, (3, (2, (1, (0, (), ()), ()), ()), ()), ()), ())),
    ([3, 1, 4, 1, 5, 9, 2, 6], 5, 2, 3, 1132,
     (2, (1, (0, (), ()), ()),
         (5, (4, (3, (), ()), ()), (7, (6, (), ()), ())))),
    ([20, 5, 1, 1, 30, 2, 2, 40], 4, 1, 0, 1512,
     (0, (), (1, (), (2, (), (3, (), (4, (), (5, (), (6, (), (7, (), ()))))))))),
]

# Fifty bins. Only a memoized solution finishes this one -- plain backtracking would
# have to look at more trees than there are atoms in anything you care about.
FIFTY_BIN_FREQUENCIES = (4, 3, 28, 100, 5) * 10
FIFTY_BIN_COST = 96532


def test_backtracking_finds_the_optimal_cost():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert cost == optimal_cost_backtracking(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_memoized_finds_the_same_costs():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert cost == optimal_cost_memoized(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_memoized_handles_fifty_bins():
    assert FIFTY_BIN_COST == optimal_cost_memoized(
        list(FIFTY_BIN_FREQUENCIES), cost_per_rotation=3, move_cost_per_distance=1, cost_per_scan=2)


def test_optimal_tree_and_its_cost():
    for frequencies, rotation, move, scan, cost, tree in OPTIMAL_BST_CASES:
        assert (cost, tree) == optimal_tree(
            frequencies, cost_per_rotation=rotation, move_cost_per_distance=move, cost_per_scan=scan
        ), frequencies


def test_optimal_tree_still_works_on_fifty_bins():
    frequencies = list(FIFTY_BIN_FREQUENCIES)
    cost, tree = optimal_tree(
        frequencies, cost_per_rotation=3, move_cost_per_distance=1, cost_per_scan=2)
    assert FIFTY_BIN_COST == cost
    # every bin appears exactly once, and the tree is a search tree on the bin numbers
    def bins_in_order(t):
        return [] if t == () else bins_in_order(t[1]) + [t[0]] + bins_in_order(t[2])
    assert list(range(len(frequencies))) == bins_in_order(tree)


if __name__ == "__main__":
    # Runs the tests without pytest, so you can step through them in a debugger.
    for test in [test_backtracking_finds_the_optimal_cost,
                 test_memoized_finds_the_same_costs,
                 test_memoized_handles_fifty_bins,
                 test_optimal_tree_and_its_cost,
                 test_optimal_tree_still_works_on_fifty_bins]:
        test()
        print("passed:", test.__name__)

```

Part 5 -- Submission and Evaluation

Make sure that your names and the date are included in comments at the top of your .py file.

Screenshots are how parts 2, 3, and 4 get graded, so take one per part, each showing that part's tests passing along with the command you ran.

Submit:

Your .py file
The three screenshots, labeled by part
A brief paragraph (this can be a canvas comment) describing how the assignment went, how well you (and your partner) accomplished each of the 4 parts.
View Rubric
Rubric for Assignment: Group Project - Optimal Binary Search Tree (1)
Rubric for Assignment: Group Project - Optimal Binary Search Tree (1)
Criteria	Ratings	Points

good answers for the questions in part 1 (other parts should be straigh-forward given your answers)
	
Full Marks
10 pts
No Marks
0 pts
	
/10 pts


part 2 - correct and clean backtracking implementation, with a screenshot of its tests passing
	
Full Marks
5 pts
No Marks
0 pts
	
/5 pts


part 3 - correct and clean dynamic programming implementation, with a screenshot of its tests passing, including the fifty-bin case
	
Full Marks
4 pts
No Marks
0 pts
	
/4 pts


part 4 - correct and clean dynamic programming implementation that returns the optimal tree, with a screenshot of its tests passing
	
Full Marks
4 pts
No Marks
0 pts
	
/4 pts


satisfactory reflection
	
Full Marks
2 pts
No Marks
0 pts
	
/2 pts
