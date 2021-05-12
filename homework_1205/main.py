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
    s = parse_dominos(item)
    df = df.append(s, ignore_index=True)

df.to_excel('dominos.xlsx')

url2 = 'https://dominos.by/bread'
connect2 = requests.get(url2)
df2 = pd.DataFrame()
soup2 = BeautifulSoup(connect2.text, features='html.parser')
cards2 = soup2.find_all('div', {'class': 'product-card'})  # найти все карточки товаров

for item in cards2:
    print(item)
    s = parse_dominos(item)
    df2 = df2.append(s, ignore_index=True)

df2.to_excel('bread.xlsx')
