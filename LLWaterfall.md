### Learning Log Waterfall — generated 9/16/2026

For: **Week of Learning Log 5 and 6** (next due — Project 3, Recursion Trees
and Karatsuba, due Fri 9/18/2026 11:59pm)

Mode: Complete, default granularity (5-7 insight bullets per candidate).
Ordered 0-to-hero: each candidate assumes the ones above it. Candidate 3
picks up right where your existing Learning Log 6 entry on `karatsuba`'s
combine step left off. Read through all 7, then personalize whichever ones
strike a chord into `learning log.md` yourself.

---

## Candidate 6.1: Why can't the algorithm just use Python's `*`, `+`, `-` on the numbers?

- Question/Problem: The spec says not to use Python's native `*`/`+`/`-` on
  the number strings anywhere inside the algorithms, only on indices and
  lengths — why does that restriction exist, and what would break about the
  assignment's whole point if I ignored it?
- Importance (1-5): 3 — not directly rubric-scored, but if this doesn't
  click first, the recursion-tree analysis later (4 pts) won't make sense
  either, since it's built on the same idea.
- How to Learn: Reread the Motivation section of the Project 3 spec
  ("treat arithmetic as a computational problem with a real input size...
  not a free primitive") side by side with the `single_digit_multiply` /
  `full_add` lookup tables you were given, and ask: what is the actual unit
  of work being counted?
- Insight/Answer:
  - Python's `*` on two big integers is O(1) from your code's point of
    view — it hides its own cost, so you can't use it as your "step
    counter" without lying to yourself about what n is.
  - The whole assignment defines "one step" as one single-digit table
    lookup (`single_digit_multiply`, `full_add`) — that's the cost model
    the spec calls out explicitly ("here, one single-digit operation is one
    step").
  - This is why every provided helper (`n_digit_add`, `n_digit_subtract`,
    `left_shift`) is built entirely out of digit-by-digit loops over those
    lookups, never raw `+`/`-`/`*` on the number strings.
  - If you used real Python arithmetic instead, your three algorithms would
    all just be "however fast Python's bignum multiply is," and there would
    be no recurrence to derive, no recursion tree to draw, and no
    predicted-vs-measured exponent gap to explain — the entire second half
    of the assignment (worth more points than the implementation) would be
    meaningless.
  - Practical translation: n = number of digits, not "the size of the
    number" in the everyday sense — a 100-digit number is n=100 regardless
    of its numeric value, which is exactly why doubling n (4, 8, 16...) in
    the benchmark is the right way to grow the input.

---

## Candidate 6.2: Why is `divide_and_conquer_multiply` (4-way split) not actually faster than grade-school?

- Question/Problem: The checkpoint splits x and y into hi/lo halves and
  does 4 recursive half-size multiplications instead of doing it all at
  once — that sounds like progress, so why does the spec say this version
  is "asymptotically no better than the grade-school algorithm"?
- Importance (1-5): 4 — this is a full rubric line (4 pts for correct
  `divide_and_conquer_multiply`) and it's the recurrence you have to derive
  and solve with a recursion tree before you can even appreciate what
  Karatsuba fixes.
- How to Learn: Write out the recurrence for this version yourself
  (T(n) = 4T(n/2) + O(n)) and compare it against T(n) = n^2 for grade-school
  using the Master Theorem intuition you already built in Learning Log 5's
  "increasing/equal/decreasing level totals" insight — don't just take the
  spec's word for it, derive why 4 recursive calls of half size lands you
  back at n^2.
- Insight/Answer:
  - This maps directly onto your own Learning Log 5 insight about level
    totals: r = 4 children, c = 2 (each half the size), non-recursive work
    per node is O(n) for the shifts/adds — so T(n) = 4T(n/2) + O(n).
  - Using your own "equal/increasing/decreasing" classification: level i
    has 4^i nodes each doing O(n/2^i) work, so each level's total is
    4^i * n/2^i = n * 2^i — that's growing level to level (an "Increasing"
    case in your own terms), so the bottom level (the leaves) dominates.
  - Number of leaves at the bottom = 4^(log2 n) = n^2 — that's where the
    n^2 comes from, it's baked into "4 recursive calls each half the size,"
    same total work as grade-school just rearranged into a tree shape.
  - The intuitive read: splitting the multiplication into 4 pieces
    (xhi·yhi, xhi·ylo, xlo·yhi, xlo·ylo) doesn't reduce the total amount of
    single-digit multiplying being done anywhere — it's still every
    digit-pair of x against every digit-pair of y, just computed
    recursively instead of in nested loops.
  - This is exactly the stepping-stone the spec wants: "confirming that (in
    your analysis and in your plot) is part of the assignment" — your
    benchmark should show divide_and_conquer tracking grade-school's curve,
    not beating it.
  - Practical bug to watch for while implementing: your base case must call
    `single_digit_multiply` directly and never call back into
    `divide_and_conquer_multiply` itself, or you'll get exactly the
    infinite-recursion-on-len-1 bug you already diagnosed once in your
    merge sort entry (9/2) — same shape of off-by-one/base-case mistake,
    different algorithm.

