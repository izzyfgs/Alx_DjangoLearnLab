from django.test import TestCasefrom django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Tests for the Book API endpoints.
    """
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create authors
        self.author1 = Author.objects.create(name='Author 1')
        self.author2 = Author.objects.create(name='Author 2')

        # Create books
        self.book1 = Book.objects.create(title='Book 1', author=self.author1, publication_year=2020)
        self.book2 = Book.objects.create(title='Book 2', author=self.author2, publication_year=2021)
        self.book3 = Book.objects.create(title='Another Book', author=self.author1, publication_year=2022)

    def test_list_books(self):
        """
        Ensure we can list all books.
        """
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        url = reverse('book-list') + '?title=Book%201'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        url = reverse('book-list') + '?search=Another'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Another Book')

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

    def test_create_book_authenticated(self):
        """
        Ensure an authenticated user can create a new book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': self.author1.id, 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a new book.
        """
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': self.author1.id, 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """
        Ensure an authenticated user can update a book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {'title': 'Updated Book 1'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_delete_book_authenticated(self):
        """
        Ensure an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-delete', kwargs={'pk': self.book1.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

class AuthorAPITests(APITestCase):
    """
    Tests for the Author API endpoints.
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author')

    def test_list_authors(self):
        """
        Ensure we can list all authors.
        """
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_author_authenticated(self):
        """
        Ensure an authenticated user can create an author.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_create_author_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create an author.
        """
        url = reverse('author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



# Create your tests here.
