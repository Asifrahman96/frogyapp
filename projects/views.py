from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Theatre, Movie, Series, Tvshow, Animation

#Projects Page View
def projects(request):
    #Filtering theatre projects by ( is_published ) and order by ( year in descending order)
    theatres = Theatre.objects.order_by('-year').filter(is_published=True)
    series = Series.objects.order_by('-year').filter(is_published=True)
    movies = Movie.objects.order_by('-year').filter(is_published=True)
    context = {
        'theatres':theatres,
        'series':series,
        'movies':movies
    }
    return render(request, 'projects/projects.html', context)

#Theatre Page View
def theatre(request, theatre_id):
    #if theatre_id is not available, it returns 404 error page
    theatre = get_object_or_404(Theatre, pk=theatre_id)
    context = {
        'theatre':theatre,
    }
    return render(request, 'projects/theatre.html', context)

#Series Page View
def series(request, series_id):
    #if series_id is not available, it returns 404 error page
    series = get_object_or_404(Series, pk=series_id)
    context = {
        'series':series,
    }
    return render(request, 'projects/series.html', context)

#movie Page View
def movie(request, movie_id):
    #if movie_id is not available, it returns 404 error page
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie':movie,
    }
    return render(request, 'projects/movie.html', context)

#tvshows Page View
def tvshows(request):
    return render(request, 'projects/tvshows.html')

#animation Page View
def animation(request):
    return render(request, 'projects/animation.html')