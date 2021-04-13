from django.urls import path

from .views import CinemaListView, CinemaView, ScreeningView, ScreeningListView


urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('cinema/<int:pk>/', CinemaView.as_view(), name='cinema-detail'),
    path('screenings/', ScreeningListView.as_view(), name='screening-list'),
    path('screening/<int:pk>/', ScreeningView.as_view(), name='screening-detail'),
]