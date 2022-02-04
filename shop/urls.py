from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('search/', views.search, name='search'),
    path('category/<slug:slug>/', views.shop, name='category_filter'),
    path('manufacturer/<slug:slug>/', views.shop, name='manufacturer_filter'),
    path('product_details/<slug:slug>/', views.product_details, name='product'),
    path('review/<slug:slug>/', views.add_review, name='review'),
    path('wishlist/', views.liked, name='liked'),
    path('add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),  # For add to wishlist
]
