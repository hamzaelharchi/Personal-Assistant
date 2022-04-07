from django.db import models
from django.conf import settings
# Create your models here.

from django.contrib.auth.models import User
        
class Task(models.Model):   
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Chat(models.Model):
    message=models.TextField(max_length=500000)

    def __str__(self):
        return self.message