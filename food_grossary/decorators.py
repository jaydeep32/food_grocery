from django.shortcuts import redirect, render
from django.urls import reverse


def login_redirect(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        to_go = request.get_full_path()
        if request.user.is_authenticated:
            return func(*args, **kwargs)
        return redirect('users:login')
        # return reverse(f"//127.0.0.1:8000/users/login/?go_next={to_go}/")
    return wrapper


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('users:login')


class AntiLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('product:home')

