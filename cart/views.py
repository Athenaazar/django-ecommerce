from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .forms import CartAddForm
from shop.models import Product
from django.views.decorators.http import require_POST


def cart(request):
    cart = Cart(request)
    form = CartAddForm()
    return render(request, 'cart/cart.html', {'cart': cart, 'form': form})


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


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def cart_update(request):
    if is_ajax(request=request) and request.POST and 'attr_id' in request.POST:
        cart = Cart(request)
        print('hekeeooe')
        product = get_object_or_404(Product, id=int(request.POST['attr_id']))
        cart.update(product=product, quantity=int(request.POST['quantity']))
    else:
        print("No Product is Found")
    return redirect('cart:cart')
