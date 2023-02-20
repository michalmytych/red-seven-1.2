class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        return_string = ''
        for card in self.cards:
            return_string += str(card) + '\n'
        return return_string
    
    def filter(self):
        self.cards = [card for card in self.cards if card]

    def set_card_to_canvas(self, index, canvas):
        card = self.cards[index]
        canvas.card = card
        self.cards[index] = None

    def set_card_to_palette(self, index, palette):
        card = self.cards[index]
        palette.cards.append(card)
        self.cards[index] = None

    def sort(self):
        self.cards.sort(key=lambda x: (x.value, x.color), reverse=True)
