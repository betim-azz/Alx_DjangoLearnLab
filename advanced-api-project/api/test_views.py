from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create initial data
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book = Book.objects.create(title='Harry Potter', publication_year=1997, author=self.author)

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    def test_get_books(self):
        # Test unauthenticated read access
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Chamber of Secrets', 'publication_year': 1998, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        # Do not log in
        data = {'title': 'Prisoner of Azkaban', 'publication_year': 1999, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)