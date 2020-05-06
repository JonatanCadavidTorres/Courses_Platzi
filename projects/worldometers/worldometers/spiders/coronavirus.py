# -*- coding: utf-8 -*-
import scrapy
import logging
from datetime import date


class CoronavirusSpider(scrapy.Spider):
    name = 'coronavirus'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        countries = response.xpath('//a[@class="mt_a"]')
        for country in countries:
            country_name = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            #absolute_url = f"https://www.worldometers.info/coronavirus/{country_link}"
            #absolute_url = response.urljoin(country_link)

            yield response.follow(url=country_link, callback=self.parse_country, meta={'countryname':country_name})

    def parse_country(self, response):
        country_name = response.request.meta['countryname']
        consulting_day = date.today()
        coronavirus_cases = response.xpath("(//div[@class='maincounter-number']/span/text())[1]").get()
        coronavirus_deaths = response.xpath("(//div[@class='maincounter-number']/span/text())[2]").get()
        coronavirus_recovered = response.xpath("(//div[@class='maincounter-number']/span/text())[3]").get()
        yield {
            'country_name': country_name,
            'consulting_day':consulting_day,
            'coronavirus_cases':coronavirus_cases,
            'coronavirus_deaths':coronavirus_deaths,
            'coronavirus_recovered':coronavirus_recovered
        }

#to get the csv, json or xml file, we can use the command: scrapy crawl coronavirus -o coronavirus_cases.json