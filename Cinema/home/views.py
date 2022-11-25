from django.shortcuts import render
from movies.models import *
from accounts.models import *
# Create your views here.


# function to render movies on homepage
# It returns four movie lists which are displayed on home page
def index(request):

    ### Top IMDB movies
    # These are filtered movies with IMDB rating >= 9
    movies=Movie.objects.filter(imdb_rating__gte=9)

    ### Reccomanded movies
    
    # These movies are filtered based on users favourite list
    # We are finding movies of which category(i.e. genre) 
    # the user likes most and display movies of those genre and 
    # not present in user's watched list as recommended movies
    rec_movies=[]
    try:
        user=request.user
        user_obj = User.objects.filter(username = user)
        user=user_obj[0].profile
        mvs=user.fav_movies.all()
        gn_dict={}
        for m in mvs:
            mv=Movie.objects.filter(movie_name=m)[0]
            for gn in mv.category.all():
                if not gn in gn_dict:
                    gn_dict[gn]=0
        for m in mvs:
            mv=Movie.objects.filter(movie_name=m)[0]
            for gn in mv.category.all():
                    gn_dict[gn]+=1
        max_gnr = [key for key, value in gn_dict.items() if value == max(gn_dict.values())]
        mvs=Movie.objects.all()

        # Excluding those movies which user had already watched
        num=len(max_gnr)
        i=0
        wmvs=user.watched_list.all()
        wmvss=[]
        for wmv in wmvs:
            wmvss.append(wmv.movie_name)

        mvss1=user.fav_movies.all()
        mvs1=[]
        for mmv in mvss1:
            mvs1.append(mmv.movie_name)
        # Adding movies to reccomended list of user
        for mv in mvs:
            if max_gnr[i % num] in mv.category.all() and (not mv.movie_name in wmvss) and (not mv.movie_name in mvs1):
                rec_movies.append(mv)
                i+=1
    except:
        rec_movies=[]
    

    ### Recently released movies

    # Filtering those movies which are released in 2022
    recent_movies=Movie.objects.filter(release_year='2022')

    ### Horror movies

    # Filtering movies with genre horror
    hr_movies=[]
    mvs=Movie.objects.all()
    hr=Category.objects.filter(category_name='Horror')
    for mv in mvs:
        if hr[0] in mv.category.all():
            hr_movies.append(mv)

    return render(request,'home/index.html',{'movies':movies[:5],'rec_movies':rec_movies[:5],
    'recent_movies':recent_movies[:5],'horror_movies':hr_movies[:5]
    })

