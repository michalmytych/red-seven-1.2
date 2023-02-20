from core.Hand import Hand
from core.Palette import Palette
from core.Turn import Turn


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

    def run_turn(self, canvas, turn: Turn):
        self.hand.sort()
        if len(turn.to_canvas):
            for card_number in turn.to_canvas:
              self.hand.set_card_to_canvas(card_number, canvas)              
        if len(turn.to_palette):
            for card_number in turn.to_palette:
              self.hand.set_card_to_palette(card_number, self.palette)
        self.hand.filter()
        self.hand.sort()
        self.palette.sort()

