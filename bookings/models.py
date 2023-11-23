from django.db import models
from users.models import User
from rooms.models import Room

# Create your models here.


class Booking(models.Model):
    booking_number = models.CharField(max_length=255, unique=True)
    customer = models.ForeignKey( User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey( Room, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_nights = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.booking_number)
