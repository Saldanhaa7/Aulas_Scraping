import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com.br"]
    start_urls = ["https://www.amazon.com.br/gp/bestsellers/amazon-devices/ref=zg_bs_nav_0"]

    def parse(self, response):
        for product in response.xpath("//div[@class='a-section a-spacing-none p13n-asin']"):
            yield {
                "name": product.xpath(".//span[@class='a-size-small a-color-base']/text()").get(),
                "price": product.xpath(".//span[@class='p13n-sc-price']/text()").get(),
                "image_url": product.xpath(".//img/@src").get(),
            }
