from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

# class Curation(models.Model):
#   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
#   movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#   title = models.CharField(max_length=100)
#   content = models.TextField()
#   rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)


# class Community(models.Model):
#   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="communities")
#   title = models.CharField(max_length=100)
#   content = models.TextField()
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_comments")
#   content = models.TextField()
#   rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   review = models.ForeignKey(Curation, on_delete=models.CASCADE)