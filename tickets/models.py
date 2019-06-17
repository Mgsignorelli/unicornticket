from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

    class Meta:
        abstract = True


class Bug(Ticket):
    pass


class Feature(Ticket):
    pass


class Vote(models.Model):
    class Meta:
        abstract = True


class BugVote(Vote):
    bug = models.ForeignKey(Bug)
    voter = models.ForeignKey(User)


class FeatureVote(Vote):
    feature = models.ForeignKey(Feature)
    voter = models.ForeignKey(User)
