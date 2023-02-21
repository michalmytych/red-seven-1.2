from uuid import uuid4
from core.game import Game
from core.turn import Turn
from core.config import PLAYERS_LIMIT


def test_run_full_game():
    players_ids = [uuid4() for _ in range(PLAYERS_LIMIT)]
    game = Game(players_ids)

    assert len(game.deck.cards) == 49

    game.prepare_round()

    assert len(game.players) == PLAYERS_LIMIT
    assert all([len(p.hand.cards) == 7 for p in game.players])
    assert all([len(p.palette.cards) == 1 for p in game.players])
    assert game.canvas.card.value == 'START'

    old_player_ix = game.player_counter
    current_player = game.players[game.player_counter]
    turn = Turn(current_player.id, 0, 1)
    game.run_turn(turn)

    if not game.winner:
        assert game.player_counter != old_player_ix
    else:
        assert game.player_counter == old_player_ix
