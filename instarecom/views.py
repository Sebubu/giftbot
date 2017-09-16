from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from instarecom import task
from .models import RecommendRequest
import os


bs = os.getenv('my_os', 'linux')

if bs == 'linux':
    import imageio
    imageio.plugins.ffmpeg.download()


def get_personality(username, password, target_user):
    from instarecom.personality import personalityapi

    personality = personalityapi.PersonalityApi()
    return personality.get_personality()


@csrf_exempt
def create_recommend(request):
    if not (request.method == 'POST' or request.method == 'GET'):
        return JsonResponse({}, safe=False)
    if request.method == 'POST':
        anfrage = request.body.decode('unicode_escape')
        anfrage = json.loads(anfrage)
        username = anfrage['userName']
        password = anfrage['password']
        target = anfrage['targetUser']
        print('userName', username)
        print('password', password)
        print('targetUser', target)
    if request.method == 'GET':
        username = 'marcel.amsler'
        password = 'stupidfucker'
        target = 'chucknorris'

    req = RecommendRequest.objects.create(username=username, password=password, targetUser=target)
    req.save()
    response = {
        'ticket': req.id
    }
    task.fetch_products(req.id)
    return JsonResponse(response, safe=False)


@csrf_exempt
def get_recommend(request):
    if 'id' not in request.GET:
        req = RecommendRequest.objects.last()
    else:
        req = RecommendRequest.objects.get(id=request.GET['id'])
    if not req.is_finished:
        return JsonResponse({'status': 'not_finished_yet'}, safe=False)
    product_list = json.loads(req.productList)
    personality = json.loads(req.personality)
    content = {
        'status': 'finished',
        'result': product_list,
        'personality_result': personality
    }
    return JsonResponse(content, safe=False)



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
        target = 'chucknorris'

    personality = get_personality(username, password, target)
    return JsonResponse(personality, safe=False)

