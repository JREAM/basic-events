from django.shortcuts import render
from .models import Event
from .forms import TicketForm, ModelForm

def event_list(request):
    """
    """
    context = {
        'events': Event.objects.all()
    }

    return render(request, 'event_list.html', context)


def event(request, slug):
    """
    """
    context = {
        'events': Event.objects.get(slug=slug)
    }
    return render(request, 'event.html', context)


def create(request):
    """
    """
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST['title'],
            starts_on=request.POST['starts_on'],
            ends_on=request.POST['ends_on'],
            description=request.POST['description'],
            # tickets=
        )

    context = {
        'form': TicketForm()
    }

    # if request post ...
    # f = CreateEventForm(PostDataHereDogg)
    # Or do ajax, I dunno, whipping it together in vim rite quick
    return render(request, 'create.html', context)


def edit(request, slug):
    """
    """

    context = {
        'form': TicketForm(slug=slug)
    }

    return render(request, 'edit.html', context)
