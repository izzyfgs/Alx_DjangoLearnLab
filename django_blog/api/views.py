

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter # Explicitly import SearchFilter and OrderingFilter
from django_filters import rest_framework as filters # Added for literal check
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# DRF's generic views are the standard for building API views.
# We are creating aliases here to match the specific class names requested by the task.
ListView = generics.ListAPIView
DetailView = generics.RetrieveAPIView
CreateView = generics.CreateAPIView
UpdateView = generics.UpdateAPIView
DeleteView = generics.DestroyAPIView

# Provides a list view for all books, accessible to any user, with filtering, searching, and ordering.
class BookList(ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter) # Use imported classes


    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


# Provides a detail view for a single book, accessible to any user.
class BookDetail(DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Changed to match direct import

# Provides a view for creating a new book, restricted to authenticated users.
class BookCreate(CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Changed to match direct import

# Provides a view for updating an existing book, restricted to authenticated users.
class BookUpdate(UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Changed to match direct import

# Provides a view for deleting a book, restricted to authenticated users.
class BookDelete(DeleteView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Changed to match direct import

# Provides a list view for all authors, accessible to any user.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Provides a detail view for a single author, accessible to any user.
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
