from django.db.models import Count

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить заведение', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(restaurants_count=Count('restaurants'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)  # убираем меню с индексом 1

        context['menu'] = user_menu
        context['get_cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
