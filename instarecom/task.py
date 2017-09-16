from shopybot.settings import HUEY
from .models import RecommendRequest
import json




def get_product_list(username, password, target_user):
    from instarecom.instagram.hashscrapper import InstaApi
    from instarecom.siroop.siroopapi import getproductlist
    api = InstaApi()
    api.login(username, password)
    hashtags = api.get_hashtags(target_user)
    products = getproductlist(hashtags)
    return products


@HUEY.task()
def fetch_products(request_id):
    print('proccess', request_id)
    ids = RecommendRequest.objects.all().values_list('id', flat=True)
    print(list(ids))
    req = RecommendRequest.objects.get(id=int(request_id))
    print('fetch for', req.targetUser)
    liste = get_product_list(req.username, req.password, req.targetUser)
    print(len(liste), 'products found')
    req.productList = json.dumps(liste)
    print(req.productList)
    req.save()