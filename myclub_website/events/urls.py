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
    path('search_venue/', views.search_venue,  name='search_venue'),
    path('venue_update/<venue_id>/', views.venue_update,  name='venue_update'),
    path('event_update/<event_id>/', views.event_update,  name='event_update'),
    path('event_add/', views.event_add,  name='event_add'),
    path('event_delete/<event_id>/', views.event_delete,  name='event_delete'),
    path('venue_delete/<venue_id>/', views.venue_delete,  name='venue_delete'),
    path('venue_text/', views.venue_text, name='venue_text'),
    path('venue_csv/', views.venue_csv, name='venue_csv'),
    path('venue_pdf/', views.venue_pdf, name='venue_pdf'),
    path('my_events/', views.my_events, name='my_events'),
    path('search_events/', views.search_events, name='search_events'),
    path('admin_aprroval/', views.admin_aprroval, name='admin_aprroval'),



]

