from django.db import models

class Author(models.Model):
    """
    Represents an author of books.
    Attributes:
        name (str): The full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    Attributes:
        title (str): The title of the book.
        publication_year (int): The year the book was released.
        author (ForeignKey): The author who wrote the book (One-to-Many).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
