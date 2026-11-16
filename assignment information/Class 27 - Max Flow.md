# Class 27 - Max Flow

- **Canvas page:** https://snow.instructure.com/courses/1254074/pages/class-27-max-flow
- **Synced:** 2026-11-12 (class activity, not graded)

## Reading for Prep

JEA 10.0-10.3: flows, cuts, and max-flow/min-cut.

## Main Points

- The Applications of Max Flow project is assigned today ([Project - Applications of Maxflow](Project%20-%20Applications%20of%20Maxflow.md)): pick a problem from JEA Ch. 11 (problems 4-19), build the flow network for an instance, turn a max flow back into the answer. You don't implement a max-flow algorithm; the next project finds the flow via a linear program.
- **Max flow:** given a directed graph with edge capacities, a source and a sink, what is the most flow from source to sink? A flow assigns an amount to every edge subject to:
  - **Capacity:** each edge carries between 0 and its capacity.
  - **Conservation:** at every vertex other than `s` and `t`, flow in equals flow out.
  - The flow's value is the total flow out of `s` (equals the total into `t`).
- **Max-flow min-cut:** an s-t cut splits vertices into S (containing `s`) and T (containing `t`); its capacity is the total capacity of edges from S to T. Every unit of flow crosses from S to T, so no flow beats any cut, and a flow and a cut of equal value prove each other optimal.
- **Integrality:** with integer capacities, some max flow puts an integer on every edge, and solvers find one. That is why capacity-1 edges can mean yes/no choices.
- Solvers: Ford-Fulkerson pushes flow along augmenting paths until none remain; the next project writes max flow as an LP. For applications, what matters is the model: what vertices, edges and capacities stand for, and how to read the answer off the flow.
- **Bipartite matching as max flow:** one node per item in A, one per item in B, source -> every A-node (cap 1), every B-node -> sink (cap 1), and a cap-1 edge A-item -> B-item exactly when that pairing is legal. Max flow = maximum matching size.

## Pictures (described)

1. A flow network with capacity labels.
2. A flow on it, labeled flow/capacity. Capacity and conservation both check (3 in to `a`, 1 + 2 out; 2 + 1 in to `b`, 3 out). Value = 3 + 2 = 5 out of `s` = 2 + 3 into `t`.
3. A cut proving no flow beats 5: S = {s, a}, T = {b, t}; capacity 2 + 1 + 2 = 5. Flow 5 and cut 5 prove each other optimal.
4. The project example network (based on Fig. 7.4 of Dasgupta, Papadimitriou, Vazirani) with max flow 7. Every S-to-T edge is full (4 + 2 + 1 = 7) and no edge goes T to S, which is what makes flow value equal cut capacity.
5. Bipartite matching: tutors on the left, time slots on the right, edge when a tutor can take a slot, all capacities 1. Max flow is 3, not 4: B, C, D can only take 9am or 11am, and three tutors can't share two slots. The proving cut holds s, B, C, D, 9am, 11am on the S side.
6. Capacities express "how much is allowed." If the center fits two tutors per slot, only the slot -> `t` edges change to capacity 2, and all four tutors fit (e.g. B and C at 9am, A at 10am, D at 11am). Edges into each tutor stay capacity 1 so no tutor takes two slots.

## Practice Quiz

Linked: "Class 27 Practice Quiz" (external quiz link on the page).
