from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

base_url = 'https://stockx.com/handbags/most-popular'

search_limit = 100 # Tells the number of products to limit our search

count_total = 0 # Stores the total count of products accounted for
count_page = 0 # Stores the count of products accounted in a single page
page_num = 1 # Stores the current page number of catalog

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

# For XPath of links used for moving to next page
pagination_head = '/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a['
pagination_tail = ']'

# For XPath of links used to select individual products on a page
product_head = '/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div/div['
product_tail = ']/div/a'

options = Options()
options.headless = True

# driver = webdriver.Firefox() # Opens a new Firefox window in headfull mode
driver = webdriver.Firefox(options = options) # Opens a new Firefox windows in headless mode

driver.maximize_window() # Maximizes the Firefox window

driver.get(base_url) # Opens Handbags (Most Popular):Page 1

# Cancels the first popup
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section/div/img').click()

# Cancels the second popup
# driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div/a/img').click()
driver.find_element_by_class_name('close-btn').click()

# CAPTURING THE URLs OF PAGE OF EACH PRODUCT

while True:

    # Now moving to next page of product catalog

    # Example of XPath to URLs of pagination links of product catalog page
    # First example is the XPath of page 1
    #
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[2]
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[3]
    #/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/ul/a[4]
    
    pagination_xpath = pagination_head + str(page_num+1) + pagination_tail
    # Moving to next page by clicking on the button corresponding to next page number
    #pagination_url = driver.find_element_by_xpath(pagination_xpath).click()

    pagination_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pagination_xpath)))
    pagination_button.click()
    
    # Prevents any action for 1 second, meanwhile allowing the page to load
    # time.sleep(1)

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

        print('Link of product ', count_total, ' extracted from page ', page_num)

    # Provides exit condition for the while loop, if the desired number of products are scannned
    if count_total == search_limit:
        break

    # URLs of all 40 products of present page have been captured
    page_num += 1


print('*'*50)
print('All links leading to individual pages are captured')
print('*'*50)

# CAPTURING ALL INFORMATION FROM INDIVIDUAL PRODUCT PAGE 

loop_counter = 0

for page in pages_urls:
    
    # Opening page corresponding to an individual product
    driver.get(page)
    
    # Extracting brand name of the product
    brand_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div/ul/li[3]/a').text
    brand.append(brand_item)

    # Extracting model name of the product
    model_item = driver.find_element_by_class_name('product-title').text[len(brand_item)+1:]
    model.append(model_item)

    # Extracting last sale price of the product
    retail_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/ul/li[1]/span/span/p[2]').text
    retail_item = retail_item.replace('$','').replace(',','')
    sale_price.append(retail_item)

    # Extracting the lowest ask value of the product
    ask_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/a/div[1]/div').text
    ask_item = ask_item.replace('$','').replace(',','')
    
    if ask_item == '--':
        ask_lowest.append(0)
    else:
        ask_lowest.append(ask_item)

    # Extracting the highest bid value of the product

    if ask_item == '--':
        bid_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/a/div[1]/div').text
    else: # If "Lowest Ask" is not null, then XPath of "Highest Bid" changes
        bid_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/div/div[3]/div[1]/a/div[1]/div').text
    bid_item = bid_item.replace('$','').replace(',','')
    
    if bid_item == '--':
        bid_highest.append(0)
    else:
        bid_highest.append(bid_item)

    # Extracting the number of sales of the product in last 12 months
    sales_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[1]/div[3]').text
    sales_item = sales_item.replace(',','')
    
    if sales_item == '--':
        total_sales.append(0)
    else:
        total_sales.append(sales_item)

    # Extracting the product's premium price above retail price
    premium_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[2]/div[3]').text
    
    if premium_item == '--':
        price_premium.append(0)
    else:
        price_premium.append(premium_item)

    # Extracting the average price of the product in the last 12 months
    avg_item = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[11]/div/div/div/div[3]/div[2]/div[3]/div[3]').text
    avg_item = avg_item.replace('$','').replace(',','')
    
    if avg_item == '--':
        avg_price.append(0)
    else:
        avg_price.append(avg_item)

    # If a brand is already present in the dictionary, then updating its values 
    if brand_item.title() in brand_product_count.keys():
        brand_product_count[brand_item.title()] += 1
        brand_product_total[brand_item.title()] += float(avg_item)
    
    # If a brand is not present in the dictionary, then adding it
    else:
        brand_product_count[brand_item.title()] = 1
        brand_product_total[brand_item.title()] = float(avg_item)

    loop_counter += 1
    print('Details of product ', loop_counter, ' are captured')

print('*'*50)
print('Details from all the individual pages are captured')
print('*'*50)
print()

# Closing the geckodriver
driver.close()

# Storing all retrieved data in a dictionary, which will be used to create a dataframe
all_data = {'Brand Name': brand,
            'Model Name': model,
            'Last Sales Price (in $)': sale_price,
            'Lowest Ask (in $)': ask_lowest,
            'Highest Bid (in $)': bid_highest,
            'Total Sales (in last 12 months)': total_sales,
            'Price Premium above Retail Price': price_premium,
            'Average Price (in $)': avg_price
            }

# Dictionary to store the average price of products of each brand
brand_product_details = {}

for i in brand_product_count.keys():
    brand_product_details[i] = [brand_product_count[i], 
                                brand_product_total[i],
                                round(brand_product_total[i]/brand_product_count[i],2)]

# Creates a dataframe for data of all products individually
individual_product_data = pd.DataFrame(all_data)

# Creates a dataframe for data of products (brand-wise) 
brand_wise_product_data = pd.DataFrame(brand_product_details, 
                                        index=['Number of Products',
                                                'Total Amount of all Products', 
                                                'Average Price of each Product'])

# Stores all data in a CSV file
individual_product_data.to_csv('Stockx Handbags (Most Popular).csv')
brand_wise_product_data.to_csv('Stockx Handbags (Most Popular) - Brand-wise.csv')