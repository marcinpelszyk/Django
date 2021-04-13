from django.contrib import admin
from .models import Recipe, Plan, RecipePlan, Page

admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(RecipePlan)
admin.site.register(Page)

