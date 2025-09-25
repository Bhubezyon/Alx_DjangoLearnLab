from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.author1 = author.objects.create(name='Author One')
        self.book1 = Book.objects.create(title='Test Book', author=self.author, publication_year='2024')

def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'author': self.author1.id,
            'publication_year': '2023'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': 'Updated Book',
            'author': self.author1.id,
            'publication_year': '2022'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')

def test_delete_book(self):
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
        