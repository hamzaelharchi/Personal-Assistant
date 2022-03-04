from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('index', views.index, name='index'),


    path('record/', views.recordings, name='record'),

    #api
    path('api/tasks/', api.taskList, name='task_list_api'),
    path('api/tasks/<int:pk>', api.taskDetail, name='task_detail_api'),

    path('api/task-create/', api.taskCreate, name="task-create"),

	path('api/task-update/<str:pk>/', api.taskUpdate, name="task-update"),
	path('api/task-delete/<str:pk>/', api.taskDelete, name="task-delete"),

    #chat
    path('api/chat/', api.chatList, name='chat_list_api'),
    path('api/chat/<int:pk>', api.chatDetail, name='chat_detail_api'),

    path('api/chat-create/', api.chatCreate, name="chat-create"),
    
    path("register/", views.register_req, name="register"),
    path("login/", views.login_req, name="login"),

]