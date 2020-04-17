# Selenium

Selenium is an open-source web testing tool. It is used to automate browser activities, hence it is also known as a web-driver. It is particularly useful for scraping, if the website uses JavaScript to serve content.

## Installation

To install Selenium on your system, execute the following command on your Terminal (if on Linux or macOS) or Command Prompt (if on Windows).
> `pip install selenium`
------------------
To download driver for Firefox (**geckodriver**), execute the following commands. Check the latest version of geckodriver on their [Releases page](https://github.com/mozilla/geckodriver/releases), and download it. The latest version at the time of writing this was v0.26.0.
> `wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz`

Extract the file using
> `tar -xvzf geckodriver*`

Make the extracted file executable using
> `sudo chmod +x geckodriver`

Now move the geckodriver to **/usr/local/bin/** using
> `sudo mv geckodriver /usr/local/bin/`
------------------
To do the same for Chrome,  download the latest version of **chromedriver** from [ChromeDriver Downloads page](https://sites.google.com/a/chromium.org/chromedriver/downloads), and execute the following commands. The latest version at the time of writing this was 83.0.4103.14.
> `wget https://chromedriver.storage.googleapis.com/83.0.4103.14/chromedriver_linux64.zip`

Extract the file using
> `unzip chromedriver_linux64.zip`

Make the extracted file executable using
> `sudo chmod +x chromedrive`

Now move the chromedriver to **/usr/local/bin/** using
> `sudo mv chromedriver /usr/local/bin/`


## Resources

1. [Selenium: Official Documentation](https://www.selenium.dev/selenium/docs/api/py/index.html)
1. [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
1. [Selenium Webdriver Python Tutorial for Web Automation](https://www.techbeamers.com/selenium-webdriver-python-tutorial/)
1. [Web Scraping with Selenium and Python](https://www.scrapingbee.com/blog/selenium-python/)