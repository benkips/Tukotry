import scrapy

from..items import KenyansItem


class kenyanscrapy(scrapy.Spider):
    name = "kenyans"
    page_number = 1
    start_urls = ['https://www.kenyamoja.com/news/kenyans']

    def parse(self, response):
        items = KenyansItem()

        for quote in response.css('div.item-list ul li div.news-title'):
            titles = quote.css('a::text').extract()
            links = quote.css('a::attr(href)').extract()

            items['title'] = titles
            items['links'] = links

            yield items

        next_page = 'https://www.kenyamoja.com/news/kenyans?page=' + str(kenyanscrapy.page_number)
        if kenyanscrapy.page_number < 2:
           kenyanscrapy.page_number += 1
           yield response.follow(next_page, self.parse)
