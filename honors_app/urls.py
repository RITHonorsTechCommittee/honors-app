from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

# Handle URLs for the HealthNet application specifically
urlpatterns = [
	url('^', include('django.contrib.auth.urls')),  # Includes Django default URLs
	url(r'^$', views.homepage, name='homePage'),
	url(r'^loginUser/$', views.user_login, name='userLogin'),
	url(r'^logoutUser/$', views.user_logout, name='userLogout'),
]
