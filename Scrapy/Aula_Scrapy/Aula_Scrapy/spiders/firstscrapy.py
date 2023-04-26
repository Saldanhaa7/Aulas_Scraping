import scrapy


class FirstscrapySpider(scrapy.Spider):
    name = "firstscrapy"
    start_urls = [            
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
        ]

    def parse(self, response):
        for citacao in response.css('div.quote'):
            yield {
                'texto': citacao.css('span.text::text').extract_first(),
                'autor': citacao.css('small.author::text').extract_first(),
                'tags': citacao.css('div.tags a.tag::text').extract
            }