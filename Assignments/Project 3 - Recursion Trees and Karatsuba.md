# Project 3 - Recursion Trees and Karatsuba

- **Type:** Assignment (Canvas)
- **Due:** Fri Sep 18, 2026 11:59pm
- **Points:** 24
- **Module:** 02 - Divide and Conquer and Recursion Trees for Sort and Select

## Motivation

This assignment is meant to help you:

- treat arithmetic as a computational problem with a real input size (the number of digits), not a free primitive
- see why a running time is only meaningful once you fix a cost model (Class 6) -- here, one single-digit operation is one step
- implement two divide-and-conquer algorithms for the same problem, one naive and one clever
- derive a recurrence from your own code, and solve it with a recursion tree
- check a predicted asymptotic exponent against a measured one on a log-log plot

The point of the project is the last two bullets. Getting Karatsuba to pass its tests is necessary, but the payoff is being able to say in advance what the benchmark plot will look like, and then see it.

## Assignment

You may work alone or with one partner on this project -- your choice. If you pair up, both of you submit (the same code is fine), name your partner in your write-up, and make sure each of you can derive the recurrences and explain the code on your own; the analysis and reflection should be in your own words even if the implementation was shared.

As always unless otherwise specified, use your non-AI-enabled Classwork Profile for this assignment (no AI code generation, post-processing, or completion). Working with a partner does not change this -- a partner is not an AI.

You are given elementary-school implementations of n-digit addition, subtraction, and multiplication, built out of single-digit table lookups. Do not use Python's `*`, `+`, or `-` on the numbers themselves anywhere in your multiplication algorithms -- that is the whole point of the digit-string representation. You may use Python arithmetic freely on indices and lengths.

### Warm-up (easy): get comfortable with the representation

Write 2-3 additional pytest test cases (with products you compute by hand) for the provided `grade_school_multiply`. This gets you used to the digit-string representation and the test style before you write any new algorithm code.

### Checkpoint (medium): the naive divide-and-conquer split

Implement and test `divide_and_conquer_multiply`. Split each n-digit number into a high half and a low half, so that

x = xhi·10^m + xlo, y = yhi·10^m + ylo, m = ceil(n/2)

and therefore

x·y = xhi·yhi·10^(2m) + (xhi·ylo + xlo·yhi)·10^m + xlo·ylo

That is four recursive half-size multiplications, plus shifts and additions. This is a stepping stone: it is asymptotically no better than the grade-school algorithm, and confirming that (in your analysis and in your plot) is part of the assignment.

Two things that will bite you if you don't plan for them:

- **Base case.** Recursing all the way to a single digit works, but a one-digit base case that calls `single_digit_multiply` is the cleanest. Make sure your base case does not call back into the recursive function.
- **Odd and unequal lengths.** Pad both inputs with leading zeros (`zfill`) to a common length before splitting, and be careful that the split point `m` you shift by matches the split point you actually used.

### Main: Karatsuba

Implement and test `karatsuba`. Karatsuba's observation is that the middle coefficient can be recovered from the other two products plus one more, instead of two:

xhi·ylo + xlo·yhi = (xhi+xlo)(yhi+ylo) - xhi·yhi - xlo·ylo

so three recursive multiplications suffice: xhi·yhi, xlo·ylo, and (xhi+xlo)(yhi+ylo). Note that the two sums can each be one digit longer than their halves -- your implementation has to tolerate that.

**Recursion-tree analysis.** For each of the three algorithms, write the recurrence your own implementation satisfies (counting single-digit operations as the unit of work), solve it with a recursion tree, and state the resulting Θ. Show the tree or the level-by-level sum -- not just the answer. Say for each one whether the root, the levels, or the leaves dominate, and why.

**Benchmark** all three algorithms on n-digit numbers, with n doubling (4, 8, 16, ... ) until each one gets too slow. Note that grade-school and the naive divide-and-conquer will fall over long before Karatsuba does; use the timeout pattern from Project 1 rather than fixed sizes, so a slow algorithm doesn't stall your whole run.

**Plot** the results on log-log axes (instead of plotting points (n, time), plot points (log n, log time)) and compare the measured slope of each line to the exponent you predicted in step 2. On a log-log plot a Θ(n^p) running time is a straight line of slope p, so your three predicted exponents (2, 2, and log2(3) ≈ 1.585) are directly readable off the graph. They will not match perfectly at small n -- explain what you see.

