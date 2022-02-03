from django.shortcuts import render

from shop.models import Product


def home(request):
    products = Product.objects.filter(available=True)
    context = {
        'products' : products
    }
    return render(request, 'company/home.html')
