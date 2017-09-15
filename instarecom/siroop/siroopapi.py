#!/usr/bin/env python3
import urllib.request
import json

def search(hashtag, limit):
    url = 'https://api.siroop.ch/product/search/?query=' + hashtag + '&limit=' + str(limit) + '&apikey=8ccd66bb1265472cbf8bed4458af4b07'
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    products = json.loads(data.decode('utf-8'))
    return products
