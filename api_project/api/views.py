from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# Keep your BookList from Task 1 if you wish
from rest_framework import generics

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW: Task 2 ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Now 'permissions' will be recognized
    permission_classes = [permissions.IsAuthenticated]