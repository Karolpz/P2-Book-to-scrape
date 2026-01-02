from scrapers.utils import get_soup, save_soup_to_file
from scrapers.book_scraper import scrape_book_info

def main():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    data_book = scrape_book_info(url)
    save_soup_to_file(data_book, "data/book_info.csv")

if __name__ == "__main__":
    main()
