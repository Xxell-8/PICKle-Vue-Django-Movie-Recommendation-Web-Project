from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


class User(AbstractUser):
    genres = models.ManyToManyField(Genre)
    introduce = models.TextField(null=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username