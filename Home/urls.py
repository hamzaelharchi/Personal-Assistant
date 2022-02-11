from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('index', views.index, name='index'),
    path("register/", views.register_req, name="register"),
    path("login/", views.login_req, name="login"),

]

