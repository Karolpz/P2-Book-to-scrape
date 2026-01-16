from scrapers.utils import get_soup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/catalogue/"

def scrape_book_from_category_info(category_url):
    
    while category_url:
        soup = get_soup(category_url)
        books = soup.find_all("div", class_="image_container")
        
        for book in books:
            book_url =  book.find("a")["href"]
            clean_url = book_url.replace("../", "")
            full_url = urljoin(BASE_URL, clean_url)
            yield full_url

        next_button = soup.find("li", class_="next")

        if next_button:
            next_url = next_button.find("a")["href"]
            build_next_url = category_url.rsplit('/', 1)[0] + '/' + next_url # On selectionne a partir de la droite (1) pour recuperer l'url de base la partie avant le / [0] et on ajoute le next_url
            category_url = build_next_url
        else:
            category_url = None

# use yield



