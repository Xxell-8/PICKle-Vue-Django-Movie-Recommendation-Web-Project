from rest_framework import serializers
from .models import Curation, Comment
# from movies.serializers import MovieSerializer


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','review')


class CurationListSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(read_only=True, source='comment_set.count')
    likes = serializers.CharField(source="liked_users.count")

    class Meta:
        model = Curation
        fields = ('title','content')


class CurationSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True, source='comment_set.count')
    comment_set = CommentSerializer(many=True)
    likes = serializers.CharField(source="liked_users.count")

    class Meta:
        model = Curation
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Curation
        fields = ('liked_users',)