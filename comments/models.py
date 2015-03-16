from django.db import models

from django.contrib.auth import models
from post.models import Post

class Comment(models.Model):
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
