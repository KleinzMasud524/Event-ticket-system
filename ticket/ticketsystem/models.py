from django.db import models

class Venue(models.Model):
  venue_name = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  capacity = models.IntegerField()
  
  def __str__(self):
      return f"Venue name: {self.venue_name}\n Address: {self.address}\n Capacity: {self.capacity}"
  
  
class Event(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False)
    venue = models.ForeignKey(Venue, verbose_name=("Venue"), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Event name: {self.event_name}\n Date: {self.date}\n Venue: {self.venue}"
    
    
class Artist(models.Model):
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female")
    ]
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    genre = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    royalty_rate = models.IntegerField(verbose_name=("Royalty rate %"))
    
    def __str__(self):
        return f"Name: {self.first_name} {self.second_name}\n Gender: {self.gender}\n Genre: {self.genre}\n Contact: {self.contact}\n Royalty_rate: {self.royalty_rate}"
    
class EventArtist(models.Model):
    event_id = models.ForeignKey(Event, verbose_name=("Event"), on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, verbose_name=("Artist"), on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Event: {self.event_id}\n Artist: {self.artist_id}"
    
    
class Ticket(models.Model):
    TICKET_OPTIONS = [
        ("Table", "100K"),
        ("VIP", "50K"),
        ("Platinum", "25K"),
        ("Ordinary","10K")
    ]
    first_name = models.CharField(verbose_name=("First name"), max_length=50)
    second_name = models.CharField(verbose_name=("Second name"), max_length=50)
    event = models.ForeignKey(Event, verbose_name=("Event"), on_delete=models.CASCADE)
    ticket_type = models.CharField(verbose_name=("Ticket"), max_length=50, choices = TICKET_OPTIONS)
    date = models.DateField(auto_now=False)

def __str__(self):
    f"Name:{self.first_name}{self.second_name}\n Event: {self.event}\n Ticket: {self.ticket}\n Date: {self.date}"
    
    


