import scrapy


class Spidercitacoes(scrapy.Spider):
    name = "citacoes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pagina = response.url.split("/")[-2]
        nome_arquivo = f'citacoes={pagina}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)


        self.log(f'arquivo salvo {nome_arquivo}')