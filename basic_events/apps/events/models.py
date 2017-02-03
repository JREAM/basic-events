from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel
)


class Ticket(TimeStampedModel):
    """
    Every event requires a ticket.
    Every event requires atleast one ticket type is available,
    meaning there are no gaps in time.
    """

    title = models.CharField(max_length=75)
    description = models.CharField(max_length=255)

    sale_starts_on = models.DateTimeField()
    sale_ends_on = models.DateTimeField()

    # Only 9999.99 max in USD for now..
    # For other currencies I'd probably add:
    #   currency: CharField() with a tuple possibly of available
    #       currencies set in settings
    #   price: integer field, would possibly need a validator
    #       for all the currencies
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        """Simple ordering."""

        ordering = ['title']
        verbose_name_plural = 'Tickets'

    def __unicode__(self):
        """Return the Title."""
        return self.title


class Event(TimeStampedModel, TitleSlugDescriptionModel):
    """
    The Events taking place which are intertwined with tickets.
    Tickets should not go on sale beyond the ends_on date.
    """

    title = models.CharField(max_length=125)
    description = models.TextField()

    starts_on = models.DateTimeField()
    ends_on = models.DateTimeField()

    tickets = models.ManyToManyField(Ticket)

    class Meta:
        """Simple ordering."""
        ordering = ['title']
        verbose_name_plural = 'Events'

#     def is_ticket_available(self, event):
#         if len(event.tickets) == 0:
#             # @TODO: Validation error
#             pass
