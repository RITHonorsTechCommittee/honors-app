from django.shortcuts import render
from django.views import generic

from .models import Event, Organization


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login_oauth.html')

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'
