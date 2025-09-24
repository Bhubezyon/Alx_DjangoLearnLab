from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

#ListView: Retrieves all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read only access for all users

# DetailView: Retrieves a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read only access for all users

# CreateView: Adds a new a book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can create books

# UpdateView: Modifies an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can update books

# DeleteView: Removes a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can delete books

# Enable filtering, searching, and ordering
filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
fiterset_fields = ['title', 'author', 'published_year']
search_fields = ['title', 'author__name']
ordering_fields = ['title', 'published_year']

# BookListView supports:
# - Filtering by title, author, and publication_year
# - Searching by title and author's name
# - Ordering by title and publication_year