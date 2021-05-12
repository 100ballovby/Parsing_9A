import pandas as pd


def parse_dominos(card):
    res = pd.DataFrame()  # таблица для результатов
    url = 'https://dominos.by/pizza/'  # ссылка на страницу с пиццами
    pizza_link = url + card.get('data-code').lower()  # ссылка на пиццу
    pizza_name = card.find('div', {'class': 'product-card__title'}).text.strip()
    # .text достает текст из тега <div class="product-card__title">
    # метод .strip() убирает пробелы справа и слева от строки
    pizza_description = card.find('div', {'class': 'product-card__description'}).text.strip()
    pizza_img_link = card.find('img', {'class': 'product-card-media__element'}).get('src')
    pizza_price = card.find('p', {'class': 'product-card__modification-info-price'}).text
    pizza_weight = card.find('p', {'class': 'product-card__modification-info-weight'}).text

    res = res.append(
        pd.DataFrame(  # создаю таблицу на основе полученных данных
            [[pizza_link, pizza_name, pizza_description, pizza_price, pizza_weight, pizza_img_link]],
            columns=['Ссылка', 'Название', 'Ингридиенты', 'Цена', 'Масса', 'картинка']),
        ignore_index=True
    )
    return res
