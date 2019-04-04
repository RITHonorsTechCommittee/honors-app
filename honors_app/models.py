from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=256)
    leaders = models.ManyToManyField(User, related_name='leader_of')
    members = models.ManyToManyField(User, related_name='member_of')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attendees = models.ManyToManyField(User, blank=True)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, blank=True)
    private = models.BooleanField()

    def __str__(self):
        return self.name
