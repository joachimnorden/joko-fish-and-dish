from django.shortcuts import render
from django.views import generic
from .models import Reservation
from .forms import Reservationform


class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'index.html'


def manage(request):
    all_reservations = Reservation.objects.all
    return render(request, 'manage.html', {'all': all_reservations})


def book_a_table(request):
    if request.method == "POST":
        form = Reservationform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'book-a-table.html', {})

    else:
        return render(request, 'book-a-table.html', {})
