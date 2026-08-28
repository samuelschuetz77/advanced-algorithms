# Project 1 - Sorting

- **Type:** Assignment (Canvas)
- **Due:** Thu 9/3/2026, 11:59pm
- **Points:** 24
- **Canvas link:** https://snow.instructure.com/courses/1254074/assignments/19125906?module_item_id=34814101

## Motivation

- Considering an important computational problem: sorting
- Remembering several classic algorithms that solve this problem
- Noting the difference between a computational problem and an algorithm
- Considering properties of different sorting algorithms
- Implementing algorithms in Python
- Running experiments to compare algorithm running time empirically
- Using Big O analysis to compare algorithm running time theoretically

## Assignment

Use your non-AI-enabled [[ClassworkProfile]] when writing or editing code or learning logs in this class — do not submit AI-generated, AI-post-processed, or AI-suggested code.

### Part 1: Theory and Implementation

For each sorting algorithm below:
- Implement the algorithm on your own
- Include sufficient `pytest` tests to give confidence the implementation is correct
- Analyze your implementation to ensure it achieves the theoretical Big O properties of the algorithm (nothing to turn in for this, but points are lost if it doesn't, and be prepared to do this kind of analysis on an exam)

**Algorithms to implement and compare:**
1. Bubble sort
2. Selection sort
3. Insertion sort
4. (Recursive) merge sort
5. (Recursive, random pivot, in-place) quick sort
6. Counting sort

### Part 2: Empirical Benchmark

The main driver of `sorting.py` should:
1. Set the random seed to `4567` (reproducible sequence)
2. Create 3 lists of length 1,000,000 of random integers between 0 and 1023
3. For each algorithm and for each prefix length `10, 100, 1000, 10000, 100000, 1000000`:
   - Run the sorting algorithm on 3 variants: original; already sorted; reverse sorted
   - Run 3 times on each and take the median running time (reasonable timeout allowed if very slow)
4. Create a plot showing how the 6 algorithms scale with list length under the 3 settings

## Submission

**Upload `sorting.py`:**
- All code and tests in a single `sorting.py` file, using `pytest` for testing
- Top of file: name, course, date
- Must run via `python -m pytest sorting.py` (tests) and `python sorting.py` (benchmark)

**In the Canvas text box or a PDF:**
- 1-2 sentences on how the assignment went
- Screenshot of test results (passing)
- Result plots showing performance comparison

## Optional Starter Code / Ideas

- pytest: use parameterized tests
- Timeouts: incrementally increase input size until the algorithm takes too long (e.g. >1s) rather than pre-specifying sizes that may be too large for some algorithms
- Plotting: use `pandas.DataFrame(list_of_dicts).to_csv('results.csv')`; iterate on plotting separately from the benchmark script; use `seaborn.relplot`
- `uv` recommended for managing Python deps (pytest, pandas, seaborn)

(Canvas linked example code for pytest parameterization, timeout benchmarking, and plotting — not captured here; re-check the assignment page if needed.)

## Rubric

| Criteria | Full Marks | No Marks |
|---|---|---|
| Correct (and correctly efficient) implementation of each sort | 12 pts | 0 pts |
| Effective tests of each sort + screenshot shows they pass | 6 pts | 0 pts |
| Screenshot shows benchmark results | 6 pts | 0 pts |

See [[course-schedule.md]] — this project lands right around the "6 Sorts Refresh" (8/31) and "Big O / Benchmarking" (9/2) class sessions.
