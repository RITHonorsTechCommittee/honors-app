from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('event/<int:pk>/', views.event_details, name='event-detail'),
    path('accounts/login/', views.login),
    path('events/', views.events_overview, name='events'),
    path('events/<int:pk>/', views.event_view, name='event-view'),
]
