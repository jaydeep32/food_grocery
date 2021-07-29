from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.AddCartView.as_view(), name='cart'),
    path('<int:pk>/<int:add>/', views.add_remove_cart, name='add-remove-cart'),
    path('cart/<str:slug>/', views.cart, name='add-cart'),
]
