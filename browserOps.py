from selenium import webdriver

def add_to_bag(url):
    # Boot up webdriver; process adidas url
    driver = webdriver.Firefox()
    driver.get(url)
    # Grab CSS to "Add to Bag" button
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag')
    # Click button
    btn.click()
