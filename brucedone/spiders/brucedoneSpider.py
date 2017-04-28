# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from brucedone.items import BrucedoneItem
from scrapy.selector import Selector

class BrucedoneSpider(Spider):
    name = 'brucedone'
    start_urls = ['http://brucedone.com']
    allowed_domains = ["brucedone.com"]

    def parse(self,response):
        item = BrucedoneItem()
        articles = response.xpath('//*[@id="main"]')
        for article in articles:
            item['title'] = article.xpath('.//article/div/div[2]/header/h2/a/text()').extract()
            item['content'] = article.xpath('.//article/div/div[2]/div/p/text()').extract()
            item['date'] = article.xpath('.//article/div/div[3]/span[1]/a[1]/text()').extract()
            item['comment'] = article.xpath('.//article/div/div[3]/span[1]/a[2]/text()').extract()
            item['views'] = article.xpath('.//article/div/div[3]/span[2]/a[1]/text()').extract()
            item['like'] = article.xpath('.//article/div/div[3]/span[2]/a[2]/text()').extract()
            yield item
