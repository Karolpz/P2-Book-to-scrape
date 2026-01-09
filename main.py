from scrapers.utils import get_soup, save_book_to_file
from scrapers.book_scraper import scrape_book_info
from scrapers.category_scraper import scrape_book_from_category_info

def get_book_info():
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    data_book = scrape_book_info(url)
    save_book_to_file(data_book, "data/book_info.csv")

def get_category_info():
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    data_category = scrape_book_from_category_info(url)
    print(data_category)
    

if __name__ == "__main__":
    get_book_info()
    get_category_info()