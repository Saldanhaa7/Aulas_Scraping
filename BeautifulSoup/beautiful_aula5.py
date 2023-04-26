from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000/site.html")
soup = BeautifulSoup(html, "html.parser")

# O método prettify "embelezar" organiza
# o conteúdo do parser mostrando
# uma árvore com as tags HTML/XML
print("Veja o conteúdo com o prettify")
print(soup.prettify())

print("\nVeja o conteúdo sem o prettify")
print(soup)

print("")
print("Título do documento:")
print(soup.title)

print("")
print("Nome da tag título:")
print(soup.title.name)

print("")
print("Texto da tag título:")
print(soup.title.string)

print("")
print("Tag pai da tag title:")
print(soup.title.parent)

print("")
print("Nome da tag pai da tag title:")
print(soup.title.parent.name)

print("")
print("Primeira tag 'p' do Texto:")
print(soup.p)

print("")
print("Conteúdo da propriedade class da primeira tag p:")
print(soup.p['class'])

print("")
print("Primeira ocorrência da tag 'a':")
print(soup.a)

print("")
print("Todas ocorrências da tag 'a':")
print(soup.findAll('a'))

print("")
print("Buscando uma tag denominada cujo id seja link3:")
print(soup.find(id="link3"))


print("")
print("Pegando todos os links do documento:")
for link in soup.findAll('a'):
    print(link.get('href'))

print("")
print("Pegando todos os textos do documento:")
print(soup.getText())