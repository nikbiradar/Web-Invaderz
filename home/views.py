from django.shortcuts import render
from movies.models import *
# Create your views here.

#function to render movies on homepage
def index(request):
    movies=Movie.objects.exclude(title_image="https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie.jpg").filter(imdb_rating__gte=8.9)
    context={'movies':movies}
    return render(request,'home/index.html',context)

