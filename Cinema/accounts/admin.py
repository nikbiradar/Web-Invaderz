from django.contrib import admin
from .models import *
# Registering our accounts' models here to admin site.

# Favourite Movies
admin.site.register(Fav_movie)

# WatchList Movies
admin.site.register(WatchList)

# Watched Movies
admin.site.register(Watched)

# User Profile
admin.site.register(Profile)