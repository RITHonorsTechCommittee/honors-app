from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage),
    path('accounts/login/', views.login),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('phome/', views.protectedHomepage),
]
