from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movielist.urls')),
    path('cinema/', include('showtimes.urls')),
]