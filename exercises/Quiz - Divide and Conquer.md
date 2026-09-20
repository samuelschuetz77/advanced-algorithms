# Quiz - Divide and Conquer

Fall 2026 Advanced Algorithms (SE-4230-001)
Score: 5.5 / 12 — submitted, quiz locked, correct answers hidden by Canvas.

## Question 1 (1.5 / 6 pts)

Solve the following recurrence relations. (Use the master theorem or draw the recursion tree.)

Recurrences:
- T(n) = 2T(n/2) + O(n)
- T(n) = 2T(n/2) + O(1)
- T(n) = T(n/2) + O(1)
- T(n) = T(n/2) + O(n)
- T(n) = 4T(n/2) + O(n)
- T(n) = 4T(n/2) + O(n^2)
- T(n) = T(n-1) + O(n)
- T(n) = T(n-1) + O(1)

Answer pool shown on page: Θ(n log n), Θ(n), Θ(n)

## Question 2 (0 / 1 pts)

Solve the recurrence: F(n) = 4F(n/2) + n^2

- Θ(n^2 log n)
- Θ(n^3)
- Θ(2^n)
- Θ(n^(1/2))
- Θ(n log n)

## Question 3 (4 / 4 pts, correct)

Match each case to the bound it gives (master theorem: T(n) = a·T(n/b) + O(n^d)).

- Root dominates: d > log_b(a) → Θ(n^d)
- Every level costs the same: d = log_b(a) → Θ(n^d log n)
- Leaves dominate: d < log_b(a) → Θ(n^(log_b a))

## Question 4 (0 / 1 pts)

A divide-and-conquer algorithm solves a problem of size n by:
- Splitting the input into 3 subproblems of size n/3
- Solving 2 of the 3 subproblems recursively
- Combining the results in O(n) time

What is the asymptotic runtime of this algorithm?

- Θ(n log n), because the combination step is linear.
- Θ(n), because only 2/3 of the work is done at each level.
- Θ(n^(log_3 2)) ≈ Θ(n^0.63), because the leaves dominate.
- Θ(n^2), because two recursive calls each see n/3 of the input.

## Question 5 (0 / 0 pts, select all that apply)

Karatsuba's algorithm multiplies two n-digit numbers significantly faster than the grade-school algorithm. Select all true statements.

- Reducing recursive calls from 4 to 3 changes which case of the master theorem applies and yields a better asymptotic bound.
- Karatsuba runs in Θ(n^(log_2 3)) ≈ Θ(n^1.585), which is asymptotically faster than the Θ(n^2) grade-school algorithm.
- Karatsuba's algorithm requires Θ(n^2) extra space.
- The grade-school algorithm uses 4 multiplications of (n/2)-digit numbers at each level of recursion; Karatsuba uses only 3, using a clever algebraic identity.
- The savings from Karatsuba come entirely from reducing the combination (addition) step.

## Question 6 (0 / 0 pts, select all that apply)

Select all true statements about divide-and-conquer.

- If a D&C algorithm's sub-problems overlap, memoization cannot help.
- The same recursion tree analysis used to derive the master theorem can be applied to recurrences the theorem doesn't neatly cover.
- Divide-and-conquer decomposes a problem into sub-problems of the same type that typically do not overlap.
- Merge sort's correctness relies on the fact that merging two sorted halves into a sorted whole can be done in O(n) time.
- Divide-and-conquer always gives a sub-quadratic algorithm.
- The recurrence T(n) = aT(n/b) + f(n) captures the runtime of a D&C algorithm that makes a recursive calls on inputs of size n/b with O(f(n)) overhead.
