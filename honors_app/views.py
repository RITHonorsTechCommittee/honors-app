

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.exceptions import PermissionDenied, SuspiciousOperation

# Create your views here.

def homepage(request):
    return render(request, 'login.html')
	
def user_login(request):
	"""Login function to log the user into website; This is present on all pages unless already logged in."""
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		# Validate username/password using Django's systems
		from django_auth_ldap.backend import LDAPBackend

		ldap_user = LDAPBackend().populate_user(username)
		user = LDAPBackend().authenticate_ldap_user(ldap_user, password)
		# If user exists, then the next statement will be true
		if user:
			login(request, user)
			# Send information to logger regarding login.
			# Send user to homepage
			return render(request, 'status.html', context={'success': True})
		else:
			# Send user back to homepage w/ login failed notification
			# Also sends it to logger for storage.
			return render(request, 'status.html', context={'success': False})
	else:  # Shouldn't happen unless the HTML is incorrect or something tries to spoof login.
		return HttpResponse('Invalid login method')
		
# Logout system; requires the user to be logged in already to perform logout.
@login_required
def user_logout(request):
	# Log information, then log user out and redirect to homepage
	logger.info('{} logged out.'.format(request.user.email))
	logout(request)
	return HttpResponseRedirect(reverse('homePage'))