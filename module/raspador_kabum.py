import requests
from bs4 import BeautifulSoup

mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

def price_product(urlProduct):
    scrape_url = urlProduct
    sb_get = requests.get(scrape_url, headers=mozhdr)
    soupeddataPrincipal = BeautifulSoup(sb_get.content, "html.parser")

    price = soupeddataPrincipal.find_all('h4', itemprop="price")
    name_product = soupeddataPrincipal.find_all('h1', itemprop="name")

    
    name = str(name_product[0]).split('itemprop="name">')
    name = name[1].replace('</h1>','')

    if len(price) == 0 or price == None:	
        price = 'Fora de estoque'
    else:
        price = str(price[0]).split('itemprop="price">')
        price = price[1].replace('</h4>','')

    product = [name, ':point_right:  ' + price, urlProduct]

    return product

