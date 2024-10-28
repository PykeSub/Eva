from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=15)
    fechaDespacho = models.DateField(max_length=15)
    fechaRecepcion = models.DateField(max_length=15)