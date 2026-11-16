# Quiz - Graphs

- Canvas assignment: https://snow.instructure.com/courses/1254074/assignments/19336520
- Canvas quiz: https://snow.instructure.com/courses/1254074/quizzes/4933614
- Due: Fri 11/6/2026, 11:20am Mountain; available 11:10–11:30am. About 10 minutes in class.
- 14 points, 8 questions. Canvas showed **missing/locked** on 11/11/2026; the student has asked the instructor about making it up.
- Closed-everything. No notes during the quiz; do not save or screenshot quiz questions. This file records only the overview and study sources.

## Instructor's stated scope

Graph representations, breadth-first search, shortest paths, strongly connected components, and max flow basics.

## Study map and likely skills

These are **inferences for preparation**, not a list of actual quiz questions.

| Area | Source | Practice target |
|---|---|---|
| Graph representations | JEA §5.4; Project 2 Graph ADT | Read directed vs undirected edges, adjacency lists vs matrices; compare space and edge lookup; count each undirected edge in both neighbor lists. |
| BFS | JEA §5.6 and §8.4; Class 21's contrast with DFS | Trace a FIFO queue and discovery layers. In an unweighted graph, the first discovery gives a minimum-edge path; distinguish this from weighted shortest paths. |
| Shortest paths | JEA §8.3–8.7 and §9.5–9.6; course schedule for 10/30 and 11/2; Exam 1 scope | Relax an edge, track tentative distances/predecessors, and choose a method by edge-weight assumptions: BFS for unweighted, DAG order for DAGs, Dijkstra for nonnegative weights, Bellman–Ford if negative edges are possible. All-pairs DP may also be relevant. |
| Strongly connected components | JEA §6.5–6.6; Group Project - Strongly Connected Components | Identify vertices that reach one another, contract components into a DAG, and trace the project's two-pass Kosaraju procedure: finish order in G, reverse edges, DFS in decreasing finish order. |
| Max flow basics | JEA §10.0–10.3; course schedule for 11/4; Project - Applications of Maxflow is listed in Canvas Grades | Check capacity and flow conservation, find residual capacity/augmenting paths, and relate a flow to an s–t cut. The project spec was not saved locally, so this portion rests chiefly on the assigned reading and quiz overview. |

## Priority

Start with representation and BFS traces, then shortest-path relaxations and algorithm assumptions, SCC condensation/Kosaraju, and finally a small max-flow residual-network example. The overview gives no topic-by-topic point breakdown.

## Compact review checks

1. **Representations:** For a graph with V vertices and E edges, a standard adjacency list uses O(V + E) space and lets you list a vertex's neighbors in time proportional to its degree. A matrix uses O(V²) space and answers a particular edge-existence query in O(1), while scanning a row for all neighbors takes O(V). In an undirected adjacency list, each edge appears at both endpoints; a directed edge appears only in its source's outgoing list.
2. **BFS:** Mark a vertex when enqueuing it, save its parent, and process the FIFO queue. Its layers count edges from the source. The parent path is a shortest path by edge count in an unweighted graph. DFS order does not guarantee this.
3. **Shortest paths:** A relaxation of u→v with weight w improves d[v] when d[u] + w < d[v], and records u as predecessor. A DAG allows processing in topological order even with negative weights; Dijkstra requires nonnegative weights; Bellman–Ford handles negative edges and can detect a reachable negative cycle. Negative cycles can make a finite shortest path undefined.
4. **SCCs:** Vertices share an SCC exactly when each can reach the other. Replacing each SCC by one meta-vertex gives a DAG: a cycle among distinct meta-vertices would mean they were one SCC. For the assigned Kosaraju variant, compute finish order on G, reverse G, then start DFS on the reversal in decreasing original finish order.
5. **Max flow:** Each edge flow lies between zero and capacity, and inflow equals outflow at nonterminal vertices. A residual edge records room to send more flow forward or cancel flow backward. An augmenting s–t residual path can increase total flow by its smallest residual capacity. Any s–t cut bounds flow from above by its crossing capacity; equality certifies optimality.

Practice these checks on a fresh small graph, not by memorizing these sentences. Record the resulting explanations in `../learning log.md` only after doing the traces.
