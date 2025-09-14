# bookshelf/views.py

from django.shortcuts import render
from .models import Book
from .forms import BooksearchForm

def search_books(request):
    form = BooksearchForm(request.POST or None)
    books = []
    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        books = Book.objects.all()
        if title:
            books = books.filter(title__icontains=title)
        if author:
            books = books.filter(author__icontains=author)
    return render(request, 'bookshelf/search_books.html', {'form': form, 'books': books})

# bookshelf/forms.py

from django import forms

class BooksearchForm(forms.Form):
    title = forms.CharField(max_length=255)

# bookshelf/views.py

from django.http import HttpResponse

def simple_view(request):
    response = HttpResponse("Secure Content")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trustedscripts.example.com; object-src 'none'; style-src 'self' https://trustedstyles.example.com;"
    return response
