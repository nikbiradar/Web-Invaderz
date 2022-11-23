from django.shortcuts import render
from movies.models import Movie
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')

#search movie function to response search button in html page
def search_movies(request):
    if request.method=="POST":
        search=request.POST["search"]
        results=Movie.objects.filter(movie_name__contains=search)
        return render(request, 'movie/search.html',{
            'search':search,
            'movies':results})

    else:
        return render(request, 'movie/search.html')


#get movie function to display movie information of user selected movie
def get_movie(request, slug):
    try:
        movie=Movie.objects.get(slug=slug)
        rel_movies=Movie.objects.filter(imdb_rating__gte=9.2)
        return render(request, 'movie/movie.html', context={'movie':movie,
        'related_movies':rel_movies})
    except Exception as e:
        print(e)
