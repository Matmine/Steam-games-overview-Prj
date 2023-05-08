import requests
import csv

# Remplacez VOTRE_CLE_API par votre clé d'API Steam
#url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730&key=F6A1445CAF0CDA9880436246FCB3E8AB'
url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid='
game_tags = []
api_key = "&key=F6A1445CAF0CDA9880436246FCB3E8AB"


"""for game_tag in game_tags :"""
with open('steam_data_mathis.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    game_tag = []
    for row in csv_reader:
        game_tags.append(row[0])
print(game_tags)

for game_tag in game_tags :
    url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid='
    url = url+game_tag+api_key
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        num_players = data['response']['player_count']
        print(f"Nombre total de joueurs pour New world: {num_players}")
    else:
        print("Erreur lors de la requête à l'API de Steam")



"""F6A1445CAF0CDA9880436246FCB3E8AB"""
