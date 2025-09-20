from rest_framework import viewsets
from rest_framework import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Secure the endpoint

class BookList(ListAPIView):
    queryset = Book.object.all()
    serializer_class = BookSerializer