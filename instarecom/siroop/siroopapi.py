import urllib.request
import json
import ssl


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
        print(ex)
        return []
    products = json.loads(data.decode('utf-8'))
    return products


def getproductlist(hashlist, amount_products=60):
    hashlist = list(set(hashlist))
    productlist = []
    products_per_hashtag = amount_products/len(hashlist[:10])
    for hash in hashlist:
        products = search(hash, products_per_hashtag)
        for product in products:
            productlist.append(product)
    return productlist



