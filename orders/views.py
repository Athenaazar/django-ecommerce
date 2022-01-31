from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart

from .forms import CouponForm
from .models import Order, OrderItem, Coupon


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
    price_dis = order.get_total_without_discount() - order.get_total_price()
    return render(request, 'orders/order.html', {'order': order, 'price_dis': price_dis, 'form': form})


def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
        except Coupon.DoesNotExist:
            return redirect('orders:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
    return redirect('orders:detail', order_id)
