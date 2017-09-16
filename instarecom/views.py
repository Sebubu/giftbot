from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from instarecom import task

import imageio

imageio.plugins.ffmpeg.download()


def get_product_list(username, password, target_user):
    from instarecom.instagram.hashscrapper import InstaApi
    from instarecom.siroop.siroopapi import getproductlist
    api = InstaApi()
    api.login(username, password)
    hashtags = api.get_hashtags(target_user)
    products = getproductlist(hashtags)
    return products


def get_personality(username, password, target_user):
    from instarecom.personality import personalityapi

    personality = personalityapi.PersonalityApi()
    return personality.get_personality()


@csrf_exempt
def recommendations(request):
    task.test()
    print('pushed huey task into redis')
    if request.method == 'POST':
        anfrage = request.body.decode('unicode_escape')
        anfrage = json.loads(anfrage)
        username = anfrage['userName']
        password = anfrage['password']
        target = anfrage['targetUser']
        print('userName', username)
        print('password', password)
        print('targetUser', target)
    else:
        username = 'severinbuhler'
        password = 'HackZurich2017'
        target = 'jenlikescats'
    products = get_product_list(username, password, target)
    return JsonResponse(products, safe=False)


@csrf_exempt
def personality(request):
    if request.method == 'POST':
        anfrage = request.body.decode('unicode_escape')
        anfrage = json.loads(anfrage)
        username = anfrage['userName']
        password = anfrage['password']
        target = anfrage['targetUser']
        print('userName', username)
        print('password', password)
        print('targetUser', target)

    else:
        username = 'severinbuhler'
        password = 'HackZurich2017'
        target = 'jenlikescats'

    personality = get_personality(username, password, target)
    return JsonResponse(personality, safe=False)
