from django.conf.urls import url

from .views import (
    event_list,
    event,
    create,
    edit,
)

urlpatterns = [
    url(r'^$', event_list, name='event_list'),
    url(r'event/(?P<slug>[\w-]+)/$', event, name="event"),
    url(r'event/create', create, name='event-create')
    url(r'event/edit/(?P<slug>[\w-]+)/$', edit, name='event-edit),
]
