from selenium import webdriver
import time

driver = webdriver.Firefox()

def process_cart(url):
    # Boot up webdriver; process adidas url
    driver.get(url)
    # Get initial amount of items in bag
    items_in_bag = driver.find_element_by_css_selector('.glass_cart_count___1UWuC').text
    # If bag is empty, assign valid int value
    if items_in_bag == '':
        items_in_bag = 0
    # Cast temp, initialize constant
    items_in_bag = int(items_in_bag)
    UPDATED = items_in_bag + 1
    # Grab CSS to "Add to Bag" button
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag')
    # While bag has not updated, add to bag
    while items_in_bag != UPDATED:
        btn.click()
        items_in_bag = driver.find_element_by_css_selector('.glass_cart_count___1UWuC').text
        if items_in_bag == '':
            items_in_bag = 0
        items_in_bag = int(items_in_bag)
    # Allocate time to process item bagging (avoid unexpected error pg.)
    time.sleep(2)
    # Navigate to Checkout page
    driver.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show')
    # FWD to CardInfo page
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width')
    btn.click()

def autofill_shipping():
    # Read client info from file
    with open('ClientInfo.txt','r') as file:
        my_first = file.readline()
        my_last = file.readline()
        my_street = file.readline()
        my_city = file.readline()
        my_zip = file.readline()
        my_phone = file.readline()
        my_email = file.readline()

    # Navigate to Shipping page
    driver.get('https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/COShipping-Show')
    # Autofill first name
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_firstName')
    input.send_keys(my_first)
    # Autofill last name
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_lastName')
    input.send_keys(my_last)
    # Autofill street
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_address1')
    input.send_keys(my_street)
    # autofill city
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_city')
    input.send_keys(my_city)
    # Select Maryland as state
    driver.find_element_by_xpath(
        '//*[@id="shippingForm"]/div[1]/ng-form/div[1]/div/div[6]/div[1]/div[1]'
        ).click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[1]/ng-form/div[1]/div/div[6]/div[1]/div[2]/div[25]'
        ).click()
    # autofill zip
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_postalCode')
    input.send_keys(my_zip)
    # autofill phone
    input = driver.find_element_by_id('dwfrm_shipping_shiptoaddress_shippingAddress_phone')
    input.send_keys(my_phone)
    # autofill email
    input = driver.find_element_by_id('dwfrm_shipping_email_emailAddress')
    input.send_keys(my_email)
    # Send to Payment Screen
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div/div/div/div/div[2]/form/div[1]/ng-form/div[5]/div/button'
        ).click()
