class Card:
    DICT_OF_COLORS = {
      6: 'red',
      5: 'orange',
      4: 'gold',
      3: 'green',
      2: 'lightblue',
      1: 'navy',
      0: 'blueviolet'
    }
    LIST_OF_VALUES = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        from core.canvas import Canvas
        return f'{Card.DICT_OF_COLORS[self.color]} {self.value} Rule: {Canvas.RULES[self.color]}'

    @property
    def css_color(self):
        return self.DICT_OF_COLORS.get(self.color)

