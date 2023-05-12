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

# Remplacez l'ID de l'application et la clé d'API par les vôtres
app_id = '271590'
api_key = 'F6A1445CAF0CDA9880436246FCB3E8AB'

# Liste des codes de pays pour lesquels nous voulons récupérer les prix
country_codes = ['US', 'GB', 'FR', 'DE']

# Endpoint pour récupérer les informations de prix d'un jeu sur Steam
api_url = f'https://store.steampowered.com/api/appdetails?appids={app_id}&cc={",".join(country_codes)}&filters=price_overview&key=F6A1445CAF0CDA9880436246FCB3E8AB'

# Effectuer l'appel API
response = requests.get(api_url)

# Vérifier si la réponse est valide
if response.status_code == 200:
    # Récupérer les données JSON de la réponse
    data = response.json()

    # Vérifier si le jeu est disponible dans les pays demandés
    if data[app_id]['success']:
        # Récupérer les informations de prix pour chaque pays demandé
        for country_code in country_codes:
            price_info = data[app_id]['data']['price_overview']

            # Récupérer les informations de prix pour le pays actuel
            currency = price_info['currency']
            country_price = price_info[f'final_{currency.lower()}']
            print(f'Le prix du jeu dans le pays {country_code} est de {country_price} {currency}')
    else:
        print("Le jeu n'est pas disponible dans les pays demandés.")
else:
    print("Erreur lors de la récupération des informations de prix.")