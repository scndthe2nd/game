import random

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']

# Generate a deck of cards with unique rank-suit combinations
def create_deck():
    return [f"{rank}{suit}" for rank in ranks for suit in suits]

def generate_poker_hands(num_hands):
    deck = create_deck()
    random.shuffle(deck)
    
    hands = []
    for _ in range(num_hands):
        hand = deck[:5]
        hands.append(hand)
        deck = deck[5:]  # Remove the dealt cards from the deck
    
    return hands

def generate_poker_hands_string(num_hands):
    hands = generate_poker_hands(num_hands)
    hands_string = " ".join([" ".join(hand) for hand in hands])
    return hands_string

# Example usage
num_hands = 2  # Specify the number of poker hands to generate
poker_hands_string = generate_poker_hands_string(num_hands)

def generate_file(lines):
    with open('scratch/poker_hands_output.txt', "w") as file:
        for _ in range(lines):
            file.write(generate_poker_hands_string(num_hands) + "\n")

generate_file(100000)