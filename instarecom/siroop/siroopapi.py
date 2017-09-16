import urllib.request
import json
import ssl
from random import shuffle


def search(hashtag, limit):
    url = 'https://api.siroop.ch/product/search/?query=' + hashtag + '&limit=' + str(int(limit)) + '&apikey=8ccd66bb1265472cbf8bed4458af4b07'
    req = urllib.request.Request(url)
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    try:
        data = urllib.request.urlopen(req,context=myssl).read()
    except Exception as ex:
        try:
            data = urllib.request.urlopen(req, context=myssl).read()
        except Exception as ex:
            print('error hash', hashtag)
            return []
    products = json.loads(data.decode('utf-8'))
    print(hashtag, len(products))
    return products


def getproductlist(hashlist, amount_products=60):
    hashlist = list(set(hashlist))
    hashlist = hashlist[:100]
    print(len(hashlist), 'hashes found')
    productlist = []

    products_per_hashtag = 50
    for hash in hashlist:
        products = search(hash, products_per_hashtag)
        if len(products) == 0:
            continue
        best_product = get_best_for_hashtag(hash, hashlist,products)
        productlist.append(best_product)
    print(len(productlist), 'found')
    productlist = remove_duplicates(productlist)
    print(len(productlist), 'after duplicate removing')
    shuffle(productlist)
    return productlist


def get_best_for_hashtag(hashtag, all_hashtags, productlist):
    print(len(productlist))
    productlist = list(productlist)
    filtered_products = []

    for product in productlist:
        if hashtag.lower() in product['description'].lower():
            filtered_products.append(product)
    if len(filtered_products) == 0:
        return productlist[0]

    rating = []
    for product in filtered_products:
        count = 0
        for hash in all_hashtags:
            if hash.lower() in product['description'].lower():
                count += 1
        rating.append((count, product))

    max_count, best_product = 0, None
    for (count, product) in rating:
        if count > max_count:
            max_count = count
            best_product = product
    return best_product


def remove_duplicates(productlist: []):
    products = {}
    for product in productlist:
        products[product['id']] = product
    return list(products.values())




