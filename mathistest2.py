"""infos à récup de steam db

Name :
Developpeur : 
Supported system :
Release date :
global Review :
Nb happy :
Nb sad :
"""

import requests
from bs4 import BeautifulSoup

# Define the URL and link to click
print("Starting program")
url = "https://steamcharts.com/top"

# Make a request to the main page and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the gamesIds that are present on the page and put theml in a list
topGamesInfos = soup.findAll('tr', class_="odd")
print(topGamesInfos)


# For each element of that list just call https://steamdb.info/app/GameId/charts/ and then scrap interesting fields



