import imp
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar, LocaleHTMLCalendar, month_name
from datetime import datetime
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


def venue_detail(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/venue_detail.html', {'venue':venue})


def list_venue(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue_list.html', {'venue_list':venue_list})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list':event_list})



def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    #  Convert month fron name to number
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)
    #  GET cuurent year 
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    time2 = now.strftime('%I:%M %p')

    return render(request, 'events/home.html', {
        'name': 'John',
        'year':year,
        'month':month,
        'month_number':month_number,
        'cal' : cal,
        'current_year':current_year,
        'time': time,
        'time2': time2,
    })