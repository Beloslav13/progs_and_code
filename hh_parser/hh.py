import requests
import csv
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'https://belgorod.hh.ru/search/vacancy?search_period=30&area=1817&text=1c&page=0'


def hh_pars(base_url, headers, requests=requests):
    jobs = []
    urls = []
    urls.append(base_url)
    session = requests.Session()
    requests = session.get(base_url, headers=headers)
    if requests.status_code == 200:
        soup = bs(requests.content, 'lxml')
        try:
            pagination = soup.find_all('a', attrs={'data-qa': 'pager-page'})
            count = int(pagination[-1].text)
            for i in range(count):
                url = f'https://belgorod.hh.ru/search/vacancy?search_period=30&area=1817&text=1c&page={i}'
                if url not in urls:
                    urls.append(url)
        except:
            pass
    for url in urls:
        requests = session.get(url, headers=headers)
        soup = bs(requests.content, 'lxml')
        divs = soup.find_all('div', attrs={'class': 'vacancy-serp-item'})
        for div in divs:
            try:
                title = div.find('a', attrs={'class': 'bloko-link HH-LinkModifier'}).text
                href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
                company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
                text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
                text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
                content = text1 + ' ' + text2
                jobs.append({
                    'title': title,
                    'href': href,
                    'company': company,
                    'content': content,
                })
            except:
                pass
        print(len(jobs))
    else:
        print('ERROR or Done, Status_code = ' + str(requests.status_code))
    return jobs


def files_write(jobs):
    with open('parsed_jobs.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Название вакансии', 'URL', 'Название компании', 'Описание'))
        for job in jobs:
            a_pen.writerow((job['title'], job['href'], job['company'], job['content']))


jobs = hh_pars(base_url, headers)
files_write(jobs=jobs)