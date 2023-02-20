from collections import Counter
from core.Card import Card


class Palette:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return_string = ''
        for card in self.cards:
            return_string += str(card) + '\n'
        return return_string

    def sort(self):
        self.cards.sort(key=lambda x: (x.value, x.color), reverse=True)

    def get_one_color_cards_number(self):
        colors = Counter([card.color for card in self.cards])
        return max(colors.values())

    def get_one_value_cards_number(self):
        values = Counter([card.value for card in self.cards])
        return max(values.values())

    def get_different_colors_card_number(self):
        colors = Counter([card.color for card in self.cards])
        return len(colors.values())

    def get_even_cards_number(self):
        values = [card.value for card in self.cards if not card.value % 2]
        return len(values)

    def get_less_then_four_cards_number(self):
        values = [card.value for card in self.cards if card.value < 4]
        return len(values)

    def get_largest_order_of_cards(self):
        largest_order = 1
        order = 0
        values = [card.value for card in self.cards]
        for value in Card.LIST_OF_VALUES:
            if value in values:
                order += 1
                if order > largest_order:
                    largest_order = order
            else:
                order = 0
        return largest_order
