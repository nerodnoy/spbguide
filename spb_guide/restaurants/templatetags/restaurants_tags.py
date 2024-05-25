from django import template
from restaurants.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('restaurants/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
