from core.Canvas import Canvas
from core.Deck import Deck
from core.Player import Player


class Game:

    def __init__(self, number_of_players):
        self.players = [Player() for _ in range(number_of_players)]
        self.deck = Deck()
        self.canvas = Canvas()
        self.player_counter = 0

    def deal_cards(self):
        for player in self.players:
            for i in range(7):
                self.deck.deal_card_to_hand(player.hand)
            self.deck.deal_card_to_palette(player.palette)

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

    def run_lap(self):
        # rozdaj karty
        self.deal_cards()
        # sprawdzenie reguł po rozegraniu kart przez wszystkich graczy
        # Tutaj chyba wywali bład jak nie znajdzie gracza ????
        self.player_counter = self.check_winner() + 1
        self.check_player_counter()
        while True:
            if len(self.players[self.player_counter].hand.cards) < 1:
                self.players[self.player_counter].active = False
            if self.players[self.player_counter].active:
                self.players[self.player_counter].run_turn(
                    self,
                    self.player_counter,
                    self.canvas
                )
            if self.check_winner() != self.player_counter:
                self.players[self.player_counter].active = False
            winner = self.check_active_players()
            if winner:
                print(f'Lap ends, winner is: {winner} player')
                break
            self.player_counter += 1
            self.check_player_counter()
