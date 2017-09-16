import urllib.request
import json
import ssl
from random import shuffle


def search(hashtag, limit):
    url = 'https://api.siroop.ch/product/search/?query=' + hashtag + '&limit=' + str(int(limit)) + '&apikey=8ccd66bb1265472cbf8bed4458af4b07'
    print(url)
    req = urllib.request.Request(url)
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    try:
        data = urllib.request.urlopen(req,context=myssl).read()
    except Exception as ex:
        print('error hash', hashtag)

        return []
    products = json.loads(data.decode('utf-8'))
    return products


def getproductlist(hashlist, amount_products=60):
    hashlist = list(set(hashlist))
    hashlist = hashlist[:20]
    productlist = []
    products_per_hashtag = amount_products/len(hashlist)
    for hash in hashlist:
        products = search(hash, products_per_hashtag)
        for product in products:
            productlist.append(product)
    productlist = remove_duplicates(productlist)
    shuffle(productlist)
    print('Productlist: ', productlist)
    return productlist


def remove_duplicates(productlist: []):
    products = {}
    for product in productlist:
        products[product['id']] = product
    return list(products.values())




