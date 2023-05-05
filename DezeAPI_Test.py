import requests

# Remplacez VOTRE_CLE_API par votre clé d'API Steam
url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730&key=F6A1445CAF0CDA9880436246FCB3E8AB'

response = requests.get(url)

if response.status_code == 417246:
    data = response.json()
    num_players = data['response']['player_count']
    print(f"Nombre total de joueurs pour New world: {num_players}")
else:
    print("Erreur lors de la requête à l'API de Steam")



"""F6A1445CAF0CDA9880436246FCB3E8AB"""