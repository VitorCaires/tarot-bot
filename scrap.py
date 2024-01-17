import requests
from bs4 import BeautifulSoup
url = requests.get("https://f5.folha.uol.com.br/horoscopo/")
soup = BeautifulSoup(url.content, 'html.parser')
keys = []
values = []
daily = {}
for x in soup.find_all(class_='horoscope-list__title'):
    keys.append(x.find('a').get_text())
for x in soup.find_all(class_='horoscope-list__description'):
    values.append(x.find('p').get_text())
daily = dict(zip(keys,values))
