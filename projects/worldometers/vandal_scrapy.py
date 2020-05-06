import scrapy
from scrapy.crawler import CrawlerProcess


class SpiderVandal(scrapy.Spider):
    name = 'vandal.net'
    allowed_domains = ['https://vandal.elespanol.com/']
    custom_settings = {'FEED_FORMAT': 'json', 
                       'FEED_URI': 'resultados_scrapy.json',
                      'DEPTH_LIMIT' : 2,
                      'FEED_EXPORT_ENCODING' : 'utf-8'}
                      
    start_urls = ['https://vandal.elespanol.com/noticias/pc', 
                'https://vandal.elespanol.com/noticias/playstation-4', 
                'https://vandal.elespanol.com/noticias/xbox-one', 
                'https://vandal.elespanol.com/noticias/nintendo-switch', 
                'https://vandal.elespanol.com/noticias/playstation-5', 
                'https://vandal.elespanol.com/noticias/xbox-series-x']
    
    def parse(self, response):   
        news_list = response.xpath('//div[@class="span8"]/div/h2/a/@href').getall()
        for new in news_list:
            yield response.follow(new, callback=self.parse_new)
        
        next_page = response.xpath('//a[@id="siguientelink"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_new(self, response):
        title = response.xpath('//article[@class="articulo"]//h1/text()').get()
        body = response.xpath('//article[@class="articulo"]//span/text()').get()
        autor = response.xpath('//div[@class="autorarticulo"]//a/text()').get()
        yield {'autor' : autor,
                'url' : response.url,
                'title' : title,
                'body' : body}


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(SpiderVandal)
    process.start()