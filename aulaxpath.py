from lxml import html, etree
from urllib.request import urlopen
from urllib.request import Request
 
req = Request("http://www.pythonparatodos.com.br/formulario.html",
              headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

pagina = urlopen(req)
tree = html.fromstring(pagina.read())
body = tree.xpath('//tr')
print(body)
for elemento in body:
    print(etree.tostring(elemento))