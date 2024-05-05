from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Restaurants

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Restaurants.objects.all()
    return render(request, 'restaurants/index.html', {'posts': posts,'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'restaurants/about.html', {'title': 'О сайте'})


def categories(request, category_id):
    return HttpResponse(f'<h1>Рестораны по категориям</h1><p>{category_id}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home')

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
