from django.contrib import admin

from contact.models import Contact, User

# Register your models here.

admin.site.register(Contact)
admin.site.register(User)