from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm 
from .models import Venue, Event, Artist, EventArtist, Ticket

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        
class EventArtistForm(ModelForm):
    class Meta:
        model = EventArtist
        fields = '__all__'
        
class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        
        