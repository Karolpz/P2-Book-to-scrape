import requests
import csv
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        raise Exception(f"Failed to retrieve page: {response.status_code}")

def save_book_to_file(data, category_name):
    headers = ["Title", "Price", "Availability", "Description", "Rating"]
    file_path = f"data/{category_name}.csv"
    
    with open(file_path, 'w',newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        if isinstance(data, list):
            writer.writerows(data)
        else:
            writer.writerow(data)
