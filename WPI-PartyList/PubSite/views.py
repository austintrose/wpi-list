from django.shortcuts import render

def permission_denied(request):
	""" View for 403 (Permission Denied) error """
	return render(request, '403.html', None)