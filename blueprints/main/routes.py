from . import main_blueprint
from flask import render_template, request, jsonify
from .functions.get_data import get_data
from .functions.get_history import get_history

@main_blueprint.route('/', methods=["GET"])
def main():
    return render_template("index.html")

    
@main_blueprint.route('/player', methods=["POST"])
def player():
    summoner_name = request.form["summoner_name"]
    data_json = get_data(summoner_name)
    count_history = 1
    history_array = get_history(data_json, count_history)

    return jsonify(history_array)