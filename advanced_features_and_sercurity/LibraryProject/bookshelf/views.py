from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('bookshelf.create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
    return render(request, 'create_book.html')
       # logic to create a book passed in the request

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'delete_book.html')
       # logic to delete a book passed in the request

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to delete a book passed in the request

@permission_required('bookshelf.view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_detail.html', {'books': books})
       # logic to view books

from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def search_books(request):
    form = SearchForm(request.GET or None)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'bookshelf/books_list.html', {'form': form, 'results': books})