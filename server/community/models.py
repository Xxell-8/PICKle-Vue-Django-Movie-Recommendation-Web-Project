from django.db import models
from django.conf import settings
from movies.models import Movie


class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  liked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles', blank=True)
  movie = models.ManyToManyField(Movie)
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="article_comments")
  article= models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

