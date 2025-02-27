# 70 Coloured balls are placed in an urn,
# 10 for each of the 7 rainbow colours
# What is the expected number of distinct colours in 20 randomly picked balls?
# give your answer with 9 digits after the decimal point.
import math

def expected_distinct_colors(contents, draws):
    total_balls = sum(contents.values())
    colors = list(contents.keys())
    total_colors = len(colors)
    
    expected_value = 0
    
    for k in range(1, total_colors + 1):
        prob_k_distinct = 0
        for i in range(k):
            prob_k_distinct += (-1)**i * math.comb(k, i) * ((k - i) / total_colors)**draws
        expected_value += prob_k_distinct
    
    return expected_value

# Given contents dictionary
contents = { 
    "red": 10,
    "orange": 10,
    "yellow": 10,
    "green": 10,
    "blue" : 10,
    "indigo": 10,
    "violet": 10
}

# Number of draws
draws = 20

# Calculate the expected number of distinct colors
expected_value = expected_distinct_colors(contents, draws)

print(f"Expected number of distinct colors after {draws} draws: {expected_value}")