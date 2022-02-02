from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    # if request.method == 'POST':
    #     print('Data:', request.POST)
    #     print(shipping_form.cleaned_data['billing_name'])
    #
    #     amount = int(request.POST['amount'])
    #
    #     customer = stripe.Customer.create(
    #         email=request.POST['email'],
    #         name=request.POST['name'],
    #         source=request.POST['stripeToken']
    #     )
    #
    #     charge = stripe.Charge.create(
    #         customer=customer,
    #         amount=amount * 100,
    #         currency='usd',
    #         description="Donation"
    #     )
    #     return redirect(reverse('shop:shop'))
    # else:

    return render(request, 'checkout/checkout.html')
