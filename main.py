import requests
from bs4 import BeautifulSoup

url = 'https://www.etsy.com/search?q=anniversary+gifts&ref=hp_gbs&anchor_listing_id=681346365'
params = {
    'q': 'anniversary gifts',
    'ref': 'hp_gbs',
    'anchor_listing_id': '681346365'
}
headers = {'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)

print(res)
