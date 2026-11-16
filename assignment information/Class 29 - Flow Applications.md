# Class 29 - Flow Applications

- **Canvas page:** https://snow.instructure.com/courses/1254074/pages/class-29-flow-applications
- **Synced:** 2026-11-12 (class activity, not graded)

## Reading for Prep

JEA 11.5-11.7 (Canvas labels it "LP duality and the simplex algorithm"; the Learning Log 13 reading list pairs 11.5-11.7 with "more flow applications", and Learning Log 14 covers Extra H.1-H.5 on LP).

## Main Points

- Beyond bipartite matching, max flow solves many problems by reduction:
  - **Edge-disjoint paths:** cap every edge at 1 (it can appear in only one path).
  - **Vertex capacities:** split each vertex into an entry and an exit port joined by a capacity-bearing edge, so anything passing through must cross it.
  - **Vertex-disjoint paths:** combine both tricks, every edge (including port edges) capacity 1.
- **Min-cut / max-flow duality:** max flow from source to sink equals the minimum-capacity separating cut: a certificate of optimality (Class 12's idea).
- Recognizing a flow problem means identifying what plays "capacity" and what plays "flow" (e.g. a gift-exchange bipartite-matching problem maps onto the Class 27 reduction).
- Meta-idea: min-cut/max-flow is a concrete instance of certificates of optimality from Class 12: a specific minimum cut certifies a specific flow is maximum without re-running the algorithm.

## Walkthrough: Finding the Dual of an LP (Bodgers concession stand)

Hot dogs earn $3 (1 grill min, 1 staff min); nachos earn $5 (1 grill min, 3 staff min). 4 grill minutes and 6 staff minutes remain.

Primal:
```
maximize 3x + 5y
subject to x + y  <= 4   (grill)
           x + 3y <= 6   (staff)
           x, y >= 0
```

1. **Guess, get a lower bound.** (x, y) = (3, 1) uses all grill and staff minutes and earns 3*3 + 5*1 = 14, so the best profit is >= 14.
2. **Combine constraints for an upper bound.** Multiply grill by a >= 0 and staff by b >= 0 and add: (a+b)x + (a+3b)y <= 4a + 6b. If the coefficients dominate the profit's (a + b >= 3, a + 3b >= 5; valid since x, y >= 0) then 4a + 6b bounds the profit.
   - a=1, b=1 gives 2x + 4y <= 10: not a bound (2x < 3x).
   - a=3, b=2 gives 5x + 9y <= 24: valid but loose.
   - a=2, b=1 gives exactly 3x + 5y <= 14: tight, so (3, 1) is optimal.
3. **Best upper bound = the dual LP.**
   ```
   minimize 4a + 6b
   subject to a + b  >= 3   (one per primal VARIABLE: x's coefficient)
              a + 3b >= 5   (y's coefficient)
              a, b >= 0     (one variable per primal CONSTRAINT)
   ```
   Optimum (a, b) = (2, 1), value 14 = primal's best. **Strong duality:** if either LP has an optimum, so does the other, with the same value. Any feasible primal and dual trap the answer between them (14 <= answer <= 14): the Class 12 certificate again, and max-flow/min-cut is this picture for one particular LP.
4. **Meaning of the dual variables.** a and b are prices of a grill minute and a staff minute: $2 per grill minute and $1 per staff minute pays at least what each item earns ($2 + $1 = $3 for a hot dog's resources, $2 + $3 = $5 for nachos') and $2*4 + $1*6 = $14 in total. One more grill minute raises the best profit by about $2, one more staff minute by about $1.

### Recipe: primal to dual (maximize, <= constraints, nonnegative variables)

| Primal | Dual |
|---|---|
| maximize c.x | minimize b.y |
| one constraint row <= b_i | one variable y_i >= 0 |
| one variable x_j >= 0 | one constraint >= c_j, using column j of the constraint coefficients |
| right-hand sides b | objective coefficients |
| objective coefficients c | right-hand sides |

## Practice Quiz

Linked: "Class 29 Practice Quiz" (external quiz link on the page).
