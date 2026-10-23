"""Depth-first search on a directed graph, logged event by event (never hand-typed).

Events (in order):
  {"kind": "start",  "v", "clock", "stack": [...active vertices before v]}
  {"kind": "edge",   "u", "v", "etype": "tree"|"forward"|"back"|"cross"}
  {"kind": "finish", "v", "clock"}
"""


def dfs(graph, roots=None):
    state, pre, post, parent, events = {}, {}, {}, {}, []
    clock = [0]
    stack = []

    def go(v):
        state[v] = "active"
        clock[0] += 1
        pre[v] = clock[0]
        events.append({"kind": "start", "v": v, "clock": clock[0], "stack": list(stack)})
        stack.append(v)
        for w in graph[v]:
            if w not in state:
                events.append({"kind": "edge", "u": v, "v": w, "etype": "tree"})
                parent[w] = v
                go(w)
            else:
                if state[w] == "active":
                    et = "back"
                elif pre[w] > pre[v]:
                    et = "forward"
                else:
                    et = "cross"
                events.append({"kind": "edge", "u": v, "v": w, "etype": et})
        stack.pop()
        state[v] = "finished"
        clock[0] += 1
        post[v] = clock[0]
        events.append({"kind": "finish", "v": v, "clock": clock[0]})

    for r in (roots if roots is not None else list(graph)):
        if r not in state:
            go(r)
    pre_order = sorted(pre, key=pre.get)
    post_order = sorted(post, key=post.get)
    return {"events": events, "pre": pre, "post": post, "parent": parent, "pre_order": pre_order,
            "post_order": post_order}


def forward_ok(graph, order):
    """True if every edge points forward in `order`."""
    idx = {v: i for i, v in enumerate(order)}
    return all(idx[u] < idx[w] for u in graph for w in graph[u])


def backward_edges(graph, order):
    idx = {v: i for i, v in enumerate(order)}
    return [(u, w) for u in graph for w in graph[u] if idx[u] > idx[w]]
