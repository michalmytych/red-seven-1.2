from flask import jsonify
from flask import Flask, redirect
from flask import render_template
from flask import session
from flask import request

app = Flask(__name__)
app.secret_key = 'fde9f55f-f255-420e-95fa-fa4bb6a41064'

players_nicknames = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        if nickname in players_nicknames:
            return render_template('home.html', error='Ten nickname jest już zajęty!', nicknames=players_nicknames)
        players_nicknames.insert(0, nickname)
        print(players_nicknames)

    return render_template('home.html', nicknames=players_nicknames)


# flask --app=./http/app.py run
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
