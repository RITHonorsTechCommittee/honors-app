from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('events/<pk>/edit/', views.event_edit, name='event-edit'),
    path('accounts/login/', views.login, name='login'),
    path('events/', views.events_overview, name='events'),
    path('events/<pk>/', views.event_view, name='event-view'),
]
