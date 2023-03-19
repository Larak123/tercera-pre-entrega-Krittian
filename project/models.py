# Create your models here.
from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)


    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    def __str__(self):
      return f"Nombre: {self.nombre}, Valor: {self.valor}"
