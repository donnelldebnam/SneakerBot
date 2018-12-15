from selenium import webdriver

def add_to_bag(url):

    driver = webdriver.Firefox()
    driver.get(url)
    btn = driver.find_element_by_css_selector('.gl-cta.gl-cta--primary.gl-cta--full-width.btn-bag')
    btn.click()
    
