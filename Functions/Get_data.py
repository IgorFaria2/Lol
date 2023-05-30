import requests
def data(summoner_name, var_BR1, var_Key):
    url = f"https://{var_BR1}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={var_Key}"
    response_data = requests.get(url)    
    if response_data.status_code == 200:
        data = response_data.json()
        return data, response_data
    else:
        print("Request failed with status code:", response_data.status_code)
        return
