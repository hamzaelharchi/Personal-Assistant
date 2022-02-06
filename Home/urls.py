from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),

    #api
    path('api/users', api.user_list_api, name='user_list_api'),
    path('api/users/<int:id>', api.user_detail_api, name='user_detail_api'),
    
]

