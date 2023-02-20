class Card:

    DICT_OF_COLORS = {
        6: 'red',
        5: 'orange',
        4: 'gold',
        3: 'green',
        2: 'lightblue',
        1: 'navy',
        0: 'violet'
    }
    LIST_OF_VALUES = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.css_bg_color = Card.DICT_OF_COLORS[color].lower()
        self.css_text_color = 'white'
        if self.color == 4 or self.color == 2:
            self.text_color = 'black'

    def __str__(self):        
        from core.Canvas import Canvas
        return f'{Card.DICT_OF_COLORS[self.color]} {self.value} Rule: {Canvas.RULES[self.color]}'

    def to_log(self):
        return f'{Card.DICT_OF_COLORS[self.color]}:{self.value}'
