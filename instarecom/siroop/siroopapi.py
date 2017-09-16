import urllib.request
import json
import ssl


def search(hashtag, limit):
    url = 'https://api.siroop.ch/product/search/?query=' + hashtag + '&limit=' + str(limit) + '&apikey=8ccd66bb1265472cbf8bed4458af4b07'
    req = urllib.request.Request(url)
    myssl = ssl.create_default_context();
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    data = urllib.request.urlopen(req,context=myssl).read()
    products = json.loads(data.decode('utf-8'))
    return products


def getproductlist(hashlist):
    productlist = []
    for hash in hashlist[:4]:
        products = search(hash, 1)
        for product in products:
            productlist.append(product)
    return productlist



