from django.forms import ModelForm
from .models import Event, Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'sale_starts_on',
            'sale_ends_on',
            'price',
        ]


class EventForm(ModelForm):
     class Meta:
        model = Event
        fields = [
            'title',
            'starts_on',
            'ends_on',
            'description',
            'tickets'
        ]