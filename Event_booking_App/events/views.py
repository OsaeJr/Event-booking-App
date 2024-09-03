from django.shortcuts import render,HttpResponseRedirect, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from django.contrib.auth.models import User
from .forms import VenueForm, EventForm, EventFormAdmin
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
# Create your views here.

def admin_approval(request):
    event_count = Event.objects.all().count()
    venue_count = Venue.objects.all().count()
    user_count = User.objects.all().count()
    event_list = Event.objects.all().order_by("event_date")
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist("boxes")
            #uncheck all events
            event_list.update(approved = False)
            #update the database
            for id in id_list:
                Event.objects.filter(pk = int(id)).update(approved = True)
            messages.success(request, "Event list approval updated")
            return redirect("event_list")
        else:
            return render(request, "admin_approval.html",{"event_list": event_list, "event_count": event_count, "venue_count": venue_count, "user_count": user_count})
    else:
        messages.success(request, "Sorry,you are not a SuperUser")
        return redirect("home")
    return render(request, "admin_approval.html",{"event_list": event_list})

def event_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        message = messages.success(request, f"you searched for {searched}")
        events = Event.objects.filter(name__contains = searched)
        return render(request, "event_search.html", {"searched" : searched, "events" : events, "message" : message})
    
    else:
        return render(request, "event_search.html")

def my_events(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(attendee = request.user.id)    
        return render(request,"my_events.html", {"events": events, })
    else:
        messages.success(request, "You are not authorised to view this page")
        return redirect("home")

def venue_text_file(request):
    response = HttpResponse(content_type = "text/plain")
    response['Content-Disposition'] = 'attachment; filenmae=venues.text'

    lines = ["This is line on\n", "This is line 2\n","This is line 4\n"]

    #Designate the Model
    venues = Venue.objects.all()
    lines =  []

    #loop through
    for venue in venues:
        lines.append(f'{venue}\n')

    #write to text file
    response.writelines(lines)
    return response

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    venue.delete()
    return redirect("venues")

def delete_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, "Event deleted")
        return redirect("event_list")
    else:
        messages.success(request, "You are not authorised to delete the event")
        return redirect("event_list")

def update_event(request, event_id):

    event = Event.objects.get(pk = event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance = event)
    else:
        form = EventForm(request.POST or None, instance = event)

    if form.is_valid():
        form.save()
        messages.success(request, "Update successful") 
        return redirect("event_list")


    return render(request, "update_event.html", {"event" : event, "form" : form})


def add_event(request): 
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('events?submitted=True')
        else:
            form = EventForm(request.POST)    
            if form.is_valid():
                event = form.save(commit = False)
                event.manager = request.user
                event.save()

                return HttpResponseRedirect('events?submitted=True')


    else:
        #juset going to the form, not submitting
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "add_event.html", {"form": form, "submitted": submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    form = VenueForm(request.POST or None, request.FILES or None, instance = venue)
    if form.is_valid():
        form.save()
        return redirect("venues")

    return render(request, "update_venue.html", {"venue" : venue, "form" : form})
    
def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        message = messages.success(request, f"you searched for {searched}")
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, "search_venue.html", {"searched" : searched, "venues" : venues})
    
    else:
        return render(request, "search_venue.html")


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk = venue_id)
    venue_owner = User.objects.get(pk = venue.owner)
    return render(request, "show_venue.html", {"venue" : venue,"venue_owner": venue_owner})

def venues(request):
    venue_list = Venue.objects.all().order_by("name")

    return render(request, 'venues.html', {"venue_list": venue_list})


def event_list(request):
    event_list = Event.objects.all().order_by("event_date")
    return render(request, 'event_list.html', {"event_list": event_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit = False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "add_venue.html", {"form": form, "submitted": submitted})




def home(request, day = datetime.now().day ,  month = datetime.now().strftime("%B"), year = datetime.now().year):
    name = "Samuel"
    month = month.capitalize()


    # convert month from name to calendar
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    #get current year
    now = datetime.now()
    current_year = now.year

    #get current time
    time = now.strftime('%H:%M:%S %p')
    
    
    #create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    


    return render(request, "home.html", {
        "month_number": month_number,
        "month": month,
        "name": name,
        "day": day,
        "year": year,
        "cal": cal,
        "now": now,
        "time": time,
        "current_year": current_year
  
     })