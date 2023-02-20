from core.Game import Game

class Server:

  def __init__(self, key, host_id):
    self.key = key
    self.game = None
    self.players = []
    self.players_limit = 2
    self.host_id = host_id

  @property
  def is_active(self):
    return bool(self.game)

  def init_game(self):
    self.game = Game(self.players_limit, self.players)

  def serialize(self):
    return {
      "key": self.key,
      "players_limit": self.players_limit,
      "active": self.is_active,
      "players_count": len(self.players),
      "host_id": self.host_id
    }
