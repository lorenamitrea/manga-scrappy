import requests
import shutil
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


def save_image(url, location, headers):
    image_content = requests.get(url, headers=headers, stream=True)
    with open(location, 'wb') as out_file:
        shutil.copyfileobj(image_content.raw, out_file)
