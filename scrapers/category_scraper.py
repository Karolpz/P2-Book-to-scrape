from scrapers.utils import get_soup
from urllib.parse import urljoin

def scrape_book_from_category_info(category_url):
    
    while category_url:
        soup = get_soup(category_url)
        books = soup.find_all("div", class_="image_container")
        
        for book in books:
            book_url =  book.find("a")["href"]
            full_url = urljoin(category_url, book_url)
            yield full_url

        next_button = soup.find("li", class_="next")

        if next_button:
            next_url = next_button.find("a")["href"]
            category_url = urljoin(category_url, next_url)
        else:
            category_url = None




