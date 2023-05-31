# import sys
# import requests
# from flask import Flask, request, render_template, jsonify
# from env import var_Key, var_BR1
# from Functions.Get_Image import *
# from Functions.Get_data import *
# from Functions.Get_history import *
# summoner_name = "Big0r"
# champion = "Lulu"
# count_history = 1
# #url = f"https://{var_BR1}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={var_Key}"
# #url_champion = f"http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/{champion}.png"

# #response = requests.get(url)
# #response_champion = requests.get(url_champion, champion)

# if champion != "":
#     imagem(champion)
# else:
#     print("No champion")

# if summoner_name != "":
#     data_json, response_data = data(summoner_name, var_BR1, var_Key)
#     print(response_data)
# else:
#     print("No summoner name")

# if summoner_name != "" and response_data.status_code == 200:
#     History(data_json,var_Key,count_history)

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         summoner_name = request.form["summoner_name"]

#         if summoner_name != "":
#             # Call the functions to retrieve data and history
#             data_json, response_data = data(summoner_name, var_BR1, var_Key)
#             history_json = History(data_json, var_Key, count_history)

#             return jsonify(history_json)

#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run()

import sys
import requests
from flask import Flask, request, render_template, jsonify
from env import var_Key, var_BR1
from Functions.Get_Image import *
from Functions.Get_data import *
from Functions.Get_history import History

# Define Flask application
app = Flask(__name__)

# Route for the root URL ("/")
@app.route("/nome", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        summoner_name = request.form["summoner_name"]
        # Call the functions to retrieve data and history
        data_json, response_data = data(summoner_name, var_BR1, var_Key)
        count_history = 1
        history_array = History(data_json, var_Key, count_history)

        return jsonify(history_array)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()