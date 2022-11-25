from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Constructing all required models for the movies app
# We inherit the BaseModel constructed in base.models

# Model: Category
# This model contains objects which are genres for movie 
class Category(BaseModel):
    # name of the category
    category_name = models.CharField(max_length=100)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.category_name

# Model: Actor
# This model contains objects which are names of actors
# worked in the movie
class Actor(BaseModel):

    # name of actor
    actor_name = models.CharField(max_length=100)
    actor_image=models.CharField(max_length=500)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.actor_name
    
# Model: Directors
# This model contains objects which are names of directors
# who directed the movie
class Directors(BaseModel):

    # Name of director
    director_name = models.CharField(max_length=100)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.director_name


# Model: MovieImages
# This model contains objects which are links to 
# images to images scraped from imdb
class MovieImage(BaseModel):

    # Link of image
    image =  models.CharField(max_length=500,null=True )
    
    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.image

# Model: Movie
# This model contains objects which is a Movie 
class Movie(BaseModel):
    # Name of movie
    movie_name = models.CharField(max_length=100)
    #slug to generate unique slug for each movie
    slug = models.SlugField(unique=True  , null=True , blank=True)
    #genres of movie
    category=models.ManyToManyField(Category)
    # Runtime of movie
    length=models.CharField(max_length=50)
    # Plot of movie
    movie_desription = models.TextField(default="")
    # Year of release
    release_year=models.CharField(null=True,max_length=100)
    # IMDB rating
    imdb_rating=models.FloatField(null=True)
    # Metascore
    meta_rating=models.FloatField(null=True)
    # Tomatometer
    rott_rating=models.FloatField(null=True)
    # Casts
    cast=models.ManyToManyField(Actor)
    # Directors
    directors=models.ManyToManyField(Directors)
    # Language
    language=models.CharField(max_length=100,default="")
    # Title image
    title_image=models.CharField(max_length=500,null=True)
    # Some more images
    gallery_images=models.ManyToManyField(MovieImage)
    # Brief summary
    summary=models.TextField(null=True)
    # Extra details
    details=models.JSONField(null=True)
    # Link to trailer of movie
    trailer=models.CharField(max_length=800,null=True)
    # Reviews from Rotten Tommatoes
    reviews=models.JSONField(null=True)
    # Reviews from IMDB
    user_reviews_imdb=models.JSONField(null=True)
    # Reviews from Metacritic
    user_reviews_meta=models.JSONField(null=True)
    
    # save function modified from django to
    # save movies using uniquely identifing slug
    def save(self , *args , **kwargs):
        self.slug = slugify(self.movie_name)
        super(Movie ,self).save(*args , **kwargs)

    # This is just to display the object by its movie_name 
    # instead of non-understandable UUID
    def __str__(self):
        return self.movie_name


    