from django.db import models
from enum import Enum
from django.utils.text import slugify


class Recipe(models.Model):

    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.PositiveIntegerField(default=0)
    votes = models.IntegerField(default=0)
    preparation_description = models.TextField()


class Plan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')


class DayName(Enum):
    MONDAY = 'Poniedziałek'
    TUESDAY = 'Wtorek'
    WEDNESDAY = 'Środa'
    THURSDAY = 'Czwartek'
    FRIDAY = 'Piątek'
    SATURDAY = 'Sobota'
    SUNDAY = 'Niedziela'


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=32)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name="recipe_from_plan")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan')
    order = models.PositiveIntegerField()
    day_name = models.CharField(choices=[(tag.name, tag.value) for tag in DayName], max_length=16)


class Page(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        return self.slug

