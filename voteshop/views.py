from django.http import HttpResponse
from django.utils import timezone

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from voteshop.helpers import calculateCost
from .forms import OrderForm
from .models import Order
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    # if request.method == "POST":
    #     order_form = OrderForm(request.POST)
    #     if order_form.is_valid():
    #         order = order_form.save(commit=False)
    #         order.date = timezone.now()
    #         order.save()
    # try:
    #     customer = stripe.Charge.create(
    #         amount=int(total * 100),
    #         currency="EUR",
    #         description=request.user.email,
    #         card=payment_form.cleaned_data['stripe_id'],
    #     )
    #     if customer.paid:
    #         messages.error(request, "You have successfully paid")
    #         request.session['cart'] = {}
    #         return redirect(reverse('products'))

    if request.method != "POST":
        messages.error(request, 'Error processing checkout')
        return redirect(reverse(buyvotes))


def buyvotes(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            session = stripe.checkout.Session.create(
                customer_email=request.user.email,
                payment_method_types=['card'],
                line_items=[{
                    "name": str(order_form.cleaned_data['votecount']) + " Feature Votes",
                    "description": "Allows a user to vote on a Feature for development",
                    "amount": calculateCost(order_form.cleaned_data['votecount']),
                    "currency": "gbp",
                    "quantity": 1

                }],
                success_url=request.build_absolute_uri(reverse('success')),
                cancel_url=request.build_absolute_uri(reverse('fail')),
            )
            return render(request, "checkout.html", {'session': session.id, 'publickey': settings.STRIPE_PUBLISHABLE})

        messages.error(request, "Select a total of votes to purchase")

    return render(request, 'buyvote.html')


def success(request):
    pass


def fail(request):
    pass
