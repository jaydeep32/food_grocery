from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from food_grossary.decorators import LoginRequiredMixin
from product.models import Product
from cart.models import Cart, ProductInCart


class AddCartView(LoginRequiredMixin, ListView):
    template_name = 'cart/cart_list.html'
    context_object_name = 'carts'

    def get_queryset(self):
        self.cart = Cart.objects.filter(user=self.request.user, ordered=False).first()
        if self.cart:
            queryset = self.cart.products_incart.all()
            return queryset
        return None

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['gross_total'] = self.cart.gross_total if self.cart else 0
        return context


def cart(request, slug):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(slug=slug)
    product_in_cart, created = ProductInCart.objects.get_or_create(cart=cart, product=product)
    product_in_cart.qty += 1
    product_in_cart.cart = cart
    product_in_cart.save()
    return redirect('product:home')


def add_remove_cart(request, pk, add=True):
    product_in_cart = ProductInCart.objects.filter(cart__user=request.user, ordered=False, pk=pk).first()
    if add:
        product_in_cart.qty += 1
        product_in_cart.save()
    else:
        product_in_cart.qty -= 1
        product_in_cart.save()
        if product_in_cart.qty < 1:
            product_in_cart.delete()
    return redirect('cart:cart')


