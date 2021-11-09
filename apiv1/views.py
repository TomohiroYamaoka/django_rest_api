from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

from shop.models import Book
from .serializers import BookSerializer


class　BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    selializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
