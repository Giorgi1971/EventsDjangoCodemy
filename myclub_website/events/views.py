import imp
from os import name
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar, LocaleHTMLCalendar, month_name
from datetime import datetime
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


def venue_delete(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list_venue')


def event_delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def event_add(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/event_add?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/event_add.html', {'form':form, 'submitted':submitted})


def event_update(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/event_update.html', {'event':event, 'form':form})


def venue_update(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venue')
    return render(request, 'events/venue_update.html', {'venue':venue, 'form':form})


def search_venue(request):
    if request.method =="POST":
        searched = request.POST['q']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html', {
            'searched':searched,
            'venues':venues
            })
    return render(request, 'events/search_venue.html', {})


def venue_detail(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/venue_detail.html', {'venue':venue})


def list_venue(request):
    venue_list = Venue.objects.all().order_by('?')
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
    event_list = Event.objects.all().order_by('-event_date')
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