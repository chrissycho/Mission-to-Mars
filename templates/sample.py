def cerberus_images(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_css('h3'[class_="product-item"])
    full_image_elem.click()

    # Find the more info button and click that
    # Find 'more info' text by Boolean (wait time is 1 second)
    browser.is_element_present_by_text('Open', wait_time=1)
    # find the link associated with 'more info'text 
    open_elem = browser.links.find_by_partial_text('Open')
    # Tell splinter to click 
    open_elem.click()

    # With the new page loaded, it needs to be parsed so we can continue scrape the full-size image URL
    # Parse the resulting html with soup
    html = browser.html
    img_soup = Soup(html, 'html.parser')
    title_elem=img_soup.find("h2", class_="title").get_text()
    title_elem

    # Add try/except for error handling
    try:
        # Find the relative image url (the most recently updated image)
        img_url_rel = img_soup.find_all('img')[4]["src"]
    except AttributeError:
        return None
    
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    
    return img_url


    # Write one function and have for loop to grab all the URLs, title, & images