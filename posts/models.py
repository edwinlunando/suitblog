from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'posts'
