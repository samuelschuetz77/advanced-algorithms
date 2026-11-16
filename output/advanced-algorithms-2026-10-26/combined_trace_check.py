"""Check the combined primer's figure, path counts, and undirected example."""
import json
from pathlib import Path
from trace_check import CLASS_GRAPH

# Figure 6.4, including non-tree edges, ordered to match its illustrated traversal.
FIGURE = {
    'a': ['b'], 'b': ['f'], 'c': ['h'], 'd': ['c'],
    'e': ['i', 'f'], 'f': ['g', 'l'], 'g': ['c', 'a', 'k'],
    'h': ['d', 'l'], 'i': ['n'], 'j': ['m', 'k'], 'k': ['h', 'l'],
    'l': ['o', 'p'], 'm': ['i'], 'n': ['j', 'o'], 'o': ['k'], 'p': [],
}


def dfs(graph, starts):
    pre, post, parent = {}, {}, {}
    events = []

    def visit(vertex):
        events.append(['enter', vertex])
        pre[vertex] = len(events)
        for neighbor in graph[vertex]:
            if neighbor not in pre:
                parent[neighbor] = vertex
                visit(neighbor)
        events.append(['leave', vertex])
        post[vertex] = len(events)

    for vertex in starts:
        if vertex not in pre:
            parent[vertex] = None
            visit(vertex)
    return dict(pre=pre, post=post, parent=parent, events=events)


def path_counts(graph, order):
    to = dict.fromkeys(graph, 0)
    onward = dict.fromkeys(graph, 0)
    to[order[0]] = 1
    onward[order[-1]] = 1
    for vertex in order:
        for neighbor in graph[vertex]:
            to[neighbor] += to[vertex]
    for vertex in reversed(order):
        for neighbor in graph[vertex]:
            onward[vertex] += onward[neighbor]
    return dict(to=to, onward=onward,
                through={v: to[v] * onward[v] for v in graph})


if __name__ == '__main__':
    figure = dfs(FIGURE, FIGURE)
    assert ''.join(sorted(figure['pre'], key=figure['pre'].get)) == 'abfgchdlokpeinjm'
    assert ''.join(sorted(figure['post'], key=figure['post'].get)) == 'dkoplhcgfbamjnie'
    assert [(figure['pre'][v], figure['post'][v]) for v in ('h', 'd', 'l')] == [(6, 17), (7, 8), (9, 16)]
    dag = {'ABC': ['DE', 'FG'], 'DE': ['FG'], 'FG': []}
    counts = path_counts(dag, list(dag))
    assert list(counts['to'].values()) == [1, 1, 2]
    assert list(counts['onward'].values()) == [2, 1, 1]
    no_shortcut = path_counts({'ABC': ['DE'], 'DE': ['FG'], 'FG': []}, list(dag))
    assert no_shortcut['through']['DE'] == no_shortcut['to']['FG'] == 1
    undirected = {v: set() for v in CLASS_GRAPH}
    for vertex, neighbors in CLASS_GRAPH.items():
        for neighbor in neighbors:
            undirected[vertex].add(neighbor)
            undirected[neighbor].add(vertex)
    undirected = {v: sorted(ns) for v, ns in undirected.items()}
    root_f = dfs(undirected, ['f'])
    children = [v for v, parent in root_f['parent'].items() if parent == 'f']
    assert children == ['b', 'g']
    without_f = {v: [n for n in ns if n != 'f'] for v, ns in undirected.items() if v != 'f'}
    assert set(dfs(without_f, ['b'])['pre']) == set('abcde')
    assert without_f['g'] == []
    output = dict(figure=figure, component_dag=counts, no_shortcut=no_shortcut,
                  undirected=undirected, root_f=root_f)
    Path(__file__).with_name('combined-trace.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
    print('PASS: Figure 6.4 orders and times, DAG counts, root children, and removal connectivity.')
