from django.db import models

from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    comment_title = models.CharField(max_length=255)
    comment_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.comment_title

    class Meta:
        verbose_name_plural = 'comments'
