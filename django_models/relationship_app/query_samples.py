from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()
print("Books by", author.name, ":", list(books_by_author))

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print("Books in", library.name, ":", list(library_books))

# 3. Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of", library.name, ":", librarian.name)
