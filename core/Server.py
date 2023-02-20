from core.Game import Game

class Server:

  def __init__(self, key):
    self.key = key
    self.game = None
    self.players = []
    self.players_limit = 2

  def init_game(self):
    self.game = Game(self.players_limit)

  def serialize(self):
    return {
      "key": self.key,
      "players_limit": self.players_limit,
      "active": bool(self.game),
      "players_count": len(self.players)
    }
