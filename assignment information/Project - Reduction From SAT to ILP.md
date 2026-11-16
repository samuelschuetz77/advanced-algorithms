# Project - Reduction From SAT to ILP

- **Canvas assignment:** https://snow.instructure.com/courses/1254074/assignments/19349461
- **Due:** Fri 11/20/2026, 11:59pm (available until Sat 11/21, 11:59pm)
- **Points:** 33
- **Submission:** Canvas text box: one Python file (code + tests) with a top comment (name + brief summary of how it went), plus the Part 3 correctness proof (in the text box or as a Canvas comment)
- **Status (synced 2026-11-12):** Not submitted
- **Group:** No, individual
- **AI rule:** Use the non-AI-enabled Classwork Profile. No AI code generation or completion.
- Uses PuLP 4: `pip install "pulp[highs]"` (no bundled solver in PuLP 4; `[highs]` adds one).

## Background

The last lab reduced max flow to LP (both polynomial). This lab shows ILP is NP-hard by reducing any SAT problem to ILP in polynomial time. You implement a SAT solution checker and a SAT -> ILP reduction with PuLP.

Formula representation options. String clauses: `f = ['a;b;c', '-a;b;-c', '-d;-b', '-a;c', '-b;a']`. Or (recommended) dataclasses:

```python
from dataclasses import dataclass

@dataclass
class Literal:
    var: str
    is_true: bool

def Lit(variable: str) -> Literal:
    return Literal(variable, True)

def Not(variable: str) -> Literal:
    return Literal(variable, False)

@dataclass
class Or:
    literals: list[Literal]

@dataclass
class And:
    terms: list[Or]

f = And([
    Or([Lit('a'), Lit('b'), Lit('c')]),
    Or([Not('a'), Lit('b'), Not('c')]),
    Or([Not('d'), Not('b')]),
    Or([Not('a'), Lit('c')]),
    Or([Not('b'), Lit('a')]),
])

def verify_sat(formula, assignment):
    pass
```

## Tasks (warm-up, checkpoint, main)

**Part 1 - `verify_sat` (warm-up).** Test and implement `verify_sat(f, solution)`: True iff formula `f` is satisfied by `solution` (dict variable name -> bool). Pure formula evaluation.

**Part 2 - hard-code one formula's ILP encoding (checkpoint).** Pick a small formula (2-3 clauses; an example above or your own). Hand-encode its ILP constraints in pulp (variables plus the NOT/OR/AND gadget constraints from Hints 2-3), solve, and confirm a correct satisfying assignment. Also try a small unsatisfiable formula and confirm the encoding reports infeasibility.

**Part 3 - `sat(f)` via general reduction, with proof (main).** `sat(f)` returns a satisfying assignment or `None` if unsatisfiable, implemented as a reduction to ILP using PuLP. Also write a short correctness proof (a few paragraphs) that addresses all three:
1. **Polynomial time:** building the ILP from `f` is polynomial in the size of `f`.
2. **SAT-satisfiable => ILP-feasible:** from a satisfying assignment, the corresponding 0/1 settings of the ILP variables satisfy every constraint.
3. **ILP-feasible => SAT-satisfiable:** from any feasible integer solution, reading the variables back as booleans satisfies every clause.

(2) and (3) together form the standard "iff" argument.

## Hints

- PuLP 4: `prob.add_variable("a", lowBound=0, upBound=1, cat="Integer")`. `cat` is `"Continuous"` (default), `"Integer"`, or `"Binary"` (so `prob.add_variable("a", cat="Binary")` is a true/false variable).
- Use variables for each input variable and for the result of each binary operator; linear constraints enforce operator semantics and require the whole circuit to be True.
- `NOT_A == 1 - A`
- `A_OR_B` in [0,1] with `A_OR_B >= A`, `A_OR_B >= B`, `A_OR_B <= A + B`
- `A_AND_B` in [0,1] with `A_AND_B <= A`, `A_AND_B <= B`, `A_AND_B >= A + B - 1`
- Use integer (binary) constraints so inputs are exactly true or false. You could maximize the number of satisfied clauses instead of constraining all to True. If you only care about feasibility, maximize the boolean output of the whole formula: `prob += formula_output`.

## Submission

Put code plus tests in a single file and submit via the Canvas text box, with a top comment (name + brief summary of how the project went). Include the Part 3 correctness proof as a Canvas comment or in the text box.
