from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    genres = models.ManyToManyField(Genre)
    pick_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='pick_users')
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_users')
    watch_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_users')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_users')
    
    title = models.CharField(max_length=50)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, null=True)
    release_date = models.DateField()
    # 0보다 작은 정수값 허용 x 
    director = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    netflix = models.BooleanField()
    watcha = models.BooleanField()
    wavve = models.BooleanField()
    


class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

