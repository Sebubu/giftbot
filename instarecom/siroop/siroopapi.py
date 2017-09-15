#!/usr/bin/env python3
import urllib.request

def search(hashtag):
    the_page = ''
    req = urllib.request.Request('https://api.siroop.ch/product/search/?query=lippenstift&limit=5&apikey=8ccd66bb1265472cbf8bed4458af4b07')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    print(the_page)


search('lippenstift')