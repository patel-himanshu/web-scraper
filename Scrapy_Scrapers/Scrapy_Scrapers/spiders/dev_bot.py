# -*- coding: utf-8 -*-
import scrapy


class DevBotSpider(scrapy.Spider):
    name = 'dev_bot'
    allowed_domains = ['https://dev.to/']
    start_urls = ['http://https://dev.to//']

    def parse(self, response):
        # TITLE of the blog post
        title = response.css('h3::text').getall() # Extracts title of post and removes whitespaces from both sides
        
        # AUTHOR NAME of the blog post
        author = []
        author.append(response.css('.featured-user-name a::text').get().strip()) # Extracting author name of featured post
        author.extend(response.css('h4 a::text').extract()) # Extracting author name of remaining posts
        
        # DATE and TIME of the blog post, added after changing their formatting
        # Extracted timestamp: '2020-04-16T10:24:46Z'
        # After formatting: '2020-04-16 10:24:46'
        timestamp = response.css('time::attr(datetime)').extract()
        date_time = []
        for item in date_time:
            date_time_temp = item[:-1] # Removing "Z" present at the last index
            date_time_temp = date_time_temp.replace('T', ' ') # Replacing 'T' in between date and time, with a space
            date_time.append(date_time_temp) # Adding formatted date time
        
        # READING TIME of the blog post
        readtime = response.css('.article-reading-time::text').extract()
        
        # NUMBER OF COMMENTS AND LIKES on the blog post
        # Some blog posts don't have any comments
        engagement_details = response.css('.engagement-count-number::text').extract() # Stores comments as well as likes
        comments, likes = [], []
        
        # "flag" is being used to indicate the list in which the last entry was made
        # If "flag" == 0, means last entry was made for "comments"
        # If "flag" == 1, means last entry was made for "likes"
        flag = None

        # if response.css('.engagement-count-number::text').get()[0] != '\n': # First entry is of "comments"
        #     flag = 0
        # else: # First entry is of "likes"
        #     flag = 1

        for entry in engagement_details:
            if entry[0] != '\n': # It is an entry for "comments" list
                
                if entry == engagement_details[0]: # First entry of "engagement_details" is related to "comments"
                    flag = 0
                elif flag == 0: # Last entry was also made in the list "comments"
                    likes.append(None)
                else: # Last entry was made in the list "likes"


                comments.append(int(entry)) # Adding "comments count" entry after typecasting into "int"


            else: # It is an entry for "likes" list
                
                if entry == engagement_details[0]:
                    flag = 1
                elif flag == 0: # If last entry was of "comments", changing flag to 1
                    flag = 1
                else: # Last entry was also of "likes", which means 
                    pass

                likes_count = entry.strip('\n') # Removing newline characters from both sides
                likes_count = likes_count.strip() # Removing whitespaces from both sides
                likes.append(int(likes_count)) # Adding "likes count" entry after typecasting into "int"