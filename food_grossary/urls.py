from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls'), name='product'),
    path('cart/', include('cart.urls'), name='cart'),
    path('order/', include('order.urls'), name='order'),
    path('users/', include('users.urls'), name='users'),
]
