from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.register, name='register'),
    path('index', views.index, name='index'),

    #api
    path('api/users', api.user_list_api, name='user_list_api'),
    path('api/users/<int:id>', api.user_detail_api, name='user_detail_api'),
    
]

