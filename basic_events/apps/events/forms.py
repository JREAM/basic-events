from django.forms import ModelForm
from django.core import validators

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

    # def clean_sale_starts_on(self):
        # sale_starts_on = self.cleaned_data['sale_starts_on']
        # sale_ends_on = self.cleaned_data['sale_ends_on']
        # if sale_ends_on > sale_starts_on:
        #     ValidationError(_('Starts On must be before the end date '), code='invalid')



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

    def clean_sale_starts_on(self):
        starts_on = self.cleaned_data['starts_on']
        ends_on = self.cleaned_data['ends_on']
        if ends_on > starts_on:
            ValidationError(_('Starts On must be before the end date '), code='invalid')

