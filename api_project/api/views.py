from rest_framework import viewsets, permissions # <--- You MUST add ', permissions' here
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# ... rest of your code ...
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