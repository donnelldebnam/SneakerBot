from selenium import webdriver
import time

def checkout(url):
    # Boot up webdriver; process adidas url
    driver = webdriver.Firefox()
    driver.get(url)
    # Get initial amount of items in bag
    items_in_bag = driver.find_element_by_css_selector('.glass_cart_count___1UWuC').text
    # If bag is empty, assign valid int value
    if items_in_bag == '':
        items_in_bag = 0
    # Cast temp, initialize constant
    items_in_bag = int(items_in_bag)
    UPDATED = items_in_bag + 1
    # Grab CSS to "Add to Bag" button; click
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag')
    btn.click()
    # While bag has not updated, wait...
    while items_in_bag != UPDATED:
        time.sleep(1)
        items_in_bag = driver.find_element_by_css_selector('.glass_cart_count___1UWuC').text
        if items_in_bag == '':
            items_in_bag = 0
        items_in_bag = int(items_in_bag)
    # Navigate to Checkout page
    driver.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show')
    # FWD to CardInfo page
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width')
    btn.click()
