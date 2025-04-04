from collections import Counter

# Define the card values and their ranks
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Define the hand ranks
hand_ranks = {
    "High Card": 1,
    "One Pair": 2,
    "Two Pairs": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}

def get_hand_rank(hand):
    values = sorted([card_values[card[0]] for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    
    is_flush = len(set(suits)) == 1
    is_straight = all(values[i] - values[i+1] == 1 for i in range(len(values) - 1))
    
    value_counts = Counter(values)
    most_common = value_counts.most_common()
    
    if is_flush and values == [14, 13, 12, 11, 10]:
        return (hand_ranks["Royal Flush"], values)
    elif is_flush and is_straight:
        return (hand_ranks["Straight Flush"], values)
    elif most_common[0][1] == 4:
        return (hand_ranks["Four of a Kind"], most_common[0][0], most_common[1][0])
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        return (hand_ranks["Full House"], most_common[0][0], most_common[1][0])
    elif is_flush:
        return (hand_ranks["Flush"], values)
    elif is_straight:
        return (hand_ranks["Straight"], values)
    elif most_common[0][1] == 3:
        return (hand_ranks["Three of a Kind"], most_common[0][0], values)
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        return (hand_ranks["Two Pairs"], most_common[0][0], most_common[1][0], values)
    elif most_common[0][1] == 2:
        return (hand_ranks["One Pair"], most_common[0][0], values)
    else:
        return (hand_ranks["High Card"], values)

def compare_hands(hand1, hand2):
    rank1 = get_hand_rank(hand1)
    rank2 = get_hand_rank(hand2)
    
    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return -1
    else:
        return 0

def count_player1_wins(file_path):
    # Read the poker hands from the file
    with open(file_path, 'r') as file:
        hands = file.readlines()

    player1_wins = 0

    for hand in hands:
        cards = hand.strip().split()
        player1_hand = cards[:5]
        player2_hand = cards[5:]
        
        result = compare_hands(player1_hand, player2_hand)
        
        if result == 1:
            player1_wins += 1

    return player1_wins

# Example usage
file_path = 'poker.txt'
player1_wins = count_player1_wins(file_path)
print(f"Player 1 wins {player1_wins} hands.")