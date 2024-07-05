import os, requests
from Functions.getDD import exported_latest_version

# def imagem(champion):
#     url_champion = f"http://ddragon.leagueoflegends.com/cdn/{exported_latest_version}/img/champion/{champion}.png"
#     response_champion = requests.get(url_champion, champion)
#     print("0")
#     if response_champion.status_code == 200:
#         print("1")
#         imagem = response_champion.content
#         arquivo = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "imagens", f"{champion}.png"), "wb")

#         arquivo.write(imagem)

#         arquivo.close()
#         return
#     else:
#         print("Request failed with status code:", response_champion.status_code)
#         return
    
def imagem(champion):
    url_champion = f"http://ddragon.leagueoflegends.com/cdn/{exported_latest_version}/img/champion/{champion}.png"
    # Check if the URL is valid
    response_champion = requests.head(url_champion)
    if response_champion.status_code == 200:
        return url_champion
    else:
        print("Request failed with status code:", response_champion.status_code)
        return None