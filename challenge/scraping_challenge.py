#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as Soup
import pandas as pd
import datetime as dt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def scrape_all():
    # Set the executable path and initialize the chrome browser in splinter
    # Initiate headless driver for deployment
    browser = Browser('chrome', executable_path="chromedriver",headless=True)
    # headless=False is to see the scraping in action 
    # Put scraping codes into a function to be reused (scraping done behind the scenes)
    
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "titles_url": mars_hem_image(browser)
    } # This dictionary runs all of the functions we created & store all of the results
    browser.quit()
    return data

    
def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # ^ Searching elements with a combination of tag (ul & li) & attribute item_list & slide

    # Set HTML parser
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = Soup(html, 'html.parser')

    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None
        
    return news_title, news_p
# mars_news(browser) --> telling Python that we'll be using browser variable we defined outside the function
# Add try/except for error handling for Attribute errors --> potential error during web scraping 
#   (e.g., common one= webpage's format changed & scraping code) no longer matches the new HTML elements 
#   -if there's an error, Python will continue to run the remainder of the code but it will return nothing instead of title/paragraph

### Features Images
def featured_image(browser):
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

    # Add try/except for error handling
    try:
        # Find the relative image url (the most recently updated image)
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = "https://www.jpl.nasa.gov{}".format(img_url_rel)
    
    return img_url

## Mars Hemispheres
def mars_hem_image(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    hem_list=[]
    for i in range(4):
        hemi={}
        browser.find_by_css('h3')[i].click()
        browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
        browser.is_element_present_by_text('Sample', wait_time=1)
        Sample_elem = browser.links.find_by_partial_text('Sample')
        Sample_elem.click()
        soup= Soup(browser.html, 'html.parser')
        src=soup.select_one('img').get("src")
        hemi['img_url']= f'https://astrogeology.usgs.gov/{src}'
        hemi['title']=soup.find('h2', class_='title').get_text()
        if hemi not in hem_list:
            hem_list.append(hemi)
        browser.back()
    return hem_list
### Facts Scraping

def mars_facts():
    # Add try/except for error handling
    try:
        # Import pandas dependency on top
        # scrape the entire table using Pandas' .read_html() function
        df = pd.read_html('http://space-facts.com/mars/')[0]
        print(df)
    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# The last block of code tells Flask that our script is complete & ready for action 
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

