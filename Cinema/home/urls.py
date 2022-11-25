from django.urls import path
from home.views import index

#homepage url
urlpatterns = [

   # Url to homepage of website
   path('' , index , name="index" ),
   
]