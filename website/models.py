from django.db import models

STATUS = ((0, "Not confirmed"), (1, "Confirmed"))


class Reservation(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.fname + ' ' + self.lname