---

## Candidate 6.3: How do the three Karatsuba products actually get combined with the right shifts? (continuing your existing entry)

- Question/Problem: You already started this one — after reusing base
  case/padding/split from `divide_and_conquer_multiply`, how do you combine
  the three recursive products (hi·hi, lo·lo, and (hi+lo)(hi+lo)) using
  `n_digit_add`, `n_digit_subtract`, and `left_shift`, and specifically
  where does each of the three pieces get shifted?
- Importance (1-5): 5 — this is the single biggest rubric line (5 pts for
  correct `karatsuba`), and it's the part your current entry stops right
  before finishing.
- How to Learn: Go back to the algebra in the spec —
  x·y = xhi·yhi·10^(2m) + (xhi·ylo + xlo·yhi)·10^m + xlo·ylo — and match
  each of the three terms to one of your three recursive products, one at
  a time, writing down the shift amount for each before touching code.
- Insight/Answer:
  - Your own entry already correctly placed two of the three: hi*hi gets
    shifted by 2*m (same as in divide_and_conquer, since it's the same
    "highest place value" term), and lo*lo gets shifted by 0 because it's
    already sitting at the ones place — nothing above it to push it into.
  - The middle term is where it's genuinely different from
    divide_and_conquer: there, you had two separate products
    (xhi·ylo + xlo·yhi) that you could just add together. Here you only
    have one number for that whole middle piece, recovered algebraically:
    (xhi+xlo)(yhi+ylo) - xhi·yhi - xlo·ylo — and you already have xhi·yhi
    and xlo·lo sitting around from the other two recursive calls, so no
    extra multiplication is needed to get the middle term, only a subtract.
  - That middle term needs `n_digit_subtract` applied twice (subtract off
    both hi*hi and lo*lo from the sum-product) before it's ready to shift —
    order between the two subtractions doesn't matter, subtraction from a
    single running result just needs both terms removed eventually.
  - The middle term's shift is m, not 2m or 0 — it sits at the same "place
    value slot" the two middle terms occupied in divide_and_conquer's
    version, just arrived at differently.
  - The edge case your entry hasn't hit yet: (xhi+xlo) and (yhi+ylo) can
    each be one digit longer than xhi/xlo alone (e.g. two m-digit halves
    summing to an m+1-digit number) — the spec calls this out directly
    ("your implementation has to tolerate that"). Your `n_digit_add` and
    `n_digit_subtract` helpers are already built to handle mismatched
    lengths internally (they take `max(len(x), len(y))` and pad), so the
    thing to actually verify is that you're not truncating or re-padding
    that sum product back down to m digits by hand before combining it —
    let it stay whatever length it naturally comes out to.
  - Putting it together: final result = `n_digit_add` of all three shifted
    pieces (hi*hi shifted 2m, middle shifted m, lo*lo shifted 0) — same
    combine shape as divide_and_conquer_multiply, just with 3 inputs
    instead of 4 and one extra pair of subtracts to derive the middle one.

---

## Candidate 6.4: How do you build the recursion tree for Karatsuba's recurrence and show the level-by-level sum?

- Question/Problem: Once `karatsuba` works, what recurrence does *your own
  implementation* actually satisfy, and how do you draw/derive the
  recursion tree to get to Θ(n^log2(3)) the same rigorous way — level
  totals, not just quoting the formula?
- Importance (1-5): 4 — its own 4-point rubric line, explicitly requires
  "the level-by-level sum shown and the dominating level identified," not
  just the final answer.
- How to Learn: Reuse your own Learning Log 5 method exactly: identify r
  (branches) and c (shrink factor) from your code, write T(n) = r·T(n/c) +
  O(n), then compute level totals level by level the way you did for
  T(n)=3T(n/2)+O(n) as your "Increasing" worked example on 9/13.
