from django.conf.urls import url

from .views import (
    event_list,
    event,
    create,
    edit,
    delete,
)

urlpatterns = [
    url(r'all$', event_list, name='event-list'),
    url(r'create/$', create, name='event-create'),
    url(r'edit/(?P<id>\d+)/$', edit, name='event-edit'),
    url(r'delete/(?P<id>\d+)/$', delete, name='event-delete'),

    # Keep this at the bottom so slugs create/edit/delete come first,
    # in the real world I might prefix this with /e/<slug>
    url(r'(?P<slug>[\w-]+)/$', event, name="event"),
]
