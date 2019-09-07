import stripe
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from UnicornTicketSystem import settings
from UnicornTicketSystem.helpers import calculate_cost
from tickets.models import FeatureVote
from voteshop.models import Order

stripe.api_key = settings.STRIPE_SECRET


def get_order(order_id, user):
    return get_object_or_404(Order, pk=order_id, buyer_id__exact=user.id)


def create_order(request, total):
    order = Order()
    order.buyer = request.user
    order.created = now()
    order.total = total
    order.save()

    session = stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=[{
            "name": str(total) + " feature votes",
            "description": "Allows a user to vote for a feature for development",
            "amount": calculate_cost(total),
            "currency": "gbp",
            "quantity": 1
        }],
        success_url=request.build_absolute_uri(reverse('success', args=[order.id])),
        cancel_url=request.build_absolute_uri(reverse('fail', args=[order.id])),
    )

    order.stripe_session_id = session.id
    order.save()

    return order


def check_order_fulfillment(order):
    if order.paid is not None:
        return 'fulfilled'

    session = stripe.checkout.Session.retrieve(id=order.stripe_session_id)

    if session.payment_intent:
        payment = stripe.PaymentIntent.retrieve(id=session.payment_intent)

        if payment.status == 'canceled':
            return 'canceled'

        if payment.status == 'succeeded':
            order.paid = now()
            order.save()

            votes = []

            for i in range(order.total):
                votes.append(FeatureVote(voter=order.buyer, order=order))

            FeatureVote.objects.bulk_create(votes)

            return 'fulfilled'

    return 'pending'
