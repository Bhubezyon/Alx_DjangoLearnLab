from django.urls import path, include
from rest_framework.router import DefaultRouter
from .views import BookList, BookViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('path/', include('api.urls')), 
]

router = DefaultRouter()
router.register(r'book_all', BookViewSet, basename='book_all') # Maps to the BookList View

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), # Route for the BookList view 
    path('', include(router.urls)), # This includes all routes registered with the router
]

