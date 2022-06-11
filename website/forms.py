from django.forms import ModelForm
from .models import Reservation


class Reservationform(ModelForm):
    class Meta:
        model = Reservation
        fields = ['fname', 'lname', 'email', 'phone', 'number_of_persons', 'date', 'time']
