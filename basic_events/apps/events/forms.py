from datetime import datetime, timedelta

from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Event, Ticket


class TicketForm(ModelForm):
    """
    Share the TicketForm for front/backend validations
    """
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'sale_starts_on',
            'sale_ends_on',
            'price',
        ]

    def clean_sale_starts_on(self):
        """
        The start date must be before the end date
        """
        sale_starts_on = self.cleaned_data['sale_starts_on']
        sale_ends_on = self.cleaned_data['sale_ends_on']
        if sale_ends_on > sale_starts_on:
            ValidationError("Starts On must be before the end date")

        return sale_starts_on

    def __str__(self):
        return self.title


class EventForm(ModelForm):
    """
    Share the EventForm for front/backend validations
    """
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'starts_on',
            'ends_on',
            'tickets',
        ]

    def clean_starts_on(self):
        starts_on = self.cleaned_data['starts_on']
        ends_on = self.cleaned_data['ends_on']
        if ends_on > starts_on:
            ValidationError('Starts On must be before the end date ')

        return starts_on

    def clean_tickets(self):
        """
        Prevent Gaps in Dates
        """
        tickets = self.cleaned_data['tickets']
        event_ends_on = self.cleaned_data['event_ends_on']

        expected_next_date = False

        for t in tickets:
            sale_on = datetime.strptime(t.sale_starts_on, "%m/%d/%y")

            # 1: Check for Gaps in the next day of sale
            if expected_next_date and sale_on != expected_next_date:
                ValidationError('The date should be %s' % expected_next_date)

            expected_next_date = sale_on + timedelta(days=1)

            # 2: Tickets can sell before an Event, not after
            if t.sale_ends_on > event_ends_on:
                ValidationError('\
                    The ticket cannot end after the\
                    event on %s' % event_ends_on)

    def __str__(self):
        return self.title
