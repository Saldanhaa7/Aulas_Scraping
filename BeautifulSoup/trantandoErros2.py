from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.udemy.com")
bsObj = BeautifulSoup(html.read(), "html.parser")

try:
    resultado = bsObj.html.aaaa.aaaa
    print(resultado)
except AttributeError as erro:
    print(f"Erro: {erro}")