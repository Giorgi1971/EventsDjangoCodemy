from django.shortcuts import render
import calendar
from calendar import HTMLCalendar, LocaleHTMLCalendar, month_name
from datetime import datetime


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