from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .forms import CartAddForm
from shop.models import Product
from django.views.decorators.http import require_POST


def cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
    else:
        cart.add(product=product, quantity=1)
    return redirect('cart:cart')
