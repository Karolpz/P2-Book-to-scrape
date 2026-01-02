import requests
from bs4 import BeautifulSoup

from scrapers.utils import get_soup

def scrape_book_info(url):
    soup = get_soup(url)

    book_title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    availability = soup.find("p", class_="instock availability").text.strip()

    description_div = soup.find("div", id="product_description")
    if description_div:
        description = description_div.find_next_sibling("p").text.strip()
    else:
        description = "No description available."

    rating_class = soup.find("p", class_="star-rating")["class"]
    if rating_class:
        rating = rating_class[1]
    else:
        rating = "No rating available."
        
    return {
    "Title": book_title,
    "Price": price,
    "Availability": availability,
    "Description": description,
    "Rating": rating
}


url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

scrape_book_info(url)

