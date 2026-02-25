# CRUD Operations Documentation

## Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

Output:
<Book: 1984>

## Retrieve

```python
Book.objects.all()
```

Output:
<QuerySet [<Book: 1984>]>

## Update

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
```

Output:
<Book: Nineteen Eighty-Four>

## Delete

```python
book.delete()
Book.objects.all()
```

Output:
<QuerySet []>
