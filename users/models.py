from django.db import models

# Create your models here.


class User(models.Model):
    # Campos comunes para administrador y cliente
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Campo para validar si es administrador o no
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)
