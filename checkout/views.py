from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import  JsonResponse
import stripe
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request, order_id):
    order = get_object_or_404(Order, id=order_id, paid=False, user=request.user)
    if request.method == 'POST':
        print('Data:', request.POST)
        customer = stripe.Customer.create(
            email=order.billing_email_address,
            name=order.billing_name,
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=order.get_total_price() * 100,
            currency='usd',
            description="Paid"
        )
        return redirect(reverse('shop:shop'))
    else:
        return render(request, 'checkout/checkout.html')


@login_required
def create_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, paid=False, user=request.user)
    if request.method == 'POST':
        try:
            customer = stripe.Customer.create(
                email=order.billing_email_address,
                name=order.billing_name,
                source=request.POST['stripeToken'],
            )

            # Create a PaymentIntent with the order amount and currency
            # intent = stripe.PaymentIntent.create(
            #     customer=customer['id'],
            #     amount=int(order.get_total_price()) * 100,
            #     currency='usd',
            #     payment_method_types=["card"],
            #     metadata={"order_id": order.id},
            #
            # )
            # # return JsonResponse({
            # #     'clientSecret': intent['client_secret']
            # })

            charge = stripe.Charge.create(
                customer=customer,
                amount=int(order.get_total_price()) * 100,
                currency='usd',
                metadata={"order_id": order.id},
            )
            if charge:
                order.paid = True
                order.save()
                return redirect('shop:shop')
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return render(request, 'checkout/checkout.html')
