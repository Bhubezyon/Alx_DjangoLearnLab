# advanced_features_and_sercurity/LibraryProject/accounts/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('advanced_features_and_sercurity.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'accounts/book_list.html', {'books': books})

@permission_required('advanced_features_and_sercurity.can_create', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to edit book
    pass

@permission_required('advanced_features_and_sercurity.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to delete book
    pass