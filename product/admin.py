from django.contrib import admin
from product.models import Product
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','slug','price','created_at', ]
    search_fields = ('=title',)

   

