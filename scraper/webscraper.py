import string

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


class Poem:
    def __init__(self, poet, poem_url, poem_title, poem_text):
        self.poet = poet
        self.poem_url = poem_url
        self.poem_title = poem_title
        self.poem_text = poem_text


def get_poems_by_poet_from_poemhunter(poet):
    poet_url = poet.lower().replace(' ', '-')
    poemhunter_poet_url = 'https://www.poemhunter.com/' + poet_url + '/poems/'
    poetry_list = requests.get(poemhunter_poet_url)
    try:
        if poetry_list.status_code != requests.codes.ok:
            raise Exception('The poet {} has no poems on poemhunter.com'.format(poet))
        page_content = BeautifulSoup(poetry_list.text, 'lxml')
        pagination_container = page_content.find('div', class_='pagination')
        pages_list = pagination_container.findAll('li')
        page_count = int(pages_list[len(pages_list) - 1].find('a').text)
    except Exception as exz:
        print(exz)
        return

    poem_url_list = list()
    for x in range(page_count):
        poemhunter_poem_list_url = 'https://www.poemhunter.com/' + poet_url + '/poems/page-' + str(x) + '/?a=a&l=3&y='
        poetry_list = requests.get(poemhunter_poem_list_url)
        try:
            if poetry_list.status_code != requests.codes.ok:
                raise Exception('The poet {} has no poems on poemhunter.com'.format(poet))
            poetry_list_page_content = BeautifulSoup(poetry_list.text, 'lxml')
            poetry_list_on_page = poetry_list_page_content.findAll('td', class_='title')
            for p_link in poetry_list_on_page:
                if p_link.find('a') is not None:
                    poem_title_element = p_link.find('a')['href']
                    poem_url_list.append(poem_title_element)
        except Exception as exz:
            print(exz)
            break

    print('Poem list loaded ok')

    poems = list()
    for poem_link in poem_url_list:
        # try:
            poemhunter_poem_url = 'https://www.poemhunter.com' + poem_link
            poem_page = requests.get(poemhunter_poem_url)
            # try:
            if poem_page.status_code != requests.codes.ok:
                print(poem_page.status_code)
                raise Exception('The link {} does not exist on poemhunter.com'.format(poem_link))
            poem_page_content = BeautifulSoup(poem_page.text, 'lxml')
            poem_block = poem_page_content.find('div', class_='KonaBody')
            poem_poet = poet
            poem_url = poemhunter_poem_url
            poem_title = ''
            poem_text = ''
            if poem_block.find('h1', class_='title') is not None:
                print(poem_block.find('h1', class_='title'))
                poem_title = poem_block.find('h1', class_='title')[0].text
            if poem_block.find('p') is not None:
                poem_text = poem_block.find('p')
                print(poem_text.stripped_strings) # This creates an object of disparate strings that need to be checked and formatted.
            poem = Poem(poem_poet, poem_url, poem_title, poem_text)
            print(poem)
            poems.append(poem)
        #     except Exception as exz:
        #         print(exz)
        #         break
        # except Exception as per:
        #     print(per)
        #     break

    return poems
