from django.shortcuts import redirect, render
from users.forms import Login, Register
from django.views.generic import View
from food_grossary.decorators import AntiLoginRequiredMixin, login_redirect


# class LoginView(AntiLoginRequiredMixin, View):
#     def get(self, request):
#         form = Login(request.POST or None)
#         context = {
#             'form': form,
#         }
#         return render(request, 'users/login.html', context)

#     def post(self, request, go_next=None):
#         form = Login(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             if request.session.get('username') == username:
#                 request.session['login'] = True
#                 if go_next:
#                     return redirect(go_next)
#                 else:
#                     return redirect('product:home')
#             else:
#                 return redirect('users:register')
#         return render(request, 'users/login.html', {'form': form})


class RegisterView(AntiLoginRequiredMixin, View):
    def get(self, request):
        form = Register(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = Register(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form, })

