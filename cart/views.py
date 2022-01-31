from django.shortcuts import render
from .cart import Cart


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
