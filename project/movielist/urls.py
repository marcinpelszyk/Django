from django.urls import path

from .views import MovieListView, MovieView

app_name = 'movielist'
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieView.as_view(), name='movie-detail'),
]