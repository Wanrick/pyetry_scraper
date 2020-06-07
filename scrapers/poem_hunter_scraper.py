import requests
from bs4 import BeautifulSoup

from poem import Poem


def replace_double_br_tag_with_pipe(text_content):
    p_tag = text_content.p
    while p_tag.br is not None:
        pipe_str = BeautifulSoup('|', 'lxml')
        p_tag.br.replace_with(pipe_str)
    response = ''
    for s in p_tag.stripped_strings:
        response += str(s)
    response = response.replace('|', '\n')
    return response


def get_poem(poem_link):
    try:
        poemhunter_poem_url = 'https://www.poemhunter.com' + poem_link
        poem_page = requests.get(poemhunter_poem_url)
        try:
            if poem_page.status_code != requests.codes.ok:
                raise Exception('The link {} does not exist on poemhunter.com'.format(poem_link))
            poem_page_content = BeautifulSoup(poem_page.text, 'lxml')
            poem_container = poem_page_content.find('div', id='solSiirMetinDV')
            poem_block = poem_container.find('div', class_='KonaBody')
            poem_url = poemhunter_poem_url
            poem_title = ''
            poem_text = ''
            if poem_container.find('h1', class_='title') is not None:
                poem_title = poem_container.find('h1', class_='title').text
            if poem_block.find('p') is not None:
                poem_text = replace_double_br_tag_with_pipe(poem_block)
            return Poem('', poem_url, poem_title, poem_text)
        except Exception as exz:
            print(exz)
            return None
    except Exception as per:
        print(per)
        return None


def get_poem_urls(poet, poet_url, page_count):
    response = list()
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
                    response.append(poem_title_element)
        except Exception as exz:
            print(exz)
            break
    print('Poem list loaded ok')
    return response


def get_poem_page_count(poet, poet_url):
    poemhunter_poet_url = 'https://www.poemhunter.com/' + poet_url + '/poems/'
    poetry_list = requests.get(poemhunter_poet_url)
    try:
        if poetry_list.status_code != requests.codes.ok:
            raise Exception('The poet {} has no poems on poemhunter.com'.format(poet))
        page_content = BeautifulSoup(poetry_list.text, 'lxml')
        if len(page_content.findAll('td', class_='title')) > 40:
            pagination_container = page_content.find('div', class_='pagination')
            pages_list = pagination_container.findAll('li')
            return int(pages_list[len(pages_list) - 1].find('a').text)
        else:
            return 1
    except Exception as exz:
        print(exz)
        return


def get_poems_by_poet_from_poemhunter(poet):
    poet_url = poet.lower().replace(' ', '-')
    page_count = get_poem_page_count(poet, poet_url)
    poem_url_list = get_poem_urls(poet, poet_url, page_count)

    poems = list()
    for poem_link in poem_url_list:
        poem = get_poem(poem_link)
        if poem is not None:
            poem.poet = poet
            poems.append(poem)
    return poems
