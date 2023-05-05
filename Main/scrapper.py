from bs4 import BeautifulSoup as bs
import requests

url = 'https://steamdb.info/570'
response = requests.get(url)
html = response.content 


