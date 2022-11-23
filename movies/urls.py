from django.urls import path
from movies.views import *

#urls for each movie and searched movies
urlpatterns = [
   path('<slug>/' , get_movie , name="get_movie" ),
   path('search_movies' , search_movies , name="search_movies" ),
   
]