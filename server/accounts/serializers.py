from rest_framework import serializers
from django.db.models import fields
from django.contrib.auth import get_user_model
from movies.serializers import MovieSerializer



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'genres')


class UserInfoSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    pick_movies = MovieSerializer(many=True)
    wish_movies = MovieSerializer(many=True)
    watch_movies = MovieSerializer(many=True)
    dislike_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username', 
            'pick_movies', 
            'wish_movies', 
            'watch_movies', 
            'dislike_movies', 
            'genres'
        )