#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as Soup
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
# ^ Searching elements with a combination of tag (ul & li) & attribute item_list & slide

# Set HTML parser
html = browser.html
news_soup = Soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

### Article Scraping
# Find the most recent article
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


### Features Images
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
# Find 'more info' text by Boolean (wait time is 1 second)
browser.is_element_present_by_text('more info', wait_time=1)
# find the link associated with 'more info'text 
more_info_elem = browser.links.find_by_partial_text('more info')
# Tell splinter to click 
more_info_elem.click()

# With the new page loaded, it needs to be parsed so we can continue scrape the full-size image URL
# Parse the resulting html with soup
html = browser.html
img_soup = Soup(html, 'html.parser')

# Find the relative image url (the most recently updated image)
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


### Facts Scraping
# Import pandas dependency on top
# scrape the entire table using Pandas' .read_html() function
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
df.to_html()
browser.quit()



