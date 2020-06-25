import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://drizly.com'
dr = None


def crawl():
    dr = webdriver.Chrome(ChromeDriverManager().install())

    dr.get(BASE_URL+'/beer/ale/ipa/c15')
    soup = BeautifulSoup(dr.page_source, "html.parser")

    beers = soup.findAll(
        'li', {"class": 'CatalogGrid__CatalogListItem___3S6W5'})
    for beer in beers:
        anchor = beer.find('a')
        print(BASE_URL + anchor['href'])
        get_beer_characteristics(dr, BASE_URL + anchor['href'])


def get_beer_characteristics(dr, href):
    dr.get(href)
    soup = BeautifulSoup(dr.page_source, "html.parser")

    characteristics = soup.findAll(
        'dl', {"class": 'PDPAttributesAndReviews__row___3T_tv'})
    for char in characteristics:
        dt = char.find('dt')
        dd = char.find('dd')
        print(dt.text + ' : ' + dd.text)


if __name__ == "__main__":
    crawl()
