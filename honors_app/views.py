from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Event, Organization
from .forms import EventForm


def homepage(request):
    return render(request, 'homepage.html')


def event_edit(request, pk):
    if request.method == 'POST':
        if pk != 'new':
            form = EventForm(request.POST, instance=get_object_or_404(Event, pk=pk))
        else:
            form = EventForm(request.POST)
        if form.is_valid():
            #TODO: add check for sequence, user permsissions
            event = form.save()
            return HttpResponseRedirect(reverse('event-view', args=[event.pk]))
        else:
            return HttpResponseBadRequest()

    else:
        if pk == 'new':
            instance = None
            form = EventForm()
        else:
            instance = get_object_or_404(Event, pk=pk)
            form = EventForm(instance=instance)

    return render(request, 'event_edit.html', {'form': form, 'instance': instance})

def login(request):
    return render(request, 'login_oauth.html')

def events_overview(request):
    user_orgs = Organization.objects.filter(members__in=[request.user])   
    user_org_events = {}
    for org in user_orgs: 
        user_org_events[org] = Event.objects.filter(organization__pk__exact=org.pk)

    context = {}
    context['user_org_events'] = user_org_events
    return render(request, 'events_overview.html', context)   

def event_view(request,pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event_view.html', {'event':event}) 
