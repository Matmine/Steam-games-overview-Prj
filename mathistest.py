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
url = "https://steamdb.info"
link_to_click_1 = "Charts"

# Make a request to the main page and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to click and extract its URL
link = soup.find('a', class_='heading2 gbs-font-vanguard-red')
if link is None:
    print(f"Link '{link_to_click_1}' not found on page")
    exit()
link_url = link.get("href")

# Make a request to the linked page and parse the HTML using BeautifulSoup
response = requests.get(link_url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract information from the HTML fields using XPath expressions
game_name = soup.find("div", {"class": "css-truncate"}).text.strip()
if game_name is None:
    print("game_name not found")
    exit()


players_now = soup.find("div", {"class": "text-center green"}).text.strip()
if players_now is None:
    print("players_now not found")
    exit()

# Print the extracted information
print(f"Players Now on {game_name} : {players_now}")
