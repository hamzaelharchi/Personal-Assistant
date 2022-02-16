from rest_framework import serializers
from .models import Task, Chat

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields='__all__'