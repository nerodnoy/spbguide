from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_page/', add_page, name='add_page'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]
