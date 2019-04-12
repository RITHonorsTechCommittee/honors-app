from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Event, Organization
from .forms import EventForm


def homepage(request):
    return render(request, 'homepage.html')


def event_details(request, pk):
    if request.method == 'POST':
        form = EventForm(request.POST, instance=get_object_or_404(Event, pk=pk))
        if form.is_valid():
            #TODO: add check for sequence, user permsissions
            form.save()
            return HttpResponseRedirect(request.path)

    else:
        if pk == 'new':
            form = EventForm()
        else:
            form = EventForm(instance=get_object_or_404(Event, pk=pk))

    return render(request, 'event_detail.html', {'form': form})


def login(request):
    return render(request, 'login_oauth.html')


@login_required()
def protectedHomepage(request):
    return HttpResponse('Access granted!', status=200)

