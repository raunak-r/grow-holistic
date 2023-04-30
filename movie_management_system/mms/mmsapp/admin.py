from django.contrib import admin
from .models import User, Movie,  Genre, Review, Moviecast, Moviedirector, Watchlist

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['user_id','user_name','user_email']

class genreAdmin(admin.ModelAdmin):
    list_display=['genre_id','genre_type']    

class movieAdmin(admin.ModelAdmin):
    list_display=['movie_id','movie_name','release_year','rating','genre_id']

# class directorAdmin(admin.ModelAdmin):
#     list_display=['director_id','director_name','gender']

# class actorAdmin(admin.ModelAdmin):
#     list_display=['actor_id','actor_name','age']



class reviewAdmin(admin.ModelAdmin):
    list_display=['review_id','movie_id','user_id','rating','comment','date']


# class moviegenreAdmin(admin.ModelAdmin):
#     list_display=['movie_id','genre_id']

class moviecastAdmin(admin.ModelAdmin):
    list_display=['movie_id','actor_id','role']

class moviedirectorAdmin(admin.ModelAdmin):
    list_display=['movie_id','director_id']

class watchlistAdmin(admin.ModelAdmin):
    list_display=['watchlist_id','user_id','movie_id']


admin.site.register(User,userAdmin)
admin.site.register(Movie,movieAdmin)
# admin.site.register(director,directorAdmin)
# admin.site.register(actor,actorAdmin)
admin.site.register(Genre,genreAdmin)
admin.site.register(Review,reviewAdmin)
# admin.site.register(Moviegenre,moviegenreAdmin)
admin.site.register(Moviecast,moviecastAdmin)
admin.site.register(Moviedirector,moviedirectorAdmin)
admin.site.register(Watchlist,watchlistAdmin)

