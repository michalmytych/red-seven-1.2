from flask import jsonify
from flask import Flask, redirect
from flask import render_template
from flask import session
from flask import request
from flask_cors import CORS

from core.Server import Server


app = Flask(__name__)
CORS(app)
app.secret_key = 'SECRET KEY'

servers = {}

@app.route('/api/servers', methods=['GET'])
def get_servers():
  servers_dump = []
  for server_key in servers:
    server = servers.get(server_key)
    if server:
      servers_dump.append(server.serialize())
  return jsonify(servers_dump)


@app.route('/new-server', methods=['POST'])
def new_server():
  server_key = request.form['server_key']
  server = Server(server_key)
  session['server_key'] = server.key
  servers[server.key] = server
  
  return home()


@app.route('/', methods=['GET'])
def home():
  return render_template('home.html')
