from django.contrib import admin

# Register your models here.
from .models import Task, Chat
 
admin.site.register(Task)
admin.site.register(Chat)