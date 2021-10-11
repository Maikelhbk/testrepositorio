from django.db import models
from django.db.models.base import Model

# Create your models here.

class Rol(models.Model):
      rol_cliente = models.CharField(max_length=50)

      def __str__(self):
          return self.rol_cliente

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField()
    empresa = models.CharField(max_length=50)
    telefono = models.IntegerField()
    rol_cliente = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut_cliente

class Profesional(models.Model):
    rut_profesional = models.CharField(max_length=12)
    nombre_pro = models.CharField(max_length=50)
    correo_pro = models.EmailField()
    telefono_pro = models.CharField(max_length=12)
    rol_cliente = models.ForeignKey(Rol, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut_profesional

