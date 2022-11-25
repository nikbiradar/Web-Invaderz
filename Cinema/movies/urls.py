from django.urls import path
from movies.views import *

# urls of accounts app


urlpatterns = [
   # Add to favourite
   path('add_fav/<movie>/', Add_fav_movies,name='Add_fav_movies'),
   # Favourite movies
   path('fav_movies',Fav_movies,name='Fav_movies'),
   # Deleting favourite movie
   path('del_fav/<movie>/', del_fav,name='del_fav'),
   # Add to watchlist
   path('add_watchlist/<movie>/', Add_watchlist,name='Add_watchlist'),
   # Watchlist movies
   path('watchlist_movies',watchList_movies,name='watchList_movies'),
   # Deleting watchlisted movie
   path('del_watch/<movie>/', del_watchList,name='del_watch'),
   # Add to watched movies
   path('add_watched/<movie>/', add_watched,name='Add_watched'),
   # watched movies
   path('watched_movies',watched_movies,name='watched_movies'),
   # Deleting watched movie
   path('del_watched/<movie>/', del_watched,name='del_watched'),

   # Perticular movie page
   path('movie/<slug>/' , get_movie , name="get_movie" ),
   # Searched movies page
   path('search_movies' , search_movies , name="search_movies" ),
]