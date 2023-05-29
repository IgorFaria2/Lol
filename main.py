import sys, requests
from env import var_Key, var_BR1

summoner_name = "Big0r"
# url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={var_Key}"
url = "http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/Lillia.png"
#print(url)

response = requests.get(url)

if response.status_code == 200:
    #data = response.json()  
    #print(response.content)
    imagem = response.content
    arquivo = open("Campeao.png", "wb")

    arquivo.write(imagem)

    arquivo.close()
else:
    print("Request failed with status code:", response.status_code)