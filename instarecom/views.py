from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def recommendations(request):
    print(request)
    body = request.body.decode('utf-8')
    request = json.loads(body, ensure_ascii=False)
    response = {
        'blaa': 'asdfasdf'
    }
    return JsonResponse(response)