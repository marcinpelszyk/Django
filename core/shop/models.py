from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
         related_name='products')
    created_by = models.ForeignKey(
        User, 
        related_name='product_create',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255, default='admin')
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("shop:product_detail", args=[self.pk, self.slug])


    
    




