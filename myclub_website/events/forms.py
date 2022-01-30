from dataclasses import field
from django import forms
from django.forms import ModelForm
from . models import *

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {
            'name': "",
            'address':'',
            'zip_code': '',
            'phone': "",
            'web': "",
            'email_address': "",           
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vanue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web address'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }