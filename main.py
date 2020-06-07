from scrapers.poem_hunter_scraper import get_poems_by_poet_from_poemhunter
from writer.poem_writer import write_poems_to_files, merge_poems_by_poet, write_poems_to_single_file


def main():
    poet = 'Robert Frost'
    poems = list()
    poems += get_poems_by_poet_from_poemhunter(poet)
    write_poems_to_single_file(poems)


if __name__ == '__main__':
    main()
