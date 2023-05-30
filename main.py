import sys, requests
from env import var_Key, var_BR1
from Functions.Get_Image import *
from Functions.Get_data import *
from Functions.Get_history import *
summoner_name = "Big0r"
champion = "Katarina"
count_history = 1
#url = f"https://{var_BR1}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={var_Key}"
#url_champion = f"http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/{champion}.png"

#response = requests.get(url)
#response_champion = requests.get(url_champion, champion)

if champion != "":
    imagem(champion)
else:
    print("No champion")

if summoner_name != "":
    data_json, response_data = data(summoner_name, var_BR1, var_Key)
    print(response_data)
else:
    print("No summoner name")

if summoner_name != "" and response_data.status_code == 200:
    History(data_json,var_Key,count_history)