- Insight/Answer:
  - You've actually already derived this exact recurrence once — your
    9/13 entry worked T(n) = 3T(n/2) + O(n) as your worked example for the
    "Increasing" case. Karatsuba's real recurrence is exactly that: r=3
    (three recursive multiplications), c=2 (each half the size), O(n)
    non-recursive work per node (the adds/subtracts/shifts to combine).
  - Level-by-level: level i has 3^i nodes, each doing O(n/2^i) work, so
    level i's total is 3^i · n/2^i = n · (3/2)^i — growing by a factor of
    1.5 every level down, confirming this is your "Increasing" case again.
  - Because it's increasing, the leaves dominate the sum (same logic your
    own 9/13 entry already stated generally: "if growing, the bottom level
    alone is basically the whole sum") — so the total work is governed by
    how many leaves there are and how much work each leaf-level node does.
  - Number of levels = log2(n) (since n halves each level until reaching 1
    digit); number of leaves at the bottom = 3^(log2 n) = n^log2(3) ≈
    n^1.585 — that exponent is exactly the number the spec tells you to
    expect on the log-log plot later.
  - Concretely writing the "show the tree or level-by-level sum" part the
    rubric wants: list level 0 = n, level 1 = 1.5n, level 2 = 2.25n, ...,
    and note the sum of this geometric series is dominated by its last
    (largest) term rather than needing to sum all of it precisely — same
    shortcut insight you already wrote down generally on 9/13.
  - Sanity check against your grade-school and divide_and_conquer analyses:
    grade-school is Θ(n^2) directly, divide_and_conquer is also Θ(n^2) (via
    Candidate 2's leaf count), Karatsuba is Θ(n^1.585) — three different
    recurrences, same style of derivation, one clear winner.

---

## Candidate 6.5: What does "slope on a log-log plot = exponent" actually mean, and why won't small n match the prediction?

- Question/Problem: The spec says a Θ(n^p) running time shows up as a
  straight line of slope p on log-log axes — why is that true
  mathematically, and why does it explicitly warn "they will not match
  perfectly at small n"?
- Importance (1-5): 3 — feeds the 3-point benchmark/plot line and the
  2-point reflection line, but conceptually it's a smaller lift than
  Candidates 3-4 since it's mostly a plotting/interpretation skill, not new
  algorithm design.
- How to Learn: Take T(n) = c·n^p, apply log to both sides
  (log T = log c + p·log n), and recognize that as the equation of a line
  in (log n, log T) space with slope p — then think about what "constant
  factor c" does to a real, small-n benchmark that pure asymptotic theory
  ignores.
- Insight/Answer:
  - log(T(n)) = log(c·n^p) = log(c) + p·log(n) — this is literally
    y = mx + b with y=log(T), x=log(n), m=p (the exponent you want), and
    b=log(c) (a constant offset from whatever constant factor your
    implementation happens to have) — that's the whole reason log-log axes
    turn "n^p" into a straight line whose slope you can read directly.
  - This is why `np.polyfit(log(n), log(time), 1)[0]` in the provided
    plotting code recovers the slope — it's literally fitting that same
    line and reading off m.
  - Small-n mismatch reason #1: constant factors and lower-order terms
    (all the shifts, adds, subtracts, Python function-call overhead) matter
    relatively more when n is small, and asymptotic notation by design
    throws those away — Θ(n^1.585) only describes what dominates as n gets
    large.
  - Small-n mismatch reason #2 (recursion-specific): at small n you're
    closer to the base case, so a bigger fraction of total work is
    "recursive overhead" (splitting, padding, recombining) rather than the
    actual single-digit multiplies the cost model is counting — that ratio
    only stabilizes once n is large enough that the leaves genuinely
    dominate, same "leaves dominate" idea from Candidate 4 but now showing
    up as a practical timing artifact instead of a theoretical one.
  - Practical read for your reflection paragraph: expect all three
    measured slopes to start out messier/flatter at small n and settle
    toward their predicted values (2, 2, 1.585) as n grows through your
    doubling sequence (4, 8, 16, ... up to the timeout) — that trend itself
    is the evidence the assignment wants you to describe, not just the
    final numbers.
  - This also explains why grade-school and divide_and_conquer "fall over"
    (hit the 1-second timeout) long before Karatsuba — both are n^2, so
    their time roughly quadruples every time n doubles, while Karatsuba's
    only grows by about 2^1.585 ≈ 3x — the gap compounds fast at the large
    n values where the timeout actually bites.

---

## Candidate 6.6: What edge cases in padding/shifting are most likely to break Karatsuba even after the algebra is right?

- Question/Problem: Given how many off-by-one bugs you've hit in past
  learning logs on shift/slice boundaries (merge sort's `mid_i` bug on
  9/2, the shift-point insight you'd already started for Learning Log 6),
  what specific edge cases in padding and splitting are most likely to
  bite `karatsuba` even once the core algebra (Candidate 3) is right?
- Importance (1-5): 3 — not its own rubric line, but "effective tests for
  karatsuba" (2 pts) and passing the cross-check against grade-school (part
  of the 5-pt correctness line) both depend on catching these before
  submission.
- How to Learn: Before running any tests, hand-trace `karatsuba('9','9')`
  (single digit, hits base case immediately) and `karatsuba('123','45')`
  (unequal lengths, forces padding) on paper, writing out what m, the
  padded strings, and each of the three sub-results should be at every
  step.
- Insight/Answer:
  - Unequal-length inputs (like '123' and '45') must be zfill-padded to a
    common length *before* computing m = ceil(n/2) — if you compute m from
    the unpadded lengths, the hi/lo split point won't agree between x and
    y, which silently produces wrong place values (same family of bug as
    your merge_sort `mid_i` off-by-one on 9/2, just one level earlier in
    the pipeline).
  - Padding to an *even* length specifically matters here (unlike a generic
    pad) because the hi/lo split needs m = n/2 to be a clean integer digit
    count on both operands — the spec's own "pad both inputs...to a common
    length" note plus "the split point m you shift by matches the split
    point you actually used" is worth rereading literally, since it's
    warning about exactly this class of bug.
  - The base case must trigger on a genuinely single-digit input and call
    `single_digit_multiply` directly — test this in isolation
    (`karatsuba('9','9')` should never touch the hi/lo split logic at all).
  - Because (xhi+xlo) and (yhi+ylo) can be one digit longer than the halves
    (per Candidate 3's insight), a test that only ever uses inputs that
    conveniently avoid that carry (e.g. small digits that never sum past 9)
    would pass while still hiding a real bug — deliberately pick test
    digits that force a carry in the sum step.
  - Cheapest possible correctness net, and the one the spec explicitly
    hands you: the `test_algorithms_agree_with_python` parametrized test
    already checks all three algorithms against Python's own `*` as the
    trusted oracle — running that early and often (not just once at the
    end) turns "is my algebra right" into a fast yes/no instead of a
    multi-hour debugging session.
  - Worth a dedicated pytest case per edge type, not just per input value:
    one for single-digit base case, one for equal-length even-digit inputs,
    one for unequal lengths forcing padding, one for lengths that force a
    carry in (hi+lo).

---

## Candidate 6.7 (hero): Why does Karatsuba's crossover point sit well above n=2 instead of right at it?

- Question/Problem: Bonus question, but the most integrative one — if
  Karatsuba does strictly fewer recursive multiplications than
  divide_and_conquer at every level (3 vs 4), why doesn't Karatsuba start
  winning immediately at the smallest possible n, and where empirically
  does the crossover actually happen?
- Importance (1-5): 2 — it's explicitly optional/bonus, so lowest priority
  of the 7, but it's the one question that ties every other candidate
  above it together into a single explanation, which is why it's last.
- How to Learn: Once your benchmark/plot (Candidate 5) is working, actually
  look at the small-n end of your own data (n=4, n=8, n=16) rather than
  reasoning about it abstractly, and compare it against the "constant
  factor" reasoning from Candidate 5.
- Insight/Answer:
  - Karatsuba does 3 multiplications instead of 4 per level, but it does
    more addition/subtraction work per node to get there — computing
    (xhi+xlo) and (yhi+ylo), then recovering the middle term with two
    subtracts (Candidate 3) — divide_and_conquer's combine step is simpler
    (just two products added directly, no algebraic recovery step needed).
  - This is exactly the "constant factor c" from Candidate 5's
    log(T) = log(c) + p·log(n) equation — Karatsuba has a smaller exponent
    (p ≈ 1.585 vs 2) but a larger constant c, because of that extra
    bookkeeping overhead per recursive call.
  - At small n, the constant-factor term dominates the comparison (the
    exponent gap hasn't had room to compound yet across enough recursive
    levels), so divide_and_conquer's simpler combine step can actually be
    faster in real wall-clock time even though it's asymptotically worse.
  - The crossover is where the exponent advantage finally outweighs the
    constant-factor disadvantage — mechanically, that's the n where
    c_karatsuba · n^1.585 first dips below c_divide_and_conquer · n^2,
    which algebraically only happens once n is large enough, not at n=2
    where there's barely any recursive depth for the exponent gap to act
    over.
  - Practical way to find it without extra theory: your existing benchmark
    data already has both algorithms' times at the same n values — the
    crossover is just the smallest n in your table where Karatsuba's
    measured time drops below divide_and_conquer's, no new code needed
    beyond reading your own CSV.
  - This closes the loop on the whole assignment's motivation bullet about
    predicting the plot in advance and then seeing it: the crossover
    existing at all, and existing above n=2 specifically, is the concrete,
    visible fingerprint of "lower asymptotic exponent, higher constant
    factor" — the same tradeoff idea that's usually taught only in the
    abstract.
