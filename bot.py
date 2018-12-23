import requests
import json
import browserOps

# @param model specific model for purchase
# @param size spefific size for purchase
# NOTE: Currently only NMD_R1 Style
def url_gen(model,size):
    base_size = 560
    # this base size is for size 5.5 shoes
    shoe_size = size - 5.5
    shoe_size = shoe_size * 20
    raw_size = shoe_size + base_size
    shoe_size_code = int(raw_size)
    url = 'https://www.adidas.com/us/nmd_r1/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoe_size_code)
    return url

# @param model specific adidas model for purchase
# @return size_lookup dictionary of sizes/availability for model
def check_stock(model):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    size_url = 'https://www.adidas.com/api/products/{}/availability?sitePath=us'.format(str(model))
    raw_sizes = (requests.get(size_url,headers=headers)).text
    size_data = json.loads(raw_sizes)
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
    model = raw_input('Model #: ')
    sneaker_bot(model,size)

# Sets up bot environment to automate purchase sneaker if available.
# @param model specific model for purchase
# @param size specific size for purchase
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
