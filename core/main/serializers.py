from rest_framework import serializers
from .models import Notebook, Category


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class NotebookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ['category', 'name', 'price', 'img']