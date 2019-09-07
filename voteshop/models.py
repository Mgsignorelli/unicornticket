from django.contrib.auth.models import User
from django.db import models

from UnicornTicketSystem.helpers import calculate_cost


class Order(models.Model):
    paid = models.DateTimeField(null=True, default=None)
    buyer = models.ForeignKey(User)
    created = models.DateTimeField()
    total = models.PositiveIntegerField()
    stripe_session_id = models.TextField(null=True, default=None)

    @property
    def cost(self):
        return "£%.2f" % (calculate_cost(self.total) / 100)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.created, self.buyer.id)
