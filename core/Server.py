from core.Game import Game

class Server:

  def __init__(self, key, host_id):
    # @todo rm
    self.obj_id = id(self)
    # @todo rm
    self.key = key
    self.game = None
    self.players = []
    self.players_limit = 2
    self.host_id = host_id

  @property
  def is_active(self):
    return bool(self.game)
  
  @property
  def players_joined(self):
    return self.game and all([player.joined for player in self.game.players])

  def init_game(self):
    self.game = Game(self.players_limit, self.players)

  def get_player_by_id(self, player_id):
    for player in self.game.players:
      if player.id == player_id:
        return player
    return None

  def get_other_players(self, player_id):
    other_players = []
    for player in self.game.players:
      if player.id != player_id:
        other_players.append(player)
    return other_players

  def serialize(self):
    return {
      "key": self.key,
      "players_limit": self.players_limit,
      "active": self.is_active,
      "players_count": len(self.players),
      "host_id": self.host_id
    }
