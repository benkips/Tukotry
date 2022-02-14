import scrapy

from..items import StarItem


class starscrapy(scrapy.Spider):
    name = "star"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/star']

    def parse(self, response):
        items = StarItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/star?page=' + str(starscrapy.page_number)
        if starscrapy.page_number < 2:
           starscrapy.page_number += 1
           yield response.follow(next_page, self.parse)
