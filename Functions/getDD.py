import requests

champion_json = {}
versions = []
latest_version = None

def get_latest_ddragon():
    global champion_json, latest_version
    if champion_json:
        return champion_json

    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    versions_response = requests.get(versions_url)
    if versions_response.status_code == 200:
        versions = versions_response.json()  # Update the shared variable
        print("Versions:", versions[0])
        latest_version = versions[0]
        print("Latest version:", latest_version)
    else:
        print("Error fetching versions:", versions_response.status_code)
        return {}

    ddragon_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
    ddragon_response = requests.get(ddragon_url)
    if ddragon_response.status_code == 200:
        champions_data = ddragon_response.json()
        champion_json = champions_data["data"]
        return champion_json
    else:
        print("Error fetching champion data:", ddragon_response.status_code)
        return {}

def process_champions(champion_data):
    champion_list = []
    for champ_name, champ_info in champion_data.items():
        champ_info['id'] = champ_info['key']
        champ_info['name'] = champ_name
        champion_list.append(champ_info)
    return champion_list

champion_data = get_latest_ddragon()

champion_list = process_champions(champion_data)

champion_names_and_ids = [(champ['name'], champ['id'], champ['title']) for champ in champion_list]

# Export latest_version
exported_latest_version = latest_version
