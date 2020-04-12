import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.reddit.com/r/BabyYoda"

# response object
response = requests.get(url)

# bs instance - instantiates a web scraper
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())

images = soup.find_all("img", attr={"alt":"Post image"})

number = 0

for image in images: 
  image_src = images["src"]
  print(image_src)
  urllib.requests.urlretrieve(image_src, str(number))
  number += 1



