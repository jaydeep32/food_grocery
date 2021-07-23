from django.contrib import admin, messages
from cart.models import ProductInCart, Cart
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'qty', 'ordered', 'total', 'product_in', ]
    list_editable = ['ordered', ]

    # fieldsets = (
    #     (None, {
    #         'classes': ['wide', ],
    #         'fields': ['user', 'qty', 'ordered', ],
    #     }),
    # )

    radio_fields = {
        'user': admin.VERTICAL,
    }
    # raw_id_fields = ['user', ]

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
    # total.admin_order_field = 'total'
    product_in.short_description = "In Cart"
    product_in.admin_order_field = 'product'




@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'created_at', '__str__', ]

    filter_horizontal = ['product']
    
    def make_ordered(_, request, qs):
        for cart in qs:
            cart.ordered = not cart.ordered
            cart.save()
        # qs.update(ordered=True)
        messages.success(request, "Item ordered staus has changed..")

    # admin.site.add_action(make_ordered, "Toggle order status")
    actions = [make_ordered, ]









