from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides full CRUD operations for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
