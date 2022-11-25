from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_email
# Constructing all required models for the accounts app
# We inherit the BaseModel constructed in base.models

# Model: Favourie Movies
# This model contains objects which are movie-names 
# marked as favorite by a user
class Fav_movie(BaseModel):
    # Title of the movie
    movie_name=models.CharField(max_length=100,null=True)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.movie_name

# Model: WatchListed Movies
# This model contains objects which are movie-names 
# which have been added to watchlist by a user
class WatchList(BaseModel):
    # Title of the movie
    movie_name=models.CharField(max_length=100,null=True)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.movie_name

# Model: Watched Movies
# This model contains objects which are movie-names 
# which have been watched by a user
class Watched(BaseModel):
    # Title of the movie
    movie_name=models.CharField(max_length=100,null=True)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.movie_name


# Model: User Profile
# Models the information related to a user
class Profile(BaseModel):
    # Creating a one-to-one relation between the User
    # class pre-defined in Django to this class
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    
    # The code below was an "attempt" to incorporate email authentication

    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    
    fav_movies=models.ManyToManyField(Fav_movie) # favorite movies
    watch_list=models.ManyToManyField(WatchList) # watchlisted movies
    watched_list=models.ManyToManyField(Watched) # watched movies

    # This is just to display the object by its username 
    # instead of non-understandable UUID
    def __str__(self):
        return self.user.username


# This was an "attempt" to incorporate email authentication
# The function below sends  an account activation email for verification

@receiver(post_save , sender = User)
def  send_email_token(sender , instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)