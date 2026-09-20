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

### Example code (pytest parameterization + timeout benchmarking)

```python
import pytest
import random
import time
import statistics

def built_in_sorted(a):
	a[:] = sorted(a)

def in_place_sort(a):
	a.sort()

# bad
def do_nothing(a):
	pass

def make_two_copies(a):
	return list(a) * 2

def quadratic_garbage(a):
	for i in range(len(a)):
		for j in range(len(a)):
			a[i], a[j] = a[j], a[i]

def reverse_sorted(a):
	return list(reversed(sorted(a)))

def unchanged(a):
	return a

@pytest.mark.parametrize("original", [
	[],
	[1],
	[1,2],
	[2,1],
	[1,2,3],
	[1,3,2],
	[2,1,3],
	[2,3,1],
	[3,1,2],
	[3,2,1]
])
def test_all(original):
	for sort in sorts:
		a = list(original)
		sort(a)
		assert a == sorted(original), f"failed to sort {original} with {sort.__name__}."

def time_sort(original, prep, sort):
	a = prep(list(original))
	start = time.perf_counter()
	sort(a)
	end = time.perf_counter()
	return end - start

def aggregated_time_sort(lists, length, prep, sort, repetitions, timeout):
	return statistics.median(
		[time_sort(a[:length], prep, sort, timeout)
			for a in lists
			for _ in range(repetitions)])

import pandas as pd

sorts = [built_in_sorted, in_place_sort, do_nothing, make_two_copies, quadratic_garbage]
if __name__ == '__main__':
	random.seed(4567)
	preps = [sorted, reverse_sorted, unchanged]
	num_lengths = 7
	length_base = 10
	max_value = 2 ** 10
	max_length = length_base ** (num_lengths - 1)
	random_lists = [[random.randint(0, max_value) for _ in range(max_length)] for _ in range(3)]
	lengths = [length_base**k for k in range(num_lengths)]
	repetitions = 3
	timeout = 0.01
	results = []
	for prep in preps:
		print(f'\n{prep.__name__}')
		for sort in sorts:
			print(f'\n\t{sort.__name__}', end='')
			for length in lengths:
				median_time = aggregated_time_sort(
					lists=random_lists,
					length=length,
					prep=prep,
					sort=sort,
					repetitions=repetitions,
					timeout=timeout)
				print('.',end='')
				results.append(dict(
					sort=sort.__name__,
					prep=prep.__name__,
					length=length,
					time=median_time))
				if median_time > timeout:
					# don't consider longer lists if it already was too long on this one
					break
	print()
	print(results)
	pd.DataFrame(results).to_csv("sort_times.csv")
```

### Example code (plotting)

```python
import seaborn as sns
import pandas as pd

sns.set_theme()
data = pd.read_csv("sort_times.csv")
plot = sns.relplot(data=data, kind='line', x='length', y='time', style='prep', hue='sort')
plot.savefig("sort_times.png")
```

- "I found `uv` very easy to install and use for python dependencies (like pytest, pandas, and seaborn)" — instructor's note.

## Rubric

| Criteria | Full Marks | No Marks |
|---|---|---|
| Correct (and correctly efficient) implementation of each sort | 12 pts | 0 pts |
| Effective tests of each sort + screenshot shows they pass | 6 pts | 0 pts |
| Screenshot shows benchmark results | 6 pts | 0 pts |

See [[course-schedule.md]] — this project lands right around the "6 Sorts Refresh" (8/31) and "Big O / Benchmarking" (9/2) class sessions.
