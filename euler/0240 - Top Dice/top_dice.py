# There are 1111 ways in which 
# how many ways can 20x 12-sided dice be rolled so that the top-ten sum to 70?

### Error in dealing with large numbers

# Qtyx5 6-sided dice can be rolled so that the top three sum to 15.
from functools import lru_cache
import math

def count_ways(target, die_sides, die_quantity, number_to_score):
    @lru_cache(None)
    def helper(remaining_dice, current_dice):
        if remaining_dice == 0:
            if sum(sorted(current_dice)[-number_to_score:]) == target:
                return 1
            else:
                return 0
        count = 0
        for i in range(1, die_sides + 1):
            count += helper(remaining_dice - 1, current_dice + (i,))
        return count

    return helper(die_quantity, ())

# Parameters
target_value = 70
die_sides = 12
die_quantity = 20
number_to_score = 10

# Calculate the number of ways
number_of_ways = count_ways(target_value, die_sides, die_quantity, number_to_score)
print(number_of_ways)