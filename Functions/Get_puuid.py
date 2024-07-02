import requests
def data(summoner_name, var_BR1, var_Key, tag, var_americas):
    url = f"https://{var_americas}/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag}?api_key={var_Key}"
    response_data = requests.get(url)
    print(url)
    if response_data.status_code == 200:
        puuid = response_data.json()["puuid"]
        return puuid
    else:
        print("Request failed with status code:", response_data.status_code)
        return
