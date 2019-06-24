from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



class BookingForm(models.Model):                        # Main booking form
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email_address = models.CharField(max_length = 30)
    contact_number = models.CharField(max_length = 20)

    def get_absolute_url(self):
        return reverse('saunterer:pref_form')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name 

class Preferences(models.Model):                        # User preference form
    booking_form = models.ForeignKey(BookingForm, on_delete = models.CASCADE)
    entry_1 = models.CharField(max_length = 30)     # History
    entry_2 = models.CharField(max_length = 30)     # Religion
    entry_3 = models.CharField(max_length = 30)     # Seek
    entry_4 = models.TextField(max_length = 50)     # Intrests
    entry_5 = models.TextField(max_length = 50)     # Expect
    
    def __str__(self):
        return self.booking_form