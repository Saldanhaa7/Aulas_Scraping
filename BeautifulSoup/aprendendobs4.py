from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://lojasalways.com.br/marcas/quiksilver/?mpage=5")
bsOjt = BeautifulSoup(html.read(), "html.parser")

nome = bsOjt.find_all('div', class_="js-item-name")
preco = bsOjt.find_all('span', class_="js-price-display")
tabela = []
tbpreco = []
for x in nome:
    clear = re.compile('<.*?>')
    limpo = (re.sub(clear, '', str(x)))
    limpo = limpo.replace('Saiba Mais', '')
    print(limpo)

for y in preco:
    clear = re.compile('<.*?>')
    limpo = (re.sub(clear, '', str(y)))
    print(limpo.strip())