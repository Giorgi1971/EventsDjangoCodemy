from asyncio import events
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar, LocaleHTMLCalendar, month_name
from datetime import datetime
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User


def my_events(request):
    if request.user.is_authenticated:
        print('----')
        me = request.user.id # აქ დამსწარეების აიდის უნდა იღებდეს და შეცდომით უსერის აიდის იღებს. სხვა გზა არ აქვს
        events = Event.objects.filter(attendees=me)
        return render(request, 'events/my_events.html', {'events':events})
    else:
        messages.success(request, ('You have not permishen View this Page!'))
        return redirect('home')


#  CSV ფაილში მონაცემების შენახვა
def venue_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # create cunvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text Object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 18)

    venues = Venue.objects.all()
    lines = []
    # add some lines of text
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(" ")
    for line in lines:
        textob.textLine(line)
    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue_pdf.pdf')


#  CSV ფაილში მონაცემების შენახვა
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    #  Create a csv writer
    writer = csv.writer(response)
    # Designate The Model
    venues = Venue.objects.all()
    # Add column heading to the csv file
    writer.writerow(['Name', "Adress", 'Zip code', 'Web'])
    # loop thu and output
    for venue in venues:
        writer.writerow([venue, venue.address, venue.zip_code, venue.web])
    return response

#  ტექსტურ ფაილში მონაცემების შენახვა
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue}\n\n , {venue.address}\n\n , {venue.zip_code}\n\n, {venue}\n\n,   --- ')

    # lines = ["Line  1\n", "Line 2\n", "line3/\n"]
    response.writelines(lines)
    return response


def venue_delete(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list_venue')


def event_delete(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, ('That all done'))
    else:
        messages.success(request, ('You have not permishen delete this event'))
    return redirect('list-events')


def event_add(request):
    submitted = False
    if request.method == 'POST':
        if request.user.is_superuser:
            form = EventAdminForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/event_add?submitted=True')
        else:
            form = EventForm(request.POST)
            print('user form norm')

            if form.is_valid():
                print('user norm')
                event = form.save(commit=False)
                event.manager = request.user
                if event.manager == request.user:
                    print('good')
                event.save()
                return HttpResponseRedirect('/event_add?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventAdminForm
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/event_add.html', {'form':form, 'submitted':submitted})


def event_update(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventAdminForm(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/event_update.html', {'event':event, 'form':form})


def venue_update(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list_venue')
    return render(request, 'events/venue_update.html', {'venue':venue, 'form':form})

def search_events(request):
    if request.method =="POST":
        searched = request.POST['q']
        print(searched)
        events = Event.objects.filter(description__contains=searched)
        return render(request, 'events/search_events.html', {
            'searched':searched,
            'events':events
            })
    return render(request, 'events/search_events.html', {})



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
    venue_owner = User.objects.get(pk=venue.owner)
    return render(request, 'events/venue_detail.html', {'venue':venue, 'venue_owner':venue_owner})


def list_venue(request):
    # venue_list = Venue.objects.all().order_by('?')
    venue_list = Venue.objects.all()
    # Set Pagination
    p = Paginator(venue_list, 3)
    page = request.GET.get('page')
    venues = p.get_page(page) # აქამდე page_obj ცვლადით მხვდებოდა
    nums = 'a' * venues.paginator.num_pages

    return render(request, 'events/venue_list.html', {'venue_list':venue_list, 'venues':venues, 'nums':nums})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            print(venue)
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        print('hhere')
        form = VenueForm()
        if 'submitted' in request.GET:
            print('subbb')
            submitted = True
    print('999')
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

    event_month = Event.objects.filter(event_date__year=year, event_date__month=month_number)
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
        'event_month':event_month,
    })