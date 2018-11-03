from bs4 import BeautifulSoup
import requests

request = requests.get("http://www.amazon.com/dp/B07GTBC3WW/ref=nav_timeline_asin?_encoding=UTF8&psc=1")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price"})
print(element.text.strip())
