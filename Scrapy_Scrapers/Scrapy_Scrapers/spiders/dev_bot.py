# -*- coding: utf-8 -*-
import scrapy


class DevBotSpider(scrapy.Spider):
    name = 'dev_bot'
    allowed_domains = ['https://dev.to/']
    start_urls = ['http://https://dev.to//']

    def parse(self, response):

    # TITLE of the blog post
        
        # Extracts title of post
        titles_all = response.css('h3::text').extract()
        # Removing all whitespaces from the titles
        title = [title_single.strip() for title_single in titles_all]

    # AUTHOR NAME of the blog post
        
        author = []
        # Extracting author name of featured post, and removing trailing separator
        author.append(response.css('.featured-user-name a::text').get().strip()[:-2])
        
        # Extracting names of authors of remaining posts
        rem_names = response.css('h4 a::text').extract()
        # Removing whitespaces and removing trailing separator text from other author's names
        # and also excluding empty strings
        cleaned_names = [name.strip()[:-2] for name in rem_names if name.strip()!='']
        
        # Combining both lists into a single list
        author.extend(cleaned_names)

    # DATE and TIME of the blog post, added after changing their formatting
        
        # Example of formatting done
        # Extracted timestamp: '2020-04-16T10:24:46Z'
        # After formatting: '2020-04-16 10:24:46'
        
        timestamp = response.css('time::attr(datetime)').extract()
        date_time = []

        for item in timestamp:

            # Removing "Z" present at the last index
            date_time_temp = item[:-1]

            # Replacing 'T' in between date and time, with a space
            date_time_temp = date_time_temp.replace('T', ' ')
            # Adding formatted date time
            date_time.append(date_time_temp)  

    # READING TIME of the blog post
        
        readtime = response.css('.article-reading-time::text').extract()

    # NUMBER OF COMMENTS AND LIKES on the blog post
        
        # Some blog posts don't have any comments
        # The list "engagement_details" stores comments as well as likes
        engagement_details = response.css('.engagement-count-number::text').extract()
        comments, likes = [], []

        # "flag" is being used to indicate the list in which the last entry was made
        # If "flag" == 0, means last entry was made for "comments"
        # If "flag" == 1, means last entry was made for "likes"
        flag = None

        for entry in engagement_details:

            # COMMENTS on the blog post
            if entry[0] != '\n':

                # First entry of "engagement_details" is related to "comments"
                if entry == engagement_details[0]:
                    flag = 0
                
                # Last entry was also made in the list "comments", which means previous blog had no "likes"
                elif flag == 0:  
                    likes.append(0)
                
                # Last entry was made in the list "likes"
                else:  
                    flag = 1

                # Finally, adding "comments count" entry after typecasting into "int"
                comments.append(int(entry))

            # LIKES on the blog post
            else:

                # First entry of "engagement_details" is related to "likes"
                if entry == engagement_details[0]:
                    flag = 1
                
                # If last entry was of "comments", changing flag to 1
                elif flag == 0:  
                    flag = 1
                
                # Last entry was also made to the list "likes", which means previous blog had no "comments"
                else: 
                    comments.append(0)

                # Removing newline characters from both sides
                likes_count = entry.strip('\n')
                # Removing whitespaces from both sides
                likes_count = likes_count.strip()  
                # Adding "likes count" entry after typecasting into "int"
                likes.append(int(likes_count))

    # STORING INFORMATION IN A DICTIONARY
    # len(title)
    # len(author)
    # len(readtime)
    # len(comments)
    # len(likes)
    # len(date_time)
        for item in zip(title, author, date_time, likes, comments, readtime):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'author' : item[1],
                'created_at' : item[2],
                'likes' : item[3],
                'comments' : item[4],
                'reading_time' : item[5]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info