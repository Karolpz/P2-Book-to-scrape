from scrapers.utils import get_soup

BASE_URL = "https://books.toscrape.com/index.html"

def scrape_all_categories():
    
    soup = get_soup(BASE_URL)
    category_section = soup.find("ul", class_="nav-list").find("ul")
    category_links = category_section.find_all("a")
    
    for link in category_links:
        category_name = link.text.strip()
        category_url = link["href"]
        full_url = BASE_URL.rsplit('/', 1)[0] + '/' + category_url
        yield {"name": category_name, "url": full_url}
