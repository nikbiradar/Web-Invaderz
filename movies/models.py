from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


#category of movie (genre)
class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.category_name)
        # super(Category ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.category_name

#actors in movie
class Actor(BaseModel):
    actor_name = models.CharField(max_length=100)
    actor_image= models.ImageField()


    def __str__(self) -> str:
        return self.actor_name
    
# directors of movie
class Directors(BaseModel):
    director_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.director_name


#images of movie
class MovieImage(BaseModel):
    image =  models.CharField(max_length=500,null=True )
    
    def __str__(self) -> str:
        return self.image

# class Reviews(BaseModel):
#     reviewer_name=models.CharField(max_length=200,null=True)
#     review_text=models.TextField(null=True)

#     def __str__(self) -> str:
#         return self.reviewer_name

#Movie model
class Movie(BaseModel):
    movie_name = models.CharField(max_length=100)
    #slug to generate unique slug for each movie
    slug = models.SlugField(unique=True  , null=True , blank=True)
    category=models.ManyToManyField(Category)
    length=models.CharField(max_length=50)
    movie_desription = models.TextField(default="")
    release_year=models.IntegerField(default=2000)
    imdb_rating=models.FloatField(null=True)
    meta_rating=models.FloatField(null=True)
    rott_rating=models.FloatField(null=True)
    cast=models.ManyToManyField(Actor)
    directors=models.ManyToManyField(Directors)
    language=models.CharField(max_length=100,default="")
    title_image=models.CharField(max_length=500,null=True)
    gallery_images=models.ManyToManyField(MovieImage)
    summary=models.TextField(null=True)
    details=models.JSONField(null=True)
    trailer=models.CharField(max_length=800,null=True)
    reviews=models.JSONField(null=True)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.movie_name)
        super(Movie ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.movie_name


    