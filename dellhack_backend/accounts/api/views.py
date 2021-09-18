from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_api_handler(request):
    if request.POST:
        print(request.POST)
    return HttpResponse(False)


@csrf_exempt
def register_api_handler(request):
    if request.POST:
        print(request.POST)
    return HttpResponse(True)