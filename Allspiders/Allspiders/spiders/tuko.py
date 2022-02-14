# -*- coding: utf-8 -*-
import scrapy

from ..items import  MytukonewsItem
class TukoSpider(scrapy.Spider):
    name = "tuko"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/tuko']
    custom_settings = {
        'ITEM_PIPELINES': {'Allspiders.pipelines.MytukonewsPipeline': 300},
    }
    def parse(self, response):
        items = MytukonewsItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/tuko?page=' + str(TukoSpider.page_number)
        if TukoSpider.page_number < 2:
            TukoSpider.page_number += 1
            yield response.follow(next_page, self.parse)

