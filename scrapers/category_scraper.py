from scrapers.utils import get_soup

def scrape_book_from_category_info(url):
    all_titles = []

    while url:
        soup = get_soup(url)

        titles = soup.find_all("h3")
        
        for title in titles:
            book_title =  title.find("a")["title"]
            all_titles.append(book_title)

        next_button = soup.find("li", class_="next")

        if next_button:
            next_url = next_button.find("a")["href"]
            build_next_url = url.rsplit('/', 1)[0] + '/' + next_url # On selectionne a partir de la droite (1) pour recuperer l'url de base la partie avant le / [0] et on ajoute le next_url
            url = build_next_url
        else:
            url = None
    
    return all_titles



