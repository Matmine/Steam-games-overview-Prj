"""infos à récup de steam chart
Id
GameName
CurrentPlayers
PeakPlayers
HoursPlayed
"""
import requests
import csv

# Remplacez VOTRE_CLE_API par votre clé d'API Steam
#url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730&key=F6A1445CAF0CDA9880436246FCB3E8AB'
urlAppdetails = 'https://store.steampowered.com/api/appdetails?appids='
game_Ids = []
api_key = "&key=F6A1445CAF0CDA9880436246FCB3E8AB"

# Ouvre le csv avec les ID des jeux que l'ont veux récup
with open('Main/steam_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    game_id = []
    for row in csv_reader:
        game_Ids.append(row[0])

print(len(game_Ids))


# Pour chaque ID de jeu récup, faire l'appel à l'API mainInfo steam pour récupérer les infos du jeu
#for game_id in game_Ids :
urlAppdetails = 'https://store.steampowered.com/api/appdetails?appids='
urlAppdetails = urlAppdetails + game_Ids[5] + api_key
print(urlAppdetails)
response = requests.get(urlAppdetails)
if response.status_code == 200:
    data = response.json()
    game_info = data[game_Ids[5]]["data"]

    #Sélection des champs
    gameName = game_info["name"]
    gameId = game_info["steam_appid"]
    gameRequiredAge = game_info["required_age"]
    isFree = game_info["is_free"] #True/false
    gameDetailedDescription = game_info["detailed_description"]
    gameSupportedLanguages = game_info["supported_languages"]
    gameWebsite = game_info["website"]
    gamePcRequirements = game_info["pc_requirements"] #List (mini, ...)
    gameDevelopers = game_info["developers"] #List
    gamePublishers = game_info["publishers"] #List
    gamePlatforms = game_info["platforms"] #Dict
    gameMetacritic = game_info["metacritic"] #Dict
    gameCategories = game_info["categories"]
    gameGenres = game_info["genres"]#List of dict
    gameRecommendations = game_info["recommendations"]#Dict
    gameReleaseDate = game_info["release_date"]


    #Création du CSV
    with open('steam_data2.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'ID', 'Required age', 'Gratuit', 'Description détaillée', 'Langages supportés', 'Site web', 'Configurations recommandées', 'Développeur', 'Éditeur', 'Plateformes', 'Metacritic', 'Categories', 'Genres', 'Recommendations', 'Date de parution'])
        writer.writerow([gameName, gameId, gameRequiredAge, isFree, gameDetailedDescription, gameSupportedLanguages, gameWebsite, gamePcRequirements, gameDevelopers, gamePublishers, gamePlatforms, gameMetacritic, gameCategories, gameGenres, gameRecommendations, gameReleaseDate])
else:
    print("Erreur lors de la requête à l'API appdetails de Steam")

"""# Si le jeu n'est pas gatuit, solliciter une autre API steam pour connaitre son prix
if isFree != "true" :

    urlprice = "https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/?appid="
    urlprice = urlprice + game_Ids[5] + api_key + "&currency=3"
    print(urlprice)
    response = requests.get(urlprice)
    print(response)"""







