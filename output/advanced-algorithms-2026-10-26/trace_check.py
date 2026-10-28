"""Independent teaching trace; does not import or modify coursework.

Run with Python to regenerate trace.json and verify against mutual reachability.
The eleven solid edges reproduce the October 26 embedded drawing.
One explicitly marked teaching edge meets the standing 12-edge video minimum.
"""
import json
from pathlib import Path

CLASS_GRAPH = {
    'a': ['b', 'e'], 'b': ['c', 'f'], 'c': ['a', 'd'],
    'd': ['e'], 'e': ['d', 'f'], 'f': ['g'], 'g': ['f'],
}
GRAPH = {vertex: list(neighbors) for vertex, neighbors in CLASS_GRAPH.items()}
GRAPH['a'].append('c')
EXTRA_EDGES = [('a', 'c')]


def reverse_graph(graph):
    reverse = {}
    for vertex in graph:
        reverse[vertex] = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            reverse[neighbor].append(vertex)
    return reverse


def finish_order(graph):
    visited = set()
    finished = []
    events = []

    def visit(vertex):
        visited.add(vertex)
        events.append(['enter', vertex, sorted(visited), list(finished)])
        for neighbor in graph[vertex]:
            events.append(['edge', vertex, neighbor, neighbor in visited])
            if neighbor not in visited:
                visit(neighbor)
        finished.append(vertex)
        events.append(['finish', vertex, sorted(visited), list(finished)])

    for vertex in graph:
        if vertex not in visited:
            visit(vertex)
    return finished, events


def collect_components(graph, order):
    assigned = set()
    components = []
    events = []

    def collect(vertex, component):
        assigned.add(vertex)
        component.append(vertex)
        events.append(['collect', vertex, list(component), sorted(assigned)])
        for neighbor in graph[vertex]:
            if neighbor not in assigned:
                collect(neighbor, component)
            else:
                events.append(['skip_edge', vertex, neighbor])

    for vertex in order:
        if vertex not in assigned:
            component = []
            collect(vertex, component)
            components.append(component)
        else:
            events.append(['skip_root', vertex])
    return components, events


def reachable(graph, start):
    reached = set()
    pending = [start]
    while pending:
        vertex = pending.pop()
        if vertex in reached:
            continue
        reached.add(vertex)
        pending.extend(graph[vertex])
    return reached


def verify(graph):
    reverse = reverse_graph(graph)
    finished, first_events = finish_order(reverse)
    order = list(reversed(finished))
    components, second_events = collect_components(graph, order)
    expected = set()
    for vertex in graph:
        expected.add(frozenset(reachable(graph, vertex) & reachable(reverse, vertex)))
    actual = set(map(frozenset, components))
    assert actual == expected
    assert sum(map(len, components)) == len(graph)
    labels = {}
    for index, component in enumerate(components):
        for vertex in component:
            labels[vertex] = index
    meta_edges = set()
    for vertex in graph:
        for neighbor in graph[vertex]:
            if labels[vertex] != labels[neighbor]:
                meta_edges.add((labels[vertex], labels[neighbor]))
                assert labels[vertex] > labels[neighbor], 'Expected sink-first order'
    return {'graph': graph, 'reverse': reverse, 'finished': finished,
            'pop_order': order, 'components': components,
            'meta_edges_sink_first_indices': sorted(meta_edges),
            'first_pass': first_events, 'second_pass': second_events,
            'from_d_original': sorted(reachable(graph, 'd')) if 'd' in graph else []}


if __name__ == '__main__':
    original = verify(CLASS_GRAPH)
    expanded = verify(GRAPH)
    assert set(map(frozenset, original['components'])) == set(map(frozenset, expanded['components']))
    assert len(GRAPH) == 7 and sum(map(len, GRAPH.values())) == 12
    # Meaningful boundaries: isolated vertex, self-loop, disconnected cycle, empty graph.
    for graph in ({}, {'x': []}, {'x': ['x']}, {'x': ['y'], 'y': ['x'], 'z': []}):
        verify(graph)
    output = {'class_drawing': original, 'video': expanded, 'added_edges': EXTRA_EDGES}
    Path(__file__).with_name('trace.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
    print(json.dumps({key: expanded[key] for key in ('finished', 'pop_order', 'components', 'from_d_original')}, indent=2))
    print('PASS: both drawings agree with independent mutual-reachability checks; boundary cases pass.')
