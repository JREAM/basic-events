from django.conf.urls import url

from .views import (
    listing,
    listing_single,
    listing_create,
    listing_edit,
)

urlpatterns = [
    url(r'listing/$', listing, name='listing'),
    url(r'listing/(?P<slug>[\w-]+)/&', listing_single, name="listing-single"),
    url(r'listing/create', listing_create, name='listing-create')
    url(r'listing/edit', listing_edit, name='listing-edit),
]
