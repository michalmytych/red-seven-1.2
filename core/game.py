from enum import Enum
from core.exceptions import IllegalPlayerActionException
from core.canvas import Canvas
from core.deck import Deck
from core.player import Player
from core.turn import Turn


class Status(Enum):
    INITALIZED = 0
    ROUND_PREPARED = 1
    RUNNING_LAP = 2
    ENDED = 3


class Game:
    def __init__(self, players_ids):
        self.players = [Player(_id) for _id in players_ids]
        self.deck = Deck()
        self.canvas = Canvas()
        self.player_counter = 0
        self.winner = None
        self.statuses = [Status.INITALIZED]

    def deal_cards(self):
        """ Rozdaj karty graczom i rozpocznij ich palety. """
        for player in self.players:
            for i in range(7):
                self.deck.deal_card_to_hand(player.hand)
            self.deck.deal_card_to_palette(player.palette)
        self.statuses.append(Status.ROUND_PREPARED)

    def get_winner_index(self):
        """ Wyznacz indeks zwycięzcy na podstawie obowiązującej reguły. """
        winner_ix = self.canvas.get_winner(self.players)
        return winner_ix

    def adjust_player_counter(self):
        """ Sprawdź licznik będący wskaźnikiem do gracza i wyzeruj go, jeśli zagrał ostatni z graczy. """
        if self.player_counter >= len(self.players):
            self.player_counter = 0

    def get_winner_if_exists(self):
        active_players = 0
        winner = 0
        for num, player in enumerate(self.players):
            if player.active:
                active_players += 1
                winner = num + 1
        if active_players > 1:
            return None
        return winner

    def validate_turn(self, turn: Turn, current_player: Player):
        if turn.player_id != current_player.id:
            raise IllegalPlayerActionException

    def prepare_round(self):
        self.deal_cards()
        self.player_counter = self.get_winner_index() + 1
        self.adjust_player_counter()

    def run_turn(self, turn: Turn):
        # Ustaw status jako: zagywanie kolejki
        self.statuses.append(Status.RUNNING_LAP)

        # Pobierz referencję do aktualnego gracza
        current_player = self.players[self.player_counter]

        # Sprawdź czy zagranie pochodzi od aktualnego gracza
        self.validate_turn(turn, current_player)

        # Sprawdź czy gracz ma karty, jeśli nie - dezaktywuj go
        if len(current_player.hand.cards) < 1:
            current_player.active = False

        # Wykonaj zagrania gracza jeśli jest aktywny
        if current_player.active:
            current_player.play_turn(turn, self.canvas)

        # Jeśli po zagraniu gracz nie wygrał - dezaktywuj go
        if self.get_winner_index() != self.player_counter:
            current_player.active = False

        # Znajdź zwycięzcę jeśli istnieje
        _winner = self.get_winner_if_exists()
        if _winner:
            self.winner = _winner
            self.statuses.append(Status.ENDED)
            return _winner

        # Ustaw następnego gracza jako zagrywającego
        self.player_counter += 1
        self.adjust_player_counter()

        # Jeśli nie ma zwycięzcy, zwróć None
        return None

    def get_player_by_id(self, _id):
        return [p for p in self.players if p.id == _id][0]

