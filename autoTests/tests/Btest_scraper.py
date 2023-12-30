import params as params
import requests
from bs4 import BeautifulSoup as BS
from PIL import Image
from io import BytesIO

s= input("search for : ")
p = {'q': s}

r= requests.get("https://www.bing.com/images/search", params=params)
soup = BS(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})
for item in links:
    img_obj = requests.get(item.attrs["href"])
    title= item.attrs["href"].split("/")[-1]
    img = Image.open(img_obj.content)
    img.save("./scraped_images" + title, img.format)
print(soup)