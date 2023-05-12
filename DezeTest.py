"""import requests
import csv

# Remplacez VOTRE_CLE_API par votre clé d'API Steam
#url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730&key=F6A1445CAF0CDA9880436246FCB3E8AB'
url = 'https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/?appid=1904540&key=F6A1445CAF0CDA9880436246FCB3E8AB&currency=1&cc'
"""#game_tags = []""" """api_key = "&key=F6A1445CAF0CDA9880436246FCB3E8AB""""


"""#for game_tag in game_tags :"""
"""with open('steam_data_mathis.csv', mode='r') as file:
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



"""#F6A1445CAF0CDA9880436246FCB3E8AB"""


import requests

# ID de l'application du jeu sur Steam (CS:GO ici)
appid = 730

# Clé API Steam
api_key = "VOTRE_CLE_API"

# Codes pays pour lesquels nous voulons récupérer les prix
cc = "us,gb,fr"

# Appel de l'API pour obtenir les prix
response = requests.get(f"https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/?appid=1904540&key=F6A1445CAF0CDA9880436246FCB3E8AB&currency=1&cc={cc}")

# Vérifier si la requête a réussi
if response.status_code == 200:
    
    # Récupérer les données de la réponse au format JSON
    data = response.json()
    
    # Boucle sur les pays pour afficher les prix
    for country in data["response"]["results"]:
        country_code = country["cc"]
        country_name = country["country"]
        country_price = country["price"]
        
        # Afficher les informations de prix pour chaque pays
        print(f"Prix en {country_name} ({country_code}) : {country_price}")
    
else:
    # Afficher un message d'erreur si la requête a échoué
    print("Erreur lors de l'appel de l'API")