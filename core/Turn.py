class Turn:
    def __init__(self, player_id, to_canvas, to_palette):
        self.player_id = player_id
        self.to_canvas = to_canvas
        self.to_palette = to_palette

    def as_log(self):
        return f"""
        * * *
        Turn of player [{self.player_id}]
          To canvas: {[card.to_log() for card in self.to_canvas]}
          To palette: {[card.to_log() for card in self.to_palette]}
        * * *
        """
