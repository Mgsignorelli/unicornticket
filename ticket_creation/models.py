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
    description = models.TextField(max_length=250, default='0000000')
    creator = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)
