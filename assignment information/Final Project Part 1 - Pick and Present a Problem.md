# Final Project Part 1 - Pick and Present a Problem

- **Type:** Assignment (Canvas), presentation slides
- **Due:** Fri 10/2/2026, 11:59pm (available until Fri 10/2/2026, 11:59pm)
- **Points:** 15
- **Submission:** Upload PDF slides (Canvas offers Text / Upload); unlimited attempts
- **Canvas link:** https://snow.instructure.com/courses/1254074/assignments/19231790

## Details

Confirmed live and published in Canvas on 2026-09-28 via Chrome pull-down.

This is Part 1 of the Final Project. You are choosing your problem and giving an initial presentation. You will expand on this for the complete final project.

Pick an NP-complete problem from the Wikipedia list (yours will need to be different from everyone else in the class) and:

- Present your chosen problem to the class (make sure it is clear why the problem is given the name that it is given).
- In your presentation, include at least two examples of inputs and the corresponding solutions to help illustrate the problem.
- Demonstrate how you can verify that a candidate solution is correct.
- Describe the brute-force solution: what exactly is it enumerating, how many candidates is that as a function of the input size, and what does it cost to check each one.

By the end of your (up to 5 minute) presentation, the class should be able to:

- create an instance of the problem
- verify that a particular solution is correct
- have a good intuition about why the problem has the name that it does
- say what the obvious exhaustive search would have to try, and why that is too many

Ideally, you can capture an instance of the problem and the solution each as a Python object, and use these to create a few example test cases (not required for the presentation, but it may help ensure a sufficiently clear idea of what the problem actually is).

### Choosing Your Problem

Problems are first come, first served: post the one you want in the class discussion, and the first person to call a given problem gets it.

Four things to weigh:

1. **It should matter to you.** Pick a problem worth solving for some real-world problem that interests you. You will be living with it until December, and you will use it to solve a real problem.
2. **You have to be able to reduce to it.** For the final project you will prove your problem NP-hard by reducing from 3SAT, subset sum, or graph coloring, so be confident you can picture at least one of those turning into your problem. Numbers, weights, capacities, and schedules usually take subset sum naturally; graphs, conflicts, and mutual exclusion usually take graph coloring; problems about constraints being simultaneously satisfiable are often easiest straight from 3SAT. Class will later work through circuit SAT to 3SAT, and 3SAT to both subset sum and graph coloring, so your half completes a chain back to circuit satisfiability. You may learn and explain a reduction someone else discovered rather than inventing your own.
3. **Decision for the proof, search for the code.** The reduction is about the decision version ("is there a solution that satisfies X?", where X might include a budget to stay under), but your solvers should return an actual solution and may take on the optimization version too (find the solution that maximizes Y). You will also write a polynomial-time verifier that checks a candidate really satisfies the criteria.
4. **Quality has to be measurable.** Later you will trade solution quality against speed with an approximate solver, so you need a sensible way to say how good a non-perfect answer is.

If you cannot picture any of the three reductions turning into your problem, bring it to the professor before committing.

## Rubric (15 pts)

| Criterion | Points |
|---|---|
| Problem is well described | 6 |
| Two examples of input and their corresponding output to help illustrate the problem | 3 |
| Demonstration of how a candidate solution can be verified to be correct | 3 |
| Brute-force solution, with the number of candidates it must try as a function of input size | 3 |

## Status

Submitted 2026-10-02 at 3:00pm; ungraded (verified on Canvas Grades 2026-10-03). Presentation created 2026-10-02. Topic: general uncapacitated facility location, using sensor stations. Five slides with speaker notes, two examples, verification, and exhaustive search. Topic reservation in the class discussion has not been verified.

- Google Slides: https://docs.google.com/presentation/d/18wVuiJjEodtnxjd9sylOtgpEox4VXuGjMel8VpUhClI/edit
- Turn-in PDF: `../projects or assignments i turn in live here/Facility Location Presentation/Optimal Facility Location.pdf`

