from rest_framework import serializers
from .models import Curation, Comment
# from movies.serializers import MovieSerializer


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','review')


class CurationListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)


    class Meta:
        model = Curation
        fields = ('title','content')


class CurationSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True, source='comment_set.count')
    comment_set = CommentSerializer(many=True)


    class Meta:
        model = Curation
        fields = '__all__'

