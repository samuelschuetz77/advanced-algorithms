# Project - Applications of Maxflow

- **Canvas assignment:** https://snow.instructure.com/courses/1254074/assignments/19329090
- **Due:** Fri 11/6/2026, 11:59pm (available until Mon 11/9, 11:59pm)
- **Points:** 15
- **Submission:** Classroom 50 repository; Canvas text box with repo link, screenshot of tests passing, and a couple of sentences on how it went
- **Status (synced 2026-11-12):** **MISSING.** Canvas shows "Missing" and no submission; the availability window closed 11/9. Ask the instructor about a late/makeup submission if still wanted.
- **AI rule:** Do not use AI to help solve this or generate code or suggestions. Use the non-AI-enabled Classwork Profile.

## Task

Choose one problem from Erickson's textbook, Chapter 11, problems 4-19.

1. Describe the problem in your own words (input; what to find or optimize).
2. Describe the reduction: how to build the max flow graph, what nodes and edges represent, the capacities, and which nodes are the source `s` and sink `t`.
3. Write pytests showing how to represent the problem input and the desired output flow graph for the next step. Tests should check nodes, edges, and capacities, not the max flow answer itself.
4. Write a Python function that takes a problem instance and returns a weighted directed graph (using your graph class from earlier in the semester) such that:
   - the graph encodes the appropriate max flow network for that input;
   - the first two nodes returned by `all_nodes()` are the source (`s`) and sink (`t`), respectively.
5. Write a Python function that takes a max flow for your graph and returns the answer to the original (non-flow) problem. Test it on a small instance by building the max flow by hand.

Note: the next project ([Group Project - Reduction From Maxflow to LP](Group%20Project%20-%20Reduction%20From%20Maxflow%20to%20LP.md)) uses your max flow solver to compute the flow you pass to this function.

## Submission

Submit answers and code via the Classroom 50 repository. In the Canvas text box include: a link to the repo, a screenshot of tests passing, and a couple of sentences describing how it went.
