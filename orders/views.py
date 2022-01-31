from django.shortcuts import render, redirect


def order_create(request):
    return redirect('orders:detail')
