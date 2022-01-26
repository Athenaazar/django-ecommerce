from django.shortcuts import render


def shop(request):
    return render(request, 'shop/shop.html')


def product(request):
    return render(request, 'shop/product-details.html')
