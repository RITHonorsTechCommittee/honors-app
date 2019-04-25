from django import forms
from django.forms.widgets import DateTimeInput
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'description', 'organization', 'start_time', 'end_time', 'private')
        widgets = {
            'start_time': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
