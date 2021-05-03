from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'store/category.html', {
        'category': category,
        'products': products,
        'page': page,
        'posts': posts,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)

    return render(request, 'store/single.html', {'product': product})






