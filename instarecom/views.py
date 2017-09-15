from django.http import JsonResponse

# Create your views here.
def recommendations(request):
    response = {
        'blaa': 'asdfasdf'
    }
    return JsonResponse(response)