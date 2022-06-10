from django.shortcuts import render
from django.views import generic
from .models import Reservation


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'index.html'
