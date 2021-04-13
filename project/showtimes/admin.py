from django.contrib import admin
from .models import Cinema, Screening


from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from .models import Cinema, Screening




@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    list_filter = ('name', 'city')
    search_fields = ('name', 'city')




@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema')
    list_filter = ('movie', 'cinema')


