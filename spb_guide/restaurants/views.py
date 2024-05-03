from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения restaurants')


def categories(request):
    return HttpResponse('Статьи по категориям')
