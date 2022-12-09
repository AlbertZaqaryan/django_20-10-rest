from django.shortcuts import render
from rest_framework import viewsets
from .models import Notebook, Category
from .serializers import NotebookModelSerializer, CategoryModelSerializer
# Create your views here.

class CategoryViewSets(viewsets.ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class NotebookViewSets(viewsets.ModelViewSet):
    serializer_class = NotebookModelSerializer
    queryset = Notebook.objects.all()
