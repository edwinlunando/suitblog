from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    is_draft = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'