### Bonus (optional)

Find, empirically, the crossover input size at which your Karatsuba first beats your grade-school implementation, and explain why the crossover is where it is rather than at n = 2.

## Starter Code

Put this in `karatsuba.py` and add to it.

### Provided digit-string arithmetic and tests

```python
base = 10

def full_add(x: str, y: str, carry_in: str='0'):
    """Returns (carry_out, sum_digit) as strings from adding two digit strings"""
    return full_add.lookup[x,y,carry_in]
full_add.lookup = {(str(x),str(y),str(c)): (str((x + y + c) // base), str((x + y + c) % base)) for x in range(base) for y in range(base) for c in range(base)}

def single_digit_multiply(x, y):
    """Returns (high_digit, low_digit) as strings from multiplying two digit strings"""
    return single_digit_multiply.lookup[x,y]
single_digit_multiply.lookup = {(str(x),str(y)): (str((x * y) // base), str((x * y) % base)) for x in range(base) for y in range(base)}

def single_digit_complement(digit):
    """Returns 9's complement of digit string"""
    return single_digit_complement.lookup[digit]
single_digit_complement.lookup = {str(digit): (str(9-digit)) for digit in range(base)}

def get_digit_at(x: str, i: int):
    """Returns digit string at position i from right (0-indexed) in number string x"""
    return x[-1 - i] if i < len(x) else '0'

def sign_extend(x: str, n: int):
    """Returns number string x extended to n digits by repeating its first digit"""
    sign_digit = x[0]
    return sign_digit * (n - len(x)) + x

def remove_leading_zeros(x: str):
    """Returns number string x with leading zeros stripped, preserving '0' for zero"""
    stripped = x.lstrip('0')
    return stripped if stripped != '' else '0'

def n_digit_add(x, y):
    """Returns sum as string of number strings x and y with modular arithmetic (wraps at n digits)"""
    carry = '0'
    result = []
    n = max(len(x), len(y))
    for i in range(n):
        carry, sum_digit = full_add(get_digit_at(x, i), get_digit_at(y, i), carry)
        result.append(sum_digit)
    result.append(carry)
    return remove_leading_zeros(''.join(reversed(result)))

def tens_complement(x):
    """Returns 10's complement as string: (10^n - x) for n-digit number string x"""
    n = len(x)
    complement = ''.join(str(9 - int(d)) for d in x)
    result = n_digit_add(complement, '1'.zfill(n))
    return result.zfill(n)

def n_digit_subtract(x, y):
    """Returns difference as string (x - y) using 10's complement addition on number strings"""
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    y_complement = tens_complement(y)
    result = n_digit_add(x, y_complement)
    # If result length > n, we had a carry out (positive result)
    # If result length == n, check if we wrapped around (negative result)
    if len(result) > n:
        return remove_leading_zeros(result[1:])  # Drop the carry-out for positive results
    else:
        return remove_leading_zeros(result)

def left_shift(x: str, k: int):
    """Returns number string x * base^k (shift left k positions)"""
    return remove_leading_zeros(x + '0' * k)

def build_number_from_digits(a: list[str]):
    """Returns number string from digit string list [ones, tens, hundreds, ...]"""
    return remove_leading_zeros(''.join(reversed(a)))

def grade_school_multiply(x: str, y: str):
    """Returns product as string of number strings x and y using grade-school algorithm - O(n^2)"""
    result = '0'
    for i in range(len(y)):
        carry = '0'
        partial_product = []
        for j in range(len(x)):
            hi, lo = single_digit_multiply(get_digit_at(y, i), get_digit_at(x, j))
            carry_from_add, sum_digit = full_add(lo, carry)
            partial_product.append(sum_digit)
            carry = n_digit_add(hi, carry_from_add)
        if carry != '0':
            partial_product.append(carry)
        result = n_digit_add(result, left_shift(build_number_from_digits(partial_product), i))
    return remove_leading_zeros(result)
```

### Provided tests for the given functions -- copy these in as-is

