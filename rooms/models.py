from django.db import models

# Create your models here.


class Room(models.Model):
    room_description = models.TextField(blank=True)
    room_type = models.CharField(max_length=255)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
