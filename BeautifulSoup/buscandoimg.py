from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, "html.parser")

imagens = soup("img", {"src":re.compile("\.{2}/img/gifts/img\d*\.jpg")})

for imagem in imagens:
    print(imagem["src"])