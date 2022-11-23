from django.contrib import admin

# Register your models here.
from .models import Profile

#registering Pofile model to admin site
admin.site.register(Profile)