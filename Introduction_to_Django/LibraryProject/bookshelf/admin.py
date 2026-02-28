from django.contrib import admin
from .models import Book

# Customizing the Admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a sidebar filter for publication year
    list_filter = ('publication_year',)
    
    # Enable a search bar for title and author
    search_fields = ('title', 'author')

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)