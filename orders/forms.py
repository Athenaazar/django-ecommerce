from django import forms

from .models import Order


class CouponForm(forms.Form):
    code = forms.CharField()


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('billing_name', 'billing_address', 'billing_email_address', 'billing_city', 'billing_country',
                  'billing_post_code')
