from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=50)
    address = models.CharField('Venue Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=50, blank = True)
    phone_number = models.CharField('Phone Number', max_length=50)
    web = models.URLField( 'Website Address', max_length=200, blank = True)
    email_address = models.EmailField('Email Address', max_length=254, blank= True) 
    owner = models.IntegerField("Venue Owner",blank = False, default = 1)
    venue_image = models.ImageField( upload_to = 'images/', null = True, blank = True)

    def __str__(self):
        return self.name



class Person(models.Model):
    first_name = models.CharField('Person FirstName', max_length=50)
    last_name = models.CharField('Person LastName', max_length=50)
    email = models.EmailField("Email Address", max_length=254)    


    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    name = models.CharField('Events Name', max_length=50)
    event_date = models.DateTimeField( 'Events Date', max_length = 100)
    venue = models.ForeignKey(Venue, blank = True, null = True, on_delete = models.CASCADE)
    #venue = models.CharField(  max_length=50 )
    manager = models.ForeignKey(User, blank = True, null = True, on_delete = models.SET_NULL )
    description = models.TextField(blank = True )
    attendee = models.ManyToManyField( Person, blank = True)
    approved = models.BooleanField("Approved", default = False)


    def __str__(self):
        return self.name


    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split("," ,)[0]
        return days_till_stripped
        
    