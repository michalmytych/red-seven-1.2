from uuid import uuid4

from flask import jsonify
from flask import Flask, redirect
from flask import render_template
from flask import session
from flask import request
from flask_cors import CORS

from core.Server import Server
from core.Game import GameStatus
from core.Turn import Turn


app = Flask(__name__)
CORS(app)
app.secret_key = 'SECRET KEY'

servers = {}

@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')


@app.route('/api/servers', methods=['GET'])
def get_servers():
  servers_dump = []
  for server_key in servers:
    server = servers.get(server_key)
    if server:
      servers_dump.append(server.serialize())
  return jsonify(servers_dump)
  

@app.route('/servers/new-server', methods=['POST'])
def new_server():
  server_key = request.form['server_key']
  host_id = uuid4()
  server = Server(server_key, host_id)    
  servers[server.key] = server  
  # server.players.append(host_id)
  session['server_key'] = server.key
  session['player_id'] = host_id
  return home()


@app.route('/servers/<server_key>/await-game', methods=['GET'])
def await_game(server_key):
  server = servers.get(server_key)
  if not server:
    return render_template('not_found.html')
  player_id = session.get('player_id')
  if player_id not in server.players:
    if player_id != server.host_id:
      player_id = uuid4()
      session['player_id'] = player_id
    server.players.append(player_id)
  return render_template('await_game.html', server=server)  


@app.route('/servers/<server_key>/start-game', methods=['POST'])
def start_game(server_key):
  server = servers.get(server_key)
  if not server:
    return render_template('not_found.html')
  player_id = session.get('player_id')
  if player_id != server.host_id:
    return render_template('not_permitted.html')
  server.init_game()
  return game(server_key)  


@app.route('/servers/<server_key>/game/run-turn', methods=['POST'])
def run_turn(server_key):
  server = servers.get(server_key)
  turn_data = request.form['turn']
  turn = Turn(
    session.get('player_id'),
    turn_data['to_canvas'],
    turn_data['to_palette']
  )
  run_completed = server.game.run_player_turn(turn)
  if not run_completed:
    return 'Nie wykonano tury. Zrobiłeś coś źle!'
  return game(server_key)


@app.route('/servers/<server_key>/game', methods=['GET'])
def game(server_key):
  server = servers.get(server_key)

  if not server:
    return render_template('not_found.html')

  client_id = session.get('player_id')
  player = server.get_player_by_id(client_id)
  
  if not player:
    return render_template('not_permitted.html')
  
  if not player.joined:
    player.joined = True

  if server.players_joined:
    if GameStatus.CARDS_DEALT not in server.game.statuses:
      server.game.prepare_lap()

  other_players = server.get_other_players(client_id)

  return render_template('game.html', server=server, player=player, other_players=other_players)  


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
