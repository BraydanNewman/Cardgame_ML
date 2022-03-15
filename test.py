from card import Card

from_card = Card(0, 2, True)

foundation = [[Card(0, 1, True)], [Card(0, 2, True)], [Card(0, 3, True)], [Card(0, 4, True)]]

for i, item in enumerate(foundation):
    if item[0].suit == from_card.suit:
        foundation_index = i
