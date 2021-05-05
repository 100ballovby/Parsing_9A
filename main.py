import requests
from bs4 import BeautifulSoup
from functions import parse_table
import pandas as pd


# сохраняю урл сайта, к которому буду подключаться
bank_id = 1771062  # ID банка на сайте
page, max_page = 1, 20
url = f'https://www.banki.ru/services/questions-answers/?id={bank_id}'
res = requests.get(url)  # подключаюсь по указанному урлу

soup = BeautifulSoup(res.text)  # это сам парсер
tables = soup.find_all('table', {'class': 'qaBlock'})

result = pd.DataFrame()

for item in tables:
    parse = parse_table(item)
    result = result.append(parse, ignore_index=True)

result.to_excel('res.xlsx')

# .find('table') - ищет первое вхождение элемента в тексте
# .find_all('table') - ищет ВСЕ вхождения элемента в тексте
# find('table').text - возврат текста, который находится в объекте
# find('table').get('href') - вернет ссылки




#with open('test.html', 'w') as f:
    # открываю файл test.html в режиме записи (write)
#    f.write(res.text)  # И записываю в него ответ от сайта

