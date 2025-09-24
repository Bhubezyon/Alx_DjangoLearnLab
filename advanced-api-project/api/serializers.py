from rest_framework import serializers
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

# Bookserializer includes all fields and validates publication year.
# AuthorSerialzer nests BookSerializer to show all books by an author.
# The ,books' field uses the related_name from the Book model.