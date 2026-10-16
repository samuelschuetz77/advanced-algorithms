# Class 15 - More DP Examples

Source: https://snow.instructure.com/courses/1254074/pages/class-15-more-dp-examples
Last synced: 2026-10-03 via ChatGPT in Chrome. Class page, not a separate graded submission.

Class 15 - More DP Examples
Mini Lab
Part 1
min_coins(coins, amount) returns the fewest coins that add up to exactly
amount, where coins lists the coin values and each value can be used any
number of times. (With coins worth 1, 4, and 5, the fewest coins that make
8 are two 4s.)

Write it so that this pytest test passes in O(k * T) time, where k is the
number of coin values and T is the amount:
def test_min_coins():
    assert min_coins([1, 4, 5], 8) == 2
    assert min_coins([5, 4, 1], 13) == 3
    assert min_coins([1, 4, 5], 0) == 0
    assert min_coins([1, 4, 5], 200) == 40

Bonus
If you get done early, write make_change(coins, amount), which returns the
coins themselves (a list of fewest coins adding up to amount), or None if
no combination adds up to amount. Make this pass, still in O(k * T) time:
def test_make_change():
    assert sorted(make_change([1, 4, 5], 8)) == [4, 4]
    assert sorted(make_change([5, 4, 1], 13)) == [4, 4, 5]
    assert make_change([4, 5], 7) is None

Main Points
Continued DP practice: the goal today is pattern-matching new problems to the recipe from Class 14 -- what are the subproblems, what's the recurrence, what order do you fill them in.
A good diagnostic question when facing a new optimization problem: "if I already knew the answer to slightly smaller versions of this problem, could I combine them to answer this version?" -- if yes, DP is likely a fit.
The hard step in practice is almost always step (1), defining the subproblems -- once the subproblems are stated precisely enough, the recurrence usually writes itself and the evaluation order follows from the recurrence.
Meta-idea: DP is a technique for exploiting structure (overlapping subproblems) that many optimization problems share, even when their surface descriptions look unrelated.
Practice Quiz
Class 15 Practice Quiz
Links to an external site.
Previous