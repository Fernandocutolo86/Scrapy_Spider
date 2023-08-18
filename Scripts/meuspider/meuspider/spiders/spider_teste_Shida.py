import scrapy


class SpiderTesteShidaSpider(scrapy.Spider):
    name = "spider_teste_Shida"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        pass
    

