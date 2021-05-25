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
from django.db.models import Q


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

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



def get_recommend_movie_list(movie, movies, similar, top=30):
    search_movie_idx = movie.index.values
    similar_idx = similar[search_movie_idx, :top].reshape(-1)
    similar_idx = similar_idx[similar_idx != search_movie_idx] #제목이 movie_title 인 영화 제외
    result = movies.iloc[similar_idx].sort_values('id', ascending=False)[:5]
    return result


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request, movie_id):
    if Movie.objects.get(id=movie_id):
        
        movies = pd.DataFrame(list(Movie.objects.all().values()))
        movie = movies[movies['id'] == movie_id]

        transformer = CountVectorizer()
        genres_vector = transformer.fit_transform(movies['overview'])
        similar = cosine_similarity(genres_vector, genres_vector)
        similar = similar.argsort()
        similar = similar[:, ::-1]
        res = get_recommend_movie_list(movie, movies, similar)

        # res = dpd.convert_df_back_to_qs(res)
        r_movies = res.id
        # for i in range(5):
        #     if i < len(r_movies):
        #         r_movies.append(get_object_or_404(Movie, id=res.id[i]))
        #     else:
        #         r_movies.append(get_object_or_404(Movie, id=res.id[0]))
        reco_movies = Movie.objects.filter(Q(id=r_movies[0]) | Q(id=r_movies[1]) | Q(id=r_movies[2]) | Q(id=r_movies[3]) | Q(id=r_movies[4])).order_by('?')[:5]
        serializer = MovieSerializer(reco_movies, many=True)
        return Response(serializer.data)
        # return Response(r_movies)

        # serializer = MovieSerializer(res, many=True)
        # return Response(serializer.data)

        # return Response(res.id)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 6.
# @api_view(['GET'])
# def short_movie_list(request):
#     movies = Movie.objects.order_by('runtime')[:5]
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def genre_recommended(request):
#     my_genre = get_user_model.objects.get('genre')
#     movies = Movie.objects.filter(genre=my_genre).order_by("?")[:5]
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


