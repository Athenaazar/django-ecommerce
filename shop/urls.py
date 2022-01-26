from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product-details/', views.product, name='product'),
]
