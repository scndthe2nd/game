
value_rank = {
    1: 'A',
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

set_value = {
    1 : "high_card",
    2 : "pair",
    3 : "two_pair",
    4 : "thee_of_a_kind",
    5 : "streight",
    6 : "flush",
    7 : "full_house",
    8 : "four_of_a_kind",
    9 : "streight_flush",
    10: "royal_flush"
}

suit_value = {
    
}




## Scoring Functions ##
# flush conditions
# for card in hand
#   card_suit = card.split(2)
#   if all card_suit are equal 
#       hand_status {flush = 1}

# streight conditions
# for card in hand
#   card_rank = card.split(1)
#   
# if card_rank_value incriments by 1 for each next card
#   hand_status {streight = 1}

# royal flush conditions
# if hand_status {flush = 1 and streight = 1}
#   for card in hand
#       card_rank = card.split(1)
#   if hand contains card_rank A and card_rank T
#       hand_status {royal_flush = 1}

# duplicates conditions
# for card in hand
#   card_rank = card.split(1)
#       count card_rank
#   if qty of any card_rank = 4
#       hand_status {four_of_a_kind = 1}
#   if qty of any card_rank = 3
#       remove cards from hand that make 3 of a kind
#       if qty of any card_rank = 2
#           hand_status {full_house = 1}
#       else
#           hand_status {three_of_a_kind = 1}
#   if qty of any card_rank = 2
#       remove cards from hand that make 2 of a kind
#       if qty of any card_rank = 2
#           hand status = {two_pair = 1}
#       else
#           hand_status = {pair = 1 }

# high card
# for card in hand
#   card rank = 

## Managing cards

string = "8C TS KC 9H 4S 7D 2S 5D 3S AC"
cards = string.split(" ")
print (cards)
p1_hand = cards[:5]
p2_hand = cards[5:]
print (f"{p1_hand}        {p2_hand}")


# Function to count the quantity of each rank and suit
def count_parts(hand):
    rank_count = {}
    suit_count = {}
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1
    return rank_count, suit_count

p1_rank_count, p1_suit_count = count_parts(p1_hand)
p2_rank_count, p2_suit_count = count_parts(p2_hand)

print(f"Player 1 - Ranks: {p1_rank_count}, Suits: {p1_suit_count}")
print(f"Player 2 - Ranks: {p2_rank_count}, Suits: {p2_suit_count}")