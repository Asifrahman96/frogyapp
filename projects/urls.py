from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.projects, name="projects"),
    path('theatre/<int:theatre_id>',views.theatre, name="theatre"),
    path('series/<int:series_id>',views.series, name="series"),
    path('movie/<int:movie_id>',views.movie, name="movie"),
]