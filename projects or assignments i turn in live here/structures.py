# Name: Samuel 
# Course: Advanced Algorithms 
# Date: 09/07/2026 - 09/11/2026

import pytest


class Graph:
    def __init__(self):
        self.node_data = {}
        self.neighbors = {}
        self.parents = {}
        self.edges = []
    def add_node(self, node, data=None): # this one ony inserts new ones doesnt update
        if node not in self.node_data:
            self.node_data[node] = data
            self.neighbors[node] = {}
            self.parents[node] = []

    def add_edge(self, parent, child, data=None): # this one can update
        self.neighbors[parent][child] = data # neighnors is a dict of dict
        if parent not in self.parents[child]:
            self.parents[child].append(parent)
        self.edges.append((parent,child))

    def add_undirected_edge(self, node1, node2, data=None):
        self.add_edge( node1, node2, data)
        self.add_edge( node2, node1, data)

    def get_node_data(self, node):
        return self.node_data[node]

    def get_edge_data(self, parent, child):
        return self.neighbors[parent][child]

    def get_children(self, parent):
        return list(self.neighbors[parent].keys())

    def get_parents(self, node):
        return self.parents[node]

    def contains_node(self, node):
        return node in self.node_data

    def contains_edge(self, parent, child):
        return child in self.neighbors[parent] 

    def get_nodes(self):
        return self.node_data.keys()

    def get_edges(self):
        return self.edges


class PriorityQueue:
    def __init__(self):
        self.min_heap_array = []
        self.locator_dict = {}
        self.data_dict = {}

    def get_index_from_key(self, key):
        return self.locator_dict.get(key)
    
    def update(self, key, priority, data=None, only_if_less=False):
        if self.contains_key(key):
            index_of = self.get_index_from_key(key)
            if  only_if_less and priority >= self.get_priority(key):
                return #noop

            old_priority = self.get_priority(key)
            self.min_heap_array[index_of] = (key, priority)
            self.data_dict[key] = data

            if priority < old_priority:
                self.sift_up(key, priority)
            else:
                self.sift_down(key)
        else:
            self.min_heap_array.append((key, priority))
            self.locator_dict[key] = len(self.min_heap_array) - 1
            self.data_dict[key] = data
            self.sift_up(key,priority)


            
        
            

    def sift_up(self,key, priority):
        i = self.get_index_from_key(key)
        if i == 0:
            return
        parent_index = (i - 1) // 2
        parent_key = self.min_heap_array[parent_index][0]
        curr = i
        while (curr > 0 and priority < self.get_priority(parent_key)):
            self.swap(curr, parent_index)
            curr = parent_index
            parent_index = (curr - 1) // 2
            parent_key = self.min_heap_array[parent_index][0]

    def sift_down(self, key):
        curr = self.get_index_from_key(key)
        while True:
            left_child = 2 * curr + 1
            right_child = 2 * curr + 2
            smallest = curr

            if left_child < self.count() and self.min_heap_array[left_child][1] < self.min_heap_array[smallest][1]:
                smallest = left_child
            if right_child < self.count() and self.min_heap_array[right_child][1] < self.min_heap_array[smallest][1]:
                smallest = right_child

            if smallest == curr:
                return

            self.swap(curr, smallest)
            curr = smallest

    def swap(self, first_index, second_index):
        self.min_heap_array[first_index], self.min_heap_array[second_index] = self.min_heap_array[second_index], self.min_heap_array[first_index]
        first_key = self.min_heap_array[first_index][0]
        second_key = self.min_heap_array[second_index][0]
        self.locator_dict[first_key] = first_index
        self.locator_dict[second_key] = second_index

    def get_priority(self, key):
        index_of = self.locator_dict[key]
        priority = self.min_heap_array[index_of][1]
        return priority

    def count(self):
        return len(self.min_heap_array)

    def peek_min(self):
        return self.min_heap_array[0][0]

    def get_data(self, key):
        return self.data_dict[key]

    def remove(self, key):
        index_of = self.get_index_from_key(key)
        last_index = self.count() - 1

        self.swap(index_of, last_index)
        self.min_heap_array.pop()
        del self.locator_dict[key]
        del self.data_dict[key]

        if index_of < self.count():
            replacement_key = self.min_heap_array[index_of][0]
            self.sift_up(replacement_key, self.get_priority(replacement_key))
            self.sift_down(replacement_key)
    


        #else perform the update / inintal
    def contains_key(self, key):
        return key in self.locator_dict
    


def prim_mst(graph, edge_weight=None, start_node=None):
    """
    Find minimum spanning tree using Prim's algorithm.
    (Provided by the assignment — copy in as-is, do not modify.)
    """
    if edge_weight is None:
        edge_weight = lambda parent, child: graph.get_edge_data(parent, child)

    if start_node is None:
        start_node = next(iter(graph.get_nodes()))

    mst = Graph()
    pq = PriorityQueue()

    pq.update(start_node, 0, data=None)

    while pq.count() > 0:
        current_node = pq.peek_min()
        parent_node = pq.get_data(current_node)
        pq.remove(current_node)

        if not mst.contains_node(current_node):
            mst.add_node(current_node)
            if parent_node is not None:
                data = graph.get_edge_data(parent_node, current_node)
                mst.add_undirected_edge(parent_node, current_node, data=data)

            for child in graph.get_children(current_node):
                if not mst.contains_node(child):
                    weight = edge_weight(current_node, child)
                    pq.update(child, weight, data=current_node, only_if_less=True)

    return mst


