from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Directors)

# class MovieImageAdmin(admin.StackedInline):
#     model=MovieImage

# class MovieAdmin(admin.ModelAdmin):
#     inlines=[MovieImageAdmin]

admin.site.register(MovieImage)
admin.site.register(Movie)

