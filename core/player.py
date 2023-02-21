from core.hand import Hand
from core.palette import Palette
from core.turn import Turn


class Player:
    def __init__(self, _id):
        self.id = _id
        self.hand = Hand()
        self.palette = Palette()
        self.active = True

    def set_card_to_canvas(self, index, canvas):
        self.hand.set_card_to_canvas(index, canvas)

    def set_card_to_palette(self, index):
        self.hand.set_card_to_palette(index, self.palette)
        self.hand.sort()
        self.palette.sort()

    def play_turn(self, turn: Turn, canvas):
        if turn.to_canvas is not None:
            self.set_card_to_canvas(int(turn.to_canvas) - 1, canvas)
            self.hand.sort()
        if turn.to_palette is not None:
            self.set_card_to_palette(int(turn.to_palette) - 1)
            self.hand.sort()

