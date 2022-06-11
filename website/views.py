from django.shortcuts import render
from django.views import generic
from .models import Reservation


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'index.html'


def manage(request):
    all_reservations = Reservation.objects.all
    return render(request, 'manage.html', {'all':all_reservations})

def book_a_table(request):
    return render(request, 'book-a-table.html', {})
    