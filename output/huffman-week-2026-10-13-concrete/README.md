# Concrete-first Huffman study videos

These MP4s replace the earlier two versions. They use the Ava neural voice,
small full-sentence captions, and one changing visual at a time.

1. `01 - BANANA - One Word, Fewer Bits.mp4` (2:42) starts with BANANA, defines a bit, compares twelve bits with nine, and decodes the result. It then shows eight-bit ASCII bytes, a circled ambiguous short code with a no symbol, and the working prefix-free labels. The name *Huffman* appears only in the final beat.
2. `02 - What Greedy Means.mp4` (1:35) works from a concrete tape example toward the repeated two-smallest choice.
3. `03 - Build One Huffman Tree.mp4` (2:09) hand-traces a five-symbol practice example, separate from the assignment's six-symbol table. Its ending distinguishes the sum of leaf weights (44 letter occurrences) from the weighted code length (98 bits), then checks the result against the merge sum.
4. `04 - Use the Tree as a Codec.mp4` (2:24) explains the Project 2 Graph and priority queue roles, then defines the priority queue, min-heap, and locator dictionary in context. It shows two separate minimum removals with heap rearrangement, tree paths, the symbol-to-leaf map, and a tiny round-trip test.

The videos focus on JEA 4.1 and 4.4 and the related parts of Greedy Huffman.
JEA 4.5 (stable matching) is a separate topic. `.srt` files contain the same
captions that are burned into the videos. `storyboard.json` has the exact spoken
script. `rebuild_prefix.py`, `rebuild_leaf_cost.py`, and
`rebuild_queue_context.py` rebuild the revised portions of videos 1, 3, and 4
from saved clips. `build.py` uses the earlier rendering engine when available
and falls back to these saved-clip rebuilds when it is not.
