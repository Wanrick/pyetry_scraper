from scrapers.poem_hunter_scraper import get_poems_by_poet_from_poemhunter
from scrapers.poetry_foundation_scraper import get_poems_by_poet_from_poetryfoundation
from writer.poem_writer import write_poems_to_files


def main():
    poems = list()
    poems += get_poems_by_poet_from_poemhunter('Robert Frost')
    poems += get_poems_by_poet_from_poetryfoundation('Robert Frost')
    write_poems_to_files(poems)


if __name__ == '__main__':
    main()
