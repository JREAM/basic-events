from django.contrib import admin

from .models import Event, Ticket


class EventAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'starts_on',
        'ends_on',
        'description',
        'tickets',
        'is_cancelled',
        'cancelled_description'
    )


class TicketAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'sale_starts_on',
        'sale_ends_on',
        'price',
        'is_assigne',
    )

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)