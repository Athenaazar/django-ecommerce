from django.shortcuts import render
from shop.models import Product, Category


def home(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False, is_featured=True)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'company/home.html', context)


def about(request):
    return render(request, 'company/about.html')



