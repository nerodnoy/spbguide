from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *
from django.views.generic import ListView

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить заведение', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class RestaurantsHome(ListView):
    model = Restaurants
    template_name = 'restaurants/index.html'
    context_object_name = 'posts'

    # можем передать какие-то статические данные
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    # метод, который отображает только опубликованные статьи
    def get_queryset(self):
        return Restaurants.objects.filter(is_published=True)

# def index(request):
#     posts = Restaurants.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'restaurants/index.html', context=context)


def about(request):
    return render(request, 'restaurants/about.html', {
        'title': 'О сайте'
    })


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, 'restaurants/add_page.html', {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form,
    })


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


# Поиск по слагу
def show_post(request, post_slug):
    post = get_object_or_404(Restaurants, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'restaurants/post.html', context=context)


class RestaurantsCategory(ListView):
    model = Restaurants
    template_name = 'restaurants/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Restaurants.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_id):
#     posts = Restaurants.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'restaurants/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
