from flask import render_template, request, jsonify
from . import main_blueprints
from Functions.Get_puuid import *
from env import var_Key, var_BR1, var_americas

@main_blueprints.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("passou route")
        summoner_name = request.form["summoner_name"]
        tag = request.form["tag"]
        puuid = data(summoner_name, var_BR1, var_Key, tag, var_americas)
        print(puuid)

        return jsonify({'puuid': puuid})

    return render_template("base.html")