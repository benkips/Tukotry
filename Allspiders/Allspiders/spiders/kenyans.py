# -*- coding: utf-8 -*-
import scrapy

from ..items import  KenyansItem
class KenyansSpider(scrapy.Spider):
    name = "kenyans"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/kenyans']
    custom_settings = {
        'ITEM_PIPELINES': {'Allspiders.pipelines.KenyansPipeline': 300},
    }

    def parse(self, response):
        items = KenyansItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/kenyans?page=' + str(KenyansSpider.page_number)
        if KenyansSpider.page_number < 2:
            KenyansSpider.page_number += 1
            yield response.follow(next_page, self.parse)

