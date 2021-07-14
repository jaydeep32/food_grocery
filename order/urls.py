from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('checkout/', views.checkout_form, name='checkout'),
    path('confirm/', views.confirm_order, name='confirm-order'),
]




