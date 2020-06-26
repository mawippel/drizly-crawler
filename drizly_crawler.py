import requests
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BASE_HOST = 'https://drizly.com'
dr = None


def crawl(beer_category_url):
    dr = webdriver.Chrome(ChromeDriverManager().install())
    page_number = 1

    while True:
        try:
            page_url = '{}{}/page{}'.format(BASE_HOST,
                                            beer_category_url, page_number)
            fetch_beers(dr, page_url)
            page_number += 1
        except:
            print('An error occured: {}'.format(sys.exc_info()[0]))
            break


def fetch_beers(dr, page_url):
    dr.get(page_url)
    soup = BeautifulSoup(dr.page_source, "html.parser")

    beers = soup.findAll(
        'li', {"class": 'CatalogGrid__CatalogListItem___3S6W5'})
    for beer in beers:
        anchor = beer.find('a')
        print(BASE_HOST + anchor['href'])
        get_beer_characteristics(dr, BASE_HOST + anchor['href'])


def get_beer_characteristics(dr, href):
    dr.get(href)
    soup = BeautifulSoup(dr.page_source, "html.parser")

    characteristics = soup.findAll(
        'dl', {"class": 'PDPAttributesAndReviews__row___3T_tv'})
    for char in characteristics:
        dt = char.find('dt')
        dd = char.find('dd')
        print(dt.text + ' : ' + dd.text)


def read_sys_args():
    if not sys.argv or len(sys.argv) < 2:
        print('Please inform the seed path. To retrieve further information see the README.md file')
        exit()
    return sys.argv[1]


if __name__ == "__main__":
    beer_category_url = read_sys_args()
    crawl(beer_category_url)
