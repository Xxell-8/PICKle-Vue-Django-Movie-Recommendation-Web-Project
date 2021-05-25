from rest_framework import serializers
from .models import Article, Comment
from movies.serializers import MovieSerializer


# 전체 글 조회 및 글 생성
class ArticleListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


# 댓글 조회
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
  
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user','article')


# 상세 글 조회
class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = MovieSerializer(many=True)
    comment_set = CommentSerializer(many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_count = serializers.IntegerField(source='liked_user.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'