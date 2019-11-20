import requests
from bs4 import BeautifulSoup as bs
import csv
import re

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'https://www.avito.ru/belgorod/avtomobili/audi?cd=1&radius=200'


def avito_pars(url, headers, requests=requests):
    car = []
    urls = []
    session = requests.Session()
    requests = session.get(url, headers=headers)
    if requests.status_code == 200:
        print('Yes')
        pars = bs(requests.content, 'lxml')
        try:
            pagination = pars.find_all('div', attrs={'class': 'pagination-pages'})
            # Находим все ссылки пагинации
            for pag in pagination:
                hrefs = pag.find_all('a', attrs={'class': 'pagination-page'})
                for href in hrefs:
                    result_link = href['href']
                # С помощью регулярного выражения извлекаем номер последней страницы из последней ссылки пагинации
                relative_url = result_link
                regex = re.compile(r'\/(.+)\/(.+)?p=(\d+)(.+)')
                page = int(regex.findall(relative_url)[0][2])
            for i in range(1, page + 1):
                url = f'https://www.avito.ru/belgorod/avtomobili/audi?p={i}&cd=1&radius=200'
                if url not in urls:
                    urls.append(url)
        except:
            pass
        for url in urls:
            requests = session.get(url, headers=headers)
            pars = bs(requests.content, 'lxml')
            divs = pars.find_all('div', attrs={'class': 'item_table-wrapper'})
            for div in divs:
                title = div.find('span', attrs={'itemprop': 'name'}).text.strip()
                price = div.find('span', attrs={'class': 'price'}).text.strip()
                info = div.find('div', attrs={'class': 'specific-params specific-params_block'}).text.strip()
                car.append({
                    'title': title,
                    'price': price,
                    'info': info,
                })
    else:
        print('ERROR')
    return car


def file_writer(cars):
    with open('cars_avito.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Марка', 'Цена', 'Инфо'))
        for car in cars:
            model = car['title']
            price = car['price']
            info = car['info']
            a_pen.writerow((model, price, info))


pars_car = avito_pars(base_url, headers)
file_writer(pars_car)
