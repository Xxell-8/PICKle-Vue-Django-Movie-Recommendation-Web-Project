from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre


class User(AbstractUser):
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.username
