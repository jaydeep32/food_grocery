from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.AddCartView.as_view(), name='cart'),
    path('<str:slug>/', views.cart, name='add-cart'),
]
