from shopybot.settings import HUEY
from instarecom.personality.personalityapi import PersonalityApi
from .models import RecommendRequest
import json




def get_product_list(username, password, target_user):
    from instarecom.instagram.hashscrapper import InstaApi
    from instarecom.siroop.siroopapi import getproductlist
    api = InstaApi()
    api.login(username, password)
    hashtags, captions = api.get_hashtags(target_user)
    products = getproductlist(hashtags)
    return products, captions


def getPersonality(captions):
    api = PersonalityApi()
    return api.get_personality(captions)

@HUEY.task()
def fetch_products(request_id):
    req = RecommendRequest.objects.get(id=int(request_id))
    print('fetch for', req.targetUser)
    liste, captions = get_product_list(req.username, req.password, req.targetUser)
    print(len(liste), 'products found')
    req.productList = json.dumps(liste)
    print(req.productList)

    req.personality = getPersonality(captions)
    print(req.personality)

    req.save()