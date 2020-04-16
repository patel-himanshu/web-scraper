# -*- coding: utf-8 -*-
import scrapy


class RedditMcuSpider(scrapy.Spider):
    name = 'reddit_mcu'
    allowed_domains = ['https://www.reddit.com/r/marvelstudios/']
    start_urls = ['http://https://www.reddit.com/r/marvelstudios//']

    def parse(self, response):
        title = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
        #author = response.css('a._2tbHP6ZydRpjI44J3syuqC._23wugcdiaj44hdfugIAlnX.oQctV4n0yUb0uiHDdGnmE::text').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()