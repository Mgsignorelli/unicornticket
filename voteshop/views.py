from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from voteshop.helpers import get_order, create_order, check_order_fulfillment
from .forms import OrderForm
from django.conf import settings


# Buy votes views

@login_required()
def buyvotes(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = create_order(request, order_form.cleaned_data['votecount'])
            return render(request, "checkout.html",
                          {'session': order.stripe_session_id, 'publickey': settings.STRIPE_PUBLISHABLE})

        messages.error(request, "Select a total of votes to purchase")

    return render(request, 'buyvote.html')


@login_required()
def success(request, order_id):
    order = get_order(order_id, user=request.user)

    if check_order_fulfillment(order) == 'fulfilled':
        messages.success(request, "Purchase was successfull")
        return redirect(reverse('index'))

    messages.info(request, "Payment is pending, refresh")
    return render(request, 'success.html', {'status': 'pending'})


@login_required()
def fail(request):
    pass
