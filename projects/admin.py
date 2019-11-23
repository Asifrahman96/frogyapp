from django.contrib import admin
from .models import Theatre, Series, Movie, Tvshow, Animation

# Register your models here.

class TheatreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'theatre_type',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year',)
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','cast_1','cast_2','cast_3','theatre_type')

admin.site.register(Theatre, TheatreAdmin)

class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'series_type',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year',)
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','cast_1','cast_2','cast_3','series_type')

admin.site.register(Series, SeriesAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'movie_type',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year',)
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','cast_1','cast_2','cast_3','movie_type')

admin.site.register(Movie, MovieAdmin)

class TvshowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'show_type',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year',)
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','cast_1','cast_2','cast_3','show_type')

admin.site.register(Tvshow, TvshowAdmin)

class AnimationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'animation_type',
        'year',
        'created_date',
        'is_cover',
        'is_published',
        'is_trending'
    )
    list_display_links = ('id', 'title')
    list_filter = ('year',)
    list_editable = ('is_published','is_cover','is_trending')
    search_fields = ('title','director','cast_1','cast_2','cast_3','animation_type')

admin.site.register(Animation, AnimationAdmin)
