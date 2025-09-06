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