from __future__ import unicode_literals

from datetime import datetime, timedelta
from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel
)


# class SimpleValidator():
#     """
#     This is a validator for the admin, and frontend for the Ticket and
#     Event models. Do NOT add any variables, we don't need or want a migration
#     for this class.
#     """

#     def is_ticket_available(self, event):
#         if len(event.tickets) == 0:
#             # @TODO: Validation error
#             pass

#     def check_ticket_gap(self, event):
#         """
#         Ensure there is atleast one ticket on sale for an event
#         """
#         expected_next_date = False

#         for t in event.tickets:
#             sale_on = datetime.strptime(t.sale_starts_on, "%m/%d/%y")

#             """ Check for the next day of sale"""
#             if expected_next_date and sale_on != expected_next_date:
#                 # @TODO: Validation error
#                 pass
#             expected_next_date = sale_on + timedelta(days=1)

#     def date_misaligned(self, event, ticket_objects):
#         """
#         It's okay for a ticket to sell before event starts_on
#         """
#         for t in ticket_objects:
#             if t.sale_ends_on > event.ends_on:
#                 # @TODO: Validation error
#                 pass

#     def clean(self, *args, **kwargs):
#         # @TODO Call some functions here based on the model type
#         super(SimpleValidator, self).clean(*args, **kwargs)

#     def save(self, *args, **kwargs):
#         self.full_clean()
#         super(SimpleValidator, self).save(*args, **kwargs)


class Ticket(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Every event requires a ticket.
    Every event requires atleast one ticket type is available,
    meaning there are no gaps in time.
    """

    title = models.CharField(max_length=75, unique=True)

    sale_starts_on = models.DateTimeField()
    sale_ends_on = models.DateTimeField()

    # Only 9999.99 max in USD for now..
    # For other currencies I'd probably add:
    #   currency: CharField() with a tuple possibly of available
    #       currencies set in settings
    #   price: integer field, would possibly need a validator
    #       for all the currencies
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        """Simple ordering."""

        ordering = ['-sale_starts_on']
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

    starts_on = models.DateTimeField()
    ends_on = models.DateTimeField()

    description = models.TextField()

    # @TODO With NO tickest the event will NOT appear in the view
    tickets = models.ManyToManyField(Ticket)

    class Meta:
        """Simple ordering."""
        ordering = ['-starts_on']
        verbose_name_plural = 'Events'

    def save(self, *args, **kwargs):
        if self.starts_on > self.ends_on:
            #self.add_error(self.start_date, 'The start date must come before end date.')
            # @TODO: Ill want to fix tihs
            #raise('ERROR FIX HERE')
            pass

        super(Event, self).save(*args, **kwargs)
