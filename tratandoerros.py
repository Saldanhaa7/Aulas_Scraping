from urllib.request import urlopen
from urllib.error import HTTPError, URLError

html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/")
print(f"html 1: {html}")

try:
    html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/aaaaa")
    print(f"html 2: {html}")
except HTTPError as erro:
    print(f"Erro HTTP: {erro}")

html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/")
print(f"html 3: {html}")

try:
    html = urlopen("https://www.kgnhewrlbaaslfqawrfqwmgvdsm.com.br")
    print(f"html 4: {html}")
except URLError as erro:
    print(f"Erro URL: {erro}")

html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/")
print(f"html 5: {html}")