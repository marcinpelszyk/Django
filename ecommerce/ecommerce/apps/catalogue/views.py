from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .models import Category, Product, ProductImage


def product_all(request):
    products = Product.objects.prefetch_related('product_image').filter(is_active=True)
    return render(request, 'catalogue/index.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True)
        )
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    return render(request, 'catalogue/category.html', {
        'category': category,
        'products': products,
        'page': page,
        'product': product,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    return render(request, 'catalogue/single.html', {'product': product})






