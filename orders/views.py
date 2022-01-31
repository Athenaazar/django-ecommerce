from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart

from .forms import CouponForm
from .models import Order, OrderItem


def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect('orders:detail', order.id)


def detail(request, order_id):
    form = CouponForm()
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {'order': order, 'form': form})
