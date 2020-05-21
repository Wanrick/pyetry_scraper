from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

poemhunter_poet_url = 'https://www.poemhunter.com/robert-frost/poems/'

poetry_list = requests.get(poemhunter_poet_url)

if poetry_list.status_code == requests.codes.ok:
    print('Poem list loaded ok')
    page_content = BeautifulSoup(poetry_list.text, 'lxml')
    poems_on_page = page_content.findAll('td', class_='title')
    poem_title_element = poems_on_page[0]
    poem_title = poem_title_element.find('a')['href']
    print(poem_title)