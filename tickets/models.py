from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from voteshop.models import Order


class Ticket(models.Model):
    """Ticket model"""

    STATUS_CHOICES = (
        ('todo', 'Todo'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description = models.TextField(max_length=250, default='')
    creator = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)

    # comments = models.CharField(max_length=250)

    class Meta:
        abstract = True


class Bug(Ticket):
    pass


class Feature(Ticket):
    pass


class TicketWork(models.Model):
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class BugWork(TicketWork):
    bug = models.ForeignKey(Bug)


class FeatureWork(TicketWork):
    feature = models.ForeignKey(Feature)


class Vote(models.Model):
    class Meta:
        abstract = True


class BugVote(Vote):
    bug = models.ForeignKey(Bug)
    voter = models.ForeignKey(User)


class FeatureVote(Vote):
    feature = models.ForeignKey(Feature, blank=True, null=True)
    voter = models.ForeignKey(User)
    order = models.ForeignKey(Order, blank=True, null=True)


class Comment(models.Model):
    commenter = models.ForeignKey(User)
    content = models.TextField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BugComment(Comment):
    bug = models.ForeignKey(Bug)


class FeatureComment(Comment):
    feature = models.ForeignKey(Feature)
