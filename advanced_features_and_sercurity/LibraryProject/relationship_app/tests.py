from django.test import TestCase
from .models import Author, Book, Library, Librarian

class RelationshipModelTests(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Calvin")
        book = Book.objects.create(title="Django Deep Dive", author=author)
        library = Library.objects.create(name="Tech Library")
        library.books.add(book)
        Librarian.objects.create(name="Alice", library=library)

    def test_author_creation(self):
        author = Author.objects.get(name="Calvin")
        self.assertEqual(author.books.count(), 1)

    def test_in_library(self):
        library = Library.objects.get(name="Tech Library")
        self.assertEqual(library.books.count(), 1)

    def test_librarian_for_library(self):
        library = Library.objects.get(name="Tech Library")
        self.assertEqual(library.librarian.name, "Alice")