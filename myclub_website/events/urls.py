import imp
from django.urls import path
from . import views


urlpatterns = [
    # ეს ქვედებია: Path Converters
    # int: numbers
    # str: strings
    # path: whole urls /
    # slug: hypher-and-underscores_stuff
    # UUID: universally unique identifier

    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events,  name='list-events'),
    path('add_venue/', views.add_venue,  name='add_venue'),
    path('list_venue/', views.list_venue,  name='list_venue'),
    path('venue/<venue_id>/', views.venue_detail,  name='venue_detail'),
    # path('venue/', views.add_venue,  name='add_venue'),
]

