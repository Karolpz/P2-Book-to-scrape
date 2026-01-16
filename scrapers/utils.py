import requests
import csv
import os
import re
from bs4 import BeautifulSoup

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

def get_soup(url):
    response = session.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')

def save_book_to_file(data, category_name):
    headers = ["Title", "Price", "Availability", "Description", "Rating", "Image"]
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{category_name}.csv"

    with open(file_path, 'w',newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        if isinstance(data, list):
            writer.writerows(data)
        else:
            writer.writerow(data)

def download_image(img_url, file_name, category_name):

    clean_name = re.sub(r'[\\/*?:"<>|]', "", file_name)
    conventional_name = clean_name.replace(" ", "_").lower()[:100] 
    final_file_name = conventional_name + ".jpg"
    
    dir_path = f"images/{category_name.replace(' ', '_').lower()}"
    os.makedirs(dir_path, exist_ok=True)
    
    response = session.get(img_url)
    
    if response.status_code == 200:
        with open(os.path.join(dir_path, final_file_name), 'wb') as file:
            file.write(response.content)
    else:
        print(f"Échec du téléchargement pour {final_file_name} : {response.status_code}")
