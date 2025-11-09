from django.shortcuts import render, redirect
from django.contrib import messages
from ticketsystem.forms import ArtistForm, EventArtistForm, TicketForm, VenueForm, EventForm
from ticketsystem.models import Venue, Event, Artist, EventArtist, Ticket

def home_view(request):
    return render(request, 'home.html')

#Venue view request
def add_venue_view(request):
    message = ''
    if request.method == "POST":
        venue_form = VenueForm(request.POST) 
        
        if venue_form.is_valid():
            venue_form.save()
            messages.success(request, "Venue added successfully")
        else:
            messages.error(request, "Form has invalid data!!!")
    else:
        venue_form = VenueForm()
        
    venues = Venue.objects.all()
        
    context = {
        'form':venue_form,
        'msg':message,
        'venues': venues
    }

    return render (request, "add_venue.html", context)
        

#Event form request
def add_event_view(request):
    message=''
    if request.method == "POST":
        event_form = EventForm(request.POST)
        
        if event_form.is_valid():
            event_form.save()
            
            message = "Event added successfully"
            
    else:
        event_form = EventForm()
        
    events = Event.objects.all()
        
    context = {
        'form':event_form,
        'msg':message,
        'events':events
    }
    
    return render (request, "add_event.html", context)


#Artist form view
def add_artist_view(request):
    message = ''
    if request.method == "POST":
        artist_form = ArtistForm(request.POST)
        
        if artist_form.is_valid():
            artist_form.save()
            
            message = "Artist added successfully"
            
    else:
        artist_form = ArtistForm()
    
    artists = Artist.objects.all()
        
    context = {
        "form":artist_form,
        "msg":message,
        "artists": artists
    }
    
    return render (request, "add_artist.html", context)


#EventArtist form view
def add_event_artist_view(request):
    message = ''
    if request.method == "POST":
        event_artist_from = EventArtistForm(request.POST)
        
        if event_artist_from.is_valid():
            event_artist_from.save()
            
            message = "Event Artist added successfully"
            
    else:
        event_artist_from = EventArtistForm()
        
    event_artists = EventArtist.objects.all()
        
    context = {
        "form":event_artist_from,
        "msg":message,
        "event_artists":event_artists
    }       
    
    return render (request, "add_event_artist.html", context)


#Ticket from view
def add_ticket_view(request):
    message = ''
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        
        if ticket_form.is_valid():
            ticket_form.save()
            
            message = "Ticket added successfully"
            
    else:
        ticket_form = TicketForm()
        
    tickets = Ticket.objects.all()
        
    context = {
        "form":ticket_form,
        "msg":message,
        "tickets":tickets
    }
    
    return render (request, "add_ticket.html", context)

#Edit venue view
def edit_venue_view(request, venue_id):
    message = ''
    venue = Venue.objects.get(id=venue_id)
    
    if request.method == "POST":
        venue_form = VenueForm(request.POST, instance=venue)
        
        if venue_form.is_valid():
            venue_form.save()
            message = "Changes saved successfully"
        else:
            message = 'Form has invalid data!!!'
    else:
        venue_form = VenueForm(instance=venue)
        
    context = {
        "form": venue_form,
        "venue": venue,
        "msg": message,
    } 
    
    return render (request, "edit_venue.html", context)
    
#event edit view
def edit_event_view(request, event_id):
    message = ''
    event = Event.objects.get(id = event_id)
    
    if request.method == "POST":
        event_form = EventForm(request.POST, instance=event)
        
        if event_form.is_valid():
            event_form.save()
            message = 'Changes saved successfully'
        else:
            message = 'Form has invalid data!!!'
    
    else:
        event_form = EventForm(instance=event)
        
    context={
        'form': event_form,
        'event': event,
        'msg': message,
    }
    
    return render (request, "edit_event.html", context)
    

#Artist edit view
def edit_artist_view(request, artist_id):
    message = ''
    artist = Artist.objects.get(id=artist_id)
    
    if request.method == "POST":
        artist_form = ArtistForm(request.POST, instance=artist)
        
        if artist_form.is_valid():
            artist_form.save()
            messages.success(request, 'Changes saved successfully')
        else:
            messages.error(request, 'Form has invalid data')
            
    else:
        artist_form = ArtistForm(instance=artist)
        
    context = {
        "form": artist_form,
        "artist": artist
    }
    
    return render (request, "edit_artist.html", context)
    

#event Artist edit view
def edit_event_artist_view(request, event_artist_id):
    event_artist = EventArtist.objects.get(id=event_artist_id)
    
    if request.method == "POST":
        event_artist_form = EventArtistForm(request.POST, instance=event_artist)
        
        if event_artist_form.is_valid():
            event_artist_form.save()
            messages.success(request, 'Changes saved successfully')
        else:
            messages.error(request, 'Form has invalid data')

    else:
        event_artist_form = EventArtistForm(instance=event_artist)
        
    context = {
        'form': event_artist_form,
        'event_artist': event_artist,
    }
    
    return render (request, "edit_event_artist.html", context)
    

#ticket edit view
def edit_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        
        if ticket_form.is_valid():
            ticket_form.save()
            messages.success(request, 'Changes saved successfully')
        else:
            messages.error(request, 'Form has invalid data!!!')
        
    else:
        ticket_form  = TicketForm(instance=ticket)
        
    context = {
        "form": ticket_form,
        "ticket": ticket
    } 
    
    return render (request, "edit_ticket.html", context)

#Delete views
def delete_venue_view(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    
    venue.delete()
    
    return redirect('add_venue_page')

def delete_artist_view(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    
    artist.delete()
    
    return redirect('add_artist_page')

def delete_event_view(request, event_id):
    event = Event.objects.get(id=event_id)
    
    event.delete()
    
    return redirect('add_event_page')

def delete_event_artist_view(request, event_artist_id):
    event_artist = EventArtist.objects.get(id=event_artist_id)
    
    event_artist.delete()
    
    return redirect('add_event_artist_page')

def delete_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    
    ticket.delete()
    
    return redirect('add_ticket_page')
    