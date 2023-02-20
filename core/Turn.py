class Turn:
    
    def __init__(self, player_id, to_canvas, to_palette):
        self.player_id = player_id
        self.to_canvas = Turn.parse_cards(to_canvas)
        self.to_palette = Turn.parse_cards(to_palette)

    @classmethod
    def parse_cards(cls, cards_str: str):
        cards_numbers = [int(cards_str) for cards_str in cards_str.split(',') if cards_str.isnumeric()]
        return cards_numbers

    def as_log(self):
        return f"""
        * * *
        Turn of player [{self.player_id}]
          To canvas: {[card for card in self.to_canvas]}
          To palette: {[card for card in self.to_palette]}
        * * *
        """
