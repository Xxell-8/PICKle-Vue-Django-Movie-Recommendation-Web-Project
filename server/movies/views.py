import random
import requests
import pandas as pd
from decouple import config
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Count, Q
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


# 2. HOME > PICK Best > Pick 많은 순 + 최근 영화 순
@api_view(['GET'])
def pick_best(request):
    movies = Movie.objects.annotate(pick_count=Count('pick_users')).order_by('-pick_count', '-release_date')[:30]
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)


# 3. Search > 영화 검색 데이터 
@api_view(['GET'])
def movie_search_list(request):
    target = request.GET.get('q')
    results = Movie.objects.filter(title__icontains=target)
    serializer = MovieSerializer(results, many=True)
    return Response(serializer.data)


# 4. Recommend > 랜덤 영화 추천 + 본 영화/관심없는 영화 제외
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def random_recommend(request):
    dislikes = request.user.dislike_movies.all()
    watchs = request.user.watch_movies.all()
    exceptions = []
    for dislike in dislikes:
        exceptions.append(dislike.id)
    for watch in watchs:
        exceptions.append(watch.id)

    movies = Movie.objects.exclude(id__in=exceptions).order_by("?")[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 4. Recommend > 선호 장르 기반 추천 + 본 영화/관심없는 영화 제외
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def genre_recommend(request):
    genres = request.user.genres.all()
    if not genres:
        return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        length = len(genres)
        dislikes = request.user.dislike_movies.all()
        watchs = request.user.watch_movies.all()
        exceptions = []
        for dislike in dislikes:
            exceptions.append(dislike.id)
        for watch in watchs:
            exceptions.append(watch.id)

        if length == 1:
            movies = Movie.objects.exclude(id__in=exceptions).filter(genres=genres[0]).order_by('?')[:5]
        elif length == 2:
            movies = Movie.objects.exclude(id__in=exceptions).filter(Q(genres=genres[0]) | Q(genres=genres[1])).order_by('?')[:5]
        elif length == 3:
            movies = Movie.objects.exclude(id__in=exceptions).filter(Q(genres=genres[0]) | Q(genres=genres[1]) | Q(genres=genres[2])).order_by('?')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 4. Recommend > 팔로우한 유저 기반 추천 + 본 영화/관심없는 영화 제외
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow_recommend(request):
    dislikes = request.user.dislike_movies.all()
    watchs = request.user.watch_movies.all()
    exceptions = []
    for dislike in dislikes:
        exceptions.append(dislike.id)
    for watch in watchs:
        exceptions.append(watch.id)

    user = request.user.followings.order_by('?').first()
    movies = user.pick_movies.exclude(id__in=exceptions).order_by('-pk')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 4. Recommend > 날씨 기반 추천 + 본 영화/관심없는 영화 제외
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def weather_recommend(request):
    API_KEY= config('OPEN_WEATHER_MAP_API_KEY')
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}'

    response = requests.get(API_URL).json()
    weather = response.get('weather')[0].get('main')

    if weather == 'Thunderstorm':
        genre_list =  ['공포', '범죄', '스릴러', '미스테리']
    elif weather == 'Drizzle':
        genre_list =  ['드라마', '애니메이션', '다큐멘터리']
    elif weather == 'Rain':
        genre_list =  ['로맨스', '음악', '애니메이션']
    elif weather == 'Snow':
        genre_list =  ['모험', '판타지', '가족']
    elif weather == 'Clear':
        genre_list =  ['액션', '코미디', '가족']
    elif weather == 'Clouds':
        genre_list =  ['TV 영화', '전쟁']
    else:
        genre_list =  ['역사', '서부', 'SF']

    dislikes = request.user.dislike_movies.all()
    watchs = request.user.watch_movies.all()
    exceptions = []
    for dislike in dislikes:
        exceptions.append(dislike.id)
    for watch in watchs:
        exceptions.append(watch.id)

    genre_name = random.choice(genre_list)
    genre_id = get_object_or_404(Genre, name=genre_name)
    movies = Movie.objects.exclude(id__in=exceptions).filter(genres=genre_id).order_by('?')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


def get_recommend_movie_list(movie, movies, similar, top=10):
    search_movie_idx = movie.index.values
    similar_idx = similar[search_movie_idx, :top].reshape(-1)
    similar_idx = similar_idx[similar_idx != search_movie_idx] #제목이 movie_title 인 영화 제외
    result = movies.iloc[similar_idx].sort_values('id', ascending=False)[:5]
    return result


# 4. Recommend > 최근 Pick한 영화 기준 유사한 줄거리 영화 추천 + 본 영화/관심없는 영화 제외
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def overview_recommend(request):
    dislikes = request.user.dislike_movies.all()
    watchs = request.user.watch_movies.all()
    exceptions = []
    for dislike in dislikes:
        exceptions.append(dislike.id)
    for watch in watchs:
        exceptions.append(watch.id)

    movie_id = request.user.pick_movies.exclude(overview='').first().id
    movies = pd.DataFrame(list(Movie.objects.exclude(Q(overview='')|Q(id__in=exceptions)).values()))
    movie = movies[movies['id'] == movie_id]

    transformer = CountVectorizer()
    genres_vector = transformer.fit_transform(movies['overview'])
    similar = cosine_similarity(genres_vector, genres_vector)
    similar = similar.argsort()
    similar = similar[:, ::-1]
    res = get_recommend_movie_list(movie, movies, similar)

    movie_ids = []
    for i in range(5):
        movie_ids.append(list(res['id'])[i])

    s_movies = Movie.objects.filter(Q(id=movie_ids[0]) | Q(id=movie_ids[1]) | Q(id=movie_ids[2]) | Q(id=movie_ids[3]) | Q(id=movie_ids[4])).order_by('?')[:5]
    serializer = MovieSerializer(s_movies, many=True)
    return Response(serializer.data)