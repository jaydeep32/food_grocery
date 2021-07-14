from django.shortcuts import render, redirect
from order.forms import Chceckout
from food_grossary.decorators import login_redirect

@login_redirect
def checkout_form(request):
    context = {
        'form': Chceckout,
    }
    return render(request, 'order/order_confirm.html', context)


@login_redirect
def confirm_order(request):
    if request.method == 'POST':
        form = Chceckout(request.POST)
        if form.is_valid():
            context = {
                'data': form.cleaned_data.items(),
            }
            return render(request, 'order/shipping_form.html', context)
    else:
        return redirect('product:home')



