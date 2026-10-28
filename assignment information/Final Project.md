# Final Project

- Canvas assignment 19302867 (Module 10), https://snow.instructure.com/courses/1254074/assignments/19302867
- Points: 100
- Due: **Sun 12/13/2026, 9:59pm MST** (API 12/14 04:59Z)
- Submission: online text entry (repo link) + file upload (slides PDF)
- Status at sync (2026-10-23): unsubmitted
- Weekly progress checkpoints (6 total, every Wednesday except Thanksgiving week): see [Final Checkpoint 1.md](Final%20Checkpoint%201.md)
- Builds on Part 1 ([Final Project Part 1 - Pick and Present a Problem.md](Final%20Project%20Part%201%20-%20Pick%20and%20Present%20a%20Problem.md)); problem chosen there: Optimal Facility Location.

## Overview
A decision problem is in NP if a proposed solution can be verified in polynomial time. NP-hard: every NP problem reduces to it in polynomial time. NP-complete = both. A poly-time solver for any NP-complete problem would give poly-time solvers for all of NP (P = NP).

Choose a known NP-complete problem (Wikipedia list; must differ from everyone else's), and think deeply about theory, engineering applications, and algorithmic trade-offs.

You will:
- Keep a progress journal throughout (learning, experiments, results, challenges, changes in approach).
- Teach the class the theory: inputs/outputs, why NP-complete, poly-time verification, a poly-time reduction from a famous NP-complete problem.
- Point to at least one recent academic article on the problem or your engineering application.
- Show a real-world engineering problem reducible to your problem.
- Write code that generates sample input data for it.
- Implement and compare: brute force (baseline), an improved exact method (branch-and-bound, DP), a heuristic/approximation.
- Map the Pareto frontier (runtime vs solution quality).
- Present to the class.

## Steps
**Step 0 - Progress journal.** Accept the Classroom 50 assignment to get your repo; clone it. Add a `.gitignore` before the first commit (leave out `__pycache__/`, `.pytest_cache/`, `.venv/`, editor settings, large generated datasets; GitHub's Python template is a good start). Start a journal document with date-stamped entries. Journal entries and Learning Log entries can be reused in each other.

**Step 1 - Choose your problem.** From the Wikipedia list (unique in the class) or propose your own. The NP-hardness proof must reduce from **3SAT, subset sum, or graph coloring** (the course later covers circuit SAT -> 3SAT -> subset sum / graph coloring). You may find a published reduction; understand it, explain it, cite it. Claim your problem first-come-first-served in the class discussion.

**Step 2 - Theory presentation.** Stand-alone slideshow with:
- formal definition of the decision version
- at least two concrete instances with solutions
- the certificate for a "yes" answer (e.g. for a budgeted Hamiltonian path: the path itself)
- how to verify it in polynomial time (check edges exist, each node once, total weight <= B)
- sketch of the NP-hardness proof by reduction from 3SAT / subset sum / graph coloring (say which one you chain onto)
- a recent peer-reviewed article connected to your problem (new algorithms or complexity results for a variant, applications in engineering/CS/other fields, new approximations or heuristics; if nothing exists for your problem, use a problem it reduces to). Venues to consider: Algorithms (journal), SODA, ISAAC, ESA, APPROX, TACAS, WADS, FUN, ACL, EMNLP, NAACL, EACL.

**Step 3 - Engineering connection.** A real-world engineering problem solvable via reduction to your problem; write and present the reduction steps. **Required:** a complete worked example on a small concrete instance, detailed enough to verify each step by hand (e.g. a specific list of numbers and target and the exact scheduling instance it produces; or a specific graph and k and the instance it produces).

**Step 4 - Instance generation.** Program that creates random instances of various sizes and characteristics; control size and at least one other parameter; save datasets for reproducibility.

**Step 5 - Algorithm implementations.** The reduction/NP-completeness argument is about the decision version; your solvers should return an actual solution and may do the optimization version. The verifier checks in polynomial time that a candidate satisfies the criteria.
- Exact baseline: brute force (possibly backtracking)
- Improved exact: branch-and-bound, DP, or other pruning
- Heuristic/approximation: greedy, randomization, local search, learning-based, etc., possibly with divide and conquer
- Define a quality metric

**Step 6 - Experimentation.** Run on multiple sizes; measure runtime and quality; produce at least 3 Pareto-frontier points; tune parameters to push the frontier.

**Step 7 - Presentation.** 5-9 minutes: review the problem and why it is NP-complete; the engineering problem; your three algorithms with results and conclusions (how runtime scaled for the two exact algorithms; speed/quality trade-offs of the heuristic). Be ready for live questions.

**Optional - Peer review.** Review another student's report draft for clarity, completeness, correctness; may earn bonus points.

## Deliverables
- Written report (PDF): problem definition; citation of >= 1 recent academic article; proof of NP-completeness; engineering reduction; instance generation; implementation descriptions; experimental results (tables, graphs); description of AI use, if any; reflection.
- Progress journal (appendix)
- Source code + datasets
- Slides (and giving the presentation)

Submit: push report, journal, code, datasets to your Classroom 50 repo. On Canvas, submit the repo link in the textbox and upload the slides as PDF.

## Allowed resources / AI policy
Read papers and textbooks; discuss ideas with classmates, but all code, experiments, and writing must be your own. AI for learning only (concepts, algorithms, theory, understanding papers). **No AI for any submitted code** (suggestions, autocomplete, generated code). All written explanations and proofs must be your own. The report must include a section describing how AI was used in learning, if at all.

## Rubric (100)
| Criterion | Pts |
|---|---|
| Clear, correct decision-problem formulation (precise enough to implement a verifier from it) | 10 |
| Certificate + poly-time verification (pseudocode or step-by-step, with complexity analysis) | 5 |
| Poly-time reduction from 3SAT / subset sum / graph coloring (mapping + correctness argument preserving yes/no) | 5 |
| Cites and summarizes a recent (~10 years) peer-reviewed article | 5 |
| Realistic, specific engineering problem + reduction to the chosen problem | 5 |
| Complete worked example of the reduction on a small instance (actual values, every step) | 5 |
| Random instance generation controlling size + one non-size parameter (density, weight range, tightness) | 5 |
| Brute-force baseline + how runtime scales with size | 10 |
| Improved exact method + empirical scaling vs baseline | 10 |
| Quality metric clearly defined | 5 |
| Heuristic/approximation + speed vs quality trade-off (>= 3 Pareto points) | 10 |
| Repo: code, data, README (step-by-step run instructions, expected runtime per experiment, deliverables checklist). Data backing experiments is required for credit in the other categories too | 5 |
| Automated pytest tests for core logic | 5 |
| Slides clear and helpful | 5 |
| Presentation clarity, pacing, Q&A (inability to answer questions may lose points elsewhere) | 5 |
| Progress journal present, version-controlled, detailed enough to show work throughout | 5 |
