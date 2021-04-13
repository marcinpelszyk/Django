from django.contrib import admin
from .models import Person, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'year')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
