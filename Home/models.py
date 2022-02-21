from turtle import title
from django.db import models


        
class Task(models.Model):
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class Chat(models.Model):
    message=models.TextField(max_length=100000)

    def __str__(self):
        return self.message


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(widget=models.PasswordInput)