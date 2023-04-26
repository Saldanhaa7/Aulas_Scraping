import scrapy


class NextSpider(scrapy.Spider):
    name = "next"
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for citacao in response.css('div.quote'):
            yield {
                'texto': citacao.css('span.text::text').extract_first(),
                'autor': citacao.css('small.author::text').extract_first(),
                'tag': citacao.css('div.tags a.tag::text').extract()
            }

            pagina = response.url.split("/")[-2]
            nome_arquivo = f"citacoes-{pagina}.html"
            with open(nome_arquivo, 'wb') as f:
                f.write(response.body)
            next_page = response.css('li.next a::attr(href)').extract_first()

            for href in response.css('li.next a::attr(href)'):
                yield response.follow(href, callback=self.parse)
