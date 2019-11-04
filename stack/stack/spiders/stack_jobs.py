# -*- coding: utf-8 -*-
import scrapy


class StackJobsSpider(scrapy.Spider):
    name = 'stack_jobs'
    start_urls = ['https://stackoverflow.com/jobs?sort=p']

    def parse(self, response):
        for result in response.css('.listResults div.-item.-job'):
            yield {
                'company': result.css('div .-company span::text').extract_first(),
                'posted': result.css('span .fc-black-500::text').extract_first(),
                'title': result.css('div .job-details__spaced .job-link::text').extract_first(),
                'url': 'http://stackoverflow.com/{}'.format(
                    result.css('div .job-details__spaced .job-link::attr(href)').extract_first()
                ),
            }
            

        next_page = response.css('.pagination a.test-pagination-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
