# -*- coding: utf-8 -*-
import scrapy


class CatchTechSpider(scrapy.Spider):
    name = 'catch_tech'
    allowed_domains = ['www.catch.com.au']

    def start_requests(self):
        yield scrapy.Request(url='https://www.catch.com.au/shop/electronics/all', callback=self.parse, headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath("//div[@class='product']"):
            yield {
                'title': product.xpath(".//a[@class='js-product-link product--title-link js-dnt']/text()").get(),
                'brand': product.xpath(".//div[@class='product--brand ']/a/text()").get(),
                'price': product.xpath(".//span[@class='price--dollars']/text()").get() + " USD",
                'url': response.urljoin(product.xpath(".//a[@class='js-product-link product--title-link js-dnt']/@href").get()),
                'User-agent': response.request.headers['User-Agent']
            }

        next_page = response.urljoin(response.xpath("(//a[@class='button'])[last()]/@href").get())

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        })
