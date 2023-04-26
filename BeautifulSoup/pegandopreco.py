from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.amazon.com.br/gp/bestsellers/?ref_=nav_cs_bestsellers")
bsObjt = BeautifulSoup(html.read(), "html.parser")


for preco in bsObjt.find_all('span', class_="_cDEzb_p13n-sc-price_3mJ9Z"):
    print(preco)