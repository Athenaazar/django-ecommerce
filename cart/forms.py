from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9, initial=1, widget=forms.NumberInput(
        attrs={'class': 'input-number', 'data-min': 1, 'data-max': 9}))
