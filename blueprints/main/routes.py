from . import main_blueprint
from flask import render_template
from Functions.Get_data import *

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        summoner_name = request.form["summoner_name"]
        # Call the functions to retrieve data and history
        data_json, response_data = data(summoner_name, var_BR1, var_Key)
        count_history = 1
        history_array = History(data_json, var_Key, count_history)

        return jsonify(history_array)

    return render_template("index.html")