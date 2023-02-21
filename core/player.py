from core.hand import Hand
from core.palette import Palette


class Player:
    def __init__(self, _id):
        self.id = _id
        self.hand = Hand()
        self.palette = Palette()
        self.active = True

    def play_turn(self, game, player_counter, canvas):
        pass
