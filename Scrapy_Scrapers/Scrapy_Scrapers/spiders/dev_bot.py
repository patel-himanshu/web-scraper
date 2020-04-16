# -*- coding: utf-8 -*-
import scrapy


class DevBotSpider(scrapy.Spider):
    name = 'dev_bot'
    allowed_domains = ['https://dev.to/']
    start_urls = ['http://https://dev.to//']

    def parse(self, response):
        title = response.css('h3::text').getall() # Extracts title of post and removes whitespaces from both sides
        
        author = []
        author.append(response.css('.featured-user-name a::text').get().strip()) # Extracting author name of featured post
        author.extend(response.css('h4 a::text').extract()) # Extracting author name of remaining posts
        
        timestamp = response.css('time::attr(datetime)').extract()
        
        engagement_count = response.css('.engagement-count-number::text').extract()
        comments, likes = [], []

        readtime = response.css('.article-reading-time::text').extract()