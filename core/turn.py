class Turn:
    def __init__(self, player_id: str, to_palette = None, to_canvas = None):
        self.to_palette = to_palette
        self.to_canvas = to_canvas
        self.player_id = player_id
