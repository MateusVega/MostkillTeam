from flask import Flask, render_template, abort, url_for
import json
import random

app = Flask(__name__)

ALLOWED_MODES = ["career", "masters", "champions"]

@app.route("/")
def index():
    return render_template("index.html", description="Play the Valorant Most Kill Team game and achieve the highest score! Test your skills and compete for the top spot.")

@app.route("/<mode>/", defaults={'score_string': None})
@app.route("/<mode>/<score_string>")
def game(mode, score_string):
    if score_string is None or not score_string.isdigit():
        score_string = None
    if (not score_string is None) and int(score_string) > 100000:
        score_string = None
    if mode in ALLOWED_MODES:
        return render_template("game.html", description="Play the Valorant Most Kill Team game and achieve the highest score! Test your skills and compete for the top spot.", mode=mode, title="Game", score_string=score_string)
    else:
        abort(404)

@app.route("/players")
def players():
    data = []
    with open('data/career.json') as f:
        data.append(json.load(f))
    with open('data/masters.json') as f:
        data.append(json.load(f))
    with open('data/champions.json') as f:
        data.append(json.load(f))
    return render_template("players.html", title="Players Stats", description="See all the stats of each Valorant player.", data=data)

@app.route("/get_player/<mode>")
def get_player(mode):
    if mode not in ALLOWED_MODES:
        abort(404)
    try:
        with open(f'data/{mode}.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        abort(404)

    if not data:
        abort(404)
    return random.choice(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', title='Page not found', description="Most kill Team page not found."), 404

if __name__ == '__main__':
    app.run()
    #vercel dev
    #vercel --prod