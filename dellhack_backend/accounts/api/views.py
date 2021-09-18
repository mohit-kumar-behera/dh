from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_api_handler(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
    return HttpResponse(False)


@csrf_exempt
def register_api_handler(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
    return HttpResponse(True)