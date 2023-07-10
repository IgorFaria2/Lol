from blueprints.main.functions.constants import DEV_KEY , REGION_BR_KEY
import requests

def get_history(data_json, count_history):
    puuid = data_json["puuid"]
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count_history}&api_key={DEV_KEY}"
    response_history = requests.get(url)
    if response_history.status_code == 200:
        history = response_history.content.decode()
        history_array = history.replace("[","").replace("]","").replace('"',"").split(",")
    else:
        print("Error", response_history.status_code)
        return []

    matches = []
    for i in history_array:
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{i}?api_key={DEV_KEY}"
        response_match_info = requests.get(url)
        if response_match_info.status_code == 200:
            match = response_match_info.json()
            matches.append(match)
        else:
            print("Error in match ID", response_match_info.status_code)

    return matches