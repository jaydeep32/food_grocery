from django.contrib import admin
from cart.models import ProductInCart, Cart

@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass




