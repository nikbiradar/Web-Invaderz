from movies.models import *
from base.extract_data import *
from bs4 import BeautifulSoup
import requests


def save():
    movie_info=extract()
    for mi in movie_info:
        m=Movie(movie_name=mi['name'])
        m.save()
        m.release_year=mi['year']
        m.length=mi['runtime']
        m.imdb_rating=mi['imdb']
        m.meta_rating=mi['meta']
        m.movie_desription=mi['plot']
        m.summary=mi['extra_details']['summary']
        m.title_image=mi['extra_details']['img']
        m.language=mi['extra_details']['lang']
        m.details=mi['extra_details']['details']
        m.trailer=mi['trailer']
        dir_list=mi['directors'].split(', ')
        for dir in dir_list:
            d=Directors.objects.filter(director_name=dir)
            if d:
                m.directors.add(d[0])
            else:
                d=Directors(director_name=dir)
                d.save()
                m.directors.add(d)
        cl=mi['stars'].split(", ")
        for c in cl:
            c1=Actor.objects.filter(actor_name=c)
            if c1:
                m.cast.add(c1[0])
            else:
                c1=Actor(actor_name=c)
                c1.save()
                m.cast.add(c1)
        gnr=mi['genre'].split(", ")
        for gn in gnr:
            g=Category.objects.filter(category_name=gn)
            if g:
                m.category.add(g[0])
            else:
                g=Category(category_name=gn)
                g.save()
                m.category.add(g)
        imgs=mi['extra_details']['gallery']
        for img in imgs:
            i=MovieImage.objects.filter(image=img)
            if i:
                m.gallery_images.add(i[0])
            else:
                i=MovieImage(image=img)
                i.save()
                m.gallery_images.add(i)
        m.reviews=mi['reviews']
        m.save()
