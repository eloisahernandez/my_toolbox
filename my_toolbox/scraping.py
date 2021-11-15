import re
import requests
from bs4 import BeautifulSoup
import csv


def scrape_webpage(url):
    '''Scrape Website and return soup'''
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


if __name__ == '__main__':
    scrape_webpage("https://recipes.lewagon.com/")
