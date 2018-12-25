import requests
import json
import time
import browserOps
from fake_useragent import UserAgent

# @param size spefific size for purchase
def url_gen(size):
    base_size = 560
    # this base size is for size 5.5 shoes
    shoe_size = size - 5.5
    shoe_size = shoe_size * 20
    raw_size = shoe_size + base_size
    shoe_size_code = int(raw_size)
    url = 'https://www.adidas.com/us/yeezy-boost-350-v2-static-non-reflective/EF2905.html?forceSelSize=_' + str(shoe_size_code)
    return url

# @param model specific adidas model for purchase
# @return size_lookup dictionary of sizes/availability
def check_stock():
    ua = UserAgent()
    headers = {'User-Agent':str(ua.msie)}
    size_url = 'https://www.adidas.com/api/products/EF2905/availability?sitePath=us'
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
    size = input('Shoe size: ')
    sneaker_bot(size)

# Sets up bot environment to automate purchase sneaker if available.
# @param size specific size for purchase
def sneaker_bot(size):
    sizes = check_stock()
    url = url_gen(size)
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
