from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Ticket(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Every event requires a ticket.
    Every event requires one ticket type to be on sale
    """
    title = models.CharField(max_length=75, unique=True)

    sale_starts_on = models.DateTimeField()
    sale_ends_on = models.DateTimeField()

    # Only 9999.99 max in USD for now..
    # For other currencies I'd probably add:
    #   currency: CharField() with a tuple possibly of available currencies set in settings
    #   price: integer field, would possibly need a validator for all the currencies
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['-sale_starts_on']
        verbose_name_plural = 'Tickets'

    def __unicode__(self):
        return self.title


class Event(TimeStampedModel, TitleSlugDescriptionModel):
    """
    """
    title = models.CharField(max_length=125)

    starts_on = models.DateTimeField()
    ends_on = models.DateTimeField()

    description = models.TextField()
    tickets = models.ManyToManyField(Ticket)

    is_cancelled = models.BooleanField(default=False)
    cancelled_description = models.TextField(null=True)

    class Meta:
        ordering = ['-starts_on']
        verbose_name_plural = 'Events'

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            self.add_error(self.start_date, 'The start date must come before end date.')
            # @TODO: Ill want to fix tihs
            raise('ERROR FIX HERE')

        super(Event, self).save(*args, **kwargs)


# @TODO: Probably make a separate user login area so this can be all legit,
# Then users will have their own listings, and signups, and keep count of things.
#class EventSignup(models.Model):
#    pass
#   event.. ticket qty... what ticket...
