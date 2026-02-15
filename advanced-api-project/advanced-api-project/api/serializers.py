from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation for the publication year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value): # Ensure this matches the 'if' statement
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested BookSerializer to handle the one-to-many relationship.
    """
    # The 'books' field matches the related_name in the Author/Book model relationship
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books'] # The requirement only specifically asks for these
