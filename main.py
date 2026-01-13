from scrapers.utils import save_book_to_file
from scrapers.book_scraper import scrape_book_info
from scrapers.category_scraper import scrape_book_from_category_info
from scrapers.all_categories_scraper import scrape_all_categories

def main():
    for category in scrape_all_categories():
        category_name = category["name"]
        category_url = category["url"]
        
        book_urls = scrape_book_from_category_info(category_url)
        
        book_data_list = []
        for book_url in book_urls:
            book_data = scrape_book_info(book_url)
            book_data_list.append(book_data)
        
        save_book_to_file(book_data_list, category_name)
    
if __name__ == "__main__":
    main()

# imbriquez le main
# __main__