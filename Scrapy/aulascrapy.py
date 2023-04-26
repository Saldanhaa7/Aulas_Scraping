from scrapy import Selector
from urllib.request import urlopen, Request


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = 'https://www.saraiva.com.br/livros/ciencias-exatas-engenharia-e-tecnologia?map=c,c&order=OrderByBestDiscountDESC'
req = Request(url=reg_url, headers=headers)
html = urlopen(req)
sel = Selector(text = html.read())
lista = sel.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "vtex-product-price-1-x-currencyInteger", " " ))]')
print(lista)