from rest_framework import serializers
from .models import Movie, Genre


# 1. Movie Model (default)
class MovieSerializer(serializers.ModelSerializer):

    genres = serializers.StringRelatedField(many=True)
    pick_count = serializers.IntegerField(source='pick_users.count', read_only=True)
    wish_count = serializers.IntegerField(source='wish_users.count', read_only=True)
    watch_count = serializers.IntegerField(source='watch_users.count', read_only=True)
    dislike_count = serializers.IntegerField(source='dislike_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


