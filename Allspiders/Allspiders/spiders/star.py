# -*- coding: utf-8 -*-
import scrapy

from ..items import  StarItem
class StarSpider(scrapy.Spider):
    name = "star"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/star']
    custom_settings = {
        'ITEM_PIPELINES': {'Allspiders.pipelines.StarPipeline': 300},
    }
    
    def parse(self, response):
        items = StarItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/star?page=' + str(StarSpider.page_number)
        if StarSpider.page_number < 2:
            StarSpider.page_number += 1
            yield response.follow(next_page, self.parse)