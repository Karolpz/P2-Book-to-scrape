import requests
import csv
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        raise Exception(f"Failed to retrieve page: {response.status_code}")

def save_soup_to_file(data, file_path):
    headers = ["Title", "Price", "Availability", "Description", "Rating"]
    with open(file_path, 'w',newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        if isinstance(data, list):
            writer.writerows(data)
        else:
            writer.writerow(data)
