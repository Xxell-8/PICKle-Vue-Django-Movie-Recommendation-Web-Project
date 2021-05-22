from django.db import models
from django.conf import settings
from movies.models import Movie
# from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Curation(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  liked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_curations', blank=True)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  @property
  def likes(self):
      return self.liked_user.count()



# class Comment(models.Model):
#   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_comments")
#   content = models.TextField()
#   rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   review = models.ForeignKey(Curation, on_delete=models.CASCADE)

