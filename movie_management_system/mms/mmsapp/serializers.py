from rest_framework import serializers
from .models import User, Movie,  Genre, Review, Moviecast, Moviedirector, Watchlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model=User
            fields=['user_id','user_name','user_email']


class MovieSerializer(serializers.ModelSerializer):
    release_date = serializers.DateField(format='%Y-%m-%d')
    class Meta:
            model=Movie
            fields=['movie_id','movie_name','release_year','rating','genre_id']

class MovienSerializer(serializers.ModelSerializer):
    class Meta:
            model=Movie
            fields=['movie_id','movie_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
            model=Genre
            fields=['genre_id','genre_type']  

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
            model=Review
            fields=['review_id','movie_id','user_id','rating','comment','date'] 

class MoviecastSerializer(serializers.ModelSerializer):
    class Meta:
            model=Moviecast
            fields=['movie_id','actor_id','role']

class MoviedirectorSerializer(serializers.ModelSerializer):
    class Meta:
            model=Moviedirector
            fields=['movie_id','director_id']

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
            model=Watchlist
            fields=['watchlist_id','user_id','movie_id']            
