from django.db import models
from product.models import Product
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # product = models.ManyToManyField(ProductInCart, related_name='productincart')
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def gross_total(self):
        return sum([product.product_wise_total for product in self.products_incart.all()])

    def __str__(self):
        return self.user.username


class ProductInCart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products_incart', null=True, blank=True)
    qty = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)

    @property
    def product_wise_total(self):
        return self.product.price * self.qty

    def __str__(self):
        return self.product.title

