import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movie, Genre
from .serializers import MovieSerializer, GenreListSerializer


User = get_user_model()

# 1. Default - 전체 영화 데이터
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 1. Default - 단일 영화 상세 데이터
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 1. Default - 장르 데이터
@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)


# 1. Default - PICK / WISH / WATCH / DISLIKE
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rating(request, movie_pk, options):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if options == 'pick':
        if movie.pick_users.filter(pk=request.user.pk).exists():
            movie.pick_users.remove(request.user)
        else:
            movie.pick_users.add(request.user)

    elif options == 'wish':
        if movie.wish_users.filter(pk=request.user.pk).exists():
            movie.wish_users.remove(request.user)
        else:
            movie.wish_users.add(request.user)

    elif options == 'watch':
        if movie.watch_users.filter(pk=request.user.pk).exists():
            movie.watch_users.remove(request.user)
        else:
            movie.watch_users.add(request.user)

    elif options == 'dislike':
        if movie.dislike_users.filter(pk=request.user.pk).exists():
            movie.dislike_users.remove(request.user)
        else:
            movie.dislike_users.add(request.user)

    return Response(status=status.HTTP_200_OK)


# 2. HOME > PICK Best
@api_view(['GET'])
def pick_best(request):
    movies = Movie.objects.annotate(pick_count=Count('pick_users')).order_by('-pick_count')[:10]
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)


# 3. Search > 영화 검색 데이터 
@api_view(['GET'])
def movie_search_list(request):
    target = request.GET.get('q')
    results = Movie.objects.filter(title__icontains=target)
    serializer = MovieSerializer(results, many=True)
    return Response(serializer.data)


# 4. Recommend > 랜덤 영화 추천 
@api_view(['GET'])
def random_movie_list(request):
    movies = Movie.objects.order_by("?")[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# 5. Recommend > 선호 장르 기반 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def genre_recommended(request):
    favorite_genre = random.choice(request.user.genres.all())
    movies = Genre.objects.get(pk=favorite_genre.pk).movie_set.order_by('?')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 6.
# @api_view(['GET'])
# def short_movie_list(request):
#     movies = Movie.objects.order_by('runtime')[:5]
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)




