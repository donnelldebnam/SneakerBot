import requests
import json
import bs4
import random
import webbrowser

def URLGen(model,size):
    base_size = 560
    # this base size is for size 5.5 shoes
    shoe_size = size - 5.5
    shoe_size = shoe_size * 20
    raw_size = shoe_size + base_size
    shoe_size_code = int(raw_size)
    URL = 'https://www.adidas.com/us/nmd_r1/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoe_size_code)
    return URL

def CheckStock(url,model):
    # url: 'https://www.adidas.com/us/nmd_r1-shoes/BD7730.html?forceSelSize=BD7730_620'
    # size url: 'https://www.adidas.com/api/products/BD7730/availability?sitePath=us'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    size_url = 'https://www.adidas.com/api/products/' + str(model) + '/availability?sitePath=us'
    raw_sizes =  requests.get(size_url,headers=headers)
    raw_sizes = raw_sizes.text
    size_data = json.loads(raw_sizes)
    for var in size_data['variation_list']:
        print var

def Main(model, size):
    url = URLGen(model,size)
    CheckStock(url, model)
