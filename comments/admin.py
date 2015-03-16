from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'created', 'updated')

admin.site.register(Comment, CommentAdmin)
