value_rank = {
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'T',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A'
}

rank_value = {v: k for k, v in value_rank.items()}

hand_value = {
    1: "high_card",
    2: "pair",
    3: "two_pair",
    4: "three_of_a_kind",
    5: "straight",
    6: "flush",
    7: "full_house",
    8: "four_of_a_kind",
    9: "straight_flush",
    10: "royal_flush"
}

def is_flush(hand):
    suits = [card[1] for card in hand]
    return len(set(suits)) == 1

def is_straight(hand):
    rank_values = sorted([rank_value[card[0]] for card in hand])
    if rank_values == list(range(min(rank_values), max(rank_values) + 1)):
        high_card = max(rank_values)
        return True, value_rank[high_card]
    return False, None

def is_royal_flush(hand):
    if is_flush(hand) and is_straight(hand)[0]:
        ranks = [card[0] for card in hand]
        return 'A' in ranks and 'T' in ranks
    return False

def count_ranks(hand):
    rank_count = {}
    for card in hand:
        rank = card[0]
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
    return rank_count

def check_duplicates(hand):
    rank_count = count_ranks(hand)
    hand_status = {
        'four_of_a_kind': 0,
        'full_house': 0,
        'three_of_a_kind': 0,
        'two_pair': 0,
        'pair': 0
    }
    
    counts = list(rank_count.values())
    if 4 in counts:
        hand_status['four_of_a_kind'] = 1
    elif 3 in counts:
        if counts.count(2) == 1:
            hand_status['full_house'] = 1
        else:
            hand_status['three_of_a_kind'] = 1
    elif counts.count(2) == 2:
        hand_status['two_pair'] = 1
    elif 2 in counts:
        hand_status['pair'] = 1
    
    return hand_status

def evaluate_hand(hand):
    hand_status = {
        'flush': is_flush(hand),
        'straight': is_straight(hand)[0],
        'royal_flush': is_royal_flush(hand),
        **check_duplicates(hand)
    }
    
    for rank, name in sorted(hand_value.items(), reverse=True):
        if hand_status.get(name.replace(" ", "_"), 0):
            return rank, name
    
    # Determine high card if no other hand is found
    high_card = max([rank_value[card[0]] for card in hand])
    return 1, f"high_card ({value_rank[high_card]})"

def compare_hands(p1_hand, p2_hand):
    p1_rank, p1_hand_value = evaluate_hand(p1_hand)
    p2_rank, p2_hand_value = evaluate_hand(p2_hand)
    
    if p1_rank > p2_rank:
        return "Player 1 wins", p1_hand_value
    elif p1_rank < p2_rank:
        return "Player 2 wins", p2_hand_value
    else:
        # Compare the ranks of pairs or other combinations
        p1_rank_counts = count_ranks(p1_hand)
        p2_rank_counts = count_ranks(p2_hand)
        
        p1_sorted_ranks = sorted(p1_rank_counts.items(), key=lambda x: (x[1], rank_value[x[0]]), reverse=True)
        p2_sorted_ranks = sorted(p2_rank_counts.items(), key=lambda x: (x[1], rank_value[x[0]]), reverse=True)
        
        for (p1_rank, p1_count), (p2_rank, p2_count) in zip(p1_sorted_ranks, p2_sorted_ranks):
            if rank_value[p1_rank] > rank_value[p2_rank]:
                return "Player 1 wins", p1_hand_value
            elif rank_value[p1_rank] < rank_value[p2_rank]:
                return "Player 2 wins", p2_hand_value
        
        # If still tied, compare high cards
        p1_high_cards = sorted([rank_value[card[0]] for card in p1_hand], reverse=True)
        p2_high_cards = sorted([rank_value[card[0]] for card in p2_hand], reverse=True)
        
        for p1_card, p2_card in zip(p1_high_cards, p2_high_cards):
            if p1_card > p2_card:
                return "Player 1 wins", p1_hand_value
            elif p1_card < p2_card:
                return "Player 2 wins", p2_hand_value
        
        return "It's a tie", "tie"

def read_hands_from_file(filename):
    with open(filename, 'r') as file:
        hands = file.readlines()
    return [hand.strip() for hand in hands]

def count_wins_and_hand_values(hands):
    p1_wins = 0
    p2_wins = 0
    ties = 0
    
    for hand in hands:
        cards = hand.split(" ")
        p1_hand = cards[:5]
        p2_hand = cards[5:]
        
        result, winning_hand_value = compare_hands(p1_hand, p2_hand)
        
        if result == "Player 1 wins":
            p1_wins += 1
        elif result == "Player 2 wins":
            p2_wins += 1
        else:
            ties += 1
    
    return p1_wins, p2_wins, ties

# Example usage
hands = read_hands_from_file('scratch/poker_hands_output.txt')
p1_wins, p2_wins, ties = count_wins_and_hand_values(hands)
print(f"Player 1 wins: {p1_wins}")
print(f"Player 2 wins: {p2_wins}")
print(f"Ties: {ties}")