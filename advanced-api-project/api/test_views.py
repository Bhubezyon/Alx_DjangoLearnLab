from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self
        