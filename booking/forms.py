from django import forms
from .models import Reservations, Hotels, Guests
from datetime import date, time
from datetime import timedelta

class ReservationForm(forms.ModelForm):
    rooms = forms.IntegerField(max_value=10)
    rooms.label = "Number of rooms"
    rooms.widget = forms.NumberInput()
    
    class Meta:
        model = Reservations
        fields = ('startdate', 'enddate', 'firstname', 'lastname', 'creditcardnum', 'phonenum', 'hotel_hotelid')
        labels = {
            'startdate': 'Check In:',
            'enddate': 'Check Out:',
            'firstname': 'First name:',
            'lastname': 'Last name:',
            'creditcardnum': 'Credit Card:',
            'phonenum': 'Phone number:',
            'hotel_hotelid': 'Hotels',
        }
        dateToday = date.today()
        date.strftime(dateToday,'%Y-%m-%d %H:%M:%S') 

        widgets ={
            'startdate': forms.DateInput(attrs={'type': 'date', 'min': dateToday}),
            'enddate': forms.DateInput(attrs={'type': 'date', 'min': dateToday + timedelta(days=1)}),
            'firstname': forms.TextInput(attrs={'name':'first_name'}),
            'lastname': forms.TextInput(attrs={'name':'last_name'}),
        }
class GuestsForm(forms.ModelForm):
        model = Guests
        fields = ('firstname', 'lastname')
        
        labels = {
            'firstname': 'First name:',
            'lastname': 'Last name:',
        }    


