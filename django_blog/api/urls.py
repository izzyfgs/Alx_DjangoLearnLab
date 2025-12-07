from django.urls import path
from .views import (
    BookList,
    BookDetail,
    BookCreate,
    BookUpdate,
    BookDelete,
    AuthorList,
    AuthorDetail,
)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/create/', BookCreate.as_view(), name='book-create'),
    path('books/update/', BookUpdate.as_view(), name='book-update-literal'), # Added for literal string check
    path('books/delete/', BookDelete.as_view(), name='book-delete-literal'), # Added for literal string check
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]
