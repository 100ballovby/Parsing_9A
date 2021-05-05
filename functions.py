import pandas as pd


def parse_table(table):
    res = pd.DataFrame()

    question_id = 0
    question_link = ''
    question_date = ''
    question = ''
    who_asked = ''
    who_asked_id = ''
    who_asked_link = ''
    who_asked_city = ''
    answer = ''

    question_tr = table.find('tr', {'class': 'question'})
    # получаю сам вопрос. он находится в <tr class="question">
    question = question_tr.find_all('td')[1].find('div').strip()
    # получаю текст вопроса из второй td, текст находится внутри div

    widget_info = question_tr.find_all('div', {'class': 'widget__info'})
    # получаю ссылку на сам вопрос. Она находится в <div class="widget__info ...">
    # все классы переписывать нет необходимости. Достаточно только первого
    question_link = 'https://banki.ru' + widget_info[0].find('a').get('href').strip()
    # в найденной ссылке на вопрос достаю элемент href и прикладываю его к домену сайта.
    question_id = question_link.split('=')[1]

    who_asked = widget_info[1].find('a').text.strip()
    # получаю профиль человека, который задал вопрос
    who_asked_link = 'https://banki.ru' + widget_info[1].find('a').get('href').strip()
    # записываю ссылку на профиль человека, который задал вопрос
    who_asked_id = widget_info[1].find('a').get('href').strip().split('=')[1]
    # забираю ID пользователя с сайта и записываю его в переменную

    # получаю город, из которого задан вопрос
    who_asked_city = widget_info[1].text.split('(')[1].split(')')[1].strip()

    res = res.append(pd.DataFrame([[question_id, question_link, question,
                                    who_asked, who_asked_id, who_asked_link,
                                    who_asked_city]],
                                  columns=['ID', 'Ссылка на вопрос',
                                           'Вопроос', 'Кто спросил',
                                           'ID задавшего вопрос', 'Профиль',
                                           'Город'])
                     )
    return res

