from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

def extract(page):
    url= f'https://www.pararius.com/apartments/amsterdam/page-{page}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def transform(soup):

    lists= soup.find_all('section', class_="listing-search-item")
    for list in lists:
        title = list.find('a', class_='listing-search-item__link--title').text.replace('\n', '')
        location = list.find('div', class_='listing-search-item__sub-title').text.replace('\n', '')
        price = list.find('div', class_='listing-search-item__price').text.replace('\n', '')
        area = list.find('li', class_='illustrated-features__item--surface-area').text.replace('\n', '')
        rooms = list.find('li', class_='illustrated-features__item--number-of-rooms').text.replace('\n', '')
        interior = list.find('li', class_='illustrated-features__item--interior')
        if interior is not None:
            interior= interior.text.replace('\n', '')
        else:
            interior = None

        construction_period = list.find('li', 'illustrated-features__item--construction-period')
        node = construction_period
        if construction_period is not None:
            construction_period = construction_period.text.replace('\n', '') 
        else:
            construction_period = None
    

        House_info = {'title': title, 
        'location': location,
        'price': price,
        'area': area,
        'rooms': rooms,
        'interior': interior,
        'construction_period': construction_period
        }
        Apartment.append(House_info)

Apartment = []
for i in range(1,19,1):
    print(f'page:{i}')
    c = extract(1)
    transform(c) 

df = pd.DataFrame(Apartment)

print(df.head())
 
df.to_csv('Houses_in_Amsterdam.csv')