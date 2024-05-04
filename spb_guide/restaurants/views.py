from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Страница приложения restaurants')


def categories(request, category_id):
    return HttpResponse(f'<h1>Рестораны по категориям</h1><p>{category_id}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home')

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')