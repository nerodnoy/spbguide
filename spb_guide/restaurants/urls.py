from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', RestaurantsHome.as_view(), name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', RestaurantsCategory.as_view(), name='category')
]
