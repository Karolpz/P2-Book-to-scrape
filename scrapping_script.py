import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

book_title = soup.find("h1").text
price = soup.find("p", class_="price_color").text
availability = soup.find("p", class_="instock availability").text.strip()

description_div = soup.find("div", id="product_description")
if description_div:
    description = description_div.find_next_sibling("p").text.strip()
else:
    description = "No description available."

rating_class = soup.find("p", class_="star-rating")["class"]# le ["class"] nous donne une liste
rating = rating_class[1]  

with open("book_info.csv", "w",newline="", encoding="utf-8-sig") as file:
    file.write("Title,Price,Availability,Description,Rating\n")
    file.write(f'"{book_title}","{price}","{availability}","{description}","{rating}"\n')

print(f"{book_title} costs {price} and is {availability}")