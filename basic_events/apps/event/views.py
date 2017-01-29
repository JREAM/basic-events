from django.shortcuts import render
from .forms import CreateForm


def listing(request):
    """
    """
    return render(request, 'listing.html', {})


def listing_single(request):
    """
    """
    return render(request, 'listing_single.html', {})


def listing_create(request):
    """
    """

    # if request post ...
    # f = CreateEventForm(PostDataHereDogg)
    # Or do ajax, I dunno, whipping it together in vim rite quick
    return render(request, 'create.html', {})


def listing_edit(request, slug):
    """
    """
    return render(request, 'edit.html', {})
