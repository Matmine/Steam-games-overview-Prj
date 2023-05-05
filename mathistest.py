"""infos à récup de steam chart
Id
GameName
CurrentPlayers
PeakPlayers
HoursPlayed
"""
import re
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL and link to click
url = "https://steamcharts.com/top"
url_suffixes = ["", "/p.2", "/p.3", "/p.4"]

# Make a request to the main page and parse the HTML using BeautifulSoup
with open('steam_data_mathis.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Current Players', 'Peak Players', 'Hours Played'])
    for url_suffix in url_suffixes :

        response = requests.get(url+url_suffix)
        soup = BeautifulSoup(response.content, "html.parser")

        topGamesInfos = soup.findAll("tr")
        
         # Loop through each game's row in the HTML and extract relevant information
        for game in topGamesInfos[1:]:
            game_info = game.findAll('td')
            game_id = game_info[1].find('a')
            game_id = game_id['href'].split('/')[-1] if game_id else ''
            game_id = re.sub('[^0-9]', '', game_id) 
            game_name = game_info[1].text.strip()
            current_players = game_info[2].text.strip()
            peak_players = game_info[4].text.strip()
            hours_played = game_info[5].text.strip()

            # Write the game's information to the CSV file
            writer.writerow([game_id, game_name, current_players, peak_players, hours_played])


