from django.contrib import admin

from .forms import EventForm, TicketForm
from .models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    search_fields = [
        'title',
        'starts_on',
        'ends_on',
        'tickets'
    ]

    list_display = [
        'title',
        'total_assigned_tickets',
        'starts_on',
    ]

    empty_value_display = '-empty-'

    def total_assigned_tickets(self, obj):
        return obj.tickets.count()


class TicketAdmin(admin.ModelAdmin):
    form = TicketForm
    search_fields = [
        'title',
        'sale_starts_on',
        'sale_ends_on',
        'price',
    ]

    list_display = [
        'title',
        'sale_starts_on',
        'sale_ends_on',
        'price'
    ]

    empty_value_display = '-empty-'

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)