# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.rambler.ru/'
response = requests.get(url).text
soup = bs(response, 'html.parser')

title = soup.title
print(f'Загаловок новостной страницы - "{title.text}"')
main_news = soup.find('div', class_='_2mnMl')
print(f'Главная новость на текущий момент - {main_news.text}')
print()

details = input('Хотите узнать другие топ-новости? (1 - "да, хочу", введите Enter, чтобы перейти далее): ')
if details == '1':
    news_1 = soup.find('div', class_='_1b-eY')
    news_2 = soup.find('div', class_='_2taiA')
    print()
    print(news_1.text)
    print(news_2.text)

else:
    pass

weather = input('\nХотите узнать курс доллара к рублю? (1 - "да, хочу", введите Enter, чтобы закончить): ')
if weather == '1':
    url2 = 'https://www.banki.ru/products/currency/cash/usd/moskva/'
    response2 = requests.get(url2).text
    soup2 = bs(response2, 'html.parser')
    rate = soup2.find('div', class_='currency-table__large-text')
    print(f'\nКурс ЦБ = {rate.text} рублей за доллар США')
else:
    pass


