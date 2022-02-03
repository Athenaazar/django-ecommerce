from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('pay/<order_id>/', views.create_payment, name='checkout'),
]