### Graph Tests

def test_new_graph_has_no_nodes():
    graph = Graph()
    assert list(graph.get_nodes()) == []

def test_add_node_then_contains_node():
    graph = Graph()
    graph.add_node("a")
    assert graph.contains_node("a")
    assert not graph.contains_node("b")

def test_add_node_is_idempotent():
    graph = Graph()
    graph.add_node("a", data=1)
    graph.add_node("a", data=2)  # already present -- should not duplicate
    assert list(graph.get_nodes()) == ["a"]

def test_get_node_data():
    graph = Graph()
    graph.add_node("a", data="hello")
    assert graph.get_node_data("a") == "hello"

def test_add_edge_then_contains_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.contains_edge("a", "b")
    assert not graph.contains_edge("b", "a")  # directed, so the reverse shouldn't exist

def test_get_edge_data():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b", data=5)
    assert graph.get_edge_data("a", "b") == 5

def test_add_undirected_edge_creates_both_directions():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_undirected_edge("a", "b", data=7)
    assert graph.contains_edge("a", "b")
    assert graph.contains_edge("b", "a")
    assert graph.get_edge_data("a", "b") == 7
    assert graph.get_edge_data("b", "a") == 7

def test_get_children():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert set(graph.get_children("a")) == {"b", "c"}

def test_get_parents():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("c", "b")
    assert set(graph.get_parents("b")) == {"a", "c"}

def test_get_nodes_preserves_insertion_order():
    graph = Graph()
    graph.add_node("c")
    graph.add_node("a")
    graph.add_node("b")
    assert list(graph.get_nodes()) == ["c", "a", "b"]

def test_get_edges_preserves_insertion_order():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_node("c")
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    assert list(graph.get_edges()) == [("a", "b"), ("a", "c")]

def test_contains_node_false_for_absent_node():
    graph = Graph()
    assert not graph.contains_node("nonexistent")

def test_contains_edge_false_for_absent_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    assert not graph.contains_edge("a", "b")

### Priority Queue Tests

def test_new_priority_queue_has_count_zero():
    pq = PriorityQueue()
    assert pq.count() == 0

def test_update_adds_new_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_peek_min_returns_smallest_priority_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.update("c", 9)
    assert pq.peek_min() == "b"

def test_peek_min_does_not_remove():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.peek_min()
    assert pq.count() == 1
    assert pq.contains_key("a")

def test_get_data_returns_associated_data():
    pq = PriorityQueue()
    pq.update("a", 5, data="hello")
    assert pq.get_data("a") == "hello"

def test_for_get_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("a", 2)
    assert pq.get_priority("a") == 2

def test_update_existing_key_changes_priority_without_duplicating():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 1)
    pq.update("a", 0)  # "a" should now be the minimum
    assert pq.peek_min() == "a"
    assert pq.count() == 2  # still just two keys, not duplicated

def test_update_only_if_less_ignores_higher_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("a", 10, only_if_less=True)  # 10 is not less than 5 -- should be ignored
    pq.update("b", 7)
    assert pq.peek_min() == "a"  # "a"'s priority should still be 5, which beats 7

def test_update_only_if_less_applies_lower_priority():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 3)
    pq.update("a", 1, only_if_less=True)  # 1 is less than 5 -- should apply
    assert pq.peek_min() == "a"

def test_update_only_if_less_on_new_key_still_adds_it():
    pq = PriorityQueue()
    pq.update("a", 5, only_if_less=True)  # "a" wasn't present yet -- should still be added
    assert pq.contains_key("a")
    assert pq.count() == 1

def test_remove_deletes_key():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.update("b", 2)
    pq.remove("b")
    assert not pq.contains_key("b")
    assert pq.count() == 1
    assert pq.peek_min() == "a"

def test_remove_then_reinsert():
    pq = PriorityQueue()
    pq.update("a", 5)
    pq.remove("a")
    pq.update("a", 1)
    assert pq.contains_key("a")
    assert pq.peek_min() == "a"

def test_contains_key_false_for_absent_key():
    pq = PriorityQueue()
    assert not pq.contains_key("nonexistent")

def test_many_updates_and_removes_maintain_min_heap_order():
    pq = PriorityQueue()
    for key, priority in [("a", 5), ("b", 2), ("c", 8), ("d", 1), ("e", 9), ("f", 3)]:
        pq.update(key, priority)
    order = []
    while pq.count() > 0:
        m = pq.peek_min()
        order.append(m)
        pq.remove(m)
    assert order == ["d", "b", "f", "a", "c", "e"]

# Prim's tests 

def test_prim_work_good():
    graph = Graph()
    for node in ["a", "b", "c", "d"]:
        graph.add_node(node)

    graph.add_undirected_edge("a", "b", data=1)
    graph.add_undirected_edge("a", "c", data=4)
    graph.add_undirected_edge("b", "c", data=2)
    graph.add_undirected_edge("b", "d", data=5)
    graph.add_undirected_edge("c", "d", data=1)

    mst = prim_mst(graph, start_node="a")

    assert set(mst.get_nodes()) == {"a", "b", "c", "d"}
    assert mst.contains_edge("a", "b")
    assert mst.contains_edge("b", "c")
    assert mst.contains_edge("c", "d")
    assert len(mst.get_edges()) == 6
