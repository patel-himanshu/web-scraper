# Scrapy

Scrapy is a popular open source framework for extracting the data you need from websites in a fast, simple, yet extensible way. It can be used for a wide range of useful applications, like data mining, information processing or historical archival. It can also be used to extract data using APIs. It is a complete web scraping solution.

## Installation

To install Scrapy on your system, execute the following command on your Terminal (if on Linux or Mac OSX) or Command Prompt (if on Windows).
> `pip install scrapy`

## Some Basic Commands

| Command | Purpose | Example |
| :--- | :--- | :-- |
| `scrapy startproject <project_name>` | To start a new Scrapy project | `scarpy startproject myfirstscraper` |
| `scrapy genspider <spider_name> <url>` | Creates a spider for given URL in **spiders/** folder with a basic template | `scrapy genspider reddit_mcu https://www.reddit.com/r/marvelstudios/` |

## Resources 

1. [Scrapy: Official Documentation](https://scrapy.org/)
1. [Introduction to Scrapy](https://www.pythongasm.com/introduction-to-scrapy/)
1. [Web Scraping in Python using Scrapy](https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/)