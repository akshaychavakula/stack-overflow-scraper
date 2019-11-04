# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
            
        NEXT_PAGE_SELECTOR = "//a[@title='go to page 2']/@href"
        next_page = response.xpath(NEXT_PAGE_SELECTOR)
        if next_page:
            path = next_page.extract_first()
            nextpage = response.urljoin(path)
            print("Found url: {}".format(nextpage))
            yield scrapy.Request(
                nextpage,
                callback = self.parse
            )
            
          
            
            
            
    
        
