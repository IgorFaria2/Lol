import os, requests
def imagem(champion):
    url_champion = f"http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/{champion}.png"
    response_champion = requests.get(url_champion, champion)
    if response_champion.status_code == 200:
        imagem = response_champion.content
        arquivo = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "imagens", f"{champion}.png"), "wb")

        arquivo.write(imagem)

        arquivo.close()
        return
    else:
        print("Request failed with status code:", response_champion.status_code)
        return