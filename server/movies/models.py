from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genres = models.ManyToManyField(Genre)
    pick_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pick_movies')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')
    watch_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movies')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    popular = models.FloatField()
    rating = models.FloatField()

    trailer = models.CharField(max_length=200, null=True)

    netflix = models.BooleanField()
    watcha = models.BooleanField()
    wavve = models.BooleanField()
    


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)