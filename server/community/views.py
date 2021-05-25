from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Article, Comment
from .serializers import (
    ArticleSerializer,
    ArticleListSerializer,
    CommentSerializer,
)

User = get_user_model()


# Article 전체 조회 및 글 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','DELETE','PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, curation_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user == request.user:
            comment.delete()
            data = {
                'delete': f'댓글{comment_pk}번이 삭제 되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'PUT':
        if comment.user == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# @api_view(['GET'])
# def comment_list(request):
#     comments = get_list_or_404(Comment)
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)

# @api_view(['PUT'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def likes(request, curation_pk):
#     curation = get_object_or_404(Article, pk=curation_pk)
#     user_id = (int(request.data['user']))
#     user = User.objects.get(id=user_id)
#     if curation.liked_users.filter(id=user.id).exists():
#         curation.liked_users.remove(user)
#     else:
#         curation.liked_users.add(user)
#     context = {
#         'liked_user': curation.liked_users,
#     }
#     serializer = LikeSerializer(curation, data=context)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)
