from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print("Ocorreu um erro HTTP: {erro}")
        return None
    except URLError as erro:
        print("Ocorreu um erro URL: {erro}")
        return None
    except:
        print("Ocorreu um erro na página!")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print("Ocorreu um erro de Atributo: {erro}")
        return None
    except:
        print("Ocorreu um erro ao acessar o conteúdo!")
        return None
    
    return titulo

titulo = getTitulo(input("Informe a URL completa: "))

if titulo is not None:
    print(titulo)
else:
    print("Titulo não encontrado.")