```python
import pytest

@pytest.mark.parametrize("x,y,carry_out,sum_digit", [
    ('0','0','0','0'), ('0','1','0','1'), ('1','0','0','1'), ('1','1','0','2'),
    ('0','9','0','9'), ('9','0','0','9'), ('1','9','1','0'), ('9','1','1','0'),
    ('9','8','1','7'), ('7','8','1','5'), ('9','9','1','8'),
])
def test_full_add(x, y, carry_out, sum_digit):
    assert (carry_out, sum_digit) == full_add(x, y)

@pytest.mark.parametrize("x,y,hi,lo", [
    ('0','0','0','0'), ('0','1','0','0'), ('1','0','0','0'), ('1','1','0','1'),
    ('0','9','0','0'), ('9','0','0','0'), ('1','9','0','9'), ('9','1','0','9'),
    ('9','8','7','2'), ('7','8','5','6'), ('9','9','8','1'),
])
def test_single_digit_multiply(x, y, hi, lo):
    assert (hi, lo) == single_digit_multiply(x, y)

@pytest.mark.parametrize("x,i,digit", [
    ('012345', 0, '5'), ('012345', 1, '4'), ('012345', 2, '3'),
    ('012345', 3, '2'), ('012345', 4, '1'), ('012345', 5, '0'),
])
def test_get_digit_at(x, i, digit):
    assert digit == get_digit_at(x, i)

@pytest.mark.parametrize("x,n,expected", [
    ('0123', 5, '00123'), ('123', 3, '123'), ('0005', 4, '0005'),
    ('999', 6, '999999'), ('0', 3, '000'), ('1', 4, '1111'),
])
def test_sign_extend(x, n, expected):
    assert expected == sign_extend(x, n)

@pytest.mark.parametrize("x,expected", [
    ('00123', '123'), ('123', '123'), ('0', '0'), ('000', '0'),
    ('00000123', '123'), ('100', '100'),
])
def test_remove_leading_zeros(x, expected):
    assert expected == remove_leading_zeros(x)

@pytest.mark.parametrize("x,y,expected", [
    ('0', '0', '0'), ('1', '1', '2'), ('5', '7', '12'), ('99', '1', '100'),
    ('123', '456', '579'), ('999', '1', '1000'), ('8888', '1111', '9999'),
])
def test_n_digit_add(x, y, expected):
    assert expected == n_digit_add(x, y)

@pytest.mark.parametrize("x,expected", [
    ('1', '9'), ('01', '99'), ('5', '5'), ('123', '877'), ('999', '001'), ('0001', '9999'),
])
def test_tens_complement(x, expected):
    assert expected == tens_complement(x)

@pytest.mark.parametrize("x,y,expected", [
    ('5', '3', '2'), ('10', '5', '5'), ('100', '1', '99'), ('50', '25', '25'),
])
def test_n_digit_subtract(x, y, expected):
    assert expected == n_digit_subtract(x, y)

@pytest.mark.parametrize("x,k,expected", [
    ('1', 0, '1'), ('1', 1, '10'), ('5', 2, '500'),
    ('123', 3, '123000'), ('0', 5, '0'), ('99', 2, '9900'),
])
def test_left_shift(x, k, expected):
    assert expected == left_shift(x, k)

@pytest.mark.parametrize("digits,expected", [
    (['5', '4', '3', '2', '1'], '12345'), (['0'], '0'), (['1', '2', '3'], '321'),
    (['0', '0', '0', '1'], '1000'), (['5'], '5'),
])
def test_build_number_from_digits(digits, expected):
    assert expected == build_number_from_digits(digits)

@pytest.mark.parametrize("x,y,expected", [
    ('0', '0', '0'), ('1', '1', '1'), ('5', '7', '35'), ('9', '9', '81'),
    ('1000', '1000', '1000000'), ('2', '3', '6'), ('10', '10', '100'),
    ('12345', '34567', '426729615'),
])
def test_grade_school_multiply(x, y, expected):
    assert expected == grade_school_multiply(x, y)
```

### What you write

```python
def divide_and_conquer_multiply(x: str, y: str):
    """Returns the product of number strings x and y by splitting each in half
    and making FOUR recursive half-size multiplications."""
    # TODO: base case (one digit) -> single_digit_multiply
    # TODO: pad both to a common (even) length, split into hi/lo halves
    # TODO: four recursive calls, then left_shift and n_digit_add to combine
    raise NotImplementedError

def karatsuba(x: str, y: str):
    """Returns the product of number strings x and y using THREE recursive
    half-size multiplications."""
    # TODO: base case (one digit) -> single_digit_multiply
    # TODO: pad both to a common (even) length, split into hi/lo halves
    # TODO: hi*hi, lo*lo, and (hi+lo)*(hi+lo); recover the middle term with
    #       n_digit_subtract, then left_shift and n_digit_add to combine
    raise NotImplementedError
```

