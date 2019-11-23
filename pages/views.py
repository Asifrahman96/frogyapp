from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Theatre, Tvshow, Series, Animation, Movie

# Home Page view
def home(request):
    #filtering Models which has (is_published ) selected
    theatres = Theatre.objects.order_by('-year').filter(is_published=True)
    series = Series.objects.order_by('-year').filter(is_published=True)
    movies = Movie.objects.order_by('-year').filter(is_published=True)
    #filtering Models which has (is_trending) selected
    theatre_trending = Theatre.objects.filter(is_published=True).filter(is_trending=True)
    series_trending = Series.objects.filter(is_published=True).filter(is_trending=True)
    movie_trending = Movie.objects.filter(is_published=True).filter(is_trending=True)
    #filtering Models which has (is_cover) selected
    theatre_cover = Theatre.objects.filter(is_published=True).filter(is_cover=True)
    series_cover = Series.objects.filter(is_published=True).filter(is_cover=True)
    movie_cover = Movie.objects.filter(is_published=True).filter(is_cover=True)

    context = {
        'theatres':theatres,
        'series':series,
        'movies':movies,
        'theatre_trending':theatre_trending,
        'series_trending':series_trending,
        'movie_trending':movie_trending,
        'theatre_cover':theatre_cover,
        'series_cover':series_cover,
        'movie_cover':movie_cover
    }
    
    return render(request, 'pages/home.html', context)

# About Page view
def promos(request):
    return render(request, 'pages/promos.html')

# About Page view
def about(request):
    return render(request, 'pages/about.html')