from django.contrib import admin
from .models import User, Movie,  Genre, Review, MovieCast, MovieDirector, Watchlist


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['user_id', 'user_name', 'user_email']
    list_per_page = 50


class GenreAdmin(admin.ModelAdmin):
    list_display=['genre_id', 'genre_type']
    list_per_page = 50


class MovieAdmin(admin.ModelAdmin):
    list_display=['movie_id', 'movie_name', 'release_year', 'rating', 'genre_id']
    list_per_page = 50


class ReviewAdmin(admin.ModelAdmin):
    list_display=['review_id', 'movie_id', 'user_id', 'rating', 'comment', 'date']
    list_per_page = 50


class MovieCastAdmin(admin.ModelAdmin):
    list_display=['movie_id', 'actor_id', 'role']
    list_per_page = 50


class MovieDirectorAdmin(admin.ModelAdmin):
    list_display=['movie_id', 'director_id']
    list_per_page = 50


class WatchlistAdmin(admin.ModelAdmin):
    list_display=['watchlist_id', 'user_id', 'movie_id']
    list_per_page = 50


admin.site.register(User, UserAdmin)
admin.site.register(Movie, MovieAdmin)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)

admin.site.register(MovieCast, MovieCastAdmin)
admin.site.register(MovieDirector, MovieDirectorAdmin)
admin.site.register(Watchlist, WatchlistAdmin)

