from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()

    return render(request,"movies/index.html",{'movies':movies})

def details(request, movie_id):

    movie=get_object_or_404(Movie,id=movie_id)
    return render(request,"movies/details.html",{'movie':movie})
