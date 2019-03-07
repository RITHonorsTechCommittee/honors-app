from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
]