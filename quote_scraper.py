# https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
base_url = 'https://quotes.toscrape.com'
url = '/page/1'

while url:
    res = requests.get(f'{base_url}{url}')
    print(f'scraping {base_url}{url}...')
    soup = BeautifulSoup(res.text, 'html.parser')
    quotes = soup.find_all(class_='quote')

    for quote in quotes:
        all_quotes.append({
            'text': quote.find(class_='text').get_text(),
            'author': quote.find(class_='author').get_text(),
            'bio-link': quote.find('a')['href']
        })

    next_button = soup.find(class_='next')
    url = next_button.find('a')['href'] if next_button else None
    sleep(2)

print(all_quotes)