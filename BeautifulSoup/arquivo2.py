from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/")
bsOjt = BeautifulSoup(html.read(), "html.parser")

for link in bsOjt.find_all('a'):
    print(link.get('href'))