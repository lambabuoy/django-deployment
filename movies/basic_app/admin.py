from django.contrib import admin
from basic_app.models import Movie, Actor
from basic_app import models


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title', 'plot', 'director', 'released_year', 'length']
    search_fields = ['title', 'director']
    list_display = ['title', 'director', 'plot', 'length']
    list_filter = ['released_year']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'movie']

