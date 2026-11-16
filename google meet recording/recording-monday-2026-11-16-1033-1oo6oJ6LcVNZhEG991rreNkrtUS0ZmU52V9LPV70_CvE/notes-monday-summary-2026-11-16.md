# Archive metadata

Source: https://docs.google.com/document/d/1oo6oJ6LcVNZhEG991rreNkrtUS0ZmU52V9LPV70_CvE
Meeting start: 2026-11-16 10:33 MST (America/Denver), verified from document title and source date metadata.
Classification: Advanced Algorithms lecture (NP-hardness reductions, circuit satisfiability, decision-to-search, complexity theory and integer linear programming).
Duration evidence: transcript terminal marker 00:50:17, not independently verified recording duration.
Complete available source text follows, including timestamps and machine-generated caveats. Embedded images are linked to original tabs, not downloaded. Source sharing unchanged.

---

## Source tab: Notes

https://docs.google.com/document/d/1oo6oJ6LcVNZhEG991rreNkrtUS0ZmU52V9LPV70_CvE/edit?tab=t.mqw7quywfhzv

Nov 16, 2026
Untitled Meeting
Meeting records [Transcript](https://docs.google.com/document/d/1oo6oJ6LcVNZhEG991rreNkrtUS0ZmU52V9LPV70_CvE/edit?usp=drive_web&tab=t.mddedr2dzz3g) 


Summary
Project reduction assignments and student problem sharing preceded core computer science problem discussions and complexity theory definitions.Reduction Assignments And SharingStudents utilized class time to work on problem reductions and reduce one of three problems to an NP-hard problem. Sharing individual problems helped participants identify potential similarities to solve their own challenges.Complexity Theory And SolversCircuit satisfiability established that any NP problem translates into a circuit. Decision solvers converted into search and optimization solvers by testing constraints and hardcoding variables.Turing Machines And ProgrammingDeterministic and nondeterministic Turing machines defined polynomial runtime versus verifiable problems. Integer linear programming introduced constraints to determine if solutions still exist.


Next steps
Develop Reductions: Develop the reduction for your final project to prove that your chosen problem is NP-hard. Ensure the reduction demonstrates that the problem is verifiable in polynomial time and explains how to reduce the relevant baseline problems to your own.


Details
Reduction Assignment and Final Project Work: Students are encouraged to use class time and outside-the-class hours to work on problem reductions, specifically figuring out how to reduce one of the three problems to an NP-hard problem (00:00:01). The problems chosen for the list are structured so that reductions would theoretically work in both directions (00:01:49).

---

Student Problem Sharing and Overlaps: Going around the room to share individual student problems is useful because it helps participants see potential similarities, allowing them to potentially use another person's reduction steps to help learn or solve their own (00:02:24).

---

Traveling Salesperson Problem and Hamiltonian Cycle: The Traveling Salesperson Problem and the Hamiltonian cycle are very similar, with the main difference being that the Traveling Salesperson Problem takes distance or a budget into account as a cycle, whereas the Hamiltonian cycle connects all edges without caring about distance (00:02:42) (00:07:47).

---

N-Queens Completed Problem: The problem of n-queens completed involves determining if an arrangement of queens on an n by n board can be completed so that no queens are attacking each other (00:04:56). While a board with only one queen is easy to solve due to an existing pattern, randomly placed queens on boards of size five or ten are much harder to evaluate (00:05:30).

---

Optimal Facility Location Problem: The optimal facility location problem involves deciding whether to place a facility at a certain location while minimizing or maximizing costs to service possible locations (00:06:41).

---

Nonogram Puzzle Problem: The nonogram puzzle problem, named after one of its inventors, involves a rows-by-columns grid and clues indicating the length of each cluster of filled cells in each row and column to determine if a valid solution exists (00:13:33). Some sets of row and column clues may have more than one valid solution or no valid solution at all (00:15:00).

---

Circuit Satisfiability and NP-Hardness: Circuit satisfiability, known as circuit sat, asks if there is any input that can turn on a boolean circuit and make the verifier happy (00:20:56) (00:24:54). Circuit sat is NP-hard, meaning that if a solver exists for an NP-hard problem, any NP problem can be solved in a polynomial number of calls (00:22:58). Circuit sat was discovered to be the first NP-hard problem because any NP problem has a verifier that can be translated into a circuit (00:27:03).

---

Converting Decision Solvers to Search and Optimization Solvers: A decision solver that answers yes or no can be used to find a search solution by hardcoding parts of the answer one variable at a time in a linear number of calls (00:28:27). Similarly, optimization problems like finding the smallest Hamiltonian path can be solved using a decision solver by introducing bounds or budgets and testing yes or no questions for given constraints (00:29:11) (00:30:07).

---

Definitions of P and NP: P represents problems that can be solved in polynomial runtime, expressed as big O of N to some power $K$ (00:32:04). NP stands for problems verifiable by a nondeterministic Turing machine, which is a theoretical machine with infinite tape memory, a finite state stored on a sticky note, and a lookup table that dictates the next state, writing action, and movement direction based on the current input symbol (00:32:56).

---

Deterministic Versus Nondeterministic Turing Machines: A deterministic Turing machine prescribes at most one action for any given situation, whereas a nondeterministic Turing machine allows a set of rules to prescribe multiple possible actions (00:37:10). A nondeterministic Turing machine accepts an input if at least one possible sequence of steps leads to an accepting state (00:39:03).

---

Integer Linear Programming and Constraints: Linear programming involves maximizing or minimizing an objective subject to constraints, and adding constraints such as requiring all numbers to be integers changes the problem to determine if a solution still exists (00:47:21).


You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes
How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

