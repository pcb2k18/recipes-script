import requests
page = requests.get("https://tasty.co/recipe/chicken-fried-rice")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
