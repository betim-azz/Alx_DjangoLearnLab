# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey creates a many-to-one relationship (one author, many posts)
    # on_delete=models.CASCADE ensures if a User is deleted, their posts are too
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title