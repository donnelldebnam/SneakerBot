import requests
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
    print str(URL)
    return URL

def CheckStock(url,model):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    raw_html =  requests.get(url,headers=headers)
    page = bs4.BeautifulSoup(raw_html.text, "lxml")
    list_raw_sizes = page.select('.size-dropdown-block')
    sizes = str(list_raw_sizes[0].getText()).replace('\t','')
    sizes = sizes.replace('\n\n',' ')
    sizes = sizes.split()
    sizes.remove('Select')
    sizes.remove('size')
    for size in sizes:
        print(str(model) + 'Sizes: ' + str(size) + ' Available')

def Main(model, size):
    url = URLGen(model,size)
    CheckStock(url, model)
