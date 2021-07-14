from food_grossary.decorators import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from product.models import Product


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'


class ProductDetail(LoginRequiredMixin, DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'


