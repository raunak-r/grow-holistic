from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Movie,  Genre, Review, Moviecast, Moviedirector, Watchlist
from .serializers import UserSerializer, MovieSerializer,  GenreSerializer, ReviewSerializer, MoviecastSerializer, MoviedirectorSerializer, WatchlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 

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
    return JsonResponse({'movies':serializer.data   })
