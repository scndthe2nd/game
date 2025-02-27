from itertools import product, combinations_with_replacement, permutations
from functools import lru_cache
import math

target_value = 70
die_sides = 12
die_quantity = 20
number_to_score = 10
def combinations(n, k):
    """Return C(n, k), the number of combinations of k out of n."""
    c = 1
    k = min(k, n - k)
    for i in range(1, k + 1):
        c *= (n - k + i)
        c //= i
    return c

@lru_cache(maxsize=None)
def T(n, d, k, t):
    """Return the number of ways n distinguishable d-sided dice can be
    rolled so that the top k dice sum to t.

    """
    # Base cases
    if ???: return 1
    if ???: return 0

    # Divide and conquer. Let N be the maximum number of dice that
    # can roll exactly d.
    N = ???
    return sum(combinations(n, i)
               * T(n - i, d - 1, ???)
               for i in range(N + 1))

output = T(die_quantity,die_sides,number_to_score,target_value)
print (output)