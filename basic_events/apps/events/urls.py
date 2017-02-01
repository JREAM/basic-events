from django.conf.urls import url

from .views import (
    event_list,
    event,
    create,
    edit,
)

urlpatterns = [
    url(r'all$', event_list, name='event-list'),
    url(r'(?P<slug>[\w-]+)/$', event, name="event"),
    url(r'create', create, name='event-create'),
    url(r'edit/(?P<slug>[\w-]+)/$', edit, name='event-edit')
]
