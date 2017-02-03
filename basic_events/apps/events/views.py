from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from .models import Event, Ticket
from .forms import TicketForm, ModelForm

"""
The Create/Edit/Delete would likely be locked down to a
user_auth system with group/role permissions as a event creator
or regular member perhaps.. I'd probably toss on some decorators
if I set that up.
"""


def event_list(request):
    """
    The list of all events
    """
    paginator = Paginator(Event.objects.all(), 20)
    page = request.GET.get('page')

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {
        'events': events
    }

    return render(request, 'event_list.html', context)


def event(request, slug):
    """
    The single event view by slug-name
    """
    context = {
        'events': Event.objects.get(slug=slug)
    }
    return render(request, 'event.html', context)


def create(request):
    """
    Creates an Event
    """
    if request.method == 'POST':
        result = Event.objects.create(
            title=request.POST['title'],
            starts_on=request.POST['starts_on'],
            ends_on=request.POST['ends_on'],
            description=request.POST['description'],
            # tickets=
        )

        messages.success(request, 'The event "%s" has been created.' % request.POST['title'])
        return redirect('event', slug=result.slug)

    context = {
        'form': EventForm()
    }

    # if request post ...
    # f = CreateEventForm(PostDataHereDogg)
    # Or do ajax, I dunno, whipping it together in vim rite quick
    return render(request, 'create.html', context)


def edit(request, id):
    """
    Edits an Event
    """

    try:
        event = Event.objects.get(pk=id),
    except event.DoesNotExist:
        raise Exception('Event Object Does Not Exist pk=%s' % id)

    try:
        form = TicketForm(pk=id)
    except Exception:
        raise Exception('Could not load TicketForm pk=%s' % id)

    context = {
        'event': event,
        # 'ticket': Ticket.objects.get(pk=id),
        'form': form
    }

    return render(request, 'edit.html', context)


def delete(request, id):
    """
    Deletes an Event

    Tickets could possibly be associated with OTHER Events,
        in this case I won't delete them.

    Q: What if people bought tickets?

    :param: result -1 Does Not Exist
                    0 Exists/Undeleted
                    1 Deleted
    """

    try:
        event = Event.objects.get(pk=id),
        result = 0
    except Event.DoesNotExist:
        event = 'Item does not exist.'
        result = -1

    context = {
        'event': event,
        'result': result
    }

    if request.method == 'POST':
        if request.method.GET['confirm'] == 1:
            # Integer if success.
            messages.success(request, 'The event "%s" has been deleted.' % event.title)
            context['result'] = event.delete()

    return render(request, 'delete.html', context)
