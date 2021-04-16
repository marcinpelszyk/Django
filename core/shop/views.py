from django.shortcuts import render

from .models import Category, Product



def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})








