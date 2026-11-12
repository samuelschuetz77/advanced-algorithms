"""Six ways to compute maximum flow in a directed capacity graph.

The six complete functions take ``capacity[u][v]`` as the capacity of edge
u -> v and return the maximum flow value. Capacities must be nonnegative.
The scaling version requires integer capacities. None of the six changes
the input. The unfinished ``max_flow`` draft at the bottom is yours to finish.

Study the first two versions: Edmonds-Karp BFS first, then iterative stack
DFS. Both use the same residual graph and augmentation helpers. The other
four versions are included for comparison, but the Koans focus on the first two.
"""

from collections import deque
from heapq import heappop, heappush
from itertools import count


# 1. Recommended: Edmonds-Karp breadth-first search.
def max_flow_bfs(capacity, source, sink):
    """Find the maximum flow by repeatedly using a BFS path.

    Start with zero flow and a residual graph of remaining capacity. BFS
    finds a source-to-sink path with the fewest edges, and ``parent`` records
    how to trace it backward. Send the path's bottleneck amount with
    ``_augment``, then search again. When BFS cannot reach the sink, no more
    flow can be sent; this version has an O(V E^2) time guarantee.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    total = 0

    while True:
        parent = {source: None}
        queue = deque([source])
        while queue and sink not in parent:
            u = queue.popleft()
            for v, room in residual[u].items():
                if room > 0 and v not in parent:
                    parent[v] = u
                    queue.append(v)

        if sink not in parent:
            return total
        total += _augment(residual, parent, source, sink)


# 2. Simple comparison: iterative Ford-Fulkerson depth-first search.
def max_flow_dfs_stack(capacity, source, sink):
    """Use the same residual updates, but find each path with a stack.

    A stack explores the newest discovered vertex first, so this search can
    choose a different path from BFS. Once it reaches the sink, it uses the
    same ``_augment`` helper and repeats. Integer capacities guarantee
    termination, but poor DFS path choices can take many augmentations;
    this version lacks Edmonds-Karp's O(V E^2) guarantee.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    total = 0

    while True:
        parent = {source: None}
        stack = [source]
        while stack and sink not in parent:
            u = stack.pop()
            for v, room in residual[u].items():
                if room > 0 and v not in parent:
                    parent[v] = u
                    stack.append(v)

        if sink not in parent:
            return total
        total += _augment(residual, parent, source, sink)


# Shared residual-graph and path-update helpers used above and below.
def _residual_graph(capacity):
    """Copy the forward edges, then add any missing reverse edges."""
    residual = {}
    for u in capacity:
        residual[u] = {}
        for v in capacity[u]:
            residual[u][v] = capacity[u][v]

    for u in capacity:
        for v in capacity[u]:
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0
    return residual


def _augment(residual, parent, source, sink):
    """Send as much flow as possible along a path recorded by parent."""
    amount = float("inf")
    v = sink
    while v != source:
        u = parent[v]
        amount = min(amount, residual[u][v])
        v = u

    v = sink
    while v != source:
        u = parent[v]
        residual[u][v] -= amount
        residual[v][u] += amount
        v = u
    return amount


# 3. Recursive DFS: the same search idea using Python's call stack.
def max_flow_dfs_recursive(capacity, source, sink):
    """Replace the explicit DFS stack with recursive calls.

    The recursive ``search`` records parents while exploring one branch at
    a time and returns True on reaching the sink. Augmentation is otherwise
    the same as in the first two versions. This is compact for small graphs,
    but a long path can exceed Python's recursion limit.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    total = 0

    def search(u, parent):
        if u == sink:
            return True
        for v, room in residual[u].items():
            if room > 0 and v not in parent:
                parent[v] = u
                if search(v, parent):
                    return True
        return False

    while True:
        parent = {source: None}
        if not search(source, parent):
            return total
        total += _augment(residual, parent, source, sink)


# 4. Widest path: prefer a larger bottleneck each round.
def max_flow_widest_path(capacity, source, sink):
    """Prefer the available path with the largest bottleneck.

    A heap prioritizes the widest known route to each vertex. Extending a
    route takes the minimum of its width and the next edge's residual room.
    This can send more flow per augmentation than BFS or DFS, but choosing
    the route requires more bookkeeping. The residual update is unchanged.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    total = 0
    sequence = count()  # Avoid comparing node labels in heap ties.

    while True:
        parent = {source: None}
        best = {source: float("inf")}
        settled = set()
        heap = [(-best[source], next(sequence), source)]

        while heap:
            negative_width, _, u = heappop(heap)
            if u in settled:
                continue
            settled.add(u)
            if u == sink:
                break
            for v, room in residual[u].items():
                if room <= 0 or v in settled:
                    continue
                width = min(-negative_width, room)
                if width > best.get(v, 0):
                    best[v] = width
                    parent[v] = u
                    heappush(heap, (-width, next(sequence), v))

        if sink not in settled:
            return total
        total += _augment(residual, parent, source, sink)


# 5. Capacity scaling: use large residual edges before small ones.
def max_flow_scaling(capacity, source, sink):
    """Use BFS while temporarily ignoring small residual edges.

    Begin at the largest power-of-two threshold no greater than any input
    capacity. Find and augment every path whose edges all meet that
    threshold, then halve it. At threshold one, every positive integer
    residual edge is eligible. This version requires integer capacities.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    values = [c for edges in capacity.values() for c in edges.values()]
    if any(not isinstance(c, int) for c in values):
        raise TypeError("capacity scaling requires integer capacities")
    largest = max(values, default=0)
    scale = 1
    while scale * 2 <= largest:
        scale *= 2
    total = 0

    while scale >= 1:
        while True:
            parent = {source: None}
            queue = deque([source])
            while queue and sink not in parent:
                u = queue.popleft()
                for v, room in residual[u].items():
                    if room >= scale and v not in parent:
                        parent[v] = u
                        queue.append(v)

            if sink not in parent:
                break
            total += _augment(residual, parent, source, sink)
        scale //= 2
    return total


# 6. Dinic: send several paths through each BFS level graph.
def max_flow_dinic(capacity, source, sink):
    """Send many shortest-path augmentations in each BFS phase.

    BFS assigns distance levels in the current residual graph. A DFS then
    sends flow only to the next level until those routes are blocked. After
    that, rebuild levels and repeat. This organizes several augmentations
    per phase, unlike Edmonds-Karp's one BFS path per round.
    """
    if source == sink:
        return 0
    residual = _residual_graph(capacity)
    neighbors = {u: list(residual[u]) for u in residual}
    total = 0

    while True:
        level = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in neighbors[u]:
                if residual[u][v] > 0 and v not in level:
                    level[v] = level[u] + 1
                    queue.append(v)
        if sink not in level:
            return total

        next_edge = {u: 0 for u in residual}

        def send(u, available):
            if u == sink:
                return available
            while next_edge[u] < len(neighbors[u]):
                v = neighbors[u][next_edge[u]]
                if residual[u][v] > 0 and level.get(v) == level[u] + 1:
                    pushed = send(v, min(available, residual[u][v]))
                    if pushed > 0:
                        residual[u][v] -= pushed
                        residual[v][u] += pushed
                        return pushed
                next_edge[u] += 1
            return 0

        while True:
            pushed = send(source, float("inf"))
            if pushed == 0:
                break
            total += pushed


# Your unfinished draft is kept here so you can continue it separately.
def max_flow(capacity, source, sink):
    residual = {u: edges.copy() for u, edges in capacity.items()}
    # TODO: add reverse edges, find augmenting paths, and return the total.
