from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def recommendations(request):
    response = {
        'blaa': 'asdfasdf'
    }
    return JsonResponse(response)