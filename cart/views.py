from django.shortcuts import render
from random import randint
from django.views.generic import TemplateView
from food_grossary.decorators import login_redirect, LoginRequiredMixin


class AddCartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart_detail.html'

    def get(self, request, food=None, *args, **kwargs):
        self.d = request.session.get('foods')
        self.title = food.replace('-', ' ')
        return super().get(request, food, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['price'] = randint(40, 250)
        context['data'] = self.d.get(self.title)
        return context