from shopybot.settings import HUEY
from instarecom.personality.personalityapi import PersonalityApi
from .models import RecommendRequest
import json
import random

from watson_developer_cloud import LanguageTranslatorV2
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features


def nlp_captions(captions):
    nlp = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        url='https://gateway.watsonplatform.net/natural-language-understanding/api',
        username='7972a32c-8fb3-45be-b9ce-2a4364d13914',
        password='hFUSreGR5MXf'
    )

    nlp_result = nlp.analyze(text = captions, features=[features.Categories()])
    cat_return_list = []
    for entry in nlp_result['categories']:
        category = entry['label']
        categories = category.split('/')
        for category_item in categories:
            if not category_item == '':
                cat_return_list.append(category_item)

    return cat_return_list


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

    blacklist = ['insta', 'bestof', 'oftheday', 'igdaily', '_', 'pic']
    hashtag_dict = {}

    for hashtag in hashtags:
        for blacklist_item in blacklist:
            if blacklist_item not in hashtag:
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

    hashtag_arr_len = len(hashtag_list)

    return hashtag_list[0:int(0.75*hashtag_arr_len)]


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

    caption_list = nlp_captions(caption)
    caption_list = translate_hashtags(caption_list)

    for caption in caption_list:
        hashtags.append(caption)

    print("size of hashtags: ", len(hashtags))

    random.shuffle(hashtags)

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
