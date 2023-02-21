from uuid import uuid4
from flask import jsonify
from flask import Flask, redirect
from flask import render_template
from flask import session
from flask import request
from core.config import PLAYERS_LIMIT
from core.game import Game

app = Flask(__name__)
app.secret_key = 'fde9f55f-f255-420e-95fa-fa4bb6a41064'

games = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    session['nickname'] = None
    session['game'] = None
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        game = request.form.get('game')
        if games.get(game):
            if type(games[game]) is list:
                if len(games[game]) < PLAYERS_LIMIT:
                    if nickname in games[game]:
                        return render_template('home.html', error='Ten nickname jest już zajęty!')
                    games[game].append(nickname)
                else:
                    return render_template('home.html', error='Ta gra osiągnęła limit graczy!')
        else:
            games[game] = [nickname]
        session['game'] = game
        session['nickname'] = nickname
        return redirect('/wait')

    return render_template('home.html')


@app.route('/wait', methods=['GET'])
def wait():
    game_id = session.get('game')
    _game = games.get(game_id)

    if type(_game) is Game:
        return redirect('/play')

    if _game and len(_game) == PLAYERS_LIMIT:
        games[game_id] = Game(_game)
        return redirect('/play')

    return render_template('wait.html')


@app.route('/play', methods=['GET'])
def play():
    return f'Rozgrywka w P{session["game"]}'


# flask --app=./http/app.py run
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
