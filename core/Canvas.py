from core.Card import Card


class Canvas:

    RULES = {
        6: 'Largest card.',
        5: 'Max one value card',
        4: 'Max one color card',
        3: 'Max even value card',
        2: 'Max different colors card',
        1: 'Max order of card values',
        0: 'Max card with value less then 4'
    }

    def __init__(self):
        self.card = Card(6, 'START')

    @staticmethod
    def get_winner_by_red_rule(palettes):
        largest_cards = {palette[0]: palette[1].cards[0] for palette in palettes.items()}
        largest_card = sorted(
            largest_cards.items(), key=lambda item: (item[1].value, item[1].color), reverse=True
        )[0][0]
        return largest_card

    @staticmethod
    def get_winner_by_non_red_rule(palettes, palette_func):
        numbers = {
            palette[0]: getattr(palette[1], palette_func)()
            for palette in palettes.items()
        }
        max_points = max(numbers.values())
        temp = {
            palette[0]: palette[1] for palette in palettes.items()
            if getattr(palette[1], palette_func)() == max_points
        }
        return Canvas.get_winner_by_red_rule(temp)

    def get_winner(self, players):
        palettes = {num: player.palette for num, player in enumerate(players)}
        if self.card.color == 6:
            return self.get_winner_by_red_rule(palettes)
        if self.card.color == 5:
            return self.get_winner_by_non_red_rule(palettes, 'get_one_value_cards_number')
        if self.card.color == 4:
            return self.get_winner_by_non_red_rule(palettes, 'get_one_color_cards_number')
        if self.card.color == 3:
            return self.get_winner_by_non_red_rule(palettes, 'get_even_cards_number')
        if self.card.color == 2:
            return self.get_winner_by_non_red_rule(palettes, 'get_different_colors_card_number')
        if self.card.color == 1:
            return self.get_winner_by_non_red_rule(palettes, 'get_largest_order_of_cards')
        if self.card.color == 0:
            return self.get_winner_by_non_red_rule(palettes, 'get_less_then_four_cards_number')
        try:
            assert False
        except AssertionError:
            print('Canvas has illegal card')
