from scrapers.utils import save_book_to_file, download_image
from scrapers.book_scraper import scrape_book_info
from scrapers.category_scraper import scrape_book_from_category_info
from scrapers.all_categories_scraper import scrape_all_categories
from concurrent.futures import ThreadPoolExecutor

def main():
    for category_name, category_url in scrape_all_categories():
        
        book_urls = scrape_book_from_category_info(category_url)
        
        book_data_list = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(scrape_book_info, book_urls)
            book_data_list.extend(results)
        
        save_book_to_file(book_data_list, category_name)
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            for book_data in book_data_list:
                if book_data["Image"] != "No image available.":
                    executor.submit(download_image, book_data["Image"], book_data["Title"], category_name)

    
if __name__ == "__main__":
    main()

