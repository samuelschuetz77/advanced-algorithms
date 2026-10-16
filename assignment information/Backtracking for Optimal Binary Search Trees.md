# Backtracking for Optimal Binary Search Trees

- **Type:** Assignment (Canvas)
- **Due:** Wed 9/23/2026, 11:59pm (available until Thu 9/24/2026, 11:59pm)
- **Points:** 24
- **Canvas link:** https://snow.instructure.com/courses/1254074/assignments/19207060
- **Canvas status:** "In Progress" (a draft attempt already exists)

## Details

Based on JEA §2.8 (Optimal BSTs). Staged easy → medium → main. Canvas update:
AI assistance is allowed, but the submitted work must be understood and owned
by the student.

- **Part 1 (easy/warm-up):** Implement + test a plain recursive backtracking
  method for OptCost(start, end, frequencies) per the given pseudocode
  (exponential time is expected/intended). Tree is over indexes: lower
  indexes descend left, higher indexes descend right.
- **Part 2 (medium/checkpoint):** Refactor Part 1 into a nested recursive
  function that doesn't take `frequencies` as a parameter (closes over it
  instead). Tests must still pass.
- **Part 3 (medium/checkpoint):** Implement OptCostAndTree returning both
  cost and tree structure (CombineCostsAndTrees pseudocode given). Big-Theta
  worst case must stay the same as Part 2.
- **Part 4 (main):** Variation — add a constant cost `L` (leftPenalty)
  charged each time search goes left. Complete/derive the OptCost recurrence
  for this variation yourself (pseudocode intentionally incomplete on
  Canvas).
- **Part 5 (main):** Implement + test the Part 4 variation, also retrieving
  optimal tree structure (like Part 3).

## Submission requirements

- Python code including tests, pasted in the Canvas text box
- Screenshot of test results
- A few sentences: what was challenging / what you learned
- Submission type: Text (code) — Canvas also allows Upload / more options

## Status

Published as of 9/19/2026 (was unpublished as of 9/17 sync). AI policy updated
from Canvas on 9/21/2026 per latest student check. Due 9/23.

Grades page (2026-09-28): File Upload Submission submitted Sep 23 at 11:58pm; Canvas due date now shows Sep 25 by 11:59pm. Ungraded (— / 24).
