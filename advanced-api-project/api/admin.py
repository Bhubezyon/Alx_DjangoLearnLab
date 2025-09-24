from django.contrib import admin
from .models import Author, Book

adamin.site.register(Author)
admin.site.register(Book)