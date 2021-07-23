from django.contrib import admin
from product.models import Product
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django import forms
from django.db import models
from cart.models import ProductInCart



# class ProductInCartInline(admin.TabularInline):
#     model = ProductInCart

# class ProductInCartInline(admin.StackedInline):
#     model = ProductInCart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = [('title', 'slug'), 'image', 'description', 'price']
    # readonly_fields = ['slug',]

    fieldsets = (
        ('Data', {
            'classes': ('wide', ),
            'fields': ('title', 'slug', 'description', 'price'),
        }),
        ('Media', {
            'classes': ('collapse', 'wide', ),
            'fields': ('image', ),
        })
    )   

    # formfield_overrides = {
    #     models.CharField: {'widget': forms.Textarea} 
    # }

    # inlines = [ProductInCartInline, ]
    prepopulated_fields = {
        'slug': ['title'],
    }

    save_on_top = True
    save_as = True
    # view_on_site = False

    list_display = ['title', 'slug', '__str__', 'price', 'created_at', ]
    search_fields = ('title__startswith',)
    list_display_links = ['title', 'slug']
    # list_display_links = None
    list_per_page = 15


