from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    paid = models.DateTimeField()
    buyer = models.ForeignKey(User)
    created = models.DateTimeField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.created, self.buyer)

