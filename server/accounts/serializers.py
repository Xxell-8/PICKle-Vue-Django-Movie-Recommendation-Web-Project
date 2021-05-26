from django.db import models
from rest_framework import serializers
from django.db.models import fields
from django.contrib.auth import get_user_model
from movies.serializers import MovieSerializer
from community.serializers import ArticleSerializer



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'genres')


class UserInfoSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    article_set = ArticleSerializer(many=True)
    liked_articles = ArticleSerializer(many=True)
    pick_movies = MovieSerializer(many=True)
    wish_movies = MovieSerializer(many=True)
    watch_movies = MovieSerializer(many=True)
    dislike_movies = MovieSerializer(many=True)
    pick_count = serializers.IntegerField(source='pick_movies.count', read_only=True)
    wish_count = serializers.IntegerField(source='wish_movies.count', read_only=True)
    watch_count = serializers.IntegerField(source='watch_movies.count', read_only=True)
    dislike_count = serializers.IntegerField(source='dislike_movies.count', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)


    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username',
            'introduce', 'genres', 'article_set', 'liked_articles',
            'pick_movies', 'wish_movies', 'watch_movies', 'dislike_movies',
            'pick_count', 'wish_count', 'watch_count', 'dislike_count',
            'followers', 'followings', 'followers_count', 'followings_count',
        )