from rest_framework import serializers
from .models import Movie, Genre, Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    # genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genres = GenreSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    pick_users = serializers.StringRelatedField(many=True)
    wish_users = serializers.StringRelatedField(many=True)
    watch_users = serializers.StringRelatedField(many=True)
    dislike_users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
    

