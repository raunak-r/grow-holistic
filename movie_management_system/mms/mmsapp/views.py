from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Movie,  Genre, Review, Moviecast, Moviedirector, Watchlist
from .serializers import UserSerializer, MovieSerializer,MovienSerializer,GenreSerializer, ReviewSerializer, MoviecastSerializer, MoviedirectorSerializer, WatchlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.db.models import Subquery, OuterRef
from rest_framework import serializers
import datetime


# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
    #get all user list
    #serialize them
    #return json
    if request.method == 'GET':
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return JsonResponse({'users':serializer.data})
    
    if request.method == 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return JsonResponse({'movies':serializer.data })


def genre_list(request):
    genres=Genre.objects.all()
    serializer=GenreSerializer(genres,many=True)
    return JsonResponse({'genres':serializer.data })

@api_view(['GET'])
def moviegenre_list(request,genre,format=None):
    try:
            genre_obj = Genre.objects.get(genre_type=genre)
            movies = Movie.objects.filter(genre_id=genre_obj)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
    except  Genre.DoesNotExist:
            return Response(f"No movies found for genre '{genre}'", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def directormovie_list(request,director,format=None):
    try:
            genre_obj = Genre.objects.get(genre_type=director)
            movies = Movie.objects.filter(genre_id=genre_obj)
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
    except  Genre.DoesNotExist:
            return Response(f"No movies found for genre '{director}'", status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def moviename_list(request,partial_name,format=None):
    try:
           movies=Movie.objects.filter(movie_name__icontains=partial_name)
           if movies.exists():
               serialized_movies = MovieSerializer(movies, many=True)
               return Response(serialized_movies.data, status=status.HTTP_200_OK)
           else:
               return Response(f"No movies found for partialname '{partial_name}'", status=status.HTTP_404_NOT_FOUND)
           
    except Movie.DoesNotExist:
           return Response(f"No movies found for partialname '{partial_name}'", status=status.HTTP_404_NOT_FOUND)
          
@api_view(['GET'])
def get_movie_by_director(request, director,format=None):
    # Query the movies based on director name
    movies = Movie.objects.filter(director__icontains=director)
    if movies.exists():
        movie_titles = [movie.title for movie in movies]
        return JsonResponse({'movies': movie_titles})
    else:
        return JsonResponse({'message': f"No movies found for director '{director}'"}, status=404)

@api_view(['GET'])
def get_movie_by_director(request, director,format=None):
    try:
        director_obj = User.objects.get(user_name=director)
        movie_ids = Moviedirector.objects.filter(director_id=director_obj.user_id).values('movie_id').distinct()
        movies = Movie.objects.filter(movie_id__in=Subquery(movie_ids)).values('movie_name')
        serializer = MovienSerializer(movies,many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        return JsonResponse({'error': f'director {director} does not exist'})
    except Exception as e:
        return JsonResponse({'error': str(e)})     




       