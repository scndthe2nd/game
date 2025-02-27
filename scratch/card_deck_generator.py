import random

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']

# Generate a deck of cards with unique rank-suit combinations
deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

def generate_deck_order():
    # Shuffle the deck
    random.shuffle(deck)
    return deck

# Example usage
shuffled_deck = generate_deck_order()
print(" ".join(shuffled_deck))