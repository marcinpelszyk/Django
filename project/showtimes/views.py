from datetime import timedelta

import django_filters
from django.shortcuts import render
from django.utils import timezone

from .models import Cinema, Screening
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CinemaSerializer, ScreeningSerializer
from rest_framework import generics




class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


    # def get_queryset(self):
    #     startdate = timezone.now()
    #     enddate = startdate + timedelta(days=30)
    #     return Screening.objects.filter(date__gtl=enddate)


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListAPIView):
    serializer_class = ScreeningSerializer

    def get_queryset(self):
        startdate = timezone.now()
        enddate = startdate + timedelta(days=30)
        return Screening.objects.filter(date__gte=enddate)


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
