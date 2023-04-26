from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

req = Request("https://evaldowolkers.wordpress.com/python-web-scraping-aula-05-um-pouco-mais-de-beautifulsoup/")

html = urlopen(req).read()

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("a", {"href":re.compile("/categorias/")})

for link in links:
    print(link["href"])