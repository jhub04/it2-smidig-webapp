from flask import Flask, render_template
from capitals_quiz import velg_tilfeldig_land, hovedstad

tilfeldig_land = velg_tilfeldig_land()
hovedstad = hovedstad(tilfeldig_land)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capitals_quiz")
def rute_capitals_quiz():
    return render_template("capitals_quiz.html", tilfeldig_land=tilfeldig_land)

@app.route("/flag_quiz")
def rute_flag_quiz():
    return render_template("flag_quiz.html")

@app.route("/domains_quiz")
def rute_domains_quiz():
    return render_template("domains_quiz.html")

@app.route("/mix_quiz")
def rute_mix_quiz():
    return render_template("mix_quiz.html")

app.run(debug=True)