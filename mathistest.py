"""infos à récup de steam chart
Id
GameName
CurrentPlayers
PeakPlayers
HoursPlayed
"""
import time
import requests
import csv

# Remplacez VOTRE_CLE_API par votre clé d'API Steam
#url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=730&key=F6A1445CAF0CDA9880436246FCB3E8AB'
urlAppDetails = 'https://store.steampowered.com/api/appdetails?appids='
game_Ids = []
api_key = "&key=F6A1445CAF0CDA9880436246FCB3E8AB"

# Ouvre le csv avec les ID des jeux que l'ont veux récup
with open('Main/steam_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    game_id = []
    for row in csv_reader:
        game_Ids.append(row[0])

#Création su CSV 
with open('steam_data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'ID', 'Required age', 'Gratuit', 'Price infos', 'Description détaillée', 'Langages supportés', 'Site web', 'Configurations recommandées', 'Développeur', 'Éditeur', 'Plateformes', 'Metacritic', 'Categories', 'Genres', 'Recommendations', 'Date de parution'])
    # Pour chaque ID de jeu récup, faire l'appel à l'API mainInfo steam pour récupérer les infos du jeu
    for game_id in game_Ids :

        # limiter à 1 appel par 1.6 seconde pour ne pas se faire jeter par steamAPI 
        time.sleep(2)

        urlAppDetails = 'https://store.steampowered.com/api/appdetails?appids='
        urlAppDetails = urlAppDetails + game_id + api_key
        print(urlAppDetails)
        response = requests.get(urlAppDetails)
        if response.status_code == 200:
            data = response.json()
            if game_id in data:
                if "data" in data[game_id]:
                    game_info = data[game_id]["data"]
                else :
                    print("this game has no data returned from steam API appDetails")
                    continue
            else:
                print("this game has no data returned from steam API appDetails")
                continue

            #Sélection des champs
            try:
                gameName = game_info["name"]
            except:
                print("name field doesn't exists")
                gameName = ""
            
            try:
                gameId = game_info["steam_appid"]
            except:
                print("steam_appid field doesn't exists")
                gameId = ""
            

            try:
                gameRequiredAge = game_info["required_age"]
            except:
                print("required_age field doesn't exists")
                gameRequiredAge = ""
            

            try:
                isFree = game_info["is_free"] #True/false
            except:
                print("is_free field doesn't exists")
                isFree = ""
            

            try:
                gameDetailedDescription = game_info["detailed_description"]
            except:
                print("detailed_description field doesn't exists")
                gameDetailedDescription = ""
            

            try:
                gameSupportedLanguages = game_info["supported_languages"]
            except:
                print("supported_languages field doesn't exists")
                gameSupportedLanguages = ""
            

            try:
                gameWebsite = game_info["website"]
            except:
                print("website field doesn't exists")
                gameWebsite = ""
            

            try:
                gamePcRequirements = game_info["pc_requirements"] #List (mini, ...)
            except:
                print("pc_requirements field doesn't exists")
                gamePcRequirements = ""
            
            try:
                gameDevelopers = game_info["developers"] #List
            except:
                print("developers field doesn't exists")
                gameDevelopers = ""
            
            try:
                gamePublishers = game_info["publishers"] #Li
            except:
                print("publishers field doesn't exists")
                gamePublishers = ""

            try:
                gamePlatforms = game_info["platforms"] #Dict
            except:
                print("platforms field doesn't exists")
                gamePlatforms = ""
            

            try:
                gameCategories = game_info["categories"]
            except:
                print("categories field doesn't exists")
                gameCategories = ""
            

            try:
                gameGenres = game_info["genres"]#List of dict
            except:
                print("genres field doesn't exists")
                gameGenres = ""
            

            try:
                gameReleaseDate = game_info["release_date"]
            except:
                print("release_date field doesn't exists")
                gameReleaseDate = ""
            

            try:
                gameMetacritic = game_info["metacritic"] #Dict
            except:
                print("Metacritic field doesn't exists")
                gameMetacritic = ""  
            
            try:
                gameRecommendations = game_info["recommendations"]#Dict
            except:
                print("Recommendations field doesn't exists")
                gameRecommendations = ""

            try:
                gamePriceOverview = game_info["price_overview"]#Dict
            except:
                print("price_overview field doesn't exists")
                gamePriceOverview = ""

            #complétion du CSV
            writer.writerow([gameName, gameId, gameRequiredAge, isFree, gamePriceOverview, gameDetailedDescription, gameSupportedLanguages, gameWebsite, gamePcRequirements, gameDevelopers, gamePublishers, gamePlatforms, gameMetacritic, gameCategories, gameGenres, gameRecommendations, gameReleaseDate])
        else:
            print("Erreur lors de la requête à l'API appdetails de Steam")

        """# Si le jeu n'est pas gatuit, solliciter une autre API steam pour connaitre son prix
        if isFree != "true" :
            urlprice = "https://api.steampowered.com/ISteamEconomy/GetAssetPrices/v1/?appid="
            urlprice = urlprice + game_Ids[5] + api_key + "&currency=3"
            print(urlprice)
            response = requests.get(urlprice)
            print(response)"""