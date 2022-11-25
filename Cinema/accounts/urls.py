from django.urls import path
from accounts.views import *

# urls of accounts app
urlpatterns = [
   #login page
   path('login/' , login_page , name="login" ),
   
   #signup page
   path('register/' , register_page , name="register"),
   
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   
   #logout functionality
   path('logout',logout_user,name='logout')
]