from django.shortcuts import render
from venues.models import Venue

def index(request):
    venues = Venue.objects.filter(active=True)
    context = {'venues': venues }
    return render(request, 'venues/index.html', context)

def about(request):
	return render(request, 'about.html')