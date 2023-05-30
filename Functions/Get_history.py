import requests
def History(data_json,var_Key,count_history):
    puuid = data_json["puuid"]
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count_history}&api_key={var_Key}"
    response_history = requests.get(url)
    if response_history.status_code == 200:
        History = response_history.content.decode()
        history_array = History.replace("[","").replace("]","").replace('"',"").split(",")
    else:
        print("erro", response_history.status_code)
    for i in history_array:
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{i}?api_key={var_Key}"
        response_match_info = requests.get(url)
        if response_match_info.status_code == 200:
            match = response_match_info.json()
            print(match)
        else:
            print("erro no match ID", response_match_info.status_code)