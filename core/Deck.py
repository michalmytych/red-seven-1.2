from random import shuffle
from core.Card import Card


class Deck:

    def __init__(self):
        self.cards = []
        self.create_new_deck()
        self.shuffle_deck()

    def create_new_deck(self):
        for color in Card.DICT_OF_COLORS.keys():
            for value in Card.LIST_OF_VALUES:
                self.cards.append(Card(color, value))

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card_to_hand(self, hand):
        card = self.cards.pop(0)
        hand.cards.append(card)

    def deal_card_to_palette(self, palette):
        card = self.cards.pop(0)
        palette.cards.append(card)
