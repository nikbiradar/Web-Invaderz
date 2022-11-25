from django.shortcuts import render,redirect
from movies.models import Movie
from accounts.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse



# Favourite movies page
@login_required                         # Ensures user is logged in or redirects to login page
def Fav_movies(request):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile

        # Finding all movies which are added to favourite list by user
        ms=user.fav_movies.all()
        movies=[]
        # Adding fav movies to a list
        for m in ms:
            m1=Movie.objects.filter(movie_name=m.movie_name)
            if m1:
                movies.append(m1[0])
        return render(request ,'movie/fav_movies.html',{'movies':movies})
    except:
        return redirect('accounts/login/')

# Searched movies page
def search_movies(request):
    if request.method=="POST":
        search=request.POST["search"]

        # filtering all movies containing keyword searched by user
        results=Movie.objects.filter(movie_name__contains=search)
        return render(request, 'movie/search.html',{
            'search':search,
            'movies':results})

    else:
        return render(request, 'movie/search.html')


# Functionality to add movie to favourites
@login_required
def Add_fav_movies(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0]
        if request.user.is_authenticated:
            user.save()
            # Checking if movie is already present in favourite list
            f=Fav_movie.objects.filter(movie_name=movie)
            # Adding movie to fav list
            if f:
                user.profile.fav_movies.add(f[0])
            else:
                f=Fav_movie(movie_name=movie)
                f.save()
                user.profile.fav_movies.add(f)
            user.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('accounts/login/')

    except Exception as e:
        return redirect('accounts/login/')

#get movie function to display movie information of user selected movie
def get_movie(request, slug):
    try:
        # Finding movie of given slug
        movie=Movie.objects.get(slug=slug)

        # extracting genres of this movies
        gnrs=movie.category.all()
        r_movies=[]
        mvs=Movie.objects.exclude(movie_name=movie.movie_name)

        ### Related movies

        # Finding movies of same genre set as this movie or 
        # contained in it and adding 3 movies of each genre
        for gnr in gnrs:
            count=0
            for mv in mvs:
                if count<3 and gnr in mv.category.all() and not mv in r_movies:
                    r_movies.append(mv)
                    count+=1
        return render(request, 'movie/movie.html', context={'movie':movie,
        'related_movies':r_movies})
    except Exception as e:
        print(e)


# Watchlist page 
@login_required
def watchList_movies(request):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile

        # Obtaining movies watchlisted by user
        ms=user.watch_list.all()
        movies=[]
        # creating movie list
        for m in ms:
            m1=Movie.objects.filter(movie_name=m.movie_name)
            if m1:
                movies.append(m1[0])
        return render(request ,'movie/watchlist.html',{'movies':movies})
    except:
        return redirect('accounts/login/')


# Functionality to add movie to watchlist
@login_required
def Add_watchlist(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0]
        # Checking if user is authenticated or not
        if request.user.is_authenticated:
            user.save()
            # Checking if movie is already present
            f=WatchList.objects.filter(movie_name=movie)
            # Adding movie to watch list
            if f:
                user.profile.watch_list.add(f[0])
            else:
                f=WatchList(movie_name=movie)
                f.save()
                user.profile.watch_list.add(f)
            user.save()
            # notation is to specify a default value of no value is present
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('accounts/login/')

    except Exception as e:
        return redirect('accounts/login/')


# Functionality to delete favourite listed movies
@login_required
def del_fav(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile
        # Filtering movie
        fv=Fav_movie.objects.filter(movie_name=movie)
        # Removing from user's favourite list
        user.fav_movies.remove(fv[0])
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return redirect('accounts/login/')


# Functionality to delete watchlisted movie
@login_required
def del_watchList(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile

        # Filtering movie 
        fv=WatchList.objects.filter(movie_name=movie)
        # Removing from user's watch list
        user.watch_list.remove(fv[0])
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return redirect('accounts/login/')
    

# Functionality to add watched movies
@login_required
def add_watched(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0]
        user.save()
        f=Watched.objects.filter(movie_name=movie)
        # Adding movie to watched list of user
        if f:
            user.profile.watched_list.add(f[0])
        else:
            f=Watched(movie_name=movie)
            f.save()
            user.profile.watched_list.add(f)
        user.save()
        # notation is to specify a default value of no value is present
        return redirect(request.META.get('HTTP_REFERER'))

    except Exception as e:
        return redirect('accounts/login/')


# Watched movies page
@login_required
def watched_movies(request):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile
        # Obtaining all movies watched by user
        ms=user.watched_list.all()
        movies=[]
        for m in ms:
            # Filtering movies with movie names in watchlist
            m1=Movie.objects.filter(movie_name=m.movie_name)
            if m1:
                movies.append(m1[0])
        return render(request ,'movie/watched.html',{'movies':movies})
    except:
        return redirect('accounts/login/')


# Delete functionality to delete watched movies 
# (if user accidently added as watched)
@login_required
def del_watched(request,movie):
    try:
        # Getting user from requests
        user=request.user
        # Filtering user profile from User model
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile
        # Filtering movie to be deleted
        fv=Watched.objects.filter(movie_name=movie)
        # Deleting from user's watched list
        user.watched_list.remove(fv[0])
        return redirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        return redirect('accounts/login/')

        
