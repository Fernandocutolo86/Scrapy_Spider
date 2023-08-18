
import scrapy
from scrapy.http import Request
import csv

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    # URLs iniciais para começar a raspagem
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # Selecionar as citações na página
        quotes = response.css(".quote")
        for quote in quotes:
            author = quote.css(".author::text").get()
            text = quote.css(".text::text").get()
            tags = quote.css(".tags .tag::text").getall()

            # Verificando os critérios
            if author == "Mark Twain" and "life" in tags:
                # Salvar os critérios em um arquivo de texto
                with open(f"quotes/{author}-{text}.txt", "w") as f:
                    f.write(text)

                # Exportar para um arquivo CSV
                with open("quotes.csv", "a", newline='') as f:
                    writer = csv.writer(f, delimiter=";")
                    writer.writerow([author, ', '.join(tags), response.url, 1, f"quotes/{author}-{text}.txt"])

        # Ir para a próxima página, se existir
        next_page = response.css(".next a::attr(href)").get()
        if next_page is not None:
            yield Request(next_page, callback=self.parse)

        # Executar o spider quando o arquivo for executado diretamente
	if _name_ == "_main_":
  	  from scrapy.crawler import CrawlerProcess
    
    	process = CrawlerProcess()
    	process.crawl(QuotesSpider)
    	process.start()



