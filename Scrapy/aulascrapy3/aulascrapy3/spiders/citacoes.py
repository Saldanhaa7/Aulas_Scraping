import scrapy


class CitacoesSpider(scrapy.Spider):
    name = "citacoes"

    start_urls = [            
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
        "https://quotes.toscrape.com/page/3/",
        "https://quotes.toscrape.com/page/4/",
        ]

    def parse(self, response):
        for citacao in response.css('div.quote'):
            yield {
                'texto': citacao.css('span.text::text').extract_first(),
                'autor': citacao.css('small.author::text').extract_first(),
            }