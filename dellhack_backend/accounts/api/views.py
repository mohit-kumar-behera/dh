from django.shortcuts import render
from django.http import HttpResponse


def login_api_handler(request):
    return HttpResponse('hj')


def register_api_handler(request):
    return HttpResponse('u')