import urllib.request
import json
import ssl
from random import shuffle


def search(hashtag, limit):
    url = 'https://api.siroop.ch/product/search/?query=' + hashtag + '&limit=' + str(
        int(limit)) + '&apikey=8ccd66bb1265472cbf8bed4458af4b07'
    req = urllib.request.Request(url)
    myssl = ssl.create_default_context()
    myssl.check_hostname = False
    myssl.verify_mode = ssl.CERT_NONE
    try:
        data = urllib.request.urlopen(req, context=myssl).read()
    except Exception as ex:
        try:
            data = urllib.request.urlopen(req, context=myssl).read()
        except Exception as ex:
            print('error hash', hashtag)
            return []
    products = json.loads(data.decode('utf-8'))
    print(hashtag, len(products))

    return products


def getproductlist(hashlist, captionlist, amount_products=60):
    hashlist = list(set(hashlist))
    hashlist = hashlist[:100]
    print(len(hashlist), 'hashes found')
    productlist = []

    products_per_hashtag = 1000
    for caption in captionlist:
        products = search(caption, products_per_hashtag)

        if isinstance(products, list) and len(products) > 0:
            best_products = get_best_for_hashtag(caption, hashlist, products)
            for best_product in best_products:
                productlist.append(best_product)

    print(len(productlist), 'found')

    productlist = remove_duplicates(productlist)
    print(len(productlist), 'after duplicate removing')
    shuffle(productlist)
    return productlist


def get_best_for_hashtag(hashtag, all_hashtags, productlist):
    productlist = list(productlist)
    filtered_products = []

    for product in productlist:
        if hashtag.lower() in product['description'].lower():
            filtered_products.append(product)

    rating = []
    for product in filtered_products:
        count = 0
        for hash in all_hashtags:
            if hash.lower() in product['description'].lower():
                count += 1
        rating.append((count, product))

    sorted_rating_list = sorted(rating, key=lambda x: x[0])

    best_products = []
    for (count, product) in sorted_rating_list:
        if count > 0:
            best_products.append(product)

    if len(best_products) > 3:
        return best_products[0:3]
    return best_products


def remove_duplicates(productlist: []):
    products = {}
    for product in productlist:
        if product:
            id = product['id']
            products[id] = product

    return list(products.values())
