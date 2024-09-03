from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# Admin SuperUser Event Form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ("name", "event_date", "venue", "manager", "attendee", "description")

        labels = {
            "name": "",
            "event_date" : "YYYY-MM-DD HH:MM:SS",
            "venue": " Select Venue",
            "manager": "Select Manager",
            "attendee": "Select Attendee(s)",
             "description":"",    

        }

        widgets = {
                    "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Event Name"}),
                   "event_date" : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Event Date"}),
                    "venue": forms.Select(attrs={'class': 'form-select', 'placeholder':"Venue"}),
                    "manager": forms.Select(attrs={'class': 'form-select', 'placeholder':"Manager"}),
                    "attendee": forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': "Attendee(s)"}),
                    "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Description" ,'rows': 5, 'cols': 30}),
                }



#User Event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name", "event_date", "venue","attendee", "description")

        labels = {
            "name": "",
            "event_date" : "YYYY-MM-DD HH:MM:SS",
            "venue": " Select Venue",
            "attendee": "Select Attendee(s)",
             "description":"",    

        }

        widgets = {
                    "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Event Name"}),
                   "event_date" : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Event Date"}),
                    "venue": forms.Select(attrs={'class': 'form-select', 'placeholder':"Venue"}),
                    "attendee": forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': "Attendee(s)"}),
                    "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Description" ,'rows': 5, 'cols': 30}),
                }



class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("name", "address", "zip_code", "phone_number", "web", "email_address","venue_image")

        labels = {
        "name": "",
            "address" : "",
            "zip_code": "",
            "phone_number": "",
            "web":"",
            "email_address": "",  
            "venue_image" : "",
        }

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Venue Name"}),
            "address" : forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Address"}),
            "zip_code": forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Zip Code"}),
            "phone_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Phone Number"}),
            "web": forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Web"}),
            "email_address": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email Address"}),

        }

