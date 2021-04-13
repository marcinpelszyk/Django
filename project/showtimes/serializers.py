from datetime import timedelta

from django.utils import timezone
from django.db.models import Q
from rest_framework import serializers
from movielist.serializers import MovieSerializer
from movielist.models import Movie
from .models import Cinema, Screening


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='movie-detail',
    )

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'city', 'movies']
        depth = 1




class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Cinema.objects.all()
    )

    movie = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Movie.objects.all()
    )

    class Meta:
        model = Screening
        fields = ('movie', 'cinema', 'date')