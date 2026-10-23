# Practice Quiz - Backtracking and Dynamic Programming

- Status: Graded 23.33/25; submitted 10/13/2026 8:32am (late) (Canvas, as of 2026-10-20).
- Canvas assignment: https://snow.instructure.com/courses/1254074/assignments/19254540
- Quiz: https://snow.instructure.com/courses/1254074/quizzes/4912506
- Due: Wed 10/7/2026, 11:59pm Mountain
- Points / questions: 25 points; 5 questions
- Last synced: 2026-10-12 via Canvas in Chrome.

## Instructions and status

Canvas describes this as an in-class practice quiz and recommends trying solutions in English and Python before looking at answer options. Grades marks it missing; the quiz page showed “Resume Quiz,” so Canvas has no completed submission recorded.

October 12 check: resumed the existing attempt (started October 8 at 11:56am) to read all five questions and their dropdown choices. The first five dropdowns in Question 1 already have correct selections; its sixth dropdown and all other questions are blank. No selections were changed and the quiz was not submitted. Canvas instructions caution that the questions and answer key may contain errors.

## Questions and derived answer guide

The entries below are mathematically derived choices matching the live dropdown text, not a verified Canvas grading key. Each question has six dropdowns, in this order: name, parameters, base case(s), options, value of a choice, and combination rule.

### 1. Painting houses

Paint a row of n houses with k colors at costs `paint_cost[i][c]`, with no equal colors on neighboring houses. Return the minimum total cost.

1. `min_cost_from`
2. `(i, prev_color)`
3. `i == n returns 0`
4. `each color c ≠ prev_color for house i`
5. `paint_cost[i][c] + min_cost_from(i + 1, c)`
6. `minimum`

### 2. Decoding digits

Count the letter messages encoded by a digit string with A=1 through Z=26 and no separators.

1. `ways_to_decode_from`
2. `(i)`
3. `i == len(digits) returns 1`
4. `one digit (if digits[i] ≠ '0'), and two digits (if 10 ≤ int(digits[i:i+2]) ≤ 26)`
5. `ways_to_decode_from(i + j)`
6. `sum`

Reaching the end counts one completed decoding. A zero cannot begin a valid letter code.

### 3. Bursting balloons

Bursting a balloon scores its value times its nearest unburst neighbors' values, using 1 for a missing neighbor. Maximize the total; `[3, 1, 5, 8]` has optimum 167. Pad with `a = [1] + balloons + [1]`; padding is never burst.

1. `max_score_between`
2. `(lo, hi), with a[lo] and a[hi] still standing`
3. `hi == lo + 1 returns 0`
4. `each k with lo < k < hi, as the last balloon burst between them`
5. `a[lo]·a[k]·a[hi] + max_score_between(lo, k) + max_score_between(k, hi)`
6. `maximum`

Choosing the last balloon fixes its final neighbors and separates two independent open intervals.

### 4. Dropping eggs

Find the highest floor from which an egg survives (possibly none), minimizing drops needed to guarantee the answer. Broken eggs are lost; surviving eggs can be reused.

1. `min_guaranteed_drops`
2. `(eggs_left, floors_left)`
3. `floors_left == 0 returns 0, and eggs_left == 1 returns floors_left`
4. `each floor x from 1 to floors_left, as the next drop`
5. `1 + max(min_guaranteed_drops(eggs_left − 1, x − 1), min_guaranteed_drops(eggs_left, floors_left − x))`
6. `minimum`

Take the maximum of break/survive outcomes to guarantee success, then minimize over the chosen drop floor.

### 5. Taking coins from the ends

Two perfect players alternate taking a coin from either end of a row. Return the first player's total. `total(i, j)` gives the inclusive interval sum in constant time.

1. `most_mover_can_get`
2. `(i, j)`
3. `i > j returns 0`
4. `the left coin, and the right coin`
5. `coins[i] + total(i + 1, j) − most_mover_can_get(i + 1, j)`
6. `maximum`

The helper describes whichever player moves next. Subtract the opponent's optimal share from the remaining interval sum.

Submission type: Canvas quiz. Turn-in path: N/A.
