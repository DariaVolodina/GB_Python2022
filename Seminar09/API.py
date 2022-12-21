# API (Application Programming Interface)
# Руководство с описанием команд и т д (типа инструкции по работе)
# Например, https://github.com/public-apis/public-apis

# Необх библиотека пайтоновская

# HTTP - запросы(HTTP Requests) — сообщения, которые отправляются клиентом на сервер,
# чтобы вызвать выполнение некоторых действий.
# Зачастую для получения доступа к определенному ресурсу. Основой запроса является HTTP-заголовок.

import requests

# response = requests.get('https://mail.ru')
# print(response)
# #
# if response:
#     print('OK')
# else:
#     print('NO')

# print(response.headers) # заголовки
# print(response.text)    # код страницы ( в браузере - F12)



# https://openweathermap.org/
API_key = '4321a3d417b53045aa1b6617c529c910'
city_name = 'Оймякон'

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ru")

temp = response.json()
temp1 = temp['main']
print(temp1['temp'])

#
# from bs4 import BeautifulSoup as bs
#
# url = 'https://www.anekdot.ru/'
# response = requests.get(url).text
# # print(response)
# soup = bs(response, 'html.parser')
# # print(soup)
# weather = soup.find('div', class_='text')   # . find(....) можно дальше проваливаться в код
# print(weather.text)

# find_all(...)

# import requests
# from bs4 import BeautifulSoup as bs
#
# url = 'https://www.life-is-good.org/vdohnovlyayushchie-tsitaty-dlya-nachala-dnya/'
# response = requests.get(url).text
# soup = bs(response, 'html.parser')
#
# title = soup.title
# print(title)    # tag
# print(title.text)   # содержимое тэга
# print(title.string) # то же самое

# методы .find()    & .find_all()
# find работае сверхху вниз, т.е. забирает данные из первого попавшегося на странице искомого элемента
# А .find_all выведет все подходящие нашему запросу элементы и сохранит их в СПИСОК,
# которые далее мы можем перебрать в цикле

# phrase_1 = soup.find('blockquote', class_='wp-block-quote')
# print(phrase_1.text)


# ссылка всегда хранится в атрибуте <href>
# и мы можем её забрать, применив метод .get
# item_url = item.get('href')

# методы    .find_parent()  &   .find_parents()
# Поднимаются по структуре страницы снизу вверх

# .next_element     &   .previous_element
# .find_next_sibling()  .find_previous_sibling()
