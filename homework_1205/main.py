import requests
import pandas as pd
from bs4 import BeautifulSoup
from my_parser import *
# ^ это мой файл, в котором будет функция парсинга

url = 'https://dominos.by/pizza'
connect = requests.get(url)
df = pd.DataFrame()
soup = BeautifulSoup(connect.text, features='html.parser')
cards = soup.find_all('div', {'class': 'product-card'})  # найти все карточки товаров

for item in cards:
    print(item)

