# Greedy Huffman
#
# Part 1: attached as image1 
#
# Part 2: Priority queue alternatives
# 1. Slower but still produces an optimal tree | O(n^2 log n).
#    Where the time goes: Sorting all remaining nodes after each merge.
# 2. Slower but still produces an optimal tree. O(n^2) expected overall.
#    Where the time goes| Quickselect scans remaining nodes after each merge.
# 3. Wrong: the merged node may outweigh two lesser nodes, which should merge first.
#    Counterexample: a=3, b=8, c=10, d=14, e=17, f=42.
#    Third merge: one time sort takes 21+14=35; Huffman takes 14+17=31.
#    Tree costs: one time sort = 213; Huffman = 209.
#
# Part 3: Huffman codec
# 3.1. The tree shares branches, and separate code strings repeat those same bits. 
#       For n unrepeated symbols, the tree plus one leaf id per symbol uses O(n) space
#       separate complete code strings can use O(n^2) space.
#       In a lobsided tree, many symbols end up with codes nearly n bits long. So if you store all n of those code strings you end up with quadratic  space complex.


class Codec:
    def __init__(self, tree, symbol_to_leaf, root):
        self.tree = tree
        self.symbol_to_leaf = symbol_to_leaf
        # my shape is redundant: {"a": "a", "b": "b", "c": "c"}
        self.root = root

    def encode(self, symbols):
        huffman_code = []
        for symbol in symbols:
            leaf_key = self.symbol_to_leaf[symbol]
            current = leaf_key
            symb_code = []
            while (current != self.root):
                parent_key = self.tree.get_parents(current)[0]
                symb_code.append(self.tree.get_edge_data(parent_key, current))
                current = parent_key
            symb_code.reverse()
            huffman_code.extend(symb_code)
        return huffman_code
                
    def decode(self, bits):
        symbols = []
        current = self.root
        for bit in bits:
            for child in self.tree.get_children(current):
                if self.tree.get_edge_data(current, child) == bit:
                    current = child
                    break
            if not self.tree.get_children(current):
                symbols.append(current)
                current = self.root
        return symbols


def huffman_codec(frequencies):
    tree = Graph()
    pq = PriorityQueue()
    symbol_to_leaf = {}
    for symb,occurs in frequencies:
        pq.update(symb, occurs)
        tree.add_node(symb)
        symbol_to_leaf[symb] = symb  
    parent_number_for_label = 1
    while(pq.count() > 1):
        a_min_key = pq.peek_min()
        a_priority = pq.get_priority(a_min_key)
        pq.remove(a_min_key)

        b_min_key =  pq.peek_min()
        b_priority = pq.get_priority(b_min_key)
        pq.remove(b_min_key)

        
        parent_key_name = f"parent {parent_number_for_label}"
        pq.update(parent_key_name, a_priority+b_priority)
        parent_number_for_label += 1

        tree.add_node(parent_key_name, a_priority+b_priority)
        tree.add_edge(parent_key_name, a_min_key, 0)
        tree.add_edge(parent_key_name, b_min_key, 1)

    # at the end the only thing left in the queue is root
    huffman_root_key = pq.peek_min()

    return Codec(tree, symbol_to_leaf, huffman_root_key)



# My Project 2 PriorityQueue
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

# My Project 2 Graph
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

# Professor-provided tests (adapted to call this file directly).
"""Optional tests for Part 3 (Huffman codec).

Huffman's algorithm can break ties either way, so these never check for a particular
bit string -- only for things every correct codec agrees on: decoding undoes encoding,
code lengths when there are no ties, and the total length of an encoded message.

The three functions in this first block are the only place the tests care what you
named things; point them at your own code and the rest just works.
"""
import random

import pytest



def build(frequencies):
    """frequencies: a list of (symbol, frequency) pairs"""
    return huffman_codec(frequencies)


def encode(codec, symbols):
    return list(codec.encode(symbols))


def decode(codec, bits):
    return list(codec.decode(bits))


