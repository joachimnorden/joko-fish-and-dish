from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    search_fields = ['fname', 'lname']
    list_filter = ('date','fname')
    
