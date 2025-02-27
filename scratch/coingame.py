#In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = (1,2,5, 10, 20, 50, 100, 200)
target_value = 200
values_set = coins

def count_ways(target, values):
    # Initialize a list to store the number of ways to make each amount
    ways = [0] * (target + 1)
    ways[0] = 1  # There is one way to make 0, which is to use no coins

    # Iterate over each value in the set
    for value in values:
        # Update the number of ways for each amount from value to target
        for amount in range(value, target + 1):
            ways[amount] += ways[amount - value]

    return ways[target]

number_of_ways = count_ways(target_value, values_set)
print(f"The number of ways to divide {target_value} evenly by the set of values {values_set} is {number_of_ways}.")
