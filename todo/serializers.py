from rest_framework import serializers
from .models import Todo, TodoComment

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'




class TodoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoComment
        fields = '__all__'