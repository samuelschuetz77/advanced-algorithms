# Greedy Huffman
#
# Part 1: See the photo of my hand-drawn Huffman tree.
#
# Part 2: Priority queue alternatives
# 1. Slower (still produces an optimal tree). O(n^2 log n).
#    Where the time goes: Sorting all remaining nodes after each merge.
# 2. Slower (still produces an optimal tree). O(n^2) expected overall.
#    Where the time goes: Quickselect scans remaining nodes after each merge.
# 3. Wrong: the merged node may outweigh two unmerged nodes, which should merge first.
#    Counterexample: a=3, b=8, c=10, d=14, e=17, f=42.
#    Third merge: one-time-sort takes 21+14=35; Huffman takes 14+17=31.
#    Tree costs: one-time-sort = 213; Huffman = 209.
#
# Part 3: Huffman codec
# 3.1. The tree shares branches; separate code strings repeat those same bits.
#      For n distinct symbols, the tree plus one leaf ID per symbol uses O(n)
#      space; separate complete code strings can use O(n^2) space.
# 3.2. Build and test the Huffman codec.
