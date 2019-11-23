from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

# Theatre models here.
class Theatre(models.Model):
    title = models.CharField(max_length=200)
    theatre_type = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    year = models.DateField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4 = models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    # Card image in Home Page & Details Page
    photo_card = models.ImageField(blank=True)
    # carousel Image in Home Page
    photo_cover = models.ImageField(blank=True)
    # Gallery Images in Details Page( lightbox )
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    # Embed Video Field
    promo = EmbedVideoField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Series models here.
class Series(models.Model):
    title = models.CharField(max_length=200)
    series_type = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    year = models.DateField()
    episodes = models.IntegerField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4 = models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    # Card image in Home Page & Details Page
    photo_card = models.ImageField(blank=True)
    # carousel Image in Home Page
    photo_cover = models.ImageField(blank=True)
    # Gallery Images in Details Page( lightbox )
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    # Embed Video Field
    promo = EmbedVideoField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "series"

    def __str__(self):
        return self.title

# Movie models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    year = models.DateField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4 = models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    # Card image in Home Page & Details Page
    photo_card = models.ImageField(blank=True)
    # carousel Image in Home Page
    photo_cover = models.ImageField(blank=True)
    # Gallery Images in Details Page( lightbox )
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    # Embed Video Field
    promo = EmbedVideoField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Tvshow(models.Model):
    title = models.CharField(max_length=200)
    show_type = models.CharField(max_length=100)
    description = RichTextField(blank=True) 
    year = models.DateField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4= models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    photo_card = models.ImageField(blank=True)
    photo_cover = models.ImageField(blank=True)
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Animation(models.Model):
    title = models.CharField(max_length=200)
    animation_type = models.CharField(max_length=100)
    description = RichTextField(blank=True) 
    year = models.DateField()
    director = models.CharField(max_length=50)
    cast_1 = models.CharField(max_length=50)
    cast_2= models.CharField(max_length=50, blank=True)
    cast_3 = models.CharField(max_length=50, blank=True)
    cast_4= models.CharField(max_length=50, blank=True)
    cast_5 = models.CharField(max_length=50, blank=True)
    photo_card = models.ImageField(blank=True)
    photo_cover = models.ImageField(blank=True)
    gallery_1 = models.ImageField(blank=True)
    gallery_2 = models.ImageField(blank=True)
    gallery_3 = models.ImageField(blank=True)
    gallery_4 = models.ImageField(blank=True)
    gallery_5 = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default = True)
    is_cover = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title