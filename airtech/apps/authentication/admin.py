from django.contrib import admin

from airtech.apps.authentication.models import Profile, User

admin.site.register(User)
admin.site.register(Profile)
