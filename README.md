* **Note**: This repository is a work in progress. More scripts are supposed to be added in this repository in near future.

# What is Web Scraping

**Web Scraping** is a computer software technique used for extracting large amounts of information from websites. It mainly focuses on the transformation of unstructured data (in the form of HTML) to structured tree format data (database, CSV). This is particularly useful when we want to organize and analyse data obtained from a website, outside of the browse, and then study and draw patterns in them.

# Difference between Web Crawler and Web Scraper

**Web crawlers** browse through a series of links present on webpages and index them in a database. This process of following various links of webpages is referred to as **crawling**. As they are used on a large scale at a time (i.e. run on larg e number of websites at once), they yield generic information. Its main purpose is locating information on the web and indexing it.

**Web scrapers** primarily extract data from webpages. They capture the contents of pages that it has crawled, extracts the required information and stores them in an organized manner for further study. Though web scrapers can crawl to different pages their primary purpose is scraping the data on those pages, not indexing the web.

# Is it Legal?

Generally, if you are using scraped data for personal use and do not plan to republish that data, it may not cause any problems. Read the Terms of Use, Conditions of Use, and also the **robots.txt** before scraping the website. You must follow the robots.txt rules before scraping, otherwise, the website owner has every right to take legal action against you.

One may check the robots.txt of a website by adding a `/robots.txt` after the URL of the website. The following link would give a beneficial insight about robots.txt

1. [How to Read and Respect Robots.txt](https://www.promptcloud.com/blog/how-to-read-and-respect-robots-file/)

# Python Tools for Web Scraping

**Beautiful Soup** is a Python library for getting data out of HTML, XML, and other markup languages. It is a data parser. Beautiful Soup helps you pull particular content from a webpage, remove the HTML markup, and save the information. It is a tool for web scraping that helps you clean up and parse the documents you have pulled down from the web.

**Scrapy** is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival. It can also be used to extract data using APIs. It is a complete web scraping solution.

**Selenium** is an open-source web testing tool. It is used to automate browser activities, hence it is also known as a web-driver. It is particularly useful for scraping, if the website uses JavaScript to serve content.

Other libraries (such as **Requests**, **lxml**), also have their own benefits. All of these libraries have quite a simple learning curve, and contain good documentation.

# Resources

1. [Web Scraping Toolbox](http://toscrape.com/)
1. [Python Web Scraping Tutorial](https://medium.com/quick-code/python-web-scraping-tutorial-74ace70e01)
1. [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
1. [How to Build a Web Scraper With Python [Step-by-Step Guide]](https://hackernoon.com/how-to-build-a-web-scraper-with-python-step-by-step-guide-jxkp3yum)
1. [Beginner’s guide to Web Scraping in Python using BeautifulSoup](https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/)
1. [5 Tasty Python Web Scraping Libraries](https://elitedatascience.com/python-web-scraping-libraries)
