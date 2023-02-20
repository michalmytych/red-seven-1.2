from core.Hand import Hand
from core.Palette import Palette
from core.Turn import Turn
from core.Logger import Logger


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

    # def display_player_desk(self, game, player_number):
    #     self.hand.sort()
    #     game.display_desk()
    #     print(f'Your({player_number + 1} player) hand: ')
    #     for num, card in enumerate(self.hand.cards):
    #         print(f'{num + 1}: {card}')

    def run_turn(self, canvas, turn: Turn):
        self.hand.sort()
        Logger.log(f'INFO : Running turn for player {turn.player_id}.')
        Logger.log(turn.as_log())
        if len(turn.to_canvas):
            Logger.log('TRUE : len(turn.to_canvas)')
            for card_number in turn.to_canvas:
              self.hand.set_card_to_canvas(card_number, canvas)              
        if len(turn.to_palette):
            Logger.log('TRUE : len(turn.to_palette)')
            for card_number in turn.to_palette:
              self.hand.set_card_to_palette(card_number, self.palette)
        self.hand.filter()
        self.hand.sort()
        self.palette.sort()
        Logger.log(f'INFO : Turn for player {turn.player_id} finished.')

    # def run_turn(self, game, player_number, canvas, turn):
    #     self.display_player_desk(game, player_number)
    #     answer = input('Do you want set card to canvas(y/n): ')
    #     if answer.lower() == 'y':
    #         card_number = input('Select number of card you want to set to canvas: ')
    #         self.set_card_to_canvas(int(card_number)-1, canvas)
    #         self.display_player_desk(game, player_number)
    #     answer = input('Do you want set card to palette(y/n): ')
    #     if answer.lower() == 'y':
    #         card_number = input('Select number of card you want to set to palette: ')
    #         self.set_card_to_palette(int(card_number)-1)
    #         self.display_player_desk(game, player_number)
