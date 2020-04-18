# By making use of only 1 tab

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time

base_url = 'https://stockx.com/handbags/most-popular'

search_limit = 200 # Tells the number of products to limit our search

count_total = 0 # Stores the total count of products accounted for
count_page = 0 # Stores the count of products accounted in a single page
page_num = 1 # Stores the current page number of catalog
flag = 1

pages_urls = [] # Stores the links of all products which will be taken into consideration
brand = [] # Stores the brand name of products
model = [] # Stores the model name of products
sale_price = [] # Stores the last sale price of products
ask_lowest = [] # Stores the lowest ask value of products
bid_highest = [] # Stores the highest bid value of products
total_sales = [] # Stores the total number of sale of products
price_premium = [] # Stores the premium price above the retail price of products
avg_price = [] # Stores the average sale price of products

brand_product_count = {} # Stores the total number of products of a brand
brand_product_total = {} # Stores the sum of average price of each product of a brand

# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options = options)

driver = webdriver.Firefox() # Opens a new Firefox window

# For XPath of links used for moving to next page
pagination_head = '/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a['
pagination_tail = ']'

# For XPath of links used to select individual products on a page
product_head = '/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div['
product_tail = ']/div/a'

driver.get(base_url) # Opens Handbags (Most Popular):Page 1
# Cancels the first popup
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/img').click()
# Cancels the second popup
driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div/a/img').click()

# CAPTURING THE URLs OF PAGE OF EACH PRODUCT

while flag == 1:

    count_page = 0 # As it will be used in setting XPath of product URL

    while (count_page<40 and count_total<search_limit):

        # Example of XPath to URLs of individual pages of 40 products on a single page
        # First example is the XPath of first product on the page
        #
        # /html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/a
        # /html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/a
        # /html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/a
        # /html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div[40]/div/a
        
        product_xpath = product_head + str(count_page+1) + product_tail
        product_url = driver.find_element_by_xpath(product_xpath).get_attribute('href')

        pages_urls.append(product_url) # Adding the product URL to "pages_urls"

        count_page += 1
        count_total += 1

    if count_total == search_limit:
        flag = 0

    # URLs of all 40 products of present page have been captured
    # Now moving to next page of product catalog

    # Example of XPath to URLs of pagination links of product catalog page
    # First example is the XPath of page 1
    #
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[2]
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[3]
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[4]
    
    pagination_xpath = pagination_head + str(page_num+1) + pagination_tail
    # Moving to next page by clicking on the button corresponding to next page number
    pagination_url = driver.find_element_by_xpath(pagination_xpath).click() 

    page_num += 1

    time.sleep(2)
    
# CAPTURING ALL INFORMATION FROM INDIVIDUAL PRODUCT PAGE 

for page in pages_urls:
    
    driver.get(page)
    
    brand_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div/ul/li[3]/a').text
    brand.append(brand_item)

    model_item = driver.find_element_by_class_name('product-title').text[len(brand_item)+1:]
    model.append(model_item)

    retail_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/ul/li[1]/span/span/p[2]').text
    retail_item = retail_item.replace('$','').replace(',','')
    sale_price.append(retail_item)

    ask_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/a/div[1]/div').text
    ask_item = ask_item.replace('$','').replace(',','')
    ask_lowest.append(ask_item)

    bid_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div/div[3]/div[1]/a/div[1]/div').text
    bid_item = bid_item.replace('$','').replace(',','')
    bid_highest.append(bid_item)

    sales_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[1]/div[3]').text
    sales_item = sales_item.replace(',','')
    total_sales.append(sales_item)

    premium_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[2]/div[3]').text
    price_premium.append(premium_item)

    avg_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[3]/div[3]').text
    avg_item = avg_item.replace('$','').replace(',','')
    avg_price.append(avg_item)

    if brand_item.title() in brand_product_count.keys():
        brand_product_count[brand_item.title()] += 1
        brand_product_total[brand_item.title()] += float(avg_item)
    else:
        brand_product_count[brand_item.title()] = 1
        brand_product_total[brand_item.title()] = float(avg_item)

driver.close()