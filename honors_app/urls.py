from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('event/<int:pk>/', views.event_details, name='event-detail'),
    path('accounts/login/', views.login),
    path('phome/', views.protectedHomepage),
]
