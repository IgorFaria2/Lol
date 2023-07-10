from blueprints.main.functions.constants import DEV_KEY , REGION_BR_KEY
import requests

def get_data(summoner_name):
    url = f"https://{REGION_BR_KEY}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={DEV_KEY}"
    response_data = requests.get(url)    
    if response_data.status_code == 200:
        data = response_data.json()
        return data
    else:
        print("Request failed with status code:", response_data.status_code)
        return
