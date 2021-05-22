from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Curation, Comment
from accounts.models import User
from .serializers import (
    CurationSerializer,
    CurationListSerializer,
    CommentSerializer,
)
# from django.contrib.auth import get_user_model

# curation 
@api_view(['GET', 'POST'])
def curation_list(request):
    if request.method == 'GET':
        curations = get_list_or_404(Curation)
        context = {
            'request': request
        }
        serializer = CurationListSerializer(curations, many=True, context=context)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CurationSerializer(data=request.data)
        user = request.user
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def curation_detail(request, curation_pk):
    curation = get_object_or_404(Curation, pk=curation_pk)
    if request.method == 'GET':
        serializer = CurationSerializer(curation)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        curation.delete()
        data = {
            'delete': f'{curation_pk}번 큐레이션이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CurationSerializer(curation, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, curation_pk):
    curation = get_object_or_404(Curation, pk=curation_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, curation=curation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
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


