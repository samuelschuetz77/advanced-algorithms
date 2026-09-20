# Samuel Schuetz
# Advanced Algorithms
# 9/15/2026

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


# my algorithms

def divide_and_conquer_multiply(x: str, y: str):
    if len(x) == 1 and len(y) == 1: 
         result = "".join(single_digit_multiply(x,y))
         result = remove_leading_zeros(result)
         return result
    
    n = max(len(x), len(y))
    if n % 2 == 1:
        n += 1 
    x = x.zfill(n)
    y = y.zfill(n)

    splitted_index = int(n / 2)
    xhi = x[:splitted_index]
    xlo = x[splitted_index:]
    yhi = y[:splitted_index]
    ylo = y[splitted_index:]

    rec1 = divide_and_conquer_multiply(xhi, yhi)
    k1 = splitted_index * 2
    shifted_rec1 = left_shift(rec1, k1)
    rec2 = divide_and_conquer_multiply(xhi, ylo)
    rec3 = divide_and_conquer_multiply(xlo, yhi)
    k2 = splitted_index
    shifted_rec2_and_rec3 = left_shift(n_digit_add(rec2, rec3), k2)
    rec4 = divide_and_conquer_multiply(xlo, ylo)
    part1 = n_digit_add(shifted_rec1,shifted_rec2_and_rec3)
    result = n_digit_add(part1, rec4)

    return remove_leading_zeros(result)

def karatsuba(x: str, y: str):
    if len(x) == 1 and len(y) == 1: 
             result = "".join(single_digit_multiply(x,y))
             result = remove_leading_zeros(result)
             return result

    n = max(len(x), len(y))
    if n % 2 == 1:
        n += 1 
    x = x.zfill(n)
    y = y.zfill(n)

    splitted_index = int(n / 2)
    xhi = x[:splitted_index]
    xlo = x[splitted_index:]
    yhi = y[:splitted_index]
    ylo = y[splitted_index:]

    rec1 = karatsuba(xhi, yhi)
    k1 = splitted_index * 2
    shifted_rec1 = left_shift(rec1, k1)

    rec2 = karatsuba(xlo, ylo)

    rec3 = karatsuba(n_digit_add(xhi, xlo), n_digit_add(yhi, ylo))

    middle = n_digit_subtract(n_digit_subtract(rec3, rec2), rec1)
    k2 = splitted_index
    shifted_middle = left_shift(middle, k2)

    part1 = n_digit_add(shifted_rec1,shifted_middle)
    result = n_digit_add(part1, rec2)

    return remove_leading_zeros(result)
    

ALGORITHMS = [grade_school_multiply, divide_and_conquer_multiply, karatsuba]


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

# my tests for grade school multiply

@pytest.mark.parametrize("x,y,expected", [
    ('0', '123', '0'),
    ('1', '456', '456'),
    ('4', '6', '24'),
    ('11', '11', '121'),
    ('25', '4', '100'),
])
def test_my_grade_school_multiply(x, y, expected):
    assert expected == grade_school_multiply(x, y)

@pytest.mark.parametrize("multiply", ALGORITHMS)
@pytest.mark.parametrize("x,y", [
    ('0', '0'), ('7', '8'), ('99', '99'), ('12345', '34567'),
    ('1000', '1000'), ('9', '12345'), ('123456789', '987654321'),
])
def test_algorithms_agree_with_python(multiply, x, y):
    assert multiply(x, y) == str(int(x) * int(y))

# my tests for divide and conquer and karatsuba multiply

@pytest.mark.parametrize("x,y,expected", [
    ('0', '2', '0'), ('12', '3', '36'), ('50000', '5', '250000'), ('9', '9', '81'),
    ('1000', '1000', '1000000'), ('2', '3', '6'), ('10', '10', '100'),
    ('12345', '34567', '426729615'),
])
def test_divide_and_conquer_multiply(x, y, expected):
    assert expected == divide_and_conquer_multiply(x, y)

@pytest.mark.parametrize("x,y,expected", [
    ('0', '2', '0'), ('12', '3', '36'), ('50000', '5', '250000'), ('9', '9', '81'),
    ('1000', '1000', '1000000'), ('2', '3', '6'), ('10', '10', '100'),
    ('12345', '34567', '426729615'),
])
def test_karatsuba(x, y, expected):
    assert expected == karatsuba(x, y)

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
