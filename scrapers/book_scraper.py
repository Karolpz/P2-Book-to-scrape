from scrapers.utils import get_soup
from urllib.parse import urljoin
BASE_URL = "https://books.toscrape.com/"
def scrape_book_info(book_url):
    soup = get_soup(book_url)

    product_page_url = book_url
    universal_product_code = soup.find("th", text="UPC").find_next_sibling("td").text
    title = soup.find("h1").text
    price_including_tax = soup.find("th", text="Price (incl. tax)").find_next_sibling("td").text
    price_excluding_tax = soup.find("th", text="Price (excl. tax)").find_next_sibling("td").text
    number_available = soup.find("th", text="Availability").find_next_sibling("td").text
    category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()

    description_div = soup.find("div", id="product_description")
    if description_div:
        product_description = description_div.find_next_sibling("p").text.strip()
    else:
        product_description = "No description available."

    rating_class = soup.find("p", class_="star-rating")["class"]
    if rating_class:
        review_rating = rating_class[1]
    else:
        review_rating = "No rating available."

    img_div = soup.find("div", class_="item active")
    if img_div:
        image_url_relative = img_div.find("img")["src"]
        image_url = urljoin(BASE_URL, image_url_relative)
    else:
        image_url = "No image available."

    return {
    "Product Page URL": product_page_url,
    "UPC": universal_product_code,
    "Title": title,
    "Price (incl. tax)": price_including_tax,
    "Price (excl. tax)": price_excluding_tax,
    "Availability": number_available,
    "Description": product_description,
    "Rating": review_rating,
    "Image": image_url,
    "Category": category
}



