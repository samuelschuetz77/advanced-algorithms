# Group Project - Reduction From Maxflow to LP

- **Canvas assignment:** https://snow.instructure.com/courses/1254074/assignments/19336517
- **Due:** Fri 11/13/2026, 11:59pm (available until Sat 11/14, 11:59pm)
- **Points:** 20
- **Submission:** Canvas text entry (link to Classroom 50 repo + screenshot of all tests passing + brief description of how the project went)
- **Status (synced 2026-11-12):** Not submitted (Canvas shows "In Progress")
- **Partner:** yes (shared Classroom 50 group repo)
- **AI rule:** Use your non-AI-enabled Classwork Profile. No AI code generation or completion.

## Task

With a partner, use the Python `pulp` library to reduce max flow to LP, and use that reduction to solve the problems from the previous max flow applications project.

PuLP 4 note: install with `pip install "pulp[highs]"` (PuLP 4 no longer bundles a solver; `[highs]` adds one). Variables are created by the problem: `prob.add_variable("f_s_a", lowBound=0, upBound=3)`.

### Shared repository

One partner opens the Classroom 50 assignment, clicks Create group, and accepts it. They click Manage my group and add the other partner by GitHub username; the other partner opens the link and clicks Check again. Both clone. The repo starts empty, so add a `.gitignore` before the first commit (track only code, tests, small data files; leave out `__pycache__/`, `.pytest_cache/`, `.venv/`, editor settings; GitHub's Python template is a good start).

### Part 1 - max flow solver via LP (with automated tests)

Interface:
- Input: weighted directed graph (weights = capacities; reuse your graph class from earlier in the semester), start node `s`, target node `t`.
- Output: weighted directed graph whose edge weights are the flow on each edge in a max flow.

Built in three stages:

- **1a - Hard-code the example (warm-up).** Hand-write the LP for the one example graph (the s,a,b,c,d,e,t graph): a variable per specific edge via `prob.add_variable`, constraints for that graph, objective, call pulp's solver. Confirm it produces the expected flow. No generalizing yet.
- **1b - Nonnegativity and capacity constraints, generalized (checkpoint).** Write the skeleton of `max_flow_via_lp(graph, s, t)`. Create one variable per edge of an arbitrary input graph, and add the first two constraint categories (nonnegativity and capacity). Simplest in PuLP 4: `lowBound=0`, `upBound=capacity` at creation (separate constraints also work). Write a test or two confirming the right variables exist with the right bounds/constraints. A solvable LP isn't needed yet.
- **1c - Flow conservation, objective, solving (main).** Add flow conservation, the objective, solve, and return the flow graph. Must satisfy the full interface for arbitrary graphs, including the 1a example.

Hints:
- One variable per edge = flow on that edge.
- Objective: total flow into `t` (or equivalently total flow out of `s`).
- Three constraint categories: (1) flow >= 0 per edge, (2) flow <= capacity per edge, (3) for every node except `s` and `t`, flow in = flow out.
- Create each edge's variable once and store it, e.g. `flow[(u, v)] = prob.add_variable(f"f_{u}_{v}", lowBound=0, upBound=capacity)`; the bounds also cover nonnegativity and capacity.
- Hard-code a simple concrete example with a test first, then generalize.
- Review the rubric before submitting.

Example graph is based on Fig 7.4 of Dasgupta, Papadimitriou, Vazirani (capacity graph + one possible flow graph shown as images in Canvas).

### Part 2

Each partner implemented a reduction from a different problem to max flow. For at least one of them, complete the reduction: use your max flow solver to compute the flow, then write code that extracts the answer to the original problem from that flow.

## Submit

Push to the Classroom 50 repo:
- Max flow solver (via LP reduction) with pytests (correct total flow on the example; for a graph with a unique max flow, edge flows match expected).
- Complete solution to one of the problems from the max flow applications project, using the LP-based solver to actually solve the original problem, with pytests on a small example.

In Canvas:
- Link to the Classroom 50 repo
- Screenshot of all tests passing
- Brief description of how you satisfied the requirements and how the project went

## Related

- [Project - Applications of Maxflow](Project%20-%20Applications%20of%20Maxflow.md) (previous project this builds on)