Once both work, this cross-check gives you confidence cheaply -- all three algorithms must agree with each other on the same inputs:

```python
ALGORITHMS = [grade_school_multiply, divide_and_conquer_multiply, karatsuba]

@pytest.mark.parametrize("multiply", ALGORITHMS)
@pytest.mark.parametrize("x,y", [
    ('0', '0'), ('7', '8'), ('99', '99'), ('12345', '34567'),
    ('1000', '1000'), ('9', '12345'), ('123456789', '987654321'),
])
def test_algorithms_agree_with_python(multiply, x, y):
    assert multiply(x, y) == str(int(x) * int(y))
```

Note that `str(int(x) * int(y))` is fine in a test -- it is the trusted oracle you are checking against. It is not allowed inside the algorithms themselves.

### Benchmark and plotting starter

```python
import random
import time
import statistics

def random_digits(n, rng):
    """Returns a random n-digit number string with no leading zero"""
    return str(rng.randint(1, 9)) + ''.join(str(rng.randint(0, 9)) for _ in range(n - 1))

def time_multiply(multiply, x, y):
    start = time.perf_counter()
    multiply(x, y)
    return time.perf_counter() - start

def median_time(multiply, n, rng, repetitions=3):
    return statistics.median(
        time_multiply(multiply, random_digits(n, rng), random_digits(n, rng))
        for _ in range(repetitions))

if __name__ == '__main__':
    rng = random.Random(4567)
    timeout = 1.0  # stop growing n for an algorithm once it exceeds this
    lengths = [2 ** k for k in range(2, 12)]  # 4, 8, ..., 2048
    results = []
    for multiply in ALGORITHMS:
        print(f'\n\t{multiply.__name__}', end='')
        for n in lengths:
            t = median_time(multiply, n, rng)
            print('.', end='', flush=True)
            results.append(dict(algorithm=multiply.__name__, n=n, time=t))
            if t > timeout:
                break  # don't try longer inputs for an algorithm already too slow
    print()
    import pandas as pd
    pd.DataFrame(results).to_csv('multiply_times.csv', index=False)
```

Plot it in a separate script so you can iterate on the picture without re-running the benchmark. Log-log axes are what make the exponents readable:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
data = pd.read_csv('multiply_times.csv')
plot = sns.relplot(data=data, kind='line', x='n', y='time', hue='algorithm', marker='o')
plot.set(xscale='log', yscale='log')
plot.savefig('multiply_times.png')
```

To read a measured exponent off the data directly (this is the slope of the log-log line):

```python
import numpy as np
for name, group in data.groupby('algorithm'):
    group = group[group.time > 0]
    slope = np.polyfit(np.log(group.n), np.log(group.time), 1)[0]
    print(f'{name}: measured exponent ~= {slope:.2f}')
```

`uv` is an easy way to install pytest, pandas, seaborn, and numpy if you don't have them.

## Submission

Upload `karatsuba.py`:
- put all of your code and tests into a single `karatsuba.py` python file, and use pytest for your testing
- at the top of the file, include your name, the course, and the date
- should be runnable as `python -m pytest karatsuba.py` (tests) and `python karatsuba.py` (benchmark)

In the canvas text box or a pdf file:
- your recursion-tree analysis for all three algorithms (a photo of neat handwritten trees is fine)
- a screenshot of your test results (hopefully passing)
- your log-log plot, and the measured exponent for each algorithm next to the exponent you predicted
- a sentence or two on how the assignment went, and on any gap between predicted and measured exponents
- your partner's name, if you worked with one

## Rubric

| Criteria | Points |
|---|---|
| warm-up tests for `grade_school_multiply` | 2 |
| correct implementation of `divide_and_conquer_multiply` | 4 |
| effective tests for `divide_and_conquer_multiply` | 2 |
| correct implementation of `karatsuba` | 5 |
| effective tests for `karatsuba` | 2 |
| recursion-tree analysis of all three algorithms, with the level-by-level sum shown and the dominating level identified | 4 |
| benchmark code and log-log plot comparing all three | 3 |
| reflection comparing predicted to measured exponents | 2 |
