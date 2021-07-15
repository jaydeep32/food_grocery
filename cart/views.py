from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from food_grossary.decorators import LoginRequiredMixin
from product.models import Product
from cart.models import Cart, ProductInCart


class AddCartView(LoginRequiredMixin, ListView):
    template_name = 'cart/cart_list.html'
    context_object_name = 'carts'

    def get_queryset(self):
        try:
            self.cart = Cart.objects.get(user=self.request.user, ordered=False)
        except:
            self.cart = None
        queryset = self.cart.product.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['gross_total'] = self.cart.gross_total
        return context


def add_qty(product):
    product.qty += 1
    return product


def cart(request, slug):
    product = Product.objects.get(slug=slug)
    product_in_cart, created = ProductInCart.objects.get_or_create(user=request.user, product=product)
    product_in_cart.qty += 1
    product_in_cart.save()
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.product.add(product_in_cart)
    return redirect('product:home')