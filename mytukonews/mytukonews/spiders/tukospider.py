import scrapy

from..items import MytukonewsItem


class mytukoscrapy(scrapy.Spider):
    name = "tuko"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/tuko']

    def parse(self, response):
        items = MytukonewsItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/tuko?page=' + str(mytukoscrapy.page_number)
        if mytukoscrapy.page_number < 1:
           mytukoscrapy.page_number += 1
           yield response.follow(next_page, self.parse)
