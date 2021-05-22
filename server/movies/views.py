# from typing_extensions import runtime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer
from django.db.models import Q, Count
# from server.movies import serializers


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def short_movie_list(request):
    # movies = get_list_or_404(Movie)
    # runtime = request.GET.get('runtime', None)
    # Movie.objects.exclude(runtime__isnull=True)
    # if runtime:
    # if Movie.objects.exclude(runtime__isnull=False):
    # Entry.objects.filter(pub_date__isnull=False).latest('pub_date')
    movies = Movie.objects.order_by('runtime').filter()
    # else:
    #     movies = Movie.objects.exclude(runtime__isnull=True)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def random_recommended(request):
    movies = Movie.objects.order_by("?")[:5]
    # movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_recommended(request):
    my_genre = get_user_model.objects.get('genre')
    movies = Movie.objects.filter(genre=my_genre).order_by("?")[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def pick_best(request):

    movies = Movie.objects.all().annotate(pick_nums=Count('pick_users'))[:5]
    # movies = Movie.objects.order_by('-pick_users')[:10]
    # movies = Movie.objects.filter(pick_user__gte=0)
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)




# @api_view(['GET'])
# def search(request):
#     text = request.GET.get('q')
#     movies = Movie.objects.filter(title__icontains=text)
#     serializer = MovieSerializer(movies, many =True)
#     return Response(serializer.data)
