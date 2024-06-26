from django import template
from django.db.models import Count

from restaurants.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.annotate(restaurants_count=Count('restaurants'))
    else:
        return Category.objects.filter(pk=filter).annotate(restaurants_count=Count('restaurants'))

@register.inclusion_tag('restaurants/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
