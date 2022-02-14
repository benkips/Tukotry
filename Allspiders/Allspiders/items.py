# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AllspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class KenyansItem(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()

class MytukonewsItem(scrapy.Item):
    title = scrapy.Field()
    links= scrapy.Field()

class StarItem(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()