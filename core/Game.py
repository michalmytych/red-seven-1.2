from enum import Enum

from core.Canvas import Canvas
from core.Deck import Deck
from core.Player import Player
from core.Turn import Turn


class GameStatus(Enum):
    INITALIZED = 0
    CARDS_DEALT = 1
    RUNNING_LAP = 2
    ENDED = 3


class Game:    

    def __init__(self, number_of_players, players_ids):
        # @todo rm
        self.obj_id = id(self)
        # @todo rm
        if len(players_ids) != number_of_players:
          raise Exception('Liczba graczy jest inna niż wymagana!')
        self.players = [Player(_) for _ in players_ids]
        self.deck = Deck()
        self.canvas = Canvas()
        self.player_counter = 0
        self.winner = None
        self.statuses = [GameStatus.INITALIZED]

    def deal_cards(self):
        for player in self.players:
            for _ in range(7):
                self.deck.deal_card_to_hand(player.hand)
            self.deck.deal_card_to_palette(player.palette)
        self.statuses.append(GameStatus.CARDS_DEALT)

    def check_winner(self):
        winner_num = self.canvas.get_winner(self.players)
        return winner_num

    def check_player_counter(self):
        if self.player_counter >= len(self.players):
            self.player_counter = 0

    def display_desk(self):
        print(f'Canvas card: {self.canvas.card}')
        print()
        for num, player in enumerate(self.players):
            print(f'{num + 1} player palette:')
            print(f'{player.palette}')

    def check_active_players(self):
        active_players = 0
        winner = 0
        for num, player in enumerate(self.players):
            if player.active:
                active_players += 1
                winner = num + 1
        if active_players > 1:
            return None
        return winner

    def run_player_turn(self, turn: Turn):
        search = [player for player in self.players if player.id == turn.player_id]
        if not len(search):
            return False
        player = search[0]
        if len(player.hand.cards) < 1:
            player.active = False
        if player.active:
            player.run_turn(
                self,
                self.player_counter,
                self.canvas,
                turn
            )
        self.post_turn_checks(self)
        if not player.active:
            return False
        return True

    def post_turn_checks(self):
        if self.check_winner() != self.player_counter:
            self.players[self.player_counter].active = False
        self.winner = self.check_active_players()
        if self.winner:
            self.statuses.append(GameStatus.ENDED)
        self.player_counter += 1
        self.check_player_counter()

    def prepare_lap(self):
        print('Preparing lap')
        self.deal_cards()
        self.player_counter = self.check_winner() + 1
        self.check_player_counter()
        self.statuses.append(GameStatus.RUNNING_LAP)

    def run_lap(self):
        while True:
            self.run_player_turn()

    @property
    def current_status(self):
      return self.statuses[-1]