def message(frequencies):
    """Each symbol repeated as many times as its frequency, in a shuffled order."""
    symbols = [symbol for symbol, count in frequencies for _ in range(count)]
    random.Random(0).shuffle(symbols)
    return symbols


TEXTBOOK = [("a", 45), ("b", 13), ("c", 12), ("d", 16), ("e", 9), ("f", 5)]
SKEWED = [("w", 8), ("x", 1), ("y", 2), ("z", 4)]
TIED = [("a", 1), ("b", 1), ("c", 2), ("d", 2), ("e", 4)]
WORDS = [("the", 7), ("cat", 3), ("sat", 2), ("on", 2), ("mat", 1)]


def test_encode_produces_only_bits():
    assert set(encode(build(TEXTBOOK), "abcdef")) == {0, 1}


@pytest.mark.parametrize("frequencies", [TEXTBOOK, SKEWED, TIED, WORDS])
def test_decode_undoes_encode(frequencies):
    codec = build(frequencies)
    symbols = message(frequencies)
    assert symbols == decode(codec, encode(codec, symbols))


# --- No ties, so every correct tree gives each symbol the same code length --

@pytest.mark.parametrize("frequencies,lengths", [
    (TEXTBOOK, {"a": 1, "b": 3, "c": 3, "d": 3, "e": 4, "f": 4}),
    (SKEWED, {"w": 1, "z": 2, "y": 3, "x": 3}),
    ([("yes", 9), ("no", 1)], {"yes": 1, "no": 1}),
])
def test_code_lengths(frequencies, lengths):
    codec = build(frequencies)
    assert lengths == {symbol: len(encode(codec, [symbol])) for symbol in lengths}


# --- Ties can change the tree, but never the total cost -----------------------

@pytest.mark.parametrize("frequencies,cost", [
    (TEXTBOOK, 224),
    (SKEWED, 25),
    (TIED, 22),
    (WORDS, 31),
])
def test_encoded_message_has_optimal_length(frequencies, cost):
    assert cost == len(encode(build(frequencies), message(frequencies)))


def test_equal_frequencies_give_equal_code_lengths():
    codec = build([(symbol, 1) for symbol in "abcdefgh"])
    assert {3} == {len(encode(codec, [symbol])) for symbol in "abcdefgh"}


# --- Any iterable works, not just lists ----------------------------------------

def test_encode_and_decode_take_any_iterable():
    codec = build(TEXTBOOK)
    bits = encode(codec, "faced")
    assert list("faced") == decode(codec, iter(bits))
    assert bits == encode(codec, (letter for letter in "faced"))


# --- Big inputs: each should finish in about a second -------------------------
# If one takes much longer, look for a hidden O(n) step inside a loop
# (list slicing, string concatenation, a linear search for the lightest node...).

def test_many_symbols():
    frequencies = [(symbol, 1) for symbol in range(2 ** 12)]
    codec = build(frequencies)
    assert {12} == {len(encode(codec, [symbol])) for symbol, _ in frequencies}


def test_long_message():
    codec = build(TEXTBOOK)
    symbols = message(TEXTBOOK) * 2000
    bits = encode(codec, symbols)
    assert 224 * 2000 == len(bits)
    assert symbols == decode(codec, bits)



# My encode/decode tests

def test_my_encode_two_symbols():
    codec = huffman_codec([("a", 1), ("b", 2)])
    assert codec.encode("aba") == [0, 1, 0]


def test_my_decode_two_symbols():
    codec = huffman_codec([("a", 1), ("b", 2)])
    assert codec.decode([1, 0, 0, 1, 0]) == ["b", "a", "a", "b", "a"]


def test_my_three_symbol_branches():
    codec = huffman_codec([("a", 1), ("b", 2), ("c", 4)])
    assert codec.encode("cba") == [1, 0, 1, 0, 0]
    assert codec.decode([1, 0, 1, 0, 0]) == ["c", "b", "a"]

