card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

hand_cards = []
while len(hand_cards) < 6:
    card = input()
    if card in card_values.keys():
        hand_cards.append(card)

summed_values = 0
for card in hand_cards:
    summed_values += card_values[card]

print(summed_values / len(hand_cards))
