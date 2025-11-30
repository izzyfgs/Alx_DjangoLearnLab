<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer




class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides full CRUD for Book model
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
>>>>>>> ce24b6e068ab3e8d4bca815c263a326773d82876
