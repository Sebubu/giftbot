from shopybot.settings import HUEY
from instarecom.personality.personalityapi import PersonalityApi
from .models import RecommendRequest
import json

from watson_developer_cloud import LanguageTranslatorV2


def translate_hashtags(hashtags):
    language_translator = LanguageTranslatorV2(
        url='https://gateway-fra.watsonplatform.net/language-translator/api',
        username='241712b3-9910-4b73-8441-682c3c911e04',
        password='kiwGx5ElNpzP'
    )

    german_tags = []
    for hashtag in hashtags:
        raw_german_str = json.dumps(language_translator.translate(hashtag, source='en', target='de'), indent=2, ensure_ascii=False)
        german_str = raw_german_str.replace('\"', '')
        german_tags.append(german_str)

    return german_tags


def clean_hashtag_list(hashtags):
    hashtag_dict = {}

    for hashtag in hashtags:
        if "insta" not in hashtag:
            if hashtag in hashtag_dict:
                hashtag_dict[hashtag] = hashtag_dict[hashtag] + 1
            else:
                hashtag_dict[hashtag] = 1

    sorted_hashtag_dict = sorted(hashtag_dict.items(), key=lambda x: x[1])
    sorted_hashtag_dict.reverse()
    print('Hashtag Dictionary: ', sorted_hashtag_dict)

    hashtag_list = []
    for hashtag_dict_item in sorted_hashtag_dict:
        hashtag_list.append(hashtag_dict_item[0])

    return hashtag_list


def improve_product_list(hashtags, productlist):
    filtered_list = []
    for hash in hashtags:
        best_product = get_best_for_hashtag(hash, hashtags, productlist)
        if best_product is not None:
            filtered_list.append(best_product)
    return filtered_list


def get_best_for_hashtag(hashtag, all_hashtags, productlist):
    print(len(productlist))
    productlist = list(productlist)
    filtered_products = []

    for product in productlist:
        if hashtag.lower() in product['description'].lower():
            filtered_products.append(product)
    if len(filtered_products) == 0:
        return None

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


def get_product_list(username, password, target_user):
    from instarecom.instagram.hashscrapper import InstaApi
    from instarecom.siroop.siroopapi import getproductlist
    api = InstaApi()
    api.login(username, password)
    user_info = api.user_infos(target_user)

    hashtags, caption = api.get_hashtags(target_user)
    hashtags = clean_hashtag_list(hashtags)

    hashtags = translate_hashtags(hashtags)

    products = getproductlist(hashtags)
    print('Found', len(products), 'products')

    #products = improve_product_list(hashtags, products)
    print('Filtered to', len(products), 'products')
    return products, caption, user_info


def getPersonality(captions):
    api = PersonalityApi()
    return api.get_personality(captions)


@HUEY.task()
def fetch_products(request_id):
    req = RecommendRequest.objects.get(id=int(request_id))
    print('fetch for', req.targetUser)
    liste, captions, user_info = get_product_list(req.username, req.password, req.targetUser)
    print(len(liste), 'products found')
    req.productList = json.dumps(liste)
    req.personality = getPersonality(captions)
    req.user_info = json.dumps(user_info)
    req.save()
