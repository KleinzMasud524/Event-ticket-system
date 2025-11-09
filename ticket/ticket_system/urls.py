"""
URL configuration for ticket_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticketsystem.views import home_view, add_venue_view, add_event_view, add_artist_view, add_event_artist_view, add_ticket_view
from ticketsystem.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    #path('venue/', venue_view, name='venue_page'),
    #path('artist/', artist_view, name='artist_page'),
    #path('event/', event_view, name='event_page'),
    #path('event_artist/', event_artist_view, name='event_artist_page'),
    #path('ticket/', ticket_view, name='ticket_page'),
    path('add_venue/', add_venue_view, name='add_venue_page'),
    path('add_event/', add_event_view, name='add_event_page'),
    path('add_artist/', add_artist_view, name='add_artist_page'),
    path('add_event_artist/', add_event_artist_view, name='add_event_artist_page'),
    path('add_ticket/', add_ticket_view, name='add_ticket_page'),
    path('edit_venue <int:venue_id>/', edit_venue_view, name='edit_venue_page'),
    path('delete_venue <int:venue_id>/', delete_venue_view, name='delete_venue_page'),
    path('edit_artist <int:artist_id>/', edit_artist_view, name='edit_artist_page'),
    path('delete_artist <int:artist_id>/', delete_artist_view, name='delete_artist_page'),
    path('edit_event <int:event_id>/', edit_event_view, name='edit_event_page'),
    path('delete_event <int:event_id>/', delete_event_view, name="delete_event_page"),
    path('edit_event_artist <int:event_artist_id>/', edit_event_artist_view, name="edit_event_artist_page"),
    path('delete_event_artist <int:event_artist_id>/', delete_event_artist_view, name='delete_event_artist_page'),
    path('edit_ticket <int:ticket_id>/', edit_ticket_view, name='edit_ticket_page'),
    path('delete_ticket <int:ticket_id>', delete_ticket_view, name='delete_ticket_page'), 
]
