from django.contrib import admin
from cart.models import ProductInCart, Cart
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'qty', 'ordered', 'total', 'product_in', ]

    def total(self, obj):
        return obj.product_wise_total

    def product_in(self, obj):
        url = (
            reverse("admin:product_product_changelist")
            + "?"
            + urlencode({"id": f"{obj.product.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.product)


    total.short_description = "Total"
    product_in.short_description = "In Cart"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'created_at', ]






