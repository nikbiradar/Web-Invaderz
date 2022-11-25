from django.contrib import admin

# Register your models here.
from .models import *

# Registering our accounts' models here to admin site.

# Category(i.e. genre)
admin.site.register(Category)

# Actors in movie
admin.site.register(Actor)

# Directors of movie
admin.site.register(Directors)

# MovieImages of movie
admin.site.register(MovieImage)

# Movie
admin.site.register(Movie)

