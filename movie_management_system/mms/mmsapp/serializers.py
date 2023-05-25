from rest_framework import serializers
from .models import User, Movie,  Genre, Review, MovieCast, MovieDirector, Watchlist


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'user_email']


class MovieSerializer(serializers.ModelSerializer):
    # release_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Movie
        fields = '__all__'


class MovienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id','movie_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCast
        fields = '__all__'


class MovieDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDirector
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
