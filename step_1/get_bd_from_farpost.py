from bs4 import BeautifulSoup
import requests
from requests import get
import time
from time import sleep
import random
import json

houses = {
    'info': [],
    'price': [],
    'house_type': [],
    'area': [],
    'stree': [],
    'adress': [],
    'rooms': [],
    'repairs': [],
    'squares':[],
    'floor': [],
    'balcony':[],
    'biulded':[],
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Geko) Chrome",
    "Accept":  "text/html,application/xhtml+xml,application/xml;x=0.9,image/webp,*/*;q=0.8"
}
count = 1
while count <= 15:
    if count == 1:
        url = 'https://www.farpost.ru/ussuriisk/realty/sell_flats/'
    else:
        url = 'https://www.farpost.ru/ussuriisk/realty/sell_flats/?page=' + str(count)

    print(url)
    response = get(url,  headers=headers
                   )
    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_data = html_soup.find_all('a', class_="bull-item__self-link")

    if house_data != []:
        for link in house_data:
            try:
                url = 'https://www.farpost.ru' + link['href']
                response = get(url, headers=headers
                               )
                soup = BeautifulSoup(response.text, 'html.parser')
                houses['price'].append(soup.find('span', class_='viewbull-summary-price__value').text)
                houses['house_type'].append(soup.find_all('div', class_='field')[0].find('span').text)
                houses['area'].append(soup.find_all('div', class_='field')[1].find('span').text)
                houses['stree'].append(soup.find_all('div', class_='field')[2].find('span').text)
                houses['rooms'].append(soup.find_all('div', class_='field')[3].find('span').text)
                houses['repairs'].append(soup.find_all('div', class_='field')[5].find('span').text)
                houses['squares'].append(soup.find_all('div', class_='field')[6].find('span').text)
                houses['floor'].append(soup.find_all('div', class_='field')[7].find('span').text)
                houses['balcony'].append(soup.find_all('div', class_='field')[8].find('span').text)
                houses['biulded'].append(soup.find_all('div', class_='field')[9].find('span').text)

                for i in range(random.randint(20, 25)):
                    print(i)
                    sleep(1)
                print(1)
            except:
                print('Some error')




    else:
        print('empty')
        break
    count += 1

    value = random.random()
    scaled_value = 1 + (value * (9 - 5))
    print(scaled_value)
    time.sleep(scaled_value)

with open('houes_db.json', 'w') as file:
    json.dump(houses, file)

    print(1)
