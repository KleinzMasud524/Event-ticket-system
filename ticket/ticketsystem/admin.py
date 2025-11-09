from django.contrib import admin

from .models import Venue, Event, Artist, EventArtist, Ticket

class VenueAdmin(admin.ModelAdmin):
    list_display = ("venue_name", "address", "capacity")

class EventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "date", "venue")

class ArtistAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "gender", "genre", "contact", "royalty_rate")
    
class EventArtistAdmin(admin.ModelAdmin):
    list_display = ("event_id", "artist_id")
    
class TicketAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "event", "ticket_type", "date")

admin.site.register(Venue, VenueAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(EventArtist, EventArtistAdmin)
admin.site.register(Ticket, TicketAdmin)


