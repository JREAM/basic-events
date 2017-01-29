from __future__ import unicode_literals

from django.db import models
from django_extensions import TimeStampedModel



class Ticket(TimeStampedModel):
    """
    Every event requires a ticket.
    Every event requires one ticket type to be on sale
    """
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField()

    def has_sale(self):
        return False


class Event(TimeStampedModel):
    """
    The purpose of is_active is incase it were cancelled.
    """
    name = models.CharField(max_length=125)
    ticket = models.hasOne(Ticket)
    description = models.TextField()
    is_cancelled = models.BooleanField(default=False)
    cancelled_description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
