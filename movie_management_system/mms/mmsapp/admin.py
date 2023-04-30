from django.contrib import admin
from .models import user, movie, director, actor, genre, review, movie_genre, movie_cast, movie_director, watchlist

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['user_id','user_name','user_email']

class movieAdmin(admin.ModelAdmin):
    list_display=['movie_id','movie_name','release_year','rating']

class directorAdmin(admin.ModelAdmin):
    list_display=['director_id','director_name','gender']

class actorAdmin(admin.ModelAdmin):
    list_display=['actor_id','actor_name','age']

class genreAdmin(admin.ModelAdmin):
    list_display=['genre_id','genre_type']

class revieAdmin(admin.ModelAdmin):
    list_display=['review_id','movie_id','user_id','rating','comment','date']


class movie_genreAdmin(admin.ModelAdmin):
    list_display=['movie_id','genre_id']

class movie_castAdmin(admin.ModelAdmin):
    list_display=['movie_id','actor_id','role']

class movie_directorAdmin(admin.ModelAdmin):
    list_display=['movie_id','director_id']

class watchlistAdmin(admin.ModelAdmin):
    list_display=['watchlist_id','user_id','movie_id']


admin.site.register(user,userAdmin)
admin.site.register(movie,movieAdmin)
admin.site.register(director,directorAdmin)
admin.site.register(actor,actorAdmin)
admin.site.register(genre,genreAdmin)
admin.site.register(review,revieAdmin)
admin.site.register(movie_genre,movie_genreAdmin)
admin.site.register(movie_cast,movie_castAdmin)
admin.site.register(movie_director,movie_directorAdmin)
admin.site.register(watchlist,watchlistAdmin)

