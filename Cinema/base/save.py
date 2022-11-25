from movies.models import *
from bs4 import BeautifulSoup
import requests

# Saving movie info to database

# takes dictionary of movie information as argument and 
# saves it to database
def save(mi):
    mn=mi['name']   
    # Checks if movie is already preasent in database
    m=Movie.objects.filter(movie_name=mn)
    if not m:
        # If not present then add all info one by one
        m=Movie(movie_name=mi['name'])
        m.save()

        # Release year
        m.release_year=str(mi['year'])
        m.length=mi['runtime']              # Runtime of movie

        # Adding imdb rating
        m.imdb_rating=mi['imdb']        
        m.meta_rating=mi['meta']        # Adding meta rating
        # Adding rotten tomatoes rating
        m.rott_rating=mi['extra_details']['tomatometer']

        # Plot of movie
        m.movie_desription=mi['plot']

        # Brief summary of movie
        m.summary=mi['extra_details']['summary']

        # Title image
        m.title_image=mi['img']
        m.language=mi['extra_details']['lang']      #Language

        # Some extra details
        m.details=mi['extra_details']['details']
        m.trailer=mi['trailer']                     # Movie trailer

        # Movie directors
        dir_list=mi['directors'].split(', ')
        for dir in dir_list:
            d=Directors.objects.filter(director_name=dir)
            if d:
                m.directors.add(d[0])
            else:
                d=Directors(director_name=dir)
                d.save()
                m.directors.add(d)

        # Movie stars
        cl=mi['stars'].split(", ")
        for c in cl:
            c1=Actor.objects.filter(actor_name=c)
            if c1:
                m.cast.add(c1[0])
            else:
                c1=Actor(actor_name=c)
                c1.save()
                m.cast.add(c1)

        # Movie genres
        gnr=mi['genre'].split(", ")
        for gn in gnr:
            g=Category.objects.filter(category_name=gn)
            if g:
                m.category.add(g[0])
            else:
                g=Category(category_name=gn)
                g.save()
                m.category.add(g)

        # Some movie images
        imgs=mi['extra_details']['gallery']
        for img in imgs:
            i=MovieImage.objects.filter(image=img)
            if i:
                m.gallery_images.add(i[0])
            else:
                i=MovieImage(image=img)
                i.save()
                m.gallery_images.add(i)

        # Reviews
        m.reviews=mi['reviews']
        m.user_reviews_imdb=mi['user_reviewsIMDB']
        # m.user_reviews_meta=mi['user_reviewsMeta']
        m.save()
