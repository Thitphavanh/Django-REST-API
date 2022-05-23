from django.shortcuts import render
from django.http import JsonResponse

data = [{'message': 'hello world'}, {'message': 'hello world'}]


def Home(request):
    return JsonResponse(data=data, safe=False, json_dumps_params={'ensure_ascii': False})
