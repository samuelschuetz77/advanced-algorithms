# Class 23 - Strongly Connected Components

- **Canvas page:** https://snow.instructure.com/courses/1254074/pages/class-23-strongly-connected-components
- **Synced:** 2026-11-12 (class activity, not graded)

## Reading for Prep

JEA 6.5-6.6: strong connectivity and strongly connected components.

## Main Points

- Project 7 (Strongly Connected Components) is assigned today: implement an algorithm that partitions a directed graph's vertices into strongly connected components (SCCs), the maximal sets where every vertex can reach every other. (Canvas name: [Group Project - Strongly Connected Components](Group%20Project%20-%20Strongly%20Connected%20Components.md).)
- Finding SCCs (Kosaraju's or Tarjan's) builds on DFS and topological sort from Classes 21-22: applied twice (graph, then reverse graph) or with extra bookkeeping in one pass.
- Collapsing each SCC into a single super-vertex turns any directed graph into a DAG, so DAG-only algorithms (like topological sort) apply to general directed graphs.
- Meta-idea: SCCs are a concrete example of extracting structure (mutual reachability) as preprocessing before solving the problem you care about.

## Pictures (described)

1. A directed graph with SCCs boxed. Inside a box every vertex reaches every other; between boxes edges go one way. A component can be a single vertex (e.g. `h`, on no cycle).
2. The same graph with every edge reversed. Components are identical (a cycle backward is still a cycle) but inter-component edges flip. Kosaraju's second pass relies on this.
3. Collapse each component to one vertex and you get a DAG. The topological order need not be unique (e.g. SCC 2 and SCC 4 in either order, both after SCC 1 and before SCC 3).

## Practice Quiz

Linked: "Class 23 Practice Quiz" (external quiz link on the page).
