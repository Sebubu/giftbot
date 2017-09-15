#!/usr/bin/env python3

from siroopapi import search

def getproductlist(hashlist):
    productlist = []
    for hash in hashlist:
        products = search(hash, 1)
        for product in products:
            productlist.append(product)
    return productlist


##################
# Testcode

hashlist = ['lippenstift', 'beauty', 'foodporn'];
productlist = getproductlist(hashlist)
print(productlist)