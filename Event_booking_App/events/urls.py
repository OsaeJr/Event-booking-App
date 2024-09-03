from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ="home"),
    path("<int:day>/<str:month>/<int:year>/", views.home, name ="home"),
    path("events", views.event_list, name ="event_list"),
    path("add_venue", views.add_venue, name ="add_venue"),
    path("venues", views.venues, name ="venues"),
    path("show_venue/<venue_id>", views.show_venue, name ="show_venue"),
    path("search_venue", views.search_venue, name ="search_venue"),
    path("update_venue/<venue_id>", views.update_venue, name ="update_venue"),
    path("add_event", views.add_event, name ="add_event"),
    path("update_event/<event_id>", views.update_event, name ="update_event"),
    path("delete_event/<event_id>", views.delete_event, name ="delete_event"),
    path("delete_venue/<venue_id>", views.delete_venue, name ="delete_venue"),
    path("venue_text_file", views.venue_text_file, name ="venue_text_file"),
    path("my_events", views.my_events, name ="my_events"),
    path("event_search", views.event_search, name ="event_search"),
    path("admin_approval", views.admin_approval, name ="admin_approval"),
     




] 