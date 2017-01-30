from django.shortcuts import render
from .forms import CreateForm


def event_list(request):
    """
    """
    return render(request, 'event_list.html', {})


def event(request):
    """
    """
    return render(request, 'event.html', {})


def create(request):
    """
    """

    # if request post ...
    # f = CreateEventForm(PostDataHereDogg)
    # Or do ajax, I dunno, whipping it together in vim rite quick
    return render(request, 'create.html', {})


def edit(request, slug):
    """
    """
    return render(request, 'edit.html', {})
