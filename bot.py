# - *- coding: utf- 8 - *-
import requests
import json
import browserOps
import threading
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor as Pool

proxies = {
    'http: '
    'https: '
}
sizes = [8.5, 9, 9.5, 10]
thread_count = 8

# :param size spefific size for purchase
def url_gen(model,size):
    url = 'https://www.adidas.com/us/yeezy/{}.html?forceSelSize='.format(model) + str(size)
    return url

# :param model specific model of sneaker
# :return size_lookup dictionary of sizes/availability
def check_stock(model):
    ua = UserAgent()
    headers = {'User-Agent':str(ua.msie)}
    size_url = 'https://www.adidas.com/api/products/{}/availability?sitePath=us'.format(model)
    raw_sizes = (requests.get(size_url,headers=headers)).text
    size_data = json.loads(raw_sizes)
    # while sneaker availability has not officially released,
    # wait until it releases...
    if size_data['availability_status'] == 'PREVIEW':
        print "Waiting for sizing to be updated..."
        check_stock()
    list = size_data['variation_list']
    size_dict = {}
    size_lookup = {}
    for i in range(21):
        size_dict[i] = {list[i]['size']:list[i]['availability_status']}
    for key,value in size_dict.items():
        size_lookup.update(value)
    return size_lookup

def main():
    model = raw_input('Model: ')
    size = input('Shoe size: ')
    sneaker_bot(model,size)

# Sets up bot environment to automate purchase sneaker if available.
# :param size specific size for purchase
def sneaker_bot(model,size):
    sizes = check_stock(model)
    url = url_gen(model,size)
    if str(size) in sizes:
        if str(sizes[str(size)]) == 'IN_STOCK':
            print "We're securing you a pair!"
            browserOps.process_cart(url)
            browserOps.autofill_shipping()
            browserOps.autofill_card()
        else:
            print "Size not available!"
    else:
        print "We were not able to save you a pair :("

# Allows for multitreading in order to purchase all sizes
# specified in size list
with Pool(thread_count) as executor:
    for size in sizes:
        executor.submit(sneaker_bot,size)﻿
