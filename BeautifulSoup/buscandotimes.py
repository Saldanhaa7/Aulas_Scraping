from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

paginas = set()
paginas_invalidas = set()
nova_pagina = ""

def abrir_pagina(url_da_pagina):
    global paginas
    global paginas_invalidas

    try:
        if url_da_pagina not in paginas_invalidas:
            html = urlopen(url_da_pagina)
            bsObj = BeautifulSoup(html, "html.parser")
            brasileirao_top10 = ('.palmeiras.|.futebol/times/internacional.|.corinthians.|.flamengo.|.fluminense.|.sao-paulo.|athletico-pr.|.atlético-mg.|.américa-mg.|.fortaleza.')
            for link in bsObj.find_all("a", href=re.compile(brasileirao_top10)):
                if "href" in link.attrs:
                    if link.attrs['href'] not in paginas and link.attrs['href'] not in paginas_invalidas:
                        nova_pagina = link.attrs['href']
                        print(nova_pagina)
                        paginas.add(nova_pagina)
                        abrir_pagina(nova_pagina)
    except:
        paginas_invalidas.add(nova_pagina)

abrir_pagina("https://ge.globo.com/")