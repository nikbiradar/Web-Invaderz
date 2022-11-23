from django.urls import path
from home.views import index

#homepage url
urlpatterns = [
   path('' , index , name="index" ),
   
]