"""Name :
Developpeur : 
Supported system :
Release date :
global Review :
Nb happy :
Nb sad :
"""

"""https://steamdb.info/

click Mostplayed Games 
 click on game 
scrapp"""


import requests
from bs4 import BeautifulSoup

# Define the URL and link to click
url = "https://steamdb.info"
link_xpath = "/html/body/div[1]/div[2]/a[3]"

# Make a request to the main page and parse the HTML using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

charts_link = soup.find("a", Xapth="/html/body/div[1]/div[2]/a[3]")
if charts_link is None:
    print("Charts link not found on page")
    exit()
charts_url = url + charts_link.get("href")

# Make a request to the "Charts" page and parse the HTML using BeautifulSoup
response = requests.get(charts_url)
soup = BeautifulSoup(response.content, "html.parser")

"""# Find the link to click and extract its URL using XPath
link = soup.findAll("a", {"xpath": link_xpath})
if link is None:
    print("Link not found")
    exit()
link_url = link.get("href")

# Make a request to the linked page and parse the HTML using BeautifulSoup
response = requests.get(link_url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract information from the HTML fields using CSS selectors
game_names = soup.select("div.app-name-column > div.css-truncate")
players_now = soup.select("div.current-players-column > div.text-center.green")"""

# Print the extracted information for each game
"""for i in range(len(game_names)):
    game_name = game_names[i].text.strip()
    players = players_now[i].text.strip()
    print(f"Players Now on {game_name}: {players}")"""


