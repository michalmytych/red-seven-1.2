class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return_string = ''
        for card in self.cards:
            return_string += str(card) + '\n'
        return return_string

    def set_card_to_canvas(self, index, canvas):
        card = self.cards.pop(index)
        canvas.card = card

    def set_card_to_palette(self, index, palette):
        card = self.cards.pop(index)
        palette.cards.append(card)

    def sort(self):
        self.cards.sort(key=lambda x: (x.value, x.color), reverse=True)
