from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message_title', 'created')

admin.site.register(Contact, ContactAdmin)
