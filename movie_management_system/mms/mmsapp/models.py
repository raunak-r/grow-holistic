from django.db import models
from datetime import datetime

# Create your models here.

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=100,null=True)

    def __str__(self):
        return self.user_name


class movie(models.Model):
    movie_id=models.AutoField(primary_key=True)
    movie_name=models.CharField(max_length=100)
    release_year=models.DateField(auto_now_add=True,null=True)
    rating=models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.movie_name

class director(models.Model):
    director_id=models.AutoField(primary_key=True)
    director_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.director_name
    

class actor(models.Model):
    actor_id=models.AutoField(primary_key=True)
    actor_name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.actor_name

class genre(models.Model):
    genre_id=models.AutoField(primary_key=True)
    genre_type=models.CharField(max_length=100)

    def __str__(self):
        return self.genre_type

class review(models.Model):
    review_id=models.AutoField(primary_key=True)
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.CharField(max_length=100)
    date=models.DateField(default=datetime.now)   #models.DateField()

    def __int__(self):
        return self.review_id

class movie_genre(models.Model):
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)
    genre_id=models.ForeignKey(genre,on_delete=models.CASCADE)

    def __int__(self):
        return self.movie_id

class movie_cast(models.Model):
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)
    actor_id=models.ForeignKey(actor,on_delete=models.CASCADE)
    role=models.CharField(max_length=100)

    def __int__(self):
        return self.movie_id

class movie_director(models.Model):
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)
    director_id=models.ForeignKey(director,on_delete=models.CASCADE)

    def __int__(self):
        return self.movie_id

class watchlist(models.Model):
    watchlist_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    movie_id=models.ForeignKey(movie,on_delete=models.CASCADE)

    def __int__(self):
        return self.movie_id
