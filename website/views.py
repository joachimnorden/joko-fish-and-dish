from django.shortcuts import render
from django.views import generic
from .models import Reservation
from .forms import Reservationform
from django.contrib import messages


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html', {})


def manage(request):
    all_reservations = Reservation.objects.all
    return render(request, 'manage.html', {'all': all_reservations})


def book_a_table(request):
    if request.method == "POST":
        form = Reservationform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your booking hast been submitted'))    
        return render(request, 'book-a-table.html', {})

    else:
        return render(request, 'book-a-table.html', {})
