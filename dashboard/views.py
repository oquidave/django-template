from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'dashboard.html')

def admin_profile(request):
	return render(request, 'admin_profile.html')

def tables(request):
	return render(request, 'tables.html')

def icons(request):
	return render(request, 'icons.html')

def notifications(request):
	return render(request, 'notifications.html')

def upgrade(request):
	return render(request, 'upgrade.html')