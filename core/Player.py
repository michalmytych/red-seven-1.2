from core.Hand import Hand
from core.Palette import Palette


class Player:

    def __init__(self, _id = None):
        # @todo rm
        self.obj_id = id(self)
        # @todo rm
        self.id = _id
        self.hand = Hand()
        self.palette = Palette()
        self.active = True
        self.joined = False

    def set_card_to_canvas(self, index, canvas):
        self.hand.set_card_to_canvas(index, canvas)

    def set_card_to_palette(self, index):
        self.hand.set_card_to_palette(index, self.palette)
        self.hand.sort()
        self.palette.sort()

    def display_player_desk(self, game, player_number):
        self.hand.sort()
        game.display_desk()
        print(f'Your({player_number + 1} player) hand: ')
        for num, card in enumerate(self.hand.cards):
            print(f'{num + 1}: {card}')

    def run_turn(self, game, player_number, canvas, turn):
        self.display_player_desk(game, player_number)
        answer = input('Do you want set card to canvas(y/n): ')
        if answer.lower() == 'y':
            card_number = input('Select number of card you want to set to canvas: ')
            self.set_card_to_canvas(int(card_number)-1, canvas)
            self.display_player_desk(game, player_number)
        answer = input('Do you want set card to palette(y/n): ')
        if answer.lower() == 'y':
            card_number = input('Select number of card you want to set to palette: ')
            self.set_card_to_palette(int(card_number)-1)
            self.display_player_desk(game, player_number)
