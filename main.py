from scraper.webscraper import get_poems_by_poet_from_poemhunter


def main():
    poems = get_poems_by_poet_from_poemhunter('Robert Frost')
    print(poems)


if __name__ == '__main__':
    main()