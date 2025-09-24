from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Author, Book
from datetime import datetime

# Serializes Book model with custom validation
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Ensures publication year is not in the future
def validate_publication_year(self, value):
    current_year = datetime.now().year
    if value > current_year:
        raise serializers.ValidationError("Publication year cannot be in the future.")
    return value

# Serializes Author model with nested related books using BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        # Example: log or modify data before saving
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_update(self, serializer):
        # Example: log or modify data before updating
        serializer.save()

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_queryset(self)
    return Book.objects.fitler(publicatio_year__lte=2025)

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Bookserializer includes all fields and validates publication year.
# AuthorSerialzer nests BookSerializer to show all books by an author.
# The ,books' field uses the related_name from the Book model.