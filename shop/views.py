from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Manufacturer
from django.urls import resolve


def shop(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    manufacturer = Manufacturer.objects.all()
    if slug:
        url_name = resolve(request.path).url_name
        if url_name == 'category_filter':
            category = get_object_or_404(Category, slug=slug)
            products = products.filter(category=category)
        elif url_name == 'manufacturer_filter':
            manufacture = get_object_or_404(Manufacturer, slug=slug)
            products = products.filter(manufacturer=manufacture)
    context = {
        'products': products,
        'categories': categories,
        'manufacturer': manufacturer,
    }
    return render(request, 'shop/shop.html', context)


def product(request):
    return render(request, 'shop/product-details.html')
