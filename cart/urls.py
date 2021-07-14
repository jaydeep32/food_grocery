from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('<str:food>/', views.AddCartView.as_view(), name='add-cart'),
]