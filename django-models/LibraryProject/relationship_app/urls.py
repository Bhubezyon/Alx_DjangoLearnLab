from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path ('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view() , name='register'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
]

from django.urls import path
from . import views

urlpatterns = [path('admin/', views.admin_view, name='admin_view'),
               path('librarian/', views.librarian_view, name='librarian_view')
               path('member/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.edit_book, name='delete_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

from django.shortcuts import render, get_object_or_404, redirect
from relationship_app.models import Library, Book, Author
from relationship_app.forms import BookForm, AuthorForm, LibraryForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})