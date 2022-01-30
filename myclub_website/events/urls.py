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
]

