from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Event, Organization


def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login_oauth.html')

@login_required()
def protectedHomepage(request):
    return render(request, 'homepage.html')

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'
