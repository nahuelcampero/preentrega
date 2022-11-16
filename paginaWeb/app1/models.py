from django.db import models

class cine(models.Model):
    
    nombre = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 40)
    
class pelicula(models.Model):
    
    nombre = models.CharField(max_length = 40)
    duracion = models.IntegerField()


class cliente(models.Model):
    
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    DNI = models.IntegerField()
    