# Greedy Huffman

- Canvas link: https://snow.instructure.com/courses/1254074/assignments/19257409
- Due: Thu 10/15/2026, 11:59pm Mountain
- Points: 28
- Status: Published and available; not submitted as of 2026-10-12.
- Available until: Fri 10/16/2026, 11:59pm Mountain.
- Submission: Canvas file upload; PDF, JPG, JPEG, PNG, PY permitted; unlimited attempts.
- Turn-in path: `../projects or assignments i turn in live here/` (specific files not identified).
- Last synced: 2026-10-12 via ChatGPT in Chrome; full assignment, rubric, and expanded optional tests captured.

## Required foundations

Reuse Project 2's `Graph` class for the tree, storing bits as data on parent-to-child edges, and the `PriorityQueue` locator heap to choose the lightest nodes. Use the non-AI-enabled [Classwork Profile](https://snow.instructure.com/courses/1254074/pages/ClassworkProfile). Implementation must be without AI code generation or completion.

## Part 1: Hand-traced Huffman tree

| Symbol | Frequency |
|---|---:|
| a | 3 |
| b | 8 |
| c | 10 |
| d | 14 |
| e | 17 |
| f | 42 |

Trace the greedy algorithm by hand: repeatedly merge the two lightest nodes into a node weighted by their sum until one tree remains. Draw the resulting tree, label every edge 0 or 1, and give the bit-code for each of the six symbols.

## Part 2: Priority queue alternatives

Using the Project 2 priority queue, Huffman removes the two lightest nodes and reinserts their merger at every step, taking O(n log n) for n symbols. For each alternative below, decide whether it is **wrong** (may produce a nonoptimal tree) or **slower** (optimal but worse than O(n log n)):

1. Before each step, sort the current node list by weight and take its first two nodes.
2. At each step, use quickselect to find the two lightest nodes.
3. Sort symbols by frequency once. Merge the first two, then repeatedly merge the result with the next symbol in sorted order.

For a wrong method, supply (symbol, frequency) pairs demonstrating failure and show both its tree cost and Huffman's tree cost. For a slower method, give its Big-O running time in n and explain where the time goes.

## Part 3: Huffman codec

1. Explain why saving a tree plus a symbol-to-leaf dictionary is more space-efficient in Big O than saving a symbol-to-bit-string dictionary.
2. Implement Huffman encoding in Python using your Project 2 `PriorityQueue`. Return a Codec containing the tree and a hash map from symbols to tree nodes. Implement and test `encode`, taking any iterable of symbols and returning an iterable of bits (0 and 1), and `decode`, taking an iterable of bits and returning an iterable of symbols.

Building the codec must take O(k log k) for k distinct symbols. Encoding and decoding must take time proportional to the number of bits. Write and submit your own encoding and decoding tests beyond the optional provided ones.

## Optional instructor-provided tests

These are not additional requirements and do not replace the student's own submitted tests. The three adapter functions at the top are the only places where the tests depend on implementation names. The following is transcribed from the expanded `test_huffman.py` section, not agent-authored coursework:

```python
"""Optional tests for Part 3 (Huffman codec).

Huffman's algorithm can break ties either way, so these never check for a particular
bit string -- only for things every correct codec agrees on: decoding undoes encoding,
code lengths when there are no ties, and the total length of an encoded message.

The three functions in this first block are the only place the tests care what you
named things; point them at your own code and the rest just works.
"""
import random

import pytest

import huffman as yours


def build(frequencies):
    """frequencies: a list of (symbol, frequency) pairs"""
    return yours.huffman_codec(frequencies)


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
```

## Part 4: K-ary Huffman (optional bonus)

1. Extend the method to k-ary Huffman encoding, using k-digits instead of bits and up to k digits per internal node.
2. Prove optimality for every n (number of symbols), if possible.
3. Write recursive backtracking code yielding all possible full k-ary trees with a given leaf count.
4. Write a cost function for a k-ary tree with specified leaf frequencies.
5. Write a top-down dynamic programming solution taking (symbol, frequency) pairs and returning the minimum cost of a k-ary tree with those leaves; the leaves need not remain in input order.

## Submission and rubric

Submit work and answers in Canvas.

| Criterion | Points |
|---|---:|
| Part 1: correct hand-traced tree and codes | 2 |
| Part 2.1: wrong or slower, with evidence | 2 |
| Part 2.2: wrong or slower, with evidence | 2 |
| Part 2.3: wrong or slower, with evidence | 2 |
| Part 3.1: representation/space explanation | 2 |
| Part 3.2: correct encoding implementation | 6 |
| Part 3.2: own encoding tests beyond provided tests | 3 |
| Part 3.2: correct decoding implementation | 6 |
| Part 3.2: own decoding tests beyond provided tests | 3 |
| Total | 28 |

Encoding receives at most half credit if it does not use your PriorityQueue and the tree-plus-map representation, if construction is not O(k log k), or if encoding is not linear in the bit count. Decoding receives at most half credit if it is not linear in the bit count. Each criterion also has a zero-point No Marks rating